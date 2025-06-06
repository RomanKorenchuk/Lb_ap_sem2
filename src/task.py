def is_subarray(nums1, nums2):
    if not nums1:
        return True 
    index = 0
    for num in nums2:
        if num == nums1[index]:
            index += 1
            if index == len(nums1):
                return True
    return False
