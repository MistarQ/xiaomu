class solution:
    a=list((map(str,input().split(" "))))
    for i in range(4):
        if a[i]=="joker" or a[i]== "JOKER":
            print("ERROR")
        if a[i]=="J":
            a[i]=11
        if a[i]=="Q":
            a[i]=12
        if a[i]=="K":
            a[i]=13
        if a[i]=="A":
            a[i]=1
        a[i]=int(a[i])
    for i