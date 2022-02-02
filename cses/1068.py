

def weirdAlgo(number):
    res = [number]
    while (number > 1):
        if number%2 ==0:
            number = number // 2
        esle: number = number*3 + 1
        res.append(number)
    print(*res) # * unpacks the list