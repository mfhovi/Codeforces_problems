# list = [1, 2, 'asdas', (1,2,3)] , here 4 elements in this list, can be called array of strings/ arrays
t = int(input())
for i in range(0,t):
    nm = input()
    nm = list(nm.split(" ")) #string to list convert, here the array is splited where " " is found and the elements are kept in a list
    a = input()
    a = list(a.split(" "))
    count = 0
    sum = 0

    while count < len(a):
        sum = sum + int(a[count])
        count+=1

    EnergyNeeded = sum
    if int(nm[1]) < EnergyNeeded:
        print(EnergyNeeded-int(nm[1]))
    else:
        print(0)
    