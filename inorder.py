# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    traversal_vec = []
    if root.left is not None:
        traversal_vec.append(root.inorderTraversal(root.left))
    traversal_vec.append(root.val)
    if root.right is not None:
        traversal_vec.append(root.inorderTraversal(root.right))

    return traversal_vec

