patternnumber=4

num=patternnumber+2
descendingcount=0
ascendingcount=num
#upperpattern
for i in range(0,(2*num)+2):
    if (i==0):
        print(' '*(num+1),'+',' '*(num+1))
    if (i==1):
        print(' '*(num),'+','+')
        ascendingcount-=1
        descendingcount+=1
    if(i>1):
        for i in range(2,(2*num)+2):
            while (i<=ascendingcount-1):
                print(' '*ascendingcount,'+',' '*((2*descendingcount)-1),'+')
                ascendingcount-=1
                descendingcount+=1
#middlepattern
if(patternnumber==1):
    print('  ','+',patternnumber,'+')
else:
    if(patternnumber>0):    
        for i in range(patternnumber+1,(2*patternnumber)+2):
            
            if (i==((patternnumber*2)+1)):
                print('  ','+',' '*(patternnumber-2),patternnumber,' '*(patternnumber-2),'+')

#lowerpattern
reducingnum=patternnumber
for i in range(0,patternnumber):
    if(i<patternnumber-1):
        print(' '*2,' '*i,'-',' '*(2*reducingnum-3),'-')
        reducingnum-=1
   
    if (i==patternnumber-1):
        print(' '*(num),'-','-')
print(' '*(num+1),'-',' '*(num+1))