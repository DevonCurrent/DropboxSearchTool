import os
import sys
import dropbox
from dropbox.exceptions import AuthError
import pdb
from urllib.request import Request, urlopen
import gzip
from bs4 import BeautifulSoup

TOKEN = os.environ.get('DROPBOX_TOKEN')
cFlag = False
yFlag = False
final_results = [[0, 0, 0]]

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

    # Check for an access token
    if (len(TOKEN) == 0):
        sys.exit("No Access token")

    # Create an instance of a Dropbox class, which can make requests to the API.
    dbx = dropbox.Dropbox(TOKEN)

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

                url = dbx.sharing_get_file_metadata(entry.path_display).preview_url
                #url = dbx.sharing_create_shared_link(entry.path_display).url
                html = urlopen(url).read()
                pdb.set_trace()

                soup = BeautifulSoup(html)
                

                # kill all script and style elements
                for script in soup(["script", "style"]):
                    script.extract()    # rip it out

                # get text
                text = soup.get_text()

                # break into lines and remove leading and trailing space on each
                lines = (line.strip() for line in text.splitlines())
                # break multi-headlines into a line each
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                # drop blank lines
                text = '\n'.join(chunk for chunk in chunks if chunk)
                
                print(text)



                # an attempt to get a temporary link and open it.
                """
                url = dbx.files_get_temporary_link(entry.path_display).link
                req = Request(url)
                pdb.set_trace()
                html = gzip.decompress(urlopen(req).read()).decode('utf-8')
                """
                
                
                # an attempt to get a link to the file and then search the file's contents
                """
                urllib3.disable_warnings()
                link = dbx.files_get_temporary_link(entry.path_display).link
                http = urllib3.PoolManager(
                    cert_reqs='CERT_REQUIRED', 
                    ca_certs=certifi.where())
                pdb.set_trace()
                r = http.request('GET', link)
                print(r.read())
                """
                
                

    
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