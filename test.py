

def interlockable(a, b):

    bina = bin(a)
    binb = bin(b)

    lena = len(str(bina))
    lenb = len(str(binb))

    result = True
    if lena >= lenb:
        for i in range(1, lenb+1):
            print(bina)
            print(binb)
            if str(binb)[-i] == "1" and str(bina)[-i] == "1":

                result = False
                break

    if lenb > lena:
        for i in range(1, lena+1):
            print(bina)
            print(binb)
            if str(bina)[-i] == "1" and str(binb)[-i] == "1":
                result = False
                break

    return result


print(interlockable(3, 6))
