import zipfile
import os
import os.path

my_zip = zipfile.ZipFile("Test.zip")
my_zip.extractall("Test_directory")
my_zip.close()

my_string = input("Введите строку для поиска:\n")

with open("result.txt", "w") as file:
    for currentDir, dirs, files in os.walk("Test_directory"):
        for i in files:
            with open(os.path.join(currentDir, i)):
                for line in i:
                    if my_string in line:
                        file.write(i)
                        file.write("\n")
