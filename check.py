#ADVAIT
#23/01/2016

import csv, pprint

with open("outDENV417.csv") as f:
    csv_reader = csv.reader ( f )
    file1_tup = { tuple(row) for row in csv_reader }

with open("D.csv") as fa:
    csv_reader = csv.reader ( fa )
    match = [ row for row in csv_reader if (tuple(row[0]) in file1_tup)]

pprint.pprint (match)