
def strOccurence(seq):
    eltOne = seq[0]
    found = 0
    allFound = 0
    for dnaElt in seq+" ":
        if dnaElt != eltOne:
            allFound = max(allFound, found)
            found = 1
            eltOne = dnaElt
        else: found+=1
    return allFound


if __name__ == "__main__":
    seq = str(input()).replace(" ", "").upper()
    print(strOccurence(seq))