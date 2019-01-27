import os
import sys
import dropbox
from dropbox.exceptions import AuthError
import pdb
from urllib.request import Request, urlopen
from pathlib import Path

TOKEN = os.environ.get('DROPBOX_TOKEN')

def CheckAgainstKeywords(file, keywords):
    file = file.lower()
    count = 0
    for i in keywords:
        i = i.lower()
        if i in file:
            count += 1
    return count

def OrderAndDisplayResults(fileList):
    # using quicksort to order the fileList based on the number of counts for the search
    less = []
    equal = []
    greater = []

    if len(fileList) > 1:
        pivot = fileList[0][1]
        for file in fileList:
            if file[1] < pivot:
                less.append(file)
            if file[1] == pivot:
                equal.append(file)
            if file[1] > pivot:
                greater.append(file)
        return OrderAndDisplayResults(greater) + equal + OrderAndDisplayResults(less)

    else:  
        return fileList

def search_dropbox(keywords, companies, years):
    cFlag = False
    yFlag = False

    if(len(companies)>0):
        cFlag = True
    if(len(years)>0):
        yFlag = True

    # Check for an access token
    if (len(TOKEN) == 0):
        sys.exit("No Access token")

    # Create an instance of a Dropbox class, which can make requests to the API.
    dbx = dropbox.Dropbox(TOKEN)

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except:
        sys.exit("ERROR: Invalid access token; try re-generating an "
                 "access token from the app console on the web.")

    fileList = []

    if(yFlag == False) and (cFlag == False):
        #searches recursively through the entire dropbox beginning at the root
        for entry in dbx.files_list_folder('', True).entries:
            if "." in entry.path_display:
                count = CheckAgainstKeywords(entry.name, keywords)
                if count != 0:
                    fileList.append([entry, count])
    
    elif(yFlag == True) and (cFlag == False):
        #searches through specific YEAR folders, but no specific companies
        for yearEntry in dbx.files_list_folder('').entries:
            if yearEntry.name in years:
                for entry in dbx.files_list_folder(yearEntry.path_display, True).entries:
                    count = CheckAgainstKeywords(entry.name, keywords)
                    if count != 0:
                        fileList.append([entry, count])
    
    elif(yFlag == False) and (cFlag == True):
        #searches through specific company folders, but any year
        for yearEntry in dbx.files_list_folder('').entries:
            for companyEntry in dbx.files_list_folder(yearEntry.path_display).entries:
                if companyEntry.name.lower() in companies:
                    for entry in dbx.files_list_folder(companyEntry.path_display).entries:
                        count = CheckAgainstKeywords(entry.name, keywords)
                        if count != 0:
                            fileList.append([entry, count])
            
    else:   #will need to search through only the years and companies specified by the user
        #searches through the YEAR folders in the Dropbox
        for yearEntry in dbx.files_list_folder('').entries:
            if yearEntry.name in years:
                for companyEntry in dbx.files_list_folder(yearEntry.path_display).entries:
                    if companyEntry.name.lower() in companies:
                        for entry in dbx.files_list_folder(companyEntry.path_display).entries:
                            count = CheckAgainstKeywords(entry.name, keywords)
                            if count != 0:
                                fileList.append([entry, count])

    sortedFileList = OrderAndDisplayResults(fileList)
    urlList = []
    for file in sortedFileList:
        path = file[0].path_display
        urlList.append(dbx.sharing_create_shared_link(path).url)
    
    return urlList