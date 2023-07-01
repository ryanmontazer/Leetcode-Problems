from collections import deque

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def level_order_traversal(root):
    if root is None:
        return 

    # Create an empty queue for level order traversal
    queue = deque()

    # Enqueue root and initialize height
    queue.append(root)

    while queue:
        # Print front of queue and remove it from queue
        node = queue.popleft()
        print(node.val, end=" ")

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)



# In-order traversal (Left, Root, Right)
def inorder_traversal(root):
    stack = []
    current_node = root

    while True:
        if current_node is not None:
            # Place pointer to a tree node on the stack before traversing the node's left subtree
            stack.append(current_node)
            current_node = current_node.left
        # Backtrack from the empty subtree and visit the node at the top of the stack; however, if the stack is empty, you are done
        elif(stack):
            current_node = stack.pop()
            print(current_node.val, end=" ")  # print the value
            # We have visited the node and its left subtree. Now, it's time to visit its right subtree
            current_node = current_node.right
        else:
            break

# Pre-order traversal (Root, Left, Right)
def preorder_traversal(root):
    if root is None:
        return

    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        print(node.val, end=" ")

        # First push right child to stack because right child must be processed after the left child
        if node.right is not None:
            stack.append(node.right)

        # Then push left child to stack
        if node.left is not None:
            stack.append(node.left)

# Post-order traversal (Left, Right, Root)
def postorder_traversal(root):
    if root is None:
        return

    stack1 = []
    stack2 = []

    # Push root to first stack
    stack1.append(root)

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        # Push left and right children of removed item to first stack
        if node.left is not None:
            stack1.append(node.left)
        if node.right is not None:
            stack1.append(node.right)

    # Print all elements of second stack
    while stack2:
        node = stack2.pop()
        print(node.val, end=" ")




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        stack=[]
        current = root
        while True:
            if current:
                stack.append(current)
                current=current.left
            elif stack:
                current=stack.pop()
                result.append(current.val)
                current=current.right
            else:
                break
        return result
