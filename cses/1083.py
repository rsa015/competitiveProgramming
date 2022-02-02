
def missingNum(number, seq):
    seqNumber = [digits for digits in range(1, number+1)]
    seqSum = sum(seq)
    sumNum = sum(seqNumber)
    missDig = sumNum - seqSum
    print(missDig)


if __name__ == "__main__":
    number = int(input())
    seq = list(map(int, input().split()))
    missingNum(number, seq)