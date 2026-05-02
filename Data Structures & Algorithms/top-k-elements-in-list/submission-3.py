class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        freq_s = []

        for key in freq.keys():
            freq_s.append(tuple((key, freq.get(key))))
        
        freq_s.sort(key=lambda item: item[1], reverse=True)

        res = []
        for i in range(k):
            res.append(freq_s[i][0])

        return res