import os
import sys
import dropbox
from dropbox.exceptions import AuthError

TOKEN = os.environ.get('DROPBOX_TOKEN')
yFlag = False
cFlag = False
year = ''
comp = ''
keywords = []

final_results = [[0, 0, 0]]


def CheckAgainstKeywords(file):
    file = file.lower()
    count = 0
    for i in keywords:
        i = i.lower()
        if i in file:
            count += 1
    return count


def ParseRawSearch(raw_search):
    # -k keywords -y year -c company
    delimited_search = raw_search.split("-")
    for value in delimited_search:
        # Apparently Python lacks a switch statement
        # immpliments keywords, year, company
        if value:
            if value[0] == 'k':
                split_keywords = value.split(" ")
                for i in range(1, len(split_keywords)):
                    keywords.append(split_keywords[i])
            elif value[0] == 'c':
                global comp
                global cFlag
                cFlag = True
                comp = value[2:]
                if comp[len(comp) - 1] == " ":
                    comp = comp[0:len(comp) - 1]
            elif value[0] == 'y':
                global year
                global yFlag
                cFlag = True
                year = value[2:]
                if year[len(year) - 1] == " ":
                    year = year[0:len(year) - 1]
            else:
                print("Bad format")


def OrderAndDisplayResults(results):
    high_count = [0, 0, 0]
    for i in results:
        if i[1] >= high_count[1]:
            high_count = i

    if high_count != [0, 0, 0]:
        final_results.append(high_count)
        results.remove(high_count)
        OrderAndDisplayResults(results)


if __name__ == '__main__':
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

    raw_search = input("Enter a search string")
    ParseRawSearch(raw_search)
    results = [[0, 0, 0]]

    for entry in dbx.files_list_folder('', True).entries:
        print(entry)
        if "." in entry.path_display:
            # Year is index 1, company is index 2, filename is index 3
            file_year = entry.path_display.split('/')[1]
            file_comp = entry.path_display.split('/')[2]
            file_name = entry.path_display.split('/')[3]

            file_flag = True

            if cFlag:
                if file_comp != comp:
                    file_flag = False

            if yFlag:
                if file_year != year:
                    file_flag = False

            if file_flag:
                count = CheckAgainstKeywords(file_name)
                if count:
                    results.append([file_name, count, entry.path_display])

    OrderAndDisplayResults(results)
    for i in final_results:
        if i[1] != 0:
            print(dbx.files_get_temporary_link(i[2]).link)