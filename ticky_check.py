#!/usr/bin/env python3
import sys
import re
import csv

Error_dict = dict()
User_entries_error = dict()
User_entries_info = dict()
User_dict = dict()
search_error = list()
search_user_error = list()
search_user_info = list()
with open("syslog.txt", "r") as workfile:
    for line in workfile:
        search_error += re.findall(r"ERROR ([\w' ]*)", line)
        search_user_error += re.findall(r"ERROR .* \(([\w\.]*)\)", line)
        search_user_info += re.findall(r"INFO .* \(([\w\.]*)\)", line)
 
for i in search_error:
    Error_dict[i] = search_error.count(i)

for i in search_user_error:
    if i not in search_user_info:
        User_entries_info[i] = 0
    else:
        User_entries_info[i] = search_user_info.count(i)

for i in search_user_error:
        User_entries_error[i] = search_user_error.count(i)

for k, v in list(User_entries_info.items()) + list(User_entries_error.items()):
    try:
        User_dict[k] += [v]
    except:
        User_dict[k] = [v]
 
sorted_Error_dict = sorted(Error_dict.items(), key = lambda kv: kv[1], reverse = True)
sorted_User_dict = sorted(User_dict.items(), key = lambda kv: kv[0])

new_dict = dict(sorted_User_dict)
error_list = []
info_list = []
for i in list(new_dict.values()):
    error_list.append(i[1])
    info_list.append(i[0])

usersname = []
usersname.extend(new_dict.keys())

merged_list = [(usersname[i], info_list[i], error_list[i]) for i in range(0, len(usersname))]

with open('error_message.csv', 'w', newline='') as file:
    csv_out = csv.writer(file)
    csv_out.writerow(["Error", "Count"])
    csv_out.writerows(sorted_Error_dict)
    
with open('user_statistics.csv', 'w', newline='') as file:
    csv_out = csv.writer(file)
    csv_out.writerow(["Username", "INFO", "ERROR"])
    csv_out.writerows(merged_list)
