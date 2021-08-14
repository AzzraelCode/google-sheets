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

# https://docs.google.com/spreadsheets/d/1IfE0sBAkKvhB6F8zHkEozEE0jpwhAU_G4UubwKTV1Bk/edit#gid=0
sheet_id = "1IfE0sBAkKvhB6F8zHkEozEE0jpwhAU_G4UubwKTV1Bk"

# https://developers.google.com/resources/api-libraries/documentation/sheets/v4/python/latest/sheets_v4.spreadsheets.html
resp = sheet.values().get(spreadsheetId=sheet_id, range="Лист1").execute()

print(resp)
