from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment
from article.models import Article
from .serializers import CommentSerializer
from .utils import CommentTree
from django.db.models import Q


@api_view(['GET'])
def comments_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_comment_to_article(request, pk):
    try:
        Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    request.data['path'] = f"{pk}"
    request.data['depth'] = 1

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_comment_to_comment(request, pk):
    try:
        parent_comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    request.data['path'] = f"{parent_comment.path}.{pk}"
    request.data['depth'] = parent_comment.depth + 1

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_comments_for_article(request, pk, dp):
    try:
        Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    start_path = f"{pk}"

    comments = Comment.objects.filter(
        Q(path__startswith=start_path) &
        Q(depth__lte=dp)
    ).order_by('-path').order_by("-depth")

    serializer = CommentSerializer(comments, many=True)

    tree = CommentTree(data=serializer.data, source=start_path)

    return Response(tree.get(), status=status.HTTP_200_OK)


@api_view(['GET'])
def get_comments_for_comment(request, pk, dp):
    try:
        parent_comment = Comment.objects.get(pk=pk)

    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    start_path = f"{parent_comment.path}.{pk}"

    comments = Comment.objects.filter(
        Q(path__startswith=start_path) &
        Q(depth__lte=parent_comment.depth + dp)
    ).order_by('-path').order_by("-depth")

    serializer = CommentSerializer(comments, many=True)

    tree = CommentTree(data=serializer.data, source=start_path)

    return Response(tree.get(), status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
