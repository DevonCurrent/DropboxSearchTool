# Requirement Match Document

## Requirement list
These are the requirements that were agreed upon with our client during our first semester:
1. The program allows for files on the dropbox to be searched by the users using Slack messages.
   - Met
2. The program allows the user the ability to add optional search parameters for company, year(s), file-type, version number, and date last modified.
   - This has been modified to search by folder(s) instead of companies and years. This is more generic and will be able to adapt to other Dropbox structures instead of a specific type of Dropbox layout. We cannot search by version number, but this was something the client confirmed we do not need.
3. Files are searchable by either keywords in their titles or filename and possible optional search parameters.
   - Met
4. Plaintext, Microsoft Word, Powerpoint, and Excel files are searched by keywords in both their title and their content.\
   - Exceeded. Able to search by the requirements, as well as PDFs. This was a modified requirement by the clients.
5. The program returns 10 files, ordered by most to least similar based on the search query, to the user.
   - Modified. The clients decided taht 5 files was enough, and this can be easily changed by future developers.
6. The program allows the user to request instructions on how to use the program.
   - Met
7. On first time usage, the program sends the user instructions.
   - Met
8. The program gives a score to each file that is searched so that files are returned in an order of most accurate searches: three points for a keyword correlation in the file’s name and one point for each correlation in the content of the file.
   - Modified. A more advanced searching algorithm is used to make searches for relatable files on Dropbox. The client only had requested that they receive accurate files. We researched into the domain, and found a solution for them that worked better than the one proposed.
9.  The program needs to be able to receive multiple search queries in a short period of time from different users and be able to return all queries to the correct users. 
   - Met
10. The program alerts the user if a connection to Dropbox cannot be established.
   - Met
11. The program alerts the user if the supplied search query is not formatted correctly.
   - Met
12. The program alerts the user if no file exists correlating to their search query.
   - Met



**All requirements were met for the client. Some requirements were modified to increase the efficiency of the application, and to make a better tool for the client.**