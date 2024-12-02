months_to_days={'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31,'Aug':30,'Sep':30,'Oct':31,'Nov':30,'Dec':31}
day_names=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
def display_grid(d,row=5,col=7):
    c=''
    c+=(('.'+'-'*5)*(col)+'.')+'\n'
    c+=('|'+'  |'.join(day_names).center(7)+'  |')+'\n'
    
    c+=(('.'+'-'*5)*(col)+'.')+'\n'
    for i in range(row):
        c+=('|')
        for j in range(col):
            c+=(f"{d[i][j]}".center(5))+'|'
        c+='\n'
        c+=(('.'+'-'*5)*(col)+'.')+'\n'
    return c
    




def cal_printer(mm=1,yy=2020):

  
    c=''
    month ={1:'January', 2:'February', 3:'March',  
            4:'April', 5:'May', 6:'June', 7:'July', 
            8:'August', 9:'September', 10:'October', 
            11:'November', 12:'December'} 
    
    # code below for calculation of odd days 
    day =(yy-1)% 400
    day = (day//100)*5 + ((day % 100) - (day % 100)//4) + ((day % 100)//4)*2
    day = day % 7
    
    nly =[31, 28, 31, 30, 31, 30,  
        31, 31, 30, 31, 30, 31] 
    ly =[31, 29, 31, 30, 31, 30,  
        31, 31, 30, 31, 30, 31] 
    s = 0
    
    if yy % 4 == 0: 
        for i in range(mm-1): 
            s+= ly[i] 
    else: 
        for i in range(mm-1): 
            s+= nly[i] 
    
    day += s % 7
    day = day % 7
    
    # variable used for white space filling  
    # where date not present 
    space ='' 
    space = space.rjust(3, ' ') 
    
    # code below is to print the calendar 
    c+=((month[mm]+' '+ str(yy)).center(20,'-')) +' '+'\n'
    c+=('Su '+ 'Mo '+ 'Tu '+ 'We '+ 'Th '+ 'Fr '+ 'Sa ') +'\n'
    no_of_days=0
    
    if mm == 9 or mm == 4 or mm == 6 or mm == 11:  
        no_of_days=32
        for i in range(31 + day): 
            if day==6:
                space=''
            if i<= day: 
                c+=(space) 
            else: 
                c+=("{:02d}".format(i-day)) +'|'
                if (i + 1)% 7 == 0: 
                    c+='\n'
    elif mm == 2: 
        if yy % 4 == 0: 
            p = 30
            no_of_days=p
        else: 
            p = 29
            no_of_days=p
            
        for i in range(p + day): 
            
            if i<= day: 
                c+=(space) 
            else: 
                c+=("{:02d}".format(i-day)) +'|'
                if (i + 1)% 7 == 0: 
                    c+='\n' 
    else: 
        no_of_days=31
        for i in range(32 + day): 
            
            if day==6:
                space=''    
            if i<= day: 
                c+=(space) 
            
            else: 
                c+=("{:02d}".format(i-day)) +'|'
                if (i + 1)% 7 == 0: 
                    c+='\n'
    return c+'   '*((no_of_days-(day))%7)




def cal_printer_print(yy,row=4,col=3,fillchar='-'):
    jan=cal_printer(1,yy).splitlines()
    feb=cal_printer(2,yy).splitlines()
    mar=cal_printer(3,yy).splitlines()
    apr=cal_printer(4,yy).splitlines()
    may=cal_printer(5,yy).splitlines()
    june=cal_printer(6,yy).splitlines()
    july=cal_printer(7,yy).splitlines()
    aug=cal_printer(8,yy).splitlines()
    sep=cal_printer(9,yy).splitlines()
    octo=cal_printer(10,yy).splitlines()
    nov=cal_printer(11,yy).splitlines()
    dec=cal_printer(12,yy).splitlines()
    months_cal=[jan,feb,mar,apr,may,june,july,aug,sep,octo,nov,dec]
    abcd=input("Enter your Format: \n1->3X4\n2->4X3\n3->6X2\n4->12X1\n5->2X6:")
    if (int(abcd)==1):
        x='3X4'
    elif (int(abcd)==2):
        x='4X3'
    elif (int(abcd)==3):
        x='6X2'
    elif (int(abcd)==4):
        x='12X1'
    elif (int(abcd)==5):
        x='2X6'
    elif(int(abcd) not in range(1,6)):
        x='3X4'

        

    if x=='3X4':
        for i in range(7):
            print(jan[i]+'   '+feb[i]+'   '+mar[i]+'   ')
        print(fillchar*69)
        for i in range(7):
            print(apr[i]+'   '+may[i]+'   '+june[i]+'   ')
        print(fillchar*69)
        for i in range(7):
            print(july[i]+'   '+aug[i]+'   '+sep[i]+'   ')
        print(fillchar*69)
        for i in range(7):
            print(octo[i]+'   '+nov[i]+'   '+dec[i]+'   ')
        print(fillchar*69)
    elif x=='4X3':
        for i in range(7):
            print(jan[i]+'   '+feb[i]+'   '+mar[i]+'   '+apr[i])
        print()
        for i in range(7):
            print(may[i]+'   '+june[i]+'   '+july[i]+'   '+aug[i])
        print()
        for i in range(7):
            print(sep[i]+'   '+octo[i]+'   '+nov[i]+'   '+dec[i])
        print()
    elif x=='2X6':
        for i in range(7):
            print(jan[i]+'   '+feb[i]+'   '+mar[i]+'   '+apr[i]+'   '+may[i]+'   '+june[i])
        print()
        for i in range(7):
            print(july[i]+'   '+aug[i]+'   '+sep[i]+'   '+octo[i]+'   '+nov[i]+'   '+dec[i])
        print()
    elif x=='12X1':
        for i in range(7):
            print(jan[i])
        print()
        for i in range(7):
            print(feb[i])
        print()
        for i in range(7):
            print(mar[i])
        print()
        for i in range(7):
            print(apr[i])
        print()
        for i in range(7):
            print(may[i])
        print()
        for i in range(7):
            print(june[i])
        print()
        for i in range(7):
            print(july[i])
        print()
        for i in range(7):
            print(aug[i])
        print()
        for i in range(7):
            print(sep[i])
        print()
        for i in range(7):
            print(octo[i])
        print()
        for i in range(7):
            print(nov[i])
        print()
        for i in range(7):
            print(dec[i])
        print()
    elif x=='6X2':
        for i in range(7):
            print(jan[i]+'   '+feb[i])
        print()
        for i in range(7):
            print(mar[i]+'   '+apr[i])
        print()
        for i in range(7):
            print(may[i]+'   '+june[i])
        print()
        for i in range(7):
            print(july[i]+'   '+aug[i])
        print()
        for i in range(7):
            print(sep[i]+'   '+octo[i])
        print()
        for i in range(7):
            print(nov[i]+'   '+dec[i])
        print()
        



        
            


            
                
y=eval(input("enter your year:"))
z=input("enter filler character:")
print(cal_printer_print(y,fillchar=z))












#from_Sun=[['1   ','2   ','3   ','4   ','5   ','6   ','7   '],['8   ','9   ','10  ','11  ','12  ','13  ','14  '],['15  ','16  ','17  ','18  ','19  ','20  ','21  '],['22  ','23  ','24  ','25  ','26  ','27  ','28  '],['29  ','30  ','31  ','    ','    ','    ','    ']]

#a1=display_grid(from_Sun).splitlines()
#a2=display_grid(from_Sun).splitlines()
#for i in range(12):
   
#    print(a1[i]+'             '+a2[i]) 

