class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []

        for i, num in enumerate(nums):
            product = 1

            for j, n in enumerate(nums):
                if i == j:
                    continue
                product *= n
            res.append(product)
        
        print(res)

        return res