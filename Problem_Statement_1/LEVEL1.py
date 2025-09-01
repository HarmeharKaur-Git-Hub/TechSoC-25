print("Enter 1 to encode and 2 to decode a message")
opt=int(input())
if opt==1:
    z=int(input("Enter by how much you want to shift:"))
    x=input("Enter the message:")
    #convert string into a list of characters
    list1=list(x)
    # make a list of their ASCII values
    list2=[]
    for n in list1:
        list2.append(ord(n))
    # shift the ASCII values of alphabets
    list3=[]
    for i in list2:
    #for capital letters
        if i in range(65,91):
            if i in range(65,91-z):
                j=i+z
            else:
            #j=64+z-(90-i)
                j=z+i-26
    #for small letters
        elif i in range(97,123):
            if i in range(97,123-z):
                j=i+z
            else:
            #j=96+z-(122-i)
                j=z+i-26
    #for anything other than letters
        else:
            j=i
        list3.append(j)
    #convert new ASCII values to their respective characters
    list4=[]
    for m in list3:
        list4.append(chr(m))
    #convert the list of new charcters to a string
    y=''.join(list4)
    print("The encoded message is :")
    print(y)
else:
    z=int(input("By how much has the message been shifted?:"))
    x=input("Enter the message:")
    #convert string into a list of characters
    list1=list(x)
    # make a list of their ASCII values
    list2=[]
    for n in list1:
        list2.append(ord(n))
    # shift the ASCII values of alphabets
    list3=[]
    for i in list2:
    #for capital letters
        if i in range(65,91):
            if i in range( 65+z,91):
                j=i-z
            else:
            #i=64+z-(90-j)
                j=i-z+26
    #for small letters
        elif i in range(97,123):
            if i in range(97+z,123):
                j=i-z
            else:
            #i=96+z-(122-j)
                j=i-z+26
    #for anything other than letters
        else:
            j=i
        list3.append(j)
    #convert new ASCII values to their respective characters
    list4=[]
    for m in list3:
        list4.append(chr(m))
    #convert the list of new charcters to a string
    y=''.join(list4)
    print("The decoded message is :")
    print(y)
