import dropbox

dbx = dropbox.Dropbox("insert your access token here")
dbx.users_get_current_account()

for entry in dbx.files_list_folder('').entries:
    #if(type(entry) == dropbox.files.FolderMetadata):
    print(entry.name)


print(dbx.files_get_metadata('/P_20171030_190556_BF.jpg').server_modified)

print("_________")



for match in dbx.files_search('', 'V').matches:
    print("%s\n\t%s" % (match.metadata.name, match.metadata.path_display))