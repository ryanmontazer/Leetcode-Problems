# Time: O(h)
# Space: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curr=root
        #Parent is the parent of curr and it will be created as TreeNode(0) if curr is root
        parent=TreeNode(0)
        #Curr at the end of this while wil be the node which node.val=key
        #If such a node doesnt exist or root is None, curr will be None
        while curr:
            if curr.val==key:
                break
            elif curr.val>key:
                parent=curr
                curr=curr.left
            elif curr.val<key:
                parent=curr
                curr=curr.right
        #If curr is None, either deired node not found or root was None
        #In each case we have to return root
        if not curr:
            return root
        
        #First handle the case which curr is root
        if curr is root:
            if not curr.left:
                return curr.right
            if not curr.right:
                return curr.left
            right_node=curr.right
            #We update right_node with the most left child of it
            while True:
                if right_node.left:
                    right_node=right_node.left
                else:
                    break
            #Now we set right_node.left=curr.left and it works becasue its a BST
            right_node.left=curr.left
            return curr.right

        #Now handle the case which curr is parent.left
        if curr is parent.left:
            if not curr.left:
                parent.left=curr.right
                return root
            if not curr.right:
                parent.left=curr.left
                return root
            #At this point we are sure curr.left and curr.right are available
            right_node=curr.right
            #We update right_node with the most left child of it
            while True:
                if right_node.left:
                    right_node=right_node.left
                else:
                    break
            #Now we set right_node.left=curr.left and it works becasue its a BST
            right_node.left=curr.left
            parent.left=curr.right
            return root

        #Now handle the case which curr is parent.right
        if curr is parent.right:
            if not curr.left:
                parent.right=curr.right
                return root
            if not curr.right:
                parent.right=curr.left
                return root
            #At this point we are sure curr.left and curr.right are available
            right_node=curr.right
            #We update right_node with the most left child of it
            while True:
                if right_node.left:
                    right_node=right_node.left
                else:
                    break
            #Now we set right_node.left=curr.left and it works becasue its a BST
            right_node.left=curr.left
            parent.right=curr.right
            return root
