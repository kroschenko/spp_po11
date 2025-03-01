def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    
   
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
   
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1


m = int(input("Введите количество элементов в nums1 (m): "))
n = int(input("Введите количество элементов в nums2 (n): "))


print("Введите элементы списка nums1 (отсортированного в неубывающем порядке):")
nums1 = []
for i in range(m):
    nums1.append(int(input(f"nums1[{i}]: ")))

nums1.extend([0] * n)


print("Введите элементы списка nums2 (отсортированного в неубывающем порядке):")
nums2 = []
for i in range(n):
    nums2.append(int(input(f"nums2[{i}]: ")))


merge(nums1, m, nums2, n)


print("Объединенный и отсортированный список nums1:", nums1)