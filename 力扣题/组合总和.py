from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result_list = []
        if sum(result_list) <target:
            for i in range(0,len(candidates)):
                result_list.append(candidates[i])


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
