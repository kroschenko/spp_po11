def merge(nums1_, m_, nums2_, n_):
    p1 = m_ - 1
    p2 = n_ - 1
    p = m_ + n_ - 1

    while p1 >= 0 and p2 >= 0:
        if nums1_[p1] > nums2_[p2]:
            nums1_[p] = nums1_[p1]
            p1 -= 1
        else:
            nums1_[p] = nums2_[p2]
            p2 -= 1
        p -= 1

    while p2 >= 0:
        nums1_[p] = nums2_[p2]
        p2 -= 1
        p -= 1


if __name__ == "__main__":
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
