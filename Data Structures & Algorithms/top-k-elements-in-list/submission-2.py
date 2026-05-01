class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Get Frequency
        map = {}
        for n in nums:
            map[n] = 1 + map.get(n, 0)

        # Flip key and value
        flipped_map = []
        for key, value in map.items():
            flipped_map.append([value, key])

        # sort in descending order
        flipped_map.sort(reverse=True)

        # print the k elements
        res = []
        for i in range(k):
            res.append(flipped_map[i][1])

        return res