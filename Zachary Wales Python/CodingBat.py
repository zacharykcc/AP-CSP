
def array_front9(nums):
  ans = False
  if nums[0:1] == 9:
    ans = True
  if nums[1:2] == 9:
    ans = True
  if nums[2:3] == 9:
    ans = True
  if str(nums[3:4]) == 9:
    ans = True
  print(nums[0:1])
  print(nums[1:2])
  print(nums[2:3])
  print(nums[3:4])

ans = array_front9([1, 2, 9, 3, 4])
print(ans)
