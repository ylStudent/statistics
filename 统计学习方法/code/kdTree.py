import numpy as np
class Node:
    def __init__(self, val) -> None:
        self.left = None
        self.right = None
        self.val = val

class kdTree:
    def __init__(self, root, k) -> None:
        self.root = root
        self.k = k
    
    def insert(self,nums):

        return self.insert_with_depth(nums, 0)

    
    def insert_with_depth(self, nums, j):
        # 找到当前切分的轴
        l = j % self.k
        n = len(nums)
        if not n:
            return None
        nums = sorted(nums, key=lambda x: x[l])
        node = Node(nums[n//2])
        node.left = self.insert_with_depth(nums[:n//2], j+1)
        node.right = self.insert_with_depth(nums[n//2+1:], j+1)
        return node

nums = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
t = kdTree(Node(None), 5)
root = t.insert(nums)
print(root.left.val)


    

        
        
        
        
        
    
