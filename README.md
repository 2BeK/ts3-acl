# Tower! Simulator 3 - Airline Callsign Lookup (ts3-acl)

## Background
The ACL should basically do what its name says - create tables to lookup the callsigns of all airlines _for a specific airport and schedule_.
Sure you could extract all airlines from the games CSVs but this will result in a long list of which you only need a few entries per airport.
As a beginner (and also as advanced player) it's a practical thing to have a list with only the emerging airlines.

## How to use
### Fast lane
You can use/download the resulting files for the basic game and Nyerges Design World Traffic standard schedules directly from the corresponding folders.
There are three flavours available - CSV, JSON (single files for each airport/schedule) or Excel (one file for all).

Current state:
- Tower! Simulator 3 - Basic game with __Tower! Places 1 Update__ (incl. KLAX, KLGA, KRDU, TIST, TXKF)
- Nyerges Design - World Traffic __v2.1__

### Need more?
If you use a __custom schedule__ or any other __DLC airports__ you will need to run the scripts by yourself to create your very own lookup tables.

#### Preparation
1. Install python 3.x from https://www.python.org/ (default settings should be okay)
2. Test if python works by opening a command line window (press ```WIN``` key, type ```cmd``` and confirm)
   - Type ```python``` and confirm. You should see someting like this:
     ```
     Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
     Type "help", "copyright", "credits" or "license" for more information.
     >>>
     ```
   - If you see it python seems to be working fine
     - If not... well, please use your search engine of choice to find help
       - Some hints:
         * Restart your computer (and redo step 2)
         * ```python.exe``` needs to be in your Windows ```PATH``` system variable to work from any path
   - Close the python prompt by typing ```exit()``` and confirm
3. If you want to use the Excel export, you'll have to install an additional library (if not continue with point 4.)
   - Back to the normal command line prompt ```C:\users\%username%>``` type in ```pip install openpyxl``` and confirm
     - This will install the openpyxl library - "A Python library to read/write Excel 2010 xlsx/xlsm files" (https://openpyxl.readthedocs.io/en/stable/)
     - It should result in a response like this:
     ```
     Collecting openpyxl
       Downloading openpyxl-3.1.1-py2.py3-none-any.whl (249 kB)
          |████████████████████████████████| 249 kB 3.3 MB/s
     Collecting et-xmlfile
       Downloading et_xmlfile-1.1.0-py3-none-any.whl (4.7 kB)
     Installing collected packages: et-xmlfile, openpyxl
     Successfully installed et-xmlfile-1.1.0 openpyxl-3.1.1
     ```
     - Look for the "Successful" statement at the end
       - If there are any problems... well, again please use your search engine of choice to find help
4. Close the command line window
 
If you've come so far - congratulations. The hardest part is done (hopefully).
 
#### Downloading the scripts
5. Now you need at least the basic script to create your lookup tables:
   - [Basic script (CSV & JSON)](ts3_acl_csv_json.py)
6. If you want to use the Excel export you also need the Excel script:
   - [Excel script](ts3_acl_excel.py)
7. Download the file(s) you need and store them in an empty folder of your choice (e.g. ```C:\users\%username%\Desktop\TS3_ACL>```)

#### Run the basic script
8. After the files are downloaded to the folder, open it and open a new command line window in the folders path (by typing ```cmd``` into the adress line of the folder window: [SCREENSHOT MISSING])
9. Start the basic script by typing ```python ts3_acl_csv_json.py``` (e.g. ```C:\users\%username%\Desktop\TS3_ACL>python ts3_acl_csv_json.py```) and confirm
10. The script will ask for your game path:
    ```
    Paste game path (e.g. C:\SteamLibrary\steamapps\common\Tower! Simulator 3):
    _
    ```
11. Copy and paste your game path (or write it down) and confirm
    - For steam installations: You can find the path under [STEAM DESCRIPTION]
    - For non-steam installations: You should know where you've installed the game ;)
12. The script now automatically browses through the game folders and reads all the data it needs

#### The Result
13. After the script has finished you will find two new subfolders (```csv``` and ```json```) in the directory where the script files are (e.g. ```C:\users\%username%\Desktop\TS3_ACL>```)
14. In there you will find your lookup tables in CSV or JSON format separated by airport and schedule

#### Run the Excel script

#### The Result 2.0
