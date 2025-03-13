def tabuada (n):
    n1=n*1
    n2=n*2
    n3=n*3
    n4=n*4
    n5=n*5
    n6=n*6
    n7=n*7
    n8=n*8
    n9=n*9
    n10=n*10

    return n1,n2,n3,n4,n5,n6,n7,n8,n9,n10

n=int(input("de qual numero voce quer a tabuada?"))

n1,n2,n3,n4,n5,n6,n7,n8,n9,n10 = tabuada(n)

print("a tabuada de {} é".format(n))
print("{} X 1 = {}".format(n,n1))
print("{} X 2 = {}".format(n,n2))
print("{} X 3 = {}".format(n,n3))
print("{} X 4 = {}".format(n,n4))
print("{} X 5 = {}".format(n,n5))
print("{} X 6 = {}".format(n,n6))
print("{} X 7 = {}".format(n,n7))
print("{} X 8 = {}".format(n,n8))
print("{} X 9 = {}".format(n,n9))
print("{} X 10 = {}".format(n,n10))
