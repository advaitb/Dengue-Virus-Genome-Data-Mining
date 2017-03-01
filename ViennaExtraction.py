#ADVAIT
#26/12/2015

with open(r"C:\Users\garfield\Python27\15Dec15-04-38-19_1.b") as file, open(r"C:\Users\garfield\Python27\result.txt","w") as f:
	inp1=''
	inp2=''
	inp1= file.readline().replace('\n', '')
	inp2=file.readline().replace('\n', '').split('	')[0]
	flag=False
	bkts = []
	nomatch = []
	pairs = []
	i=0
	j=0
	f.writelines(" ")
	f.writelines(inp1 + '\n')
	for k in range(len(inp1)):
		f.write(str(k))
	f.writelines('\n')
	f.writelines("________________________________________________________________________" + '\n')
	for idx in range(len(inp2)):
		c = inp2[idx];
		if c == '(':
			flag=True
			i=i+1
			bkts.append(inp1[idx] +'('+str(idx)+')')
			if(flag and i==1):
				f.writelines(" Initial ss: " + ' '.join(nomatch) + '\n'+ "ss length: " + str(len(nomatch)) +'\n')
				nomatch = []
				
		elif c == '.':
			nomatch.append(inp1[idx] +'('+str(idx)+')')
			if (idx == (len(inp2)-1)):
				f.writelines( " Final ss: " + ' '.join(nomatch) + '\n'+ "Final ss length: " + str(len(nomatch)) + '\n')
				f.writelines("________________________________________________________________________" + '\n')
			
				
				
		elif c == ')':
			if len(bkts) > 0:
				pair = [bkts.pop(), inp1[idx] +'('+str(idx)+')']
				pairs.append('-'.join(pair))
				if (inp2[idx+1] != ')' or (idx == (len(inp2)-1))):
					j=j+1
					f.writelines("loop number: " + str(j) + '\n')
					f.writelines("Non bonded in this loop: " + ''.join(nomatch) + '\n'+ "  non bonded length: " + str(len(nomatch)) +'\n')
					nomatch = []
					f.writelines("bonded in this loop: " + ','.join(pairs) +'\n'+'  number of pairs: ' + str(len(pairs)) + '\n')
					pairs = []
					f.writelines("______________________________________________________________________" + '\n')
					
					
					
					
					
			else:
				continue
		else:
			continue
		
        

	

	
	
	
	
