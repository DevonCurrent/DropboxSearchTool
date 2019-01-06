import os
import sys
import dropbox
from dropbox.exceptions import AuthError
import pdb
from urllib.request import Request, urlopen
from pathlib import Path
from flask import Flask, redirect, render_template, request, session, url_for

APP_KEY = os.environ.get('APP_KEY')
APP_SECRET = os.environ.get('APP_SECRET')
cFlag = False
yFlag = False
final_results = [[0, 0, 0]]



def authorize():
    flow = dropbox.oauth.DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)
    authorize_url = flow.start()
    print('1. Go to: ' + authorize_url)
    print('2. Click "Allow" (you might have to log in first)')
    print('3. Copy the authorization code.')

    code = input("Enter the authorization code here: ").strip()
    access_token = flow.finish(code).access_token
    return access_token

def login(token_save_path):
    if os.path.exists(token_save_path):
        with open(token_save_path) as token_file:
            access_token = token_file.read()
    else:
        access_token = authorize()
        with open(token_save_path, 'w') as token_file:
            token_file.write(access_token)
    return dropbox.Dropbox(access_token)




def CheckAgainstKeywords(file, keywords):
    file = file.lower()
    count = 0
    for i in keywords:
        i = i.lower()
        if i in file:
            count += 1
    return count

def OrderAndDisplayResults(results):
    high_count = [0, 0, 0]
    for i in results:
        if i[1] >= high_count[1]:
            high_count = i

    if high_count != [0, 0, 0]:
        final_results.append(high_count)
        results.remove(high_count)
        OrderAndDisplayResults(results)


def search_dropbox(keywords, companies, years):
    global yFlag
    global cFlag

    if(len(companies)>0):
        cFlag = True
    if(len(years)>0):
        yFlag = True

    # Create an instance of a Dropbox class, which can make requests to the API.
    dbx = login('token.dat')

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        sys.exit("ERROR: Invalid access token; try re-generating an "
                 "access token from the app console on the web.")

    results = [[0,0,0]]

    if(yFlag == False) and (cFlag == False):
        #searches recursively through the entire dropbox beginning at the root
        for entry in dbx.files_list_folder('', True).entries:
            if "." in entry.path_display:

                resp = dbx.files_download(entry.path_display)[1]
                content = resp.content
                
                pdb.set_trace()
                content.decode('utf-8') # this should work but it is saying invalid continuation byte


    
    elif(yFlag == True) and (cFlag == False):
        #searches through specific YEAR folders, but no specific companies
        for yearEntry in dbx.files_list_folder('').entries:
            if yearEntry.name in years:
                for entry in dbx.files_list_folder(yearEntry.display_name, True).entries:
                    r = dbx.files_get_preview(entry.path_display)[1] #response object
                    print(r.text.count("the"))
                    print(entry.name)
                    pdb.set_trace()
    
    elif(yFlag == False) and (cFlag == True):
        #searches through specific company folders, but any year
        for yearEntry in dbx.files_list_folder('').entries:
            for companyEntry in dbx.files_list_folder(yearEntry.display_name).entries:
                if companyEntry.name in companies:
                    for entry in dbx.files_list_folder(companyEntry.display_path).entries:
                        r = dbx.files_get_preview(entry.path_display)[1] #response object
                        print(r.text.count("the"))
                        print(entry.name)
                        pdb.set_trace()
            
    else:   #will need to search through only the years and companies specified by the user
        #searches through the YEAR folders in the Dropbox
        for yearEntry in dbx.files_list_folder('').entries:
            if yearEntry.name in years:
                for companyEntry in dbx.files_list_folder(yearEntry.path_display).entries:
                    if companyEntry.name in companies:
                        for entry in dbx.files_list_folder(companyEntry.path_display).entries:
                            r = dbx.files_get_preview(entry.path_display)[1] #response object
                            print(r.text.count("the"))
                            print(entry.name)
                            pdb.set_trace()

    OrderAndDisplayResults(results)
    for i in final_results:
        if i[1] != 0:
            print(dbx.files_get_temporary_link(i[2]).link)