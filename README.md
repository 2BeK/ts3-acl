# Tower! Simulator 3 - Airline Callsign Lookup (ts3-acl)

## Background
The ACL should basically do what its name says - create tables to lookup the callsigns of all airlines for a specific airport and schedule.
Sure you could extract all airlines from the games CSVs but this will result in a long list of which you only need a few entries per airport.
As a beginner (and also as advanced player) it's a nice thing to have a list with only the emerging airlines.

## How to use
### Fast lane
You can use/download the resulting files for the basic game and Nyerges Design World Traffic standard schedules directly from the corresponding folders.
There are three flavours available - CSV, JSON (single files for each airport/schedule) or Excel (one file for all)

Current state:
- Tower! Simulator 3 - Basic game with __Tower! Places 1 Update__ (incl. KLAX, KLGA, KRDU, TIST, TXKF)
- Nyerges Design - World Traffic __v2.1__

### Need more?
If you use a __custom schedule__ or any other __DLC airports__ you will need to run the scripts by yourself to create your very own lookup tables.

#### Preparation
1. Install python 3.x from https://www.python.org/ (default settings should be okay)
2. Test if python works by opening a command line window (press WIN-key and type "cmd")
   - Type "python" and you should see someting like this:
     ```
     Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
     Type "help", "copyright", "credits" or "license" for more information.
     >>>
     ```
   - If you see it - congratulations, python seems to be working fine
     - If not... well, please use your search engine of choice to find help
   - You can close python by typing ```exit()``` and confirm
3. If you want to use the Excel export, you'll have to install an additional library (if not continue with point 4.)
   - Back to the normal command line prompt ```C:\users\%username%>``` type in ```pip install openpyxl```
     -  This will install the openpyxl library - "A Python library to read/write Excel 2010 xlsx/xlsm files" (https://openpyxl.readthedocs.io/en/stable/)
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
     - Please look for the "Successful" statement at the end
     - If there are any problems... well, please use your search engine of choice to find help
   - You can close the command line window
