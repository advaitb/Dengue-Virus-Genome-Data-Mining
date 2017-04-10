'''
AUTHOR: ADVAIT 
DATE: 10/04/2017
'''

import csv

print 'Your range'
start,end = raw_input().split('-')
start = int(start)
end = int(end)
origin = []
data = []
row = []
w =0

with open('/home/advaitb/Downloads/DENV1_1303.gb','r') as file, open('/home/advaitb/DEN1_'+str(start)+'_'+str(end)+'.csv','a+') as f:

	x = file.read()
	m = x.split()
	writer = csv.writer(f, delimiter =",",quoting=csv.QUOTE_MINIMAL) 
	acc, seq = '',''
	flag = True
	header = ['ACCESSION','SEQUENCE']
	writer.writerow(header)
	for i in xrange(len(m)-1):
		if m[i] == 'ACCESSION':
			acc = m[i+1]
		if  m[i] == 'ORIGIN':
			while m[i] != '//':
				origin.append(m[i])
				i+=1
			for i in origin:
				if i.isdigit():
					pass
				else:
					data.append(i)
			seq = ''.join(data)
			data = []
			seq = seq[6:]
			seq = seq[start-1:end-1]
			row = [acc,seq]
			writer.writerow(row)

			'''
					i+=1
				else:
					#print m[i]
					i+=1
			
			if m[i].isdigit():
				print m[i]
				i+=1
			else:
				if m[i] == '//':
					seq = ''.join(origin)
					seq = seq[6:]
					seq = seq[start-1:end-1]
					data = [acc,seq]
					writer.writerow(data)
				else:
					print m[i]
					origin.append(m[i])
					i+=1
			'''
					


#with open(r"C:\Users\garfield\Python27\DENV4NEW.gb") as file, open(r"C:\Users\garfield\outDENV4.csv", "a+") as f: