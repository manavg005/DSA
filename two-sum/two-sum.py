class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp={}
        for i in range(len(nums)):
            if nums[i] not in temp:
                 temp[nums[i]]=i
            if target-nums[i] in temp.keys() and temp[target-nums[i]]!=i:
                return [temp[target-nums[i]],i]
            else:
                if target-nums[i] in temp.keys() and temp[target-nums[i]]!=i:
                    return [temp[target-nums[i]],i]