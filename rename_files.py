import os

def rename_files():
    # Get file names of the folder
    fileList = os.listdir('./prank')
    print fileList
    savedPath = os.getcwd()
    os.chdir('./prank')
    print('Current Working Directory is ' + os.getcwd())
    
    # Rename each file
    for fileName in fileList:
        print('Old name - ' + fileName)
        print('New Name - ' + fileName.translate(None, '0123456789'))
        os.rename(fileName, fileName.translate(None, '0123456789'))
    os.chdir(savedPath)

rename_files()
