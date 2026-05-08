class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n_set = set(numbers)
        front = 0
        back = len(numbers) - 1
        while True:
            addition = numbers[front] + numbers[back]
            if addition == target: return [front + 1, back + 1]
            if addition < target: front += 1
            if addition > target: back -= 1
        
        
        