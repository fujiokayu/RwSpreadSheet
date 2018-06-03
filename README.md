# RwSpreadsheet

This is the simple wrapper of [gspread](https://github.com/burnash/gspread) to read/write Google Spreadsheet.  
[gspread](https://github.com/burnash/gspread) is already enough, but just I need more simple way to initialyze. 

## Getting Started

1. Follow [this document](http://gspread.readthedocs.io/en/latest/oauth2.html), make account key json file and install some libraries.
1. Activate Google Sheets API on your [Google Developers Console](https://console.developers.google.com/apis).
1. Use this api as follows:
```
from RwSpreadsheet import RwSpreadsheet
from datetime import datetime

if __name__ == '__main__':
    
    doc_id = "your sheets id"
    json_path = "your api key json path"

    # __init__
    spreadsheet = RwSpreadsheet(doc_id, json_path)

    # if you want, you can change active worksheet by name. Default is first sheet.
    # spreadsheet.set_sheet("other_sheet")

    # append row
    write_values = ["test",datetime.now().strftime("%Y/%m/%d %H:%M:%S")]
    spreadsheet.append_row(write_values)

    # write / read cell
    spreadsheet.write_cell('A1', 'updated')
    print(spreadsheet.read_cell('A1'))
    print(spreadsheet.read_row(2))
```
