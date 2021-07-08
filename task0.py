import random


def main():
    # 1
    print('1')
    arr = random.sample(range(-100, 100), 30)
    print('Arr:', arr)
    idx = 0
    for i in range(len(arr)):
        if arr[idx] < arr[i]:
            idx = i
    print('Idx: {}, Num: {}'.format(idx, arr[idx]))
    arrOdd = new_func(arr)
    print(sorted(arrOdd, reverse=True))
    # 2
    print('2')
    arr = random.sample(range(-100, 100), 30)
    print('Arr:', arr)
    for i in range(len(arr) - 1):
        if arr[i] < 0 and arr[i + 1] < 0:
            print(arr[i], arr[i + 1])

def new_func(arr):
    arrOdd = list(filter(lambda num: (num % 2 == 0), arr))
    return arrOdd


if __name__ == '__main__':
    main()
