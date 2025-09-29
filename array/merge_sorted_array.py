nums1 = []
nums2 = []

m = int(input("Enter a number"))
n = int(input("Enter another number"))

for i in range(m):
    nums1.append( input("Enter an element"))

for j in range(n):
    nums2.append(input("Enter an element"))

nums1.extend(nums2)
nums1.sort()

print(nums1)
