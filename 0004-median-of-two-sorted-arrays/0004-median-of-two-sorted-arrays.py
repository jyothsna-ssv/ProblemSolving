class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
    
        x = len(nums1)
        y = len(nums2)
    
        low = 0
        high = x
    
        while low <= high:
            
            partX = (low + high) // 2
            partY = (x + y + 1) // 2 - partX
    
            
            maxLeftX = float('-inf') if partX == 0 else nums1[partX - 1]
            minRightX = float('inf') if partX == x else nums1[partX]
    
            maxLeftY = float('-inf') if partY == 0 else nums2[partY - 1]
            minRightY = float('inf') if partY == y else nums2[partY]
    
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                
                else:
                    return float(max(maxLeftX, maxLeftY))
            elif maxLeftX > minRightY:
                high = partX - 1
            else:
                low = partX + 1
     
    
            