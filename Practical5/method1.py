def change_case(text,style):
	
    str=text
    size=len(str)

    #lower
    if (style=='s'):
        str=str.title()
        char='S'
        str=char+str
        str=str.title()
        str=str.replace('S',' ').lstrip()
        return str

    
        #upper
    if (style=='c'):

        str1=''
        for i in range(0,size):
            
            str12=str[i].title()
            str1=str1+str12
        return str1

        # u
    if (style=='u'):

        str1=''
        for i in range(0,size):
            str12=str[i]
            if(i%2==0):
                str12=str[i].title()

            str1=str1+str12
        return str1
        

        # r
    if (style=='r'):

        str1=''
        for i in range(0,size):
            str12=str[i]
            if(i%2!=0):
                str12=str[i].title()

            str1=str1+str12
        return str1
        

print(change_case('aaaa','u'))