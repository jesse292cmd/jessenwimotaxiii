import csv
fn = 'trip_data_6.csv'
f = open(fn,'r')
reader = csv.reader(f)
n=0
for row in reader:
    print(row)
    if n % 1000000 ==0:
        print(n)
        n+=1
        print (n)
    

