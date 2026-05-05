class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        num_list = []
        for key in freq.keys():
            num_list.append(tuple([key, freq.get(key)]))

        num_list.sort(key=lambda n_list:n_list[1], reverse=True)
        
        res = []
        for i in range(k):
            res.append(num_list[i][0])

        return(res)
        