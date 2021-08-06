# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        result: AC
        in order traversal: if we do an in order traversal on a BST, the lst produced will be guaranteed to be in increasing order
        The problem states that there is two nodes that its value being swapt. 
        If we use in order traversal to produce a list of the BST, the problem can also be interpreted as given a list of nums that         is in increasing order, there are two numbers that are swapped.
        There will be two cases:
        one which the swapped node is next to each other, i.e [1,2,4,3]
        the other which the nodes are sperated, i.e [7,4,5,6,2]
        We can't simply check for if nums[i-1] > nums[i] then swap because in case 2 there will be two instances (7,4), (6,2)
        But in both cases, we only need to swap one pair of numbers, and the instance where nums[i-1] > nums[i] can only happen             twice, anything more than that will mean the bst has more than 1 swapped pairs
        runtime: O(n), space: O(n)
        """
        lst, stack = [], []
        prev = TreeNode(float('-inf'))
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if prev.val > root.val:
                    lst.append([prev, root])
                prev = root
                root = root.right
                
        lst[0][0].val, lst[-1][1].val = lst[-1][1].val, lst[0][0].val
        
                