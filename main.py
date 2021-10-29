from pprint import *

new_file = {}

with open('1.txt', 'r', encoding='utf-8') as file_1:
  counter = 0
  file_1_name = '1.txt'
  for string in file_1:
    counter += 1
  new_file[file_1_name] = counter
print(new_file)

with open('2.txt', encoding='utf-8') as file_2:
   counter = 0
   file_2_name = '2.txt'
   for string in file_2:
    counter += 1
   new_file[file_2_name] = counter
print(new_file)

with open('3.txt', encoding='utf-8') as file_3:
  counter = 0
  file_3_name = '3.txt'
  for string in file_3:
    counter += 1
  new_file[file_3_name] = counter
print(new_file)

sorted_files = list(new_file.items())
sorted_files.sort( key=lambda i: i[1])

print(sorted_files)
with open ('common_file', 'w', encoding = 'utf-8') as f:
  for i in sorted_files:
    f.write(str(i[0]) + '\n')
    f.write(str(i[1]) + '\n')
    with open (i[0],encoding = 'utf-8' ) as f_2:
      f.write(f_2.read().strip() + '\n')