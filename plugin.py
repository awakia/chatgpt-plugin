import json
import os
from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()
credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

SCOPES = ['https://googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1XoKeX8eyShOSGBnktdJ78lU1iSP_Rjf3ckKPn9mhxBA'


# def append_records_to_spreadsheet(records):
#     try:
#         creds = service_account.Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
#         service = build('sheets', 'v4', credentials=creds)
#         for record in records:
#             values = [record["timestamp"], record["text"]]
#             body = {
#                 'values': [values]
#             }
#             service.spreadsheets().values().append(
#                 spreadsheetId=SPREADSHEET_ID,
#                 range='A:B',
#                 valueInputOption='RAW',
#                 insertDataOption='INSERT_ROWS',
#                 body=body).execute()
#         return True
#     except HttpError as error:
#         print(f"An error occurred: {error}")
#         return False


def append_records_to_spreadsheet(records):
    print(records)
    for record in records:
        values = [record["timestamp"], record["message"]]
        print(values)
    return True


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
