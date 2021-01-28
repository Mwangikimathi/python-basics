array1 = ([1, 2, 6]) 
array2 = ([6, 1, 2, 3])
array3 = ([13, 6, 1, 2, 3])

def first_last6(nums):
  if nums[0] == 6:
    return True
  elif nums[-1] == 6:
    return True
  else:
    return False

ar1 = first_last6(array1)
print(ar1)

ar2 = first_last6(array2)
print(ar2)

ar3 = first_last6(array3)
print(ar3)