class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right

def pre_order_traversal(root):
    result = []

    def traverse(node):
        if node is None:
            return
        result.append(node.value)
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    return result