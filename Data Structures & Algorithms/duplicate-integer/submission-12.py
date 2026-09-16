class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
            Create a hashmap
            Enter each value in a hashmap
            If a value has been detected, return true
            Otherwise, return false at the end of the list
            
            O(n) solution
            O(1) space
            O(1) Lookup for the hashmap
        ''' 
        map = {}

        for i in nums:
            if i in map: return True
            map[i] = i
        
        return False
            
