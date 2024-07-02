class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)
    
    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert(node.right, data)
    
    def delete(self, data):
        self.root = self._delete(self.root, data)
    
    def _delete(self, node, data):
        if node is None:
            return node
        
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)
        return node
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inorder_traversal(self):
        return self._inorder_traversal(self.root)
    
    def _inorder_traversal(self, node):
        res = []
        if node:
            res = self._inorder_traversal(node.left)
            res.append(node.data)
            res = res + self._inorder_traversal(node.right)
        return res
    
    def preorder_traversal(self):
        return self._preorder_traversal(self.root)
    
    def _preorder_traversal(self, node):
        res = []
        if node:
            res.append(node.data)
            res = res + self._preorder_traversal(node.left)
            res = res + self._preorder_traversal(node.right)
        return res
    
    def postorder_traversal(self):
        return self._postorder_traversal(self.root)
    
    def _postorder_traversal(self, node):
        res = []
        if node:
            res = self._postorder_traversal(node.left)
            res = res + self._postorder_traversal(node.right)
            res.append(node.data)
        return res


bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder Traversal:", bst.inorder_traversal())
print("Preorder Traversal:", bst.preorder_traversal())
print("Postorder Traversal:", bst.postorder_traversal())

bst.delete(20)
print("Inorder Traversal after deleting 20:", bst.inorder_traversal())
