
files_num = int(input())
command_num = 0

dict_files = dict()


while files_num > 0:
    files_num -= 1
    rights_files = input().split()
    dict_files.update(rights_files)

print(dict_files)