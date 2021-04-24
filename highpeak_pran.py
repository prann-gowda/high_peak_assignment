# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 16:10:15 2021

@author: Pran_N_Gowda
"""\

d={}
with open ("sample_input.txt") as f:
    for line in f:
        key,value = line.split(':')
        d[key]=int(value)




sorted_values = sorted(d.values()) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in d.keys():
        if d[k] == i:
            sorted_dict[k] = d[k]
            break

#print(sorted_dict)



val = int(input("number of employees: "))
p=val
val1=p


for keys,values in sorted_dict.items():
    print(keys,' : ', values)
    val=val-1
    if val==0:
        break
    l=[]
    
l=(list(sorted_values))

print("And the difference between the chosen goodie with highest price and the lowest price is ",' : ',l [p-1] - l[0])


#to write into a file

outf = open("result.txt", "w")


for keys,values in sorted_dict.items():
    outf.writelines(keys + ' : '+str(values)+'\n') 
    val1=val1-1
    if val1==0:
        break
outf.writelines("And the difference between the chosen goodie with highest price and the lowest price is " +' : ' +str(l [p-1] - l[0])) 
    

outf.close()
