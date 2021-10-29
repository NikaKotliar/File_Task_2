from pprint import *
new_file = {}
def counting_strings (file_name):
    with open(file_name, encoding='utf-8') as file_1:
        counter = 0
        for string in file_1:
            counter += 1
        new_file[file_name] = counter
        return new_file

counting_strings('1.txt')
counting_strings('2.txt')
counting_strings('3.txt')

sorted_files = list(new_file.items())
sorted_files.sort( key=lambda i: i[1])

print(sorted_files)
with open ('common_file', 'w', encoding = 'utf-8') as f:
  for i in sorted_files:
    f.write(str(i[0]) + '\n')
    f.write(str(i[1]) + '\n')
    with open (i[0],encoding = 'utf-8' ) as f_2:
      f.write(f_2.read().strip() + '\n')