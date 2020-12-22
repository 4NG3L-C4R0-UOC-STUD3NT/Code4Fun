import os
import sys

directory = 'F:/___eBooks/'
#directory = 'F:/____Learning/____books/new-new/'
startWithCriteriaList = ['LetMeRead.net__', 'LetMeRead.net_']
removeAmazonIfPDFVersion = True
removePDFIfAmazonVersion = False
removeEPUBIfPDFVersion = True
removeMobiIfPDFVersion = True

assert os.path.isdir(directory)
current_path, directories, files = next(os.walk(directory))
print('** folder name: ', directory)
for fileName in files:
    for startWithCriteria in startWithCriteriaList:
        if fileName.startswith(startWithCriteria):
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
    
    if removeAmazonIfPDFVersion and fileName.endswith('.azw3'):
        print('==> file name: ', fileName)
        pdfFileNameVersion = fileName.replace('.azw3','.pdf')
        print('====> pdf version file name: ', pdfFileNameVersion)
        if pdfFileNameVersion in files:
            print('======> recommended action: remove azw3 version')
            os.remove(f"{directory}{fileName}")
        else:
            print('======> recommended action: maintain azw3 version')
    
    if removeAmazonIfPDFVersion and fileName.endswith('.azw'):
        print('==> file name: ', fileName)
        pdfFileNameVersion = fileName.replace('.azw','.pdf')
        print('====> pdf version file name: ', pdfFileNameVersion)
        if pdfFileNameVersion in files:
            print('======> recommended action: remove azw version')
            os.remove(f"{directory}{fileName}")
        else:
            print('======> recommended action: maintain azw version')
    
    if removeEPUBIfPDFVersion and fileName.endswith('.epub'):
        print('==> file name: ', fileName)
        pdfFileNameVersion = fileName.replace('.epub', '.pdf')
        print('====> pdf version file name: ', pdfFileNameVersion)
        if pdfFileNameVersion in files:
            print('======> recommended action: remove epub version')
            os.remove(f"{directory}{fileName}")
        else:
            print('======> recommended action: maintain epub version')
    
    if removeMobiIfPDFVersion and fileName.endswith('.mobi'):
        print('==> file name: ', fileName)
        pdfFileNameVersion = fileName.replace('.mobi', '.pdf')
        print('====> pdf version file name: ', pdfFileNameVersion)
        if pdfFileNameVersion in files:
            print('======> recommended action: remove mobi version')
            os.remove(f"{directory}{fileName}")
        else:
            print('======> recommended action: maintain mobi version')

