import os
import sys

#directory = 'F:/____Learning/____books/new/'
#startWithCriteria = 'LetMeRead.net__'
#removePDFIfAmazonVersion = False

directory = 'F:/cloud-storage/MyKindle/My Kindle Content/'
startWithCriteria = None
removePDFIfAmazonVersion = True

assert os.path.isdir(directory)
current_path, directories, files = next(os.walk(directory))
print('** folder name: ', directory)
for fileName in files:
    if startWithCriteria != None and fileName.startswith(startWithCriteria):
        print('==> file name: ', fileName)
        newFileName = fileName.replace(startWithCriteria, '')
        print('====> file name: ', newFileName)
        os.rename(f"{directory}{fileName}", f"{directory}{newFileName}")
    if removePDFIfAmazonVersion and fileName.endswith('.pdf'):
        print('==> file name: ', fileName)
        amazonFileNameVersion = fileName.replace('.pdf', '.azw3')
        print('====> amazon version file name: ', amazonFileNameVersion)
        if amazonFileNameVersion in files:
            print('======> recommended action: remove pdf version')
            os.remove(f"{directory}{fileName}")
        else:
            print('======> recommended action: maintain pdf version')

