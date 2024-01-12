import time
import pandas as pd
start_time = time.time()

old_date='2023_12_20'
new_date='2024_01_12'



### ----------------------------------------------------------- OLDER FILE --------------------------------------------------
file_old_ms='ncp_ms_'+old_date+'.dat'
file_old_rest='ncp_rest_'+old_date+'.dat'

print("----- Open the older files for reading .....")
input_file_ms = open(file_old_ms, 'r', encoding="utf-8")
input_file_rest = open(file_old_rest, 'r', encoding="utf-8")
lines_in_ms = input_file_ms.read().split("<strong>")
lines_in_rest = input_file_rest.read().split("<strong>")
no_lin_in_ms = len(lines_in_ms)
no_lin_in_rest = len(lines_in_rest)

print("----- Creating lists .....")
country_in = list()
names_in = list()
up_date_in = list()
rec_num_in = list()
count_in_ms = 0
count_in_rest = 0
count_check = 0

print("----- Reading data from file for Member states .....")
for i in range(0,no_lin_in_ms):
    if 'Count' in lines_in_ms[i]:
        pom0=lines_in_ms[i].split('<')
        for j in range(len(pom0)):
            if 'Count' in pom0[j]:
                pom00=pom0[j].split(':')
                count_in_ms=int(pom00[1])

    if 'Person of contact:' in lines_in_ms[i]:
        pom1=lines_in_ms[i-1].split('<')
        country=pom1[0][:-6]
        country_in.append(country)

        pom2=lines_in_ms[i].split('>')
        name=pom2[1][:-3]
        names_in.append(name)

        pom3=lines_in_ms[i+6].split('>')
        up_date_temp=pom3[1][:-2]
        up_date_in.append(up_date_temp)

        pom4=lines_in_ms[i+7].split('>')
        rec_num_temp=pom4[1][:-4]
        rec_num_in.append(int(rec_num_temp))
        
        count_check=count_check+1

print("----- Reading data from file for rest of the countries .....")
for i in range(0,no_lin_in_rest):
    if 'Count' in lines_in_rest[i]:
        pom0=lines_in_rest[i].split('<')
        for j in range(len(pom0)):
            if 'Count' in pom0[j]:
                pom00=pom0[j].split(':')
                count_in_rest=int(pom00[1])

    if 'Person of contact:' in lines_in_rest[i]:
        pom1=lines_in_rest[i-1].split('<')
        country=pom1[0][:-6]
        country_in.append(country)

        pom2=lines_in_rest[i].split('>')
        name=pom2[1][:-3]
        names_in.append(name)

        pom3=lines_in_rest[i+6].split('>')
        up_date_temp=pom3[1][:-2]
        up_date_in.append(up_date_temp)

        pom4=lines_in_rest[i+7].split('>')
        rec_num_temp=pom4[1][:-4]
        rec_num_in.append(int(rec_num_temp))
        
        count_check=count_check+1

print("----- Checking if all adds up .....")

if count_in_ms+count_in_rest != count_check:
    print('Count number at the begining of file is not same as the number of NCPs in the file!')

if len(country_in) != len(names_in) != len(up_date_in) != len(rec_num_in):
    print('Lists are not the same size!')

### Create dataframe of all lists already created
list_of_lists = list(zip(names_in, country_in, rec_num_in, up_date_in))
df_old = pd.DataFrame(list_of_lists, columns=['name', 'country', 'rec_num', 'update_date'])
print("===== Dataframe is ready =====")

# print(df_old)
df_file_name='database_of_NCPs'+old_date+'.csv'
df_old.to_csv(df_file_name, sep=',', index=False)
print("----- Dataframe printed to file -----")

input_file_ms.close()
input_file_rest.close()



### ----------------------------------------------------------- NEWER FILE --------------------------------------------------
file_new_ms='ncp_ms_'+new_date+'.dat'
file_new_rest='ncp_rest_'+new_date+'.dat'

print("----- Open the newer files for reading .....")
input_file_ms = open(file_new_ms, 'r', encoding="utf-8")
input_file_rest = open(file_new_rest, 'r', encoding="utf-8")
lines_in_ms = input_file_ms.read().split("<strong>")
lines_in_rest = input_file_rest.read().split("<strong>")
no_lin_in_ms = len(lines_in_ms)
no_lin_in_rest = len(lines_in_rest)

print("----- Creating lists .....")
country_in = list()
names_in = list()
up_date_in = list()
rec_num_in = list()
count_in_ms = 0
count_in_rest = 0
count_check = 0

print("----- Reading data from file for Member states .....")
for i in range(0,no_lin_in_ms):
    if 'Count' in lines_in_ms[i]:
        pom0=lines_in_ms[i].split('<')
        for j in range(len(pom0)):
            if 'Count' in pom0[j]:
                pom00=pom0[j].split(':')
                count_in_ms=int(pom00[1])

    if 'Person of contact:' in lines_in_ms[i]:
        pom1=lines_in_ms[i-1].split('<')
        country=pom1[0][:-6]
        country_in.append(country)

        pom2=lines_in_ms[i].split('>')
        name=pom2[1][:-3]
        names_in.append(name)

        pom3=lines_in_ms[i+6].split('>')
        up_date_temp=pom3[1][:-2]
        up_date_in.append(up_date_temp)

        pom4=lines_in_ms[i+7].split('>')
        rec_num_temp=pom4[1][:-4]
        rec_num_in.append(int(rec_num_temp))
        
        count_check=count_check+1

print("----- Reading data from file for rest of the countries .....")
for i in range(0,no_lin_in_rest):
    if 'Count' in lines_in_rest[i]:
        pom0=lines_in_rest[i].split('<')
        for j in range(len(pom0)):
            if 'Count' in pom0[j]:
                pom00=pom0[j].split(':')
                count_in_rest=int(pom00[1])

    if 'Person of contact:' in lines_in_rest[i]:
        pom1=lines_in_rest[i-1].split('<')
        country=pom1[0][:-6]
        country_in.append(country)

        pom2=lines_in_rest[i].split('>')
        name=pom2[1][:-3]
        names_in.append(name)

        pom3=lines_in_rest[i+6].split('>')
        up_date_temp=pom3[1][:-2]
        up_date_in.append(up_date_temp)

        pom4=lines_in_rest[i+7].split('>')
        rec_num_temp=pom4[1][:-4]
        rec_num_in.append(int(rec_num_temp))
        
        count_check=count_check+1

print("----- Checking if all adds up .....")

if count_in_ms+count_in_rest != count_check:
    print('Count number at the begining of file is not same as the number of NCPs in the file!')

if len(country_in) != len(names_in) != len(up_date_in) != len(rec_num_in):
    print('Lists are not the same size!')

### Create dataframe of all lists already created
list_of_lists = list(zip(names_in, country_in, rec_num_in, up_date_in))
list_of_lists = list(zip(names_in, country_in, rec_num_in, up_date_in))
df_new = pd.DataFrame(list_of_lists, columns=['name', 'country', 'rec_num', 'update_date'])
print("===== Dataframe is ready =====")

# print(df_new)
df_file_name='database_of_NCPs'+new_date+'.csv'
df_new.to_csv(df_file_name, sep=',', index=False)
print("----- Dataframe printed to file -----")

input_file_ms.close()
input_file_rest.close()


print("************************** COMPARISON of DFs **************************")
print("Old and new file are the same (True or False):", df_old.equals(df_new))
### https://stackoverflow.com/questions/70283736/how-to-compare-2-non-identical-dataframes-in-python
merged = df_old.merge(df_new, how='outer', left_on='name', right_on='name')
cols = df_old.columns
old = merged.iloc[:, [0,1,2,3]].set_axis(cols, axis=1)
new = merged.iloc[:, [0,4,5,6]].set_axis(cols, axis=1)
diff1=old.compare(new, keep_shape=True, keep_equal=True, result_names=('old', 'new'))
diff2=old.compare(new, keep_equal=True, result_names=('old', 'new'))
diff1_file_name='differences_'+new_date+'_long.csv'
diff2_file_name='differences_'+new_date+'_short.csv'
diff1.to_csv(diff1_file_name, sep=',', index=False)
diff2.to_csv(diff2_file_name, sep=',', index=False)

round(time.time() - start_time, 2)
print ("---------- %s seconds ----------" % round(time.time() - start_time, 4))
print ("---------- Main function completed ---------")