# lets import the shell utility module and os module
# this module has functions to copy, rename, move
import shutil, os


# copy a file to a directory
shutil.copy(f'{os.getcwd()}/files/data0.txt',f'{os.getcwd()}/backup')


# copy a file to directory with a new name
shutil.copy(f'{os.getcwd()}/files/data0.txt',f'{os.getcwd()}/backup/new_data0.txt')


# copy a folder and all its content to another new folder'
# check if the directory exist or else it will throw an error
if not os.path.isdir(f"/home/nexus/makery/sandbox/backup/new_files"):
    shutil.copytree(f'{os.getcwd()}/files',f'{os.getcwd()}/backup/new_files')


# moving a file to another folder
shutil.move(f'{os.getcwd()}/files/spam.txt',f'{os.getcwd()}/backup')


# moving a file to another folder and renamed it
shutil.move(f'{os.getcwd()}/backup/spam.txt',f'{os.getcwd()}/files/new_spam.txt')


# 