ar1 = [1,2,3,4,5,6,9]
ar2 = [1,2,4,6,7,8]
ar3 = []
i=0
j=0
while(i in range(len(ar1)) and j in range(len(ar2))):
    sum = int(ar1[i] + ar2[j])
    print(sum)
    if sum < 10:
        ar3.append(sum)
    else:
        su = str(sum)
        s = su.split
        for a in su:
            ar3.append(int(a))

    i+=1
    j+=1
while i in range(len(ar1)):
    ar3.append(i)
    i+=1
 
while j in range(len(ar2)):
    ar3.append(j)
    j+=1


print(ar3)
