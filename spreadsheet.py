import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint   

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive' ]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client =gspread.authorize(creds)
sheet = client.open('Legislators 2017').sheet1

# pp = pprint.PrettyPrinter()

# Coomand Below returns ALL values in a given sheet:
#result =sheet.get_all_records()

# Command Below returns ALL Values (Observations) across a given ROW:
#result = sheet.row_values(6)

# Command Below returns ALL Values (Observations) down a given COLUMN:
# result = sheet.col_values(6)

# Command Below returns the value of a SPECIFIC Cell:
# result = sheet.cell(4,20).value

# Print out the result - Phone number in this case:
# print(result)

# Commands below will update the phone number, reassign the variable and print it out in terminal:
#result = sheet.cell(6,11).value
#sheet.update_cell(6,11, '555-555-5555')
#result = sheet.cell(6,11).value
#sheet.update_cell(6,11, '555-867-5309')
#result = sheet.cell(6,11).value
#print(result)




# What if we wanted to insert our own values?

# Values which are getting inputted to the sheet
#row = ["I'm", "Updating", "A", "Spreadsheet", "From", "Python"] 

# The row that's getting updated
#index = 3 

# Function sheet.insert (gets the array which we called "row", and row which we called "index")  
#sheet.insert_row(row, index)



# What if we wanted to delete a row?
# sheet.delete_row(3)

# What if we wanted the metadata (how many rows are there?) 
#print(sheet.row_count)

