import os

# print(os.getcwd()) ## get current working directory
# os.chdir('/Users/vamsh/Desktop/')## change directory
# os.mkdir('os-Demo') ## make onlt top level directory
# os.rmdir('os-Demo') ## delete 
# os.makedirs('os-Demo2/subdir') ## make both top level and sub directories 
# os.removedirs('os-Demo2/subdir') ## deletes directory from top level
# print(os.listdir()) ## list all directories in current directory

# for dirpath,dirnames,filenames in os.walk('/users/vamsh/Desktop'):  # # os.walk ## walkst through all directories in current dir
#     print(f"current path:{dirpath}")
#     print(f"Directories:{dirnames}")
#     print(f"Files:{filenames}")

print(os.environ) ##gives path to all environ variables
# print(os.environ.get('HOMEPATH')) ## prints particular path

# file_path = os.path.join(os.environ.get('HOMEPATH'),'Desktop') ##joins path or files
# print(file_path)

# print(os.path.basename('/path/someaddress/02.jpg')) ## prints the basename or filename
# print(os.path.dirname('/path/someaddress/02.jpg')) ## prints directory 
# print(os.path.splitext('/path/someaddress/02.jpg')) ## split text directory filename and file format/extension

# print(os.path.exists('/path/someaddress/02.jpg')) ## to check if the path exists or not returns True or False
# print(os.path.isfile('/Desktop/01.jpg')
# print(os.path.isfile('/path/someaddress/02.jpg') ## checks if its file or not

# print(dir(os.path))