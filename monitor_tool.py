# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:37:47 2023

@author: milan stojanovic
"""
import time

start_time = time.time()

print("----- Find changes in Funding and tenders portal webpage-----")
# older_file will be compared with the newer_file.
# CHANGE THE NAMES OF THE FILES acordingly!
older_file = open('ncp_ms_08_05.dat', 'r', encoding="utf-8")
redovi_1 = older_file.read().split("<strong>")
br_r_1 = len(redovi_1)

newer_file = open('ncp_ms_10_05.dat', 'r', encoding="utf-8")
redovi_2 = newer_file.read().split("<strong>")
br_r_2 = len(redovi_2)

results = open('results.dat', 'w', encoding="utf-8")

if (br_r_1 != br_r_2):
    print("WARNING: number of rows in files is not the same!")
    print("WARNING: number of rows in files is not the same!", file=results)
    
li_up_date_1 = list()
li_rec_num_1 = list()

li_up_date_2 = list()
li_rec_num_2 = list()
    
brojac_1 = 0
brojac_2 = 0

for i in range(0,br_r_1):
    if 'Update date: ' in redovi_1[i]:
        pom=redovi_1[i][0:13] + redovi_1[i][22:32] + redovi_1[i+1][0:23] + redovi_1[i+1][32:39]
        li_up_date_1.append(redovi_1[i][22:32])
        li_rec_num_1.append(redovi_1[i+1][32:39])
        brojac_1=brojac_1+1

for j in range(0,br_r_2):
    if 'Update date: ' in redovi_2[j]:
        pom=redovi_2[j][0:13] + redovi_2[j][22:32] + redovi_2[j+1][0:23] + redovi_2[j+1][32:39]
        li_up_date_2.append(redovi_2[j][22:32])
        li_rec_num_2.append(redovi_2[j+1][32:39])
        brojac_2=brojac_2+1

if (brojac_1 != brojac_2):
    print("WARNING: number of NCPs in files is not the same!")
    print("WARNING: number of NCPs in files is not the same!", file=results)

# print(brojac_1, brojac_2)

if (li_rec_num_1 == li_rec_num_2):
    print("There are no changes in Record control numbers!")
    print("There are no changes in Record control numbers!", file=results)
else:
    print("The lists are not the same!")
    print("The lists are not the same!", file=results)
    # find elements in list of record control number_2, which is newer list, that are not present in older list _1
    result_1 = list(set(li_rec_num_2).difference(li_rec_num_1))
    print("Record control number(s): ", result_1, "is/are new!")
    print("Record control number(s): ", result_1, "is/are new!", file=results)
    
if (li_up_date_1 == li_up_date_2):
    print("There are no changes in Update date fields!")
    print("There are no changes in Update date fields!", file=results)
else:
    print("The lists are not the same!")
    print("The lists are not the same!", file=results)
    # find elements in list of update dates_2, which is newer list, that are not present in older list _1
    result_2 = list(set(li_up_date_2).difference(li_up_date_1))
    print("Update date(s): ", result_2, "is/are new!")
    print("Update date(s): ", result_2, "is/are new!", file=results)

older_file.close()
newer_file.close()
results.close()

round(time.time() - start_time, 2)
print ("---------- %s seconds ----------" % round(time.time() - start_time, 4))
print ("---------- kraj main-a ---------")
