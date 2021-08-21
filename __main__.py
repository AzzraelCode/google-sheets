import os
from random import randrange

import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

import creds


"""
Эта ветка для Видео о записи в электронные таблицы Google Sheets
с помощью API Google Sheets 
https://youtu.be/RV-aN_WEFPE
"""

def get_service_simple():
    return build('sheets', 'v4', developerKey=creds.api_key)


def get_service_sacc():
    """
    Могу читать и (возможно) писать в таблицы кот. выдан доступ
    для сервисного аккаунта приложения

    sacc-1@privet-yotube-azzrael-code.iam.gserviceaccount.com

    :return:
    """
    creds_json = os.path.dirname(__file__) + "/creds/sacc1.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)


sheet = get_service_sacc().spreadsheets()

# https://docs.google.com/spreadsheets/d/xxx/edit#gid=0
sheet_id = "xxx"


# https://developers.google.com/resources/api-libraries/documentation/sheets/v4/python/latest/sheets_v4.spreadsheets.html

def get_values():
    values = [[randrange(10, 99)]]
    # values = [[randrange(10, 99) for _ in range(0, 6)]]
    # values = [[randrange(10, 99)] for _ in range(0, 3)]
    # values = [[randrange(10, 99) for _ in range(0, 3)] for _ in range(0, 3)]
    return values


# https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/update
resp = sheet.values().update(
    spreadsheetId=sheet_id,
    range="Лист2!H1",
    valueInputOption="RAW",
    body={'values' : get_values() }).execute()


# https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/append
# resp = sheet.values().append(
#     spreadsheetId=sheet_id,
#     range="Лист2!A1",
#     valueInputOption="RAW",
#     # insertDataOption="INSERT_ROWS",
#     body={'values' : get_values() }).execute()

# https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/batchUpdate
# body = {
#     'valueInputOption' : 'RAW',
#     'data' : [
#         {'range' : 'Лист2!D2', 'values' : get_values()},
#         {'range' : 'Лист2!H4', 'values' : get_values()}
#     ]
# }

# resp = sheet.values().batchUpdate(spreadsheetId=sheet_id, body=body).execute()


print(resp)
