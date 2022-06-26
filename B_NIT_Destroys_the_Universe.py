
t = int(input())

for i in range(t):
    
    n = int(input())
    a = list(map(int,input().strip().split()))[:n]
    
    #adding minimum at the end and beginning
    
    zero = [0] # minimum value in the array
    a = zero+a+zero
    indx = []
    count = 0
    
    # if all elements are not zero
    if a.count(0) != len(a):

        
        #taking the index value of '0'
        
        for i in range(len(a)):
            if a[i] == 0:
                indx = indx + [i]
        

        # main program, if the difference is more than 1, then it must have elments other than '0' in berween
        for i in range(1,len(indx)):
            if indx[i]-indx[i-1] != 1:
                count = count+1
    
            
    print(count)
    

