import os
from random import randrange

import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

"""
Эта ветка для Видео о записи в электронные таблицы Google Sheets
с помощью API Google Sheets 
https://youtu.be/RV-aN_WEFPE
"""

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

# Плейлист Google Sheets API https://www.youtube.com/playlist?list=PLWVnIRD69wY75tQAmyMFP-WBKXqJx8Wpq
# https://docs.google.com/spreadsheets/d/xxx/edit#gid=0
spreadsheet_id = "1IfE0sBAkKvhB6F8zHkEozEE0jpwhAU_G4UubwKTV1Bk"

# Получаю ID листа в электронной таблице
# Нужен для repeatCell/range/sheetId
# https://docs.google.com/spreadsheets/d/1IfE0sBAkKvhB6F8zHkEozEE0jpwhAU_G4UubwKTV1Bk/edit#gid=758897038
# https://docs.google.com/spreadsheets/d/<ID электронной таблицы (spreadsheet ID)>/edit#gid=<ID листа (sheet ID) >
# sheet_id = 758897038
resp = get_service_sacc().spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=["Лист3"], includeGridData=False).execute()
sheet_id = resp.get("sheets")[0].get("properties").get("sheetId")

def get_random_color() -> dict:
    """
    Создаю случайный цвет с альфа каном
    https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/other#Color
    :return:
    """
    return {
        "red": randrange(0, 255) / 255,
        "green": randrange(0, 255) / 255,
        "blue": randrange(0, 255) / 255,
        "alpha": randrange(0, 10) / 10 # 0.0 - прозрачный
    }

# https://developers.google.com/sheets/api/samples/formatting

# ТАК сделано В ВИДЕО и так работает, однако ....
# body={
#     "requests" : { ### <<<<<--- тут словарь, так не надо
#         # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/request#repeatcellrequest
#         "repeatCell": {
#             # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/other#GridRange
#             "range": {
#                 "sheetId": sheet_id,
#                 "startRowIndex": 2,
#                 "startColumnIndex": 2,
#                 "endColumnIndex": 7,
#                 "endRowIndex": 6,
#             },
#             # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/cells
#             # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/cells#CellFormat
#             "cell": {
#                 "userEnteredFormat": {
#                     "backgroundColor" : get_random_color(),
#                     "horizontalAlignment": "LEFT",
#                     "textFormat": {
#                         "foregroundColor": get_random_color(),
#                         "fontFamily": "Arial",
#                         "bold": False
#                     }
#                 },
#             },
#             # https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask
#             "fields": "userEnteredFormat.backgroundColor"
#         }
#     }
# }

# лучше использовать массив
body = {
    "requests": [ # <<<<--- МАССИВ, так НАДО !!!
        # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/request#repeatcellrequest
        {
            "repeatCell": {
                # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/other#GridRange
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": 2,
                    "startColumnIndex": 2,
                    "endColumnIndex": 7,
                    "endRowIndex": 6,
                },
                # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/cells
                # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/cells#CellFormat
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": get_random_color(),
                        "horizontalAlignment": "LEFT",
                        "textFormat": {
                            "foregroundColor": get_random_color(),
                            "fontFamily": "Arial",
                            "bold": False
                        }
                    },
                },
                # https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask
                "fields": "userEnteredFormat.backgroundColor"
            }
        }
    ]
}

# https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/request
resp = get_service_sacc().spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()