def bubbleSort(list):
    needNextPass = True

    k = 1
    while k < len(list) and needNextPass:
        needNextPass = False
        for i in range(len(list) - k):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                needNextPass = True
        k += 1
