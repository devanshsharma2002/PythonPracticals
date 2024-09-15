def bin_add(bin1,bin2):
	bin1 = list(map(int,bin1))
	bin2 = list(map(int,bin2))
	carry = 0
	for i in range(-1,-(len(bin1)+1),-1):
		if bin1[i] == 1 and bin2[i] == 1:
			bin1[i] = 0 + carry
			carry = 1
		else:
			bin1[i] += bin2[i] + carry
			carry = 0
			if bin1[i] == 2:
				bin1[i]=0
				carry = 1
			
	return (str(carry) + ''.join(map(str,(bin1))))
	
def bin_sub(bin1,bin2):
	validele = ['-','b','0','1','B']
	for i in bin1:
		if i in validele:
			pass
		else:
			return "Enter valid binary string"
	for i in bin2:
		if i in validele:
			pass
		else:
			return "Enter valid binary string"
			
	if bin1.startswith(("-0b","-0B")):
		bin1 = bin1[3:]
		b1 = 'n'
	elif bin1.startswith(("0b","0B")):
		bin1 = bin1[2:]
		b1 = 'p'

	if bin2.startswith(("-0b","-0B")):
		bin2 = bin2[3:]
		b2 = 'n'
	elif bin2.startswith(("0b","0B")):
		bin2 = bin2[2:]
		b2 = 'p'
	
	length = max(len(bin1),len(bin2))
	if len(bin1) > len(bin2):
		bin2 = bin2.zfill(length)
	else:
		bin1 = bin1.zfill(length)
	
	if (b1 == 'n' and b2 == 'p') or (b1 == 'p' and b2 == 'n'):
		if b1 == 'n':
			return '-' + bin_add(bin1,bin2)
		else:
			return bin_add(bin1,bin2)
	flag = 0
	
	if bin1 < bin2:
		bin1,bin2 = bin2,bin1
		flag = 1
	
	
	

	bin1 = list(map(int,bin1))
	bin2 = list(map(int,bin2))
	bin1c = bin1.copy()
	for i in range(-1,-(length+1),-1):
		if bin1[i] >= bin2[i]:
			bin1[i] -= bin2[i]
		else:
			try:	
				bin1[i] = 1
				a = bin1c[i-1::-1]
				indx = a.index(1)
				bin1[len(a) -1-indx] = 0
				for i in range(1,len(a)):
					if bin1[len(a) - 1 -indx + i] == 0:
						bin1[len(a) - 1 -indx + i] = 1
					else:
						break
					
				
			except ValueError:
				print('Error')
	if flag :
		return 	'-0b'+(''.join(map(str,bin1)))
	return ''.join(map(str,bin1))

print(bin_sub('0B0','0b1'))
