def find_the_max(arr):
    arr.sort()
    arr_list = {}
    for i in range(len(arr) - 1):
        try:
            difference = abs(arr[i + 1]) - abs(arr[i])
        except IndexError:
            continue
        if difference < 0:
            arr_list[i] = abs(difference)
        else:
            arr_list[i + 1] = difference

    return arr_list


def main():
    arr = list(map(int, input("Введите последовательность: ").split()))
    sorted_arr = sorted(arr)
    res_list = find_the_max(sorted_arr)
    max_key = max(res_list, key=res_list.get)
    if res_list[max_key] == 1:
        print(*sorted_arr)
        return
    print(sorted_arr[max_key])


if __name__ == "__main__":
    main()
