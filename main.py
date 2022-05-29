import os; 

def write_file(filename): #Writes a file.
    if not os.path.exists(filename):
        open(filename, "w"); 
    else:
        print("This file already exists!"); 

def read_file(filename): #save this for later. Reads a file.
    if os.path.exists(filename):
        open(filename, "r"); 
    else:
        print("This file does not exist!"); 

def remove_file(filename): #Removes a file.
    if os.path.exists(filename):
        os.remove(filename); 
    else:
        print("This file does not exist!"); 

def create_dir(dir_name): #Creates a directory.
    if not os.path.exists(dir_name):
        os.mkdir(dir_name); 
    else:
        print("This directory already exists! \nSkipping creating this directory!")

def remove_dir(dir_name): #Removes a directory.
    if os.path.isdir(dir_name):
        if not any(os.scandir(dir_name)):
            print("This directory is empty, deleting!"); 
            os.rmdir(dir_name); 
        else:
            print("This directory is not empty, cannot delete!"); 
    else:
        print("This directory does not exist, cannot continue!"); 

def write_file_in_dir(): #Writes a file in a directory.
    parent_dir = input("Please state the parent directory."); 
    if not os.path.exists(parent_dir):
        print("That is not a path that currently exists your pc, please try again!"); 
        while not os.path.exists(parent_dir):
            print("That is not a path that currently exists your pc, please try again!"); 
            parent_dir = input("Please state the parent directory."); 

    file_name = input("Please state the name of the file with the extension you desire! (Only accepts text formats.)"); 
    path = os.path.join(parent_dir, file_name); 
    write_file(path); 
    if os.path.exists(path):
        print("The file was created successfully!"); 
    else:
        print("An unknown error has occured! Make sure you correctly input all statements!"); 
    print("Returning to main menu."); 
    program(); 

def create_dir_in_dir(): #Writes a directory in a directory.
    parent_dir = input("Please state the parent directory."); 
    if not os.path.exists(parent_dir):
        print("That is not a path that currently exists your pc, please try again!"); 
        while not os.path.exists(parent_dir):
            print("That is not a path that currently exists your pc, please try again!"); 
            parent_dir = input("Please state the parent directory."); 

    child_dir = input("Please state the child directory."); 
    path = os.path.join(parent_dir, child_dir); 
    create_dir(path); 

    if os.path.exists(path):
        print("The directory was created successfully!"); 
    else:
        print("An unknown error has occured! It is likely this path already exists! Otherwise make sure you correctly input all statements!"); 
    print("Returning to main menu."); 
    program(); 
    
def remove_file_in_dir(): #Removes a file in a directory.
    parent_dir = input("Please state the parent directory."); 
    if not os.path.exists(parent_dir):
        print("That is not a path that currently exists your pc, please try again!"); 
        while not os.path.exists(parent_dir):
            print("That is not a path that currently exists your pc, please try again!"); 
            parent_dir = input("Please state the parent directory."); 

    file_name = input("Please state the name of the file with the extension you desire! (Only accepts text formats.)"); 
    path = os.path.join(parent_dir, file_name); 
    remove_file(path); 
    if os.path.exists(path):
        print("The file was removed successfully!"); 
    else:
        print("An unknown error has occured! Make sure you correctly input all statements!"); 
    print("Returning to main menu."); 
    program(); 

def remove_dir_from_dir(): #Removes a directory in a directory.
    parent_dir = input("Please state the parent directory."); 
    if not os.path.exists(parent_dir):
        print("That is not a path that currently exists your pc, please try again!"); 
        while not os.path.exists(parent_dir):
            print("That is not a path that currently exists your pc, please try again!"); 
            parent_dir = input("Please state the parent directory."); 

    child_dir = input("Please state the child directory."); 
    path = os.path.join(parent_dir, child_dir); 
    remove_dir(path); 

    if not os.path.exists(path):
        print("The directory was removed successfully!"); 
    else:
        print("An unknown error has occured! Make sure you correctly input all statements!"); 
    print("Returning to main menu."); 
    program(); 

def create_dir_and_file(): #Creates a directory and a file.
    parent_dir = input("Please state the parent directory."); 
    if not os.path.exists(parent_dir):
        print("That is not a path that currently exists your pc, please try again!"); 
        while not os.path.exists(parent_dir):
            print("That is not a path that currently exists your pc, please try again!"); 
            parent_dir = input("Please state the parent directory."); 

    child_dir = input("Please state the child directory."); 
    file_name = input("Please state the name of the file with the extension you desire! (Only accepts text formats.)"); 

    path = os.path.join(parent_dir, child_dir); 
    create_dir(path); 
    newpath = os.path.join(path, file_name); 
    write_file(newpath); 

    if os.path.exists(newpath):
        print("The directory and file were created successfully!"); 
    else:
        print("An unknown error has occured! It is likely this path already exists! Otherwise make sure you correctly input all statements!"); 
    print("Returning to main menu."); 
    program(); 

def program(): #Runs everything.
    user_input = input("Please define what you would like to do. \nType write file in dir to write a file into a directory anywhere on your pc. \nType remove file in dir to remove a file from a directory anywhere on your pc. \nType remove dir from dir to remove a directory from anywhere on your PC. \nType create dir in dir to create a directory from anywhere on your PC. \nType create dir and file to create a dir with a file inside of it anywhere on your PC. \nType close to end the program. \n").lower(); 
    if user_input == "write file in dir":
        write_file_in_dir(); 
    else:
        if user_input == "create dir in dir":
                create_dir_in_dir(); 
        else:
            if user_input == "remove file in dir":
                remove_file_in_dir(); 
            else:
                if user_input == "remove dir from dir":
                    remove_dir_from_dir(); 
                else:
                    if user_input == "create dir and file":
                        create_dir_and_file(); 
                    else:
                        if user_input == "close":
                            print("Exiting!"); 
                            return; 
                        else:
                            print("Please input a statement or type close to exit."); 
                            program(); 

program(); 