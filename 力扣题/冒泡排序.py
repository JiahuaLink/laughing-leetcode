def bubble_sort(arr):

    length = len(arr)
    for i in range(length):
        for j in range(1, length-i):
            if arr[j] < arr[j-1]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

    return arr


if __name__ == '__main__':

    arr = [8, 5, 45, 9, 1, 2, 3, 6, 4, 9, 52, 44]
    bubble_sort(arr)
    print(arr)
 