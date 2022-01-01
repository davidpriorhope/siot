from googleapiclient import discovery
import gspread
from oauth2client.service_account import ServiceAccountCredentials


#setup & configuration
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Documents/siot_testing/credentials.json', scope) 

client = gspread.authorize(credentials)

service = discovery.build('sheets', 'v4', credentials=credentials)
spreadsheet_id = '1IcC5hPXw8ORDOmnVjd2q9RmzlfLSnAmwbr5Rk7N6taQ' # The spreadsheet to apply the updates to.


def get_chart_data(range_names):
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_names).execute()
    return result.get('values', [])

#now we will temporarily save the data locally on the system

save_name_list = ['summary_day','summary_avg_temp','summary_avg_weather','summary_no_layers']

for i in save_name_list:
    textfile = open('temp_data/' +i+".txt", "w")
    textfile.close()

for i in get_chart_data('Summary!A:D'):
    for j in range(len(i)):
        textfile = open('temp_data/' +save_name_list[j]+".txt", "a")
        textfile.write(str(i[j]) + "\n")
        textfile.close()