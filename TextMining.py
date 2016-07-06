#AUTHOR: ADVAIT
#WRITTEN ON: 06/09/2015
#CONTAINS DATA FROM DENGUE VIRUS 4.gb FILES WITH VALIDATED UTR'S

#CODE GIVES ALL THE IMPORTANT GENOTYPE INFORMATION SUCH AS COUNTRY,HOST,ACCESSION NUMBER,5' AND 3' INFORMATION OF EACH SEROTYPE IN A .CSV FILE. 



import csv

with open(r"C:\Users\garfield\Python27\DENV4NEW.gb") as file, open(r"C:\Users\garfield\outDENV4.csv", "a+") as f: #Declare Input and Output Files
 x=file.read()
 m=x.split() #Splits Files into Strings
 writer = csv.writer(f, delimiter =",",quoting=csv.QUOTE_MINIMAL)   #instantiate CSV(Comma Separator) Package
 acc, source, isolation_source, utr5, isolate, host,host1,host2,utr3,country,collection_date = '', '', '', '', '', '', '', '', '', '', ''
 source1,source2='',''
 f_s,f_e,t_s,t_e='','','',''
 flag=False
 head= ["ACCESSION","ISOLATE","ISOLATION SOURCE","HOST","COUNTRY","COLLECTION DATE","SOURCE","5'UTR","3'UTR"] # Create columns with headings
 writer.writerow(head)
 for i in range(len(m)-1): #Parse through entire file by each string 
	if "ACCESSION" in m[i]: #Store Accession number
		acc=m[i+1]
	if '/isolate' in m[i]:  #Store Isolate Number
		isolate=m[i].split('/isolate')[1].split('\n')[0].replace(",","")
	if '/host' in m[i]:     #Store Host organism
		host1=m[i].split('/host')[1].split('\n')[0]
		host2=m[i+1]
		host=host1+" "+host2
	if "/organism" in m[i]: #Store Source Sequence
		source1= m[i-1].split("..")[0]
		f_s= source1
		source2= m[i-1].split("..")[1]
		t_e= source2
		source=  source2+" nucleotides"
	if "CDS" in m[i]:       #Store CDS Information
		f_e= m[i+1].split("..")[0]
		t_s= m[i+1].split("..")[1]
		utr5=f_s+".."+f_e   #Generate 5'UTR and 3'UTR information from Source and CDS
		utr3=t_s+".."+t_e
		flag= True
		
	if "/isolation_source" in m[i]: #Store Isolation Source
		isolation_source=m[i].split('/isolation_source')[1].split('\n')[0].replace(",","")
	if "/country" in m[i]:          #Store Country of origin
		country=m[i].split('/country')[1].split('\n')[0].replace(",","")
	if "/collection_date" in m[i]:  #Store Collection Date
		collection_date=m[i].split('/collection_date')[1].split('\n')[0]
	if flag:  #Store all information in a list and write a row in a CSV file
		flag=False
		data=[acc,isolate,isolation_source,host,country,collection_date,source,utr5,utr3]
		writer.writerow(data)
		
		
		""" 
		Sample Output in a csv ( file
		ACCESSION  |  ISOLATE |ISOLATION SOURCE | HOST | COUNTRY | COLLECTION DATE | SOURCE | 5'UTR | 3'UTR
		
		ACC1          ISOLATE1 ISOLATION SOURCE1  HOST1  COUNTRY1   COLLECTION DATE1 Source1   5'UTR1  3'UTR1 
		ACC2          ISOLATE2         ""2          ""2     ""2           ""2           ""2      ""2     ""2
		ACC3          ISOLATE3         ""3          ""3     ""3          .             .        .        .
		.              .
		.              .
		.
		ACC'N'        ISOLATE'N'       ""'N'        .         .           .             .         ""'N'    ""'N'
        """
		
	