class solution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return nums[0]
        return self.createTree(nums, 0, len(nums) - 1)

    def createTree(self, nums, left, right):
        if left > right:
            return None
        