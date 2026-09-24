class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for li in matrix:
            if target <= li[(len(li) - 1)]:
                l, r = 0, len(li) - 1
                print(li)
                while l <= r:
                    half = (l + r) // 2
                    if li[half] == target: return True
                    match target > li[half]:
                        case True: 
                            l = half + 1
                        case _: 
                            r = half - 1
                break
        return False
        