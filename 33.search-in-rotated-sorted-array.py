class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        hig=len(nums)-1
        while low<=hig:
            mid=low+(hig-low)//2
            if nums[mid]== target:
                return mid
            if nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    hig=mid-1
                else: 
                    low=mid+1
            else:
                if nums[hig]>=nums[mid]:
                    if nums[mid]<target<=nums[hig]:
                        low=mid+1
                    else:   
                        hig=mid-1
        return -1
