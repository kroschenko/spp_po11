def find_the_max(arr):
    arr.sort()
    arr_list = {}
    for index in range(len(arr)):
        try:
            difference = arr[index+1]-arr[index]
        except:
            continue
        arr_list[index] = difference
    return arr_list



def main():
    arr = list(map(int, input('Введите последовательность: ').split()))
    res_list = find_the_max(arr)
    max_key = max(res_list, key=res_list.get)
    
    if res_list[max_key] == 1:
        print(*arr)
        return
    
    print(arr[max_key])


if __name__ == "__main__":
    main()
  