import os; 

def write_file(file_name): #Writes a file.
    if not os.path.exists(file_name):
        open(file_name, "w")
    else:
        print("This file already exists! \n")

    print("Ending file creation. \n")

def read_file(file_name): #save this for later. Reads a file.
    if os.path.exists(file_name):
        file = open(file_name, "r")
        file_contents = file.read()
        print(file_contents)
    else:
        print("This file does not exist! \n")
    print("Ending file reading. \n")

def remove_file(file_name): #Removes a file.
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print("This file does not exist! \n")

    print("Ending file removal. \n")

def create_dir(dir_name): #Creates a directory.
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    else:
        print("This directory already exists! \nSkipping creating this directory! \n")

    print("Ending directory creation. \n")

def remove_dir(dir_name): #Removes a directory.
    if os.path.isdir(dir_name):
        if not any(os.scandir(dir_name)):
            print("This directory is empty, deleting! \n")
            os.rmdir(dir_name)
        else:
            print("This directory is not empty, cannot delete! \n")
    else:
        print("This directory does not exist, cannot continue! \n")

    print("Ending directory removal. \n")

def create_file_in_dir(): #Creates a file in a directory.
    parent_dir = input("Please state the parent directory. \nInput: ").lower()
    print("\n")
    while not os.path.exists(parent_dir):
        print("That is not a path that currently exists your pc, please try again! \n")
        parent_dir = input("Please state the parent directory. \nInput: ").lower()
        print("\n")

    file_name = input("Please state the name of the file with the extension you desire! (Only accepts text formats.) \nInput: ").lower()
    print("\n")
    path = os.path.join(parent_dir, file_name)

    write_file(path)
    if os.path.exists(path):
        print("The file was created successfully! \n")
    else:
        print("An unknown error has occured! Make sure you correctly input all statements! \n")

    print("Returning to main menu. \n")
    input("Press any button to continue.")
    program()

def create_dir_in_dir(): #Creates a directory in a directory.
    parent_dir = input("Please state the parent directory. \nInput: ").lower()
    print("\n")
    while not os.path.exists(parent_dir):
        print("That is not a path that currently exists your pc, please try again! \n")
        parent_dir = input("Please state the parent directory. \nInput: ").lower()
        print("\n")

    child_dir = input("Please state the child directory. \nInput: ").lower()
    print("\n")
    path = os.path.join(parent_dir, child_dir)

    create_dir(path)
    if os.path.exists(path):
        print("The directory was created successfully! \n")
    else:
        print("An unknown error has occured! It is likely this path already exists! Otherwise make sure you correctly input all statements! \n")

    print("Returning to main menu. \n")
    input("Press any button to continue.")
    program()
    
def remove_file_in_dir(): #Removes a file in a directory.
    parent_dir = input("Please state the parent directory. \nInput: ").lower()
    print("\n")
    while not os.path.exists(parent_dir):
        print("That is not a path that currently exists your pc, please try again! \n")
        parent_dir = input("Please state the parent directory. \nInput: ").lower()
        print("\n")

    file_name = input("Please state the name of the file with the extension you desire! (Only accepts text formats.) \nInput: ").lower()
    print("\n")
    path = os.path.join(parent_dir, file_name)

    remove_file(path)
    if not os.path.exists(path):
        print("The file was removed successfully! \n")
    else:
        print("An unknown error has occured! Make sure you correctly input all statements! \n")

    print("Returning to main menu. \n")
    input("Press any button to continue.")
    program()

def remove_dir_from_dir(): #Removes a directory in a directory.
    parent_dir = input("Please state the parent directory. \nInput: ").lower()
    print("\n")
    while not os.path.exists(parent_dir):
        print("That is not a path that currently exists your pc, please try again! \n")
        parent_dir = input("Please state the parent directory. \nInput: ").lower()
        print("\n")

    child_dir = input("Please state the child directory. \nInput: ").lower()
    print("\n")
    path = os.path.join(parent_dir, child_dir)

    remove_dir(path)
    if not os.path.exists(path):
        print("The directory was removed successfully! \n")
    else:
        print("An unknown error has occured! Make sure you correctly input all statements! \n")

    print("Returning to main menu. \n")
    input("Press any button to continue.")
    program()

def create_dir_and_file(): #Creates a directory and a file.
    parent_dir = input("Please state the parent directory. \nInput: ").lower()
    print("\n")
    while not os.path.exists(parent_dir):
        print("That is not a path that currently exists your pc, please try again! \n")
        parent_dir = input("Please state the parent directory. \nInput: ").lower()
        print("\n")

    child_dir = input("Please state the child directory. \nInput: ").lower()
    print("\n")
    file_name = input("Please state the name of the file with the extension you desire! (Only accepts text formats.) \nInput: ").lower()
    print("\n")

    path = os.path.join(parent_dir, child_dir)
    newpath = os.path.join(path, file_name)

    create_dir(path)
    write_file(newpath)
    if os.path.exists(newpath):
        print("The directory and file were created successfully! \n")
    else:
        print("An unknown error has occured! It is likely this path already exists! Otherwise make sure you correctly input all statements! \n")

    print("Returning to main menu. \n")
    input("Press any button to continue.")
    program()

def create_many_files(): #Creates many files.
    count = input("Time to create many files! \nInput: ")
    print("\n")
    while count != int:
        count = input("How many files would you like to create? \nInput: ")
        print("\n")
        try:
            val = int(count)
            break
        except ValueError:
            print("This is not a number. Please enter a valid number! \n")

    parent_dir = input("Please state the parent directory. \nInput: ").lower()
    print("\n")
    while not os.path.exists(parent_dir):
        print("That is not a path that currently exists your pc, please try again!")
        parent_dir = input("Please state the parent directory. \nInput: ").lower()
        print("\n")

    for x in range(int(count)):
        file_name = input("Please state the name of the file with the extension you desire! (Only accepts text formats.) \nInput: ").lower()
        print("\n")
        path = os.path.join(parent_dir, file_name)

        write_file(path)
        if os.path.exists(path):
            print("The file was created successfully! \n")
        else:
            print("An unknown error has occured! Make sure you correctly input all statements! \n")

    print("Returning to main menu. \n")
    input("Press any button to continue.")
    program()

def remove_many_files(): #Removes many files.
    count = input("Time to remove many files! \nInput: ")
    print("\n")
    while count != int:
        count = input("How many files would you like to remove? \nInput: ")
        print("\n")
        try:
            val = int(count)
            break
        except ValueError:
            print("This is not a number. Please enter a valid number! \n")

    parent_dir = input("Please state the parent directory. \nInput: ").lower()
    print("\n")
    while not os.path.exists(parent_dir):
        print("That is not a path that currently exists your pc, please try again!")
        parent_dir = input("Please state the parent directory. \nInput: ").lower()
        print("\n")

    for x in range(int(count)):
        file_name = input("Please state the name of the file with the extension you desire! (Only accepts text formats.) \nInput: ")
        print("\n")
        path = os.path.join(parent_dir, file_name)

        remove_file(path)
        if not os.path.exists(path):
            print("The file was removed successfully! \n")
        else:
            print("An unknown error has occured! Make sure you correctly input all statements! \n")

    print("Returning to main menu. \n")
    input("Press any button to continue.")
    program()

def create_many_dirs(): #Creates many directories.
    count = input("Time to create many directories! \nInput: ")
    print("\n")
    while count != int:
        count = input("How many directories would you like to create? \nInput: ")
        print("\n")
        try:
            val = int(count)
            break
        except ValueError:
            print("This is not a number. Please enter a valid number! \n")

    parent_dir = input("Please state the parent directory. \nInput: ").lower()
    print("\n")
    while not os.path.exists(parent_dir):
        print("That is not a path that currently exists your pc, please try again!")
        parent_dir = input("Please state the parent directory. \nInput: ").lower()
        print("\n")

    for x in range(int(count)):
        child_dir = input("Please state the name of the child directory. \nInput: ").lower()
        print("\n")
        path = os.path.join(parent_dir, child_dir)

        create_dir(path)
        if os.path.exists(path):
            print("The directory. was created successfully! \n")
        else:
            print("An unknown error has occured! It is likely this path already exists! Otherwise make sure you correctly input all statements! \n")

    print("Returning to main menu. \n")
    input("Press any button to continue.")
    program()

def remove_many_dirs(): #Removes many directories.
    count = input("Time to remove many directories! \nInput: ")
    print("\n")
    while count != int:
        count = input("How many directories would you like to remove? \nInput: ")
        print("\n")
        try:
            val = int(count)
            break
        except ValueError:
            print("This is not a number. Please enter a valid number! \n")

    parent_dir = input("Please state the parent directory. \nInput: ").lower()
    print("\n")
    while not os.path.exists(parent_dir):
        print("That is not a path that currently exists your pc, please try again! \n")
        parent_dir = input("Please state the parent directory. \nInput: ").lower()
        print("\n")

    for x in range(int(count)):
        child_dir = input("Please state the name of the child directory. \nInput: ").lower()
        print("\n")
        path = os.path.join(parent_dir, child_dir)

        remove_dir(path)
        if os.path.exists(path):
            print("The directory was removed successfully! \n")
        else:
            print("An unknown error has occured! Make sure you correctly input all statements! \n")
            
    print("Returning to main menu. \n")
    input("Press any button to continue.")
    program()

def read_file_in_dir(): #Read file in directory.
    parent_dir = input("Please state the parent directory. \nInput: ").lower()
    print("\n")
    while not os.path.exists(parent_dir):
        print("That is not a path that currently exists your pc, please try again! \n")
        parent_dir = input("Please state the parent directory. \nInput: ").lower()
        print("\n")

    file_name = input("Please state the name of the file with the extension you desire! (Only accepts text formats.) \nInput: ").lower()
    print("\n")
    path = os.path.join(parent_dir, file_name)

    print("\n")
    read_file(path)
    print("\n")
    if os.path.exists(path):
        print("The file was read successfully! \n")
    else:
        print("An unknown error has occured! Make sure you correctly input all statements! \n")

    print("Returning to main menu. \n")
    input("Press any button to continue.")
    program()

def program(): #Runs everything.
    user_input = input("\nPlease define what you would like to do. \n \nType 'create file in dir' to create a file into a directory anywhere on your pc. \nType 'remove file in dir' to remove a file from a directory anywhere on your pc. \nType 'remove dir from dir' to remove a directory from anywhere on your PC. \nType 'create dir in dir' to create a directory from anywhere on your PC. \nType 'create dir and file' to create a dir with a file inside of it anywhere on your PC. \nType 'create many files' to create many files in a directory from anywhere on your PC. \nType 'remove many files' to remove many files in a directory from anywhere on your PC. \nType 'create many dirs' to create many dirs in a directory from anywhere on your PC. \nType 'remove many dirs' to remove many dirs in a directory from anywhere on your PC. \nType 'read file in dir' to read a file in a directory anywhere on your PC. \n \nType close to end the program. \n \nInput: ").lower()
    print("\n")
    if user_input == "create file in dir":
        create_file_in_dir()
    elif user_input == "create dir in dir":
        create_dir_in_dir()
    elif user_input == "remove file in dir":
        remove_file_in_dir()
    elif user_input == "remove dir from dir":
        remove_dir_from_dir()
    elif user_input == "create dir and file":
        create_dir_and_file()
    elif user_input == "create many files":
        create_many_files()
    elif user_input == "remove many files":
        remove_many_files()
    elif user_input == "create many dirs":
        create_many_dirs()
    elif user_input == "remove many dirs":
        remove_many_dirs()
    elif user_input == "read file in dir":
        read_file_in_dir()
    elif user_input == "close":
        print("Exiting! \n")
        return
    else:
        print("Please input a statement or type close to exit. \n")
        input("Press any button to continue. \n")
        program()

program()