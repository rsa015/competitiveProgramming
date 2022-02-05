
def inArray(n, array):
    prev = seq[0]
    res = 0
    
    for elt in array:
        if elt < prev:
            res += prev-elt
        else: prev = elt
    print(res)

if __name__ == "__main__":
    n = int(input())
    seq = list(map(int, input().split()))
    inArray(n, seq)
    