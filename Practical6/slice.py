def slice (objection, end , start=0):
    if (type(objection)==list):
        empty=[]
        for i in range (start,end+1):
            empty.append(objection[i])
        return empty

    if(type(objection)==str):
        empty=''
        for i in range(start,end+1):
            empty=(empty+objection[i])
        return empty
    

print (slice('ahbh',1,))