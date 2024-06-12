

def find_max_slicing(num_list, k):
    result_list = []
    for i in range(len(num_list) - k + 1):
        result_list.append(max(num_list[i:i + k]))
    return result_list


if __name__ == "__main__":
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    while True:
        try:
            k = int(input('Nhap k (k >= 1): '))
            if k < 1:
                raise ValueError
            break
        except ValueError:
            print('k must be int (k >= 1)')
    max_in_slicing_k_elements = find_max_slicing(num_list=num_list, k=k)
    print(max_in_slicing_k_elements)
