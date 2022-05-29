import os; 

def write_file(filename):
    open(filename, "w"); 

def read_file(filename):
    open(filename, "r"); 

def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename); 
    else:
        print("This file does not exist!"); 

def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name); 
    else:
        print("This directory already exists! \nSkipping creating this directory!")

def remove_dir(dir_name):

    if os.path.isdir(dir_name):
        if not any(os.scandir(dir_name)):
            print("This directory is empty, deleting!"); 
            os.rmdir(dir_name); 
        else:
            print("This directory is not empty, cannot delete!"); 
    else:
        print("This directory does not exist, cannot continue!"); 

def write_file_in_dir():
    parent_dir = input("Please state the parent directory.")
    if not os.path.exists(parent_dir):
        print("That is not a path that currently exists your pc, please try again!"); 
        parent_dir = input("Please state the parent directory."); 
    child_dir = input("Please state the child directory."); 
    dir = os.path.join(parent_dir,child_dir); 
    file_name = input("Please state the name of the file with the extension you desire! (Only accepts text formats.)"); 
    path = os.path.join(dir, file_name); 
    write_file(path); 
    if os.path.exists(path):
        print("The file was created successfully!"); 
    else:
        print("An unknown error has occured! Make sure you correctly input all statements!")
    print("Returning to main menu.")
    program(); 



def program():
    user_input = input("Please define what you would like to do. \nType write file to create a file in your current directory. \nType read file to read a file in your current directory. \nType remove file to remove a file in your current directory. \nType create dir to create a directory in your current directory. \nType remove dir to remove a directory in your current directory. \nType write file in dir to write a file into a directory anywhere on your pc. \nType remove file in dir to remove a file from a directory anywhere on your pc. \nType remove dir from dir to remove a directory from anywhere on your PC. \nType create dir in dir to create a directory from anywhere on your PC. \n").lower(); 
    
    if user_input == "write file in dir":
        write_file_in_dir(); 

program(); 