import csv
import re
import datetime
from itertools import islice
b=[]
def file_reader(obj):
    reader=csv.reader(obj)
    next(reader)
    for row in reader:
        s="".join(row)
        x=re.findall(r'\$(.*)\$',s) #use of regular exprssion to extract the email address
        y="".join(x)
        b.append(y)
    c=list(set(b))
    print("The unique email addresses are -",*c,sep="\n")
    days_count(obj,row)
def days_count(obj,row):
    l=re.findall(r'\d{2}/\d{2}/\d{2}',"".join(row))#regular expression 
    r="".join(l)
    date=int(r[0:2])
    month=int(r[3:5])
    year=int(r[6:8])+2000
    tday=datetime.date.today() #Today's date
    t=datetime.date(year,month,date)
    print("The last date of conversation is -",t)
    n=tday-t
    print("\nThe no of days elapsed from last conversation is -",n)
def check_array():
    e=["Opencv","python","tell","when"] #An array for searching into the csv file 
    d=[]
    with open("myexcel.csv") as a:
        reader=csv.reader(a)
        c=list(reader)
        for row in c:
            s="".join(row)
            for i in e:
                if(s.find(str(i))!=-1):
                    d.append(i)
        t=list(set(d)) #List of having common words in array and words in file 
        print("\nThe words that match with the contents of file are -",t)
        for q in range(0,len(t)):
            c[q+1].append(t[q])
    with open("myexcel.csv",'w',newline='') as f:
        write=csv.writer(f)
        write.writerows(c)  #writes into the csv file 
    print("You can see the csv file for new column")
with open("myexcel.csv") as a:
    file_reader(a)
check_array()
