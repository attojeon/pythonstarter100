# input split 사용하기
n = input()             # 입력 : 1
print(n)

nums = input()          # 입력 : 1 2 3
print(nums)
print(type(nums))

nums = input().split()  # 입력 : 1 2 3 
print(nums)

nums = input().split()  # 입력 : 1 2 3 
nums2 = []
for n in nums:
    nums2.append(int(n))
print(nums2)

nums3 = [int(n) for n in input().split()]
print(nums3)

