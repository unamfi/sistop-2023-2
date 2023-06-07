import os
import sys
import time

print("{:<35} {:<30} {:<15} {:<0}".format("File Name","Last Modified","Mode","Size"))

def get_file_info(file_path):
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    file_mtime = os.path.getmtime(file_path)
    file_mode = os.stat(file_path).st_mode

    return file_name, file_size, file_mtime, file_mode

def print_file_info(file_info):
    file_name, file_size, file_mtime, file_mode = file_info
    file_mtime_str = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(file_mtime))
    file_mode_str = oct(file_mode)[-3:]
    
    print("{:<35} {:<30} {:<15} {:<0}".format(file_name,file_mtime_str,file_mode_str,file_size))

def list_files_in_directory(directory, days):
    current_time = time.time()
    threshold_time = current_time - (days * 24 * 60 * 60)

    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_mtime = os.path.getmtime(file_path)
            if file_mtime >= threshold_time:
                file_info = get_file_info(file_path)
                file_list.append(file_info)

    file_list.sort()

    for file_info in file_list:
        print_file_info(file_info)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python program_name.py directory days")
        sys.exit(1)

    directory = sys.argv[1]
    days = int(sys.argv[2])

    list_files_in_directory(directory, days)

