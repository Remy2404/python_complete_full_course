#library binrary tree
import	binarytree
class Node:
    #Constructor:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:#if we have a node
            if data < self.data:#if data is less than the node
                #left node check:
                if self.left is None:#if left node is empty
                    self.left = Node(data)#create a new node
                else:
                    self.left.insert(data)#insert data into left node
            elif data > self.data:#if data is greater than the node
                #right node check:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
#print_tree func
    def print_tree(self):
        if self.left:#
            self.left.print_tree()#call left node
        print(self.data)
        if self.right:
            self.right.print_tree()
# inorder traversal is same as preorder traversal of tree
    def inorder(self):
        if self.left: 
            self.left.inorder()#call left node
        print(self.data)
        if self.right:
            self.right.inorder()
#preorder traversal is same as preorder traversal of tree
    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
            #print step by step of preorder traversal
            print("left:", end="")
        if self.right:
            
            self.right.preorder()
# postorder traversal is same as preorder traversal of tree
    def postorder(self):
        if self.left:
            self.left.postorder()
           #print step by step of postorder traversal
            print("left:", end="")
        if self.right:
            self.right.postorder()
            print("right:", end="")
        print(self.data)
#Find maximum value in a Binary Tree
    def max_value(self):
        if self.left is None and self.right is None:
            return self.data
        elif self.left is None:
            return self.right.max_value()
        elif self.right is None:
            return self.left.max_value()
        else:
            return max(self.data, self.left.max_value(), self.right.max_value())
#Find minimum value in a Binary Tree
    def min_value(self):
        if self.left is None and self.right is None:
            return self.data
        elif self.left is None:
            return self.right.min_value()
        elif self.right is None:
            return self.left.min_value()
        else:
            return min(self.data, self.left.min_value(), self.right.min_value())
#Height of a Binary Tree
    def height(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return self.right.height() + 1
        elif self.right is None:
            return self.left.height() + 1
        else:
            return max(self.left.height(), self.right.height()) + 1
# Size of a Binary Tree
    def size(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.size() + 1
        elif self.right is None:
            return self.left.size() + 1
        else:
            return self.left.size() + self.right.size() + 1

    def leaf_count(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.leaf_count()#call right node
        elif self.right is None:#call left node
            return self.left.leaf_count()
        else:
            return self.left.leaf_count() + self.right.leaf_count()
# Display the tree
    def display(self):
        if self.left:
            self.left.display()
        print(self.data)
        if self.right:
            self.right.display()
#delete func
    def delete(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    print("No such element in the tree")
                else:
                    self.left.delete(data)
            elif data > self.data:
                if self.right is None:
                    print("No such element in the tree")
                else:
                    self.right.delete(data)
            else:
                if self.left is None and self.right is None:
                    self.data = None
                    return
                elif self.left is None:
                    temp = self.right
                    self.data = temp.data
                    self.right = temp.right
                    self.left = temp.left
                    return
                elif self.right is None:
                    temp = self.left
                    self.data = temp.data
                    self.left = temp.left
                    self.right = temp.right
                    return
                else:
                    temp = self.right.min_value()
                    self.data = temp.data
                    self.right.delete(temp.data)
                    return
# Driver Code
print()
print("-------------------------------------")
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print()
print("Inorder Traversal of the constructed BST is")
print("-------------------------------------")
root.inorder()
print()
print("Postorder Traversal of the constructed BST is")
print("-------------------------------------")
root.postorder()
print()
print("Preorder Traversal of the constructed BST is")
print("-------------------------------------")
root.preorder()
print()
print("Height of the constructed BST is")
print("-------------------------------------")
print(root.height())
print()
print("Size of the constructed BST is")
print("-------------------------------------")
print(root.size())
print()
print("Leaf count of the constructed BST is")
print("-------------------------------------")
print(root.leaf_count())
print()
print("Maximum value of the constructed BST is")
print("-------------------------------------")
print(root.max_value())
print()
print("Minimum value of the constructed BST is")
print("-------------------------------------")
print(root.min_value())
print()
print("Deleting 10 from the constructed BST")
print("-------------------------------------")
root.delete(10)
print("Inorder Traversal of the constructed BST is")
print("-------------------------------------")
root.inorder()

