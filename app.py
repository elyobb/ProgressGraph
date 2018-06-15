"""
Shows basic usage of the Sheets API. Prints values from a Google Spreadsheet.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import json
from flask import Flask, render_template


SPREADSHEET_ID = '1-G38xZL7N4NhpiuAGbU9KKS2p_FdPf3NhFk4Bf_G124'
RANGE_NAME_1 = '1 Mile!A2:B'
RANGE_NAME_2 = '2 Miles!A2:B'

app = Flask(__name__)



def connect():
    # Setup the Sheets API
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    return build('sheets', 'v4', http=creds.authorize(Http()))


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/getData", methods=['GET'])
def retrieve_data():
    service = connect()

    result1 = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                 range=RANGE_NAME_1).execute()
    result2 = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                 range=RANGE_NAME_2).execute()
    values1 = result1.get('values', [])
    values2 = result2.get('values', [])

    dict1 = {}
    for row in values1:
        dict1[row[0]] = row[1]
    dict2 = {}
    for row in values2:
        dict2[row[0]] = row[1]

    return json.dumps({
        "1": dict1,
        "2": dict2
    })


if __name__ == "__main__":
    app.run()


