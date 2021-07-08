def main():
    s = input()
    nums = []
    words = []
    for word in s.split():
        try:
            nums.append(int(word))
        except ValueError:
            words.append(word)
    print(' '.join(words))
    print(nums)
    for i in words:
        i[0].upper() + i[1:-1] + i[-1].upper()
    words = list(map(lambda x: x.apper() if len(x) == 1 else x[0].upper() + x[1:-1] + x[-1].upper(), words))
    print(' '.join(words))
    idx = 0
    for i in range(len(nums)):
        if nums[idx] < nums[i]:
            idx = i
    print('Idx: {}, Num: {}'.format(idx, nums[idx]))
    numsPow=[]
    for i in range(len(nums)):
        if i == idx:
            continue
        numsPow.append(pow(nums[i], i))
    print(numsPow)


if __name__ == '__main__':
    main()
