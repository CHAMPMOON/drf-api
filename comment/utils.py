class CommentLeaf:
    def __init__(self, comment, source):
        self.comment = dict(comment)
        self.comment['path'] = self.comment['path'][len(source) + 1:]
        self.comment['comment'] = []

    def is_main(self) -> bool:
        return self.comment['path'] == ""

    def get_parent_id(self) -> int:
        return int(self.comment['path'].split('.')[-1])

    def insert_leafs(self, children):
        self.comment['comment'] = children

    def get_comment(self):
        return self.comment


class CommentTree:
    def __init__(self, data, source):
        self.tree = []
        self.waiting_parent = {}
        for comment in data:
            leaf = CommentLeaf(comment, source)

            children = self.waiting_parent.get(leaf.comment['id'])
            if children:
                leaf.insert_leafs(children)

            if not leaf.is_main():
                parent_id = leaf.get_parent_id()
                if self.waiting_parent.get(parent_id) is None:
                    self.waiting_parent[parent_id] = [leaf.get_comment()]
                else:
                    self.waiting_parent[parent_id].append(leaf.get_comment())
            else:
                all_children = self.waiting_parent.get(leaf.comment['id'], [])
                leaf.insert_leafs(all_children)
                self.tree.append(leaf.get_comment())

    def get(self):
        return self.tree
