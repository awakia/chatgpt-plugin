import json
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = 'your_spreadsheet_id'

def append_records_to_spreadsheet(records):
    try:
        creds = service_account.Credentials.from_service_account_info(
            json.loads(os.environ['GOOGLE_APPLICATION_CREDENTIALS']), SCOPES)
        service = build('sheets', 'v4', credentials=creds)
        for record in records:
            values = [record["timestamp"], record["text"]]
            body = {
                'values': [values]
            }
            service.spreadsheets().values().append(
                spreadsheetId=SPREADSHEET_ID,
                range='A:B',
                valueInputOption='RAW',
                insertDataOption='INSERT_ROWS',
                body=body).execute()
        return True
    except HttpError as error:
        print(f"An error occurred: {error}")
        return False

if __name__ == '__main__':
    # test_data.json ファイルを開いてデータを読み込む
    with open("test_data.json", "r") as f:
        data = json.load(f)

    # テストデータのレコードをスプレッドシートに追加する
    records = data["records"]
    success = append_records_to_spreadsheet(records)

    # 結果を表示する
    if success:
        print("Records successfully appended to the spreadsheet.")
    else:
        print("Failed to append records to the spreadsheet.")
