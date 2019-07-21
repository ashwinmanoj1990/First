no_of_chars = 256

def getarr(str):
    count = [0] * no_of_chars
    for i in str:
        count[ord(i)] += 1
    ##print(count)
    return count

def getletter(string):
    count = getarr(string)
    ind = -1
    k = 0
    ##print(count)
    for i in string:
        if count[ord(i)] == 1:
            ind = k
            break
        k += 1
    ##print(ind)
    ##print(count[ord(i)])
    return ind

string = "salesforce"
index = getletter(string)

if index == 1:
    print (string[index])
else:
    print ("All Repeat")



