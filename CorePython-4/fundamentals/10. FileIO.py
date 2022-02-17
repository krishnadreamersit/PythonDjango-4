# File Write/Read
    # 1. Creating new file

# 1. Creating new file
    # open(filename, filemode) - method used to create new file
        # filename : only file (file in current folder)
        # filename with path (file in specified path)
        # filemode:
            # r - read only
            # w - write
            # a - append

    # path1 = "D:\\Python\\PythonDjango-4\\MyFiles\\"
    # path2 = "D:/Python/PythonDjango-4/MyFiles/"
    # filename1 ="data1.txt"

# Example-1 # Creating a new file
"""
import sys
path1 = "D:/Python/PythonDjango-4/MyFiles/"
filename = "data1.txt"
try:
    file1 = open(path1+filename, "w")
    print("File create successfully")
except:
    print("Error : ", sys.exc_info()[1])
finally:
    del path1
    del filename
    del file1
"""

# Example-2 # Writing content on new file
"""
import sys
path1 = "D:/Python/PythonDjango-4/MyFiles/"
filename = "data1.txt"
contents = "New to programming? Python is free and easy to learn if you know where to start! This guide will help you to get started quickly."
try:
    file1 = open(path1+filename, "w") # Create new file
    file1.write(contents) # Write contents on file
    file1.close() # Close file
    print("File create and write contents successfully")
except:
    print("Error : ", sys.exc_info()[1])
finally:
    del path1
    del filename
    del file1
"""

# Example-3 # Reading content from file
"""
import sys
path1 = "D:/Python/PythonDjango-4/MyFiles/"
filename = "data1.txt"
try:
    file1 = open(path1+filename, "r") # Open file in read mode
    contents = file1.read()
    print(contents)
    file1.close() # Close file
    print("Read contents from file successfully")
except:
    print("Error : ", sys.exc_info()[1])
finally:
    del path1
    del filename
    del file1
"""

# Example-4 # Append in file
"""
import sys
str1 = "Files are named locations on disk to store related information. They are used to permanently store data in a non-volatile memory (e.g. hard disk)."
filename = "D:/Python/PythonDjango-4/MyFiles/data1.txt"
try:
    file1 = open(filename, "a") # Open file in append mode
    file1.write(str1)
    file1.close()
except:
    print("Error : ", sys.exc_info()[1])
finally:
    del str1
    del filename
"""

# Class and Methods
class FileIO():
    def write_content(self, file_name, str1):
        import sys
        filename = "D:/Python/PythonDjango-4/MyFiles/"+file_name
        contents = str1
        try:
            file1 = open(filename, "w") # Create new file
            file1.write(contents) # Write contents on file
            file1.close() # Close file
            print("File create and write contents successfully")
        except:
            print("Error : ", sys.exc_info()[1])
        finally:
            del filename
            del file1

    def read_content(self, file_name):
        import sys
        filename = "D:/Python/PythonDjango-4/MyFiles/"+file_name
        try:
            file1 = open(filename, "r") # Open file in read mode
            contents = file1.read()
            print(contents)
            file1.close() # Close file
            print("Read contents from file successfully")
        except:
            print("Error : ", sys.exc_info()[1])
        finally:
            del filename
            del file1

    def append_content(self, file_name, str1):
        import sys
        filename = "D:/Python/PythonDjango-4/MyFiles/"+file_name
        try:
            file1 = open(filename, "a") # Open file in append mode
            file1.write(str1)
            file1.close()
        except:
            print("Error : ", sys.exc_info()[1])
        finally:
            del str1
            del filename

# Test-1
# write_content("data2.txt","Hello")
# read_content("data2.txt")
# append_content("data2.txt", "Hi!")
# read_content("data2.txt")

# Test-2
# file1 = FileIO()
# file1.write_content("data3.txt","Hello world of Python")
# file1.append_content("data3.txt", "Welcome to Broadway")
# file1.read_content("data3.txt")
