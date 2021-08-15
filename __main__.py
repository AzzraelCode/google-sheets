import os

import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

import creds


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


# service = get_service_simple()
service = get_service_sacc()
sheet = service.spreadsheets()

# https://docs.google.com/spreadsheets/d/xxx/edit#gid=0
sheet_id = "xxx"

# https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get
# resp = sheet.values().get(spreadsheetId=sheet_id, range="Лист1!A1:A999").execute()

# https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/batchGet
resp = sheet.values().batchGet(spreadsheetId=sheet_id, ranges=["Лист1", "Лист2"]).execute()

print(resp)
