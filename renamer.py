"""
Takes directory, a certain file and certain extension to change names of files present in a directory.
Doesn't change name of folders
"""
import os


def unchangeable_files(file_name):
    """
    Takes a string parameter of the name of the file needed to be read, opens the file, reads the elements and stores
    them in a list
    :param file_name: Name of file containing the names that won't be changed
    :return: Returns those names as a list for comparison at a later stage
    """
    with open(file_name) as f:
        files = f.readlines()
    return files


def changeable_filetype(file_list, file_type):
    """
    Function to enumerate the list returned by unchangeable_files, split the names of the files in the directory
    as a head and root and compare the heads with the list and if present the loop restarts with the next file
    and if the root isn't present then the file is renamed properly then it checks for the extension intended for
    change and names those files accordingly.
    :param file_list: Takes a list of the constant file names that will be compared first
    :param file_type: Takes the extension which will be changed
    :return: Renames the files matching the conditions and doesn't return a value
    """
    for index, file in enumerate(os.listdir()):
        head, root = os.path.splitext(file)
        if (head + '\n') in file_list:
            continue
        else:
            new_head = head.capitalize()
            os.rename(head + root, new_head + root)
        if root == file_type:
            os.rename(head + root, str((index + 1)) + root)
            continue
        else:
            continue


def soldier(dir_name, file_name, file_type):
    """
    This function takes parameters from the user and executes the above functions accordingly.
    :param dir_name: The directory for making changes
    :param file_name: The file containing the names of the files that won't be changed
    :param file_type: The file extension that will be named in order
    :return: Changes the names of files in the directory but doesn't return a value
    """
    os.chdir(dir_name)
    files_list = unchangeable_files(file_name)
    changeable_filetype(files_list, file_type)


if __name__ == '__main__':
    dir_needed = input("Enter the directory you want to access: ")
    type_change = input("Enter the file type you want to change: ")
    constants = input("Enter the file with unchangeable filenames: ")
    soldier(dir_needed, constants, type_change)
