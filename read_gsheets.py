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