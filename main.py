def medians(nums1,nums2):
    
    nums = nums1 + nums2
    nums.sort()
    n = len(nums)
    if n%2==0:
        m = (nums[int(n/2-1)] + nums[int(n/2)])/2
    else:
        m = nums[int((n+1)/2 - 1)]
    return(m) 

                                                        
x = input("Введите первый список через запятую:")
nums1 = x.split(',')
nums1 = [float(nums1[i]) for i in range(len(nums1))]
                                                  
y = input("Введите второй список через запятую:")
nums2 = y.split(',')
nums2 = [float(nums2[i]) for i in range(len(nums2))]
                                                
print("Среднее значение двух списков:",medians(nums1,nums2))
