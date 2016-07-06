#AUTHOR: ADVAIT
#WRITTEN ON: 28/08/2015
#CONTAINS DATA FROM DENGUE VIRUS 4.gb FILES WITH VALIDATED UTR'S

#CODE GETS INFORMATION BETWEEN ANY KEYWORDS, CAN BE USED TO GET SEQUENCE INFO IF FIRST 10 BASES AND LAST 10 BASES ARE KNOWN

import os
directory = os.getcwd()
path = directory + "/" + "DENV4.gb"

newFileName = directory + '/' + "data" + ".txt" 
newFile = open(newFileName, 'w')
#CREATED OUTPUT AND INPUT FILES FROM PRESENT WORKING DIRECTORY
keywords = [["ORIGIN","//"]] # CAN ADD MORE KEYWORDS IN THIS LIST!
word="ACCESSION"

finp = open( path, 'r')	
objectLines = finp.readlines()

startf=False

for keyword in keywords: #SEARCHES FOR KEYWORDS
	for line in objectLines:
	    
		if word in line:
		  newFile.write(line)
        
		if startf and keyword[1] in line: #IF LAST KEYWORD FOUND SET FALSE AND WRITE LINE
			startf=False
			newFile.write("\n")
			newFile.write("---------------------------------------------------------\n")
			
			
		if startf: 
			 newFile.write(line)

		if keyword[0] in line: #IF FIRST KEYWORD FOUND SET TRUE
			  startfound=True
	
		

newFile.close()

"""
SAMPLE OUTPUT
EXAMPLE:
KEYWORD 1= FIRST 10 NUCLEOTIDES
KEYWORD 2= LAST 10 NUCLEOTIDES
.....
THEN OUTPUT= 
FIRST 10 NUCLEOTIDES 
NEXT 10 NUCLEOTIDES
NEXT 10 NUCLEOTIDES
.
.
.

LAST 10 NUCLEOTIDES.