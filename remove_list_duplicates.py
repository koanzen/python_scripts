nums = [1,1, 2, 3,3, 4, 5, 8, 9, 9, 33, 100,100]
unique = []

for num in nums:
    if num not in unique:
        unique.append(num)
print(unique)


#My Solution
# for x in nums:
#     y = nums.count(x)
#     if y > 1:
#         nums.remove(x)

# print(nums)