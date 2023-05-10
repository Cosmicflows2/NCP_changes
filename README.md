# NCP_changes
This is tool for monitoring website changes regarding NCPs for Horizon EU.

At the time of writing this project, we needed to create a website monitoring tool for specific content on one web page. The page is located on the website of the European Commission and contains data on all current National Contact Persons (NCPs) for Cluster 4 in Horizon Europe (HEU). We need to detect changes on that page so that we can contact newcomers. This tool is not designed to track email address changes, nor to track people's name changes. The page we monitor is published by the European Commission with the date of the last update as well as the identification number. This tool only tracks and searches for changes in those two fields.

This tools is not automated, so manual download of data is necessary. For this we will use Chrome developer options. After the content of webpage is downloaded it will be proccessed with this python code.

Necessary steps are next:
1) Chrome -> inspect -> <html> tag -> right click -> copy -> copy element
2) Paste in txt file -> save with some date in the name of file
2.1) if there are more than 100 entries on the page, so that they can not be presented on the same page, just repeat step 1 and paste in the same file at the bottom, and then save.
3) Next day do the same procedure and save in the new file with different name (again with some date).
4) Use python code, change at the begining of the file names of input files, for older and newer file.
5) Save python code and run the code to detect changes in "Update date:" and "Record control number" fields.
6) Changes will be written at standard output as well as in the file results.txt.
