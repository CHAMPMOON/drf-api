from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_routes(request):
    routes = [
        'GET /article',
        'POST /article',
        'GET /article/<int:pk>',
        'PUT /article/<int:pk>',
        'DELETE /article/<int:pk>',
        'GET /comment',
        'GET /comment/<int:pk>',
        'PUT /comment/<int:pk>',
        'DELETE /comment/<int:pk>',
        'POST article/<int:pk>/comment',
        'POST comment/<int:pk>/comment',
        'GET article/<int:pk>/comment/depth=<int:dp>',
        'GET comment/<int:pk>/comment/depth=<int:dp>',
    ]
    return Response(routes)
