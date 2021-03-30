# lets import the shell utility module and os module
import shutil, os


# deleting files in os module using the unlink() function
os.unlink(f'{os.getcwd()}/backup/new_data0.txt')


# deleting a directory in os module using rmdir() function
# this will throw an error if the directory or folder is not empty
# this is good for safety purposes
os.rmdir(f'{os.getcwd()}/backup/new_files')


# in shutil module we can delete the directory even if its not empty
# but be careful in using this function because deleting in python is not reversible
# shutil.rmtree(f'{os.getcwd()}/backup/new_files') # use at your own risk


# it's a good practice to do a dry run for checking files and folders before deleting
# because deleting is dangerous
for filename in os.listdir(f'{os.getcwd()}/backup/new_files'):
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)