import os
import gspread 
from oauth2client.service_account import ServiceAccountCredentials

class RwSpreadsheet:
    scope_v4 = ["https://www.googleapis.com/auth/spreadsheets"]

    def __init__(self, doc_id, json_path):
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(json_path, RwSpreadsheet.scope_v4)
        self.client = gspread.authorize(self.credentials)
        self.doc    = self.client.open_by_key(doc_id)
        self.sheet  = self.doc.sheet1

    def set_sheet(self, name):
        self.sheet = self.doc.worksheet(name)

    def read_cell(self, pos):
        return self.sheet.acell(pos)

    def write_cell(self, pos, value):
        self.sheet.update_acell(pos, value)

    def read_row(self, row):
        return self.sheet.row_values(row)

    def append_row(self, array):
        self.sheet.append_row(array)
