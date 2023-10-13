import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread.exceptions import APIError
import time


# Путь к JSON-ключу, который вы скачали
json_keyfile = 'json.json'

# Устанавливаем область видимости и аутентифицируемся
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)
gc = gspread.authorize(credentials)

def get_comment():
    try:
        # Открываем таблицу по её названию
        worksheet = gc.open('ОС Админа').sheet1

        data = worksheet.get_all_values()
        # print(data)
        return data
    except APIError as e:
        if e.response.status_code == 503:
            # The service is currently unavailable, so wait and retry
            print("Service is unavailable. Retrying in 5 seconds...")
            time.sleep(5)
            # Retry the operation here
        else:
            # Handle other API errors as needed
            print("API Error:", e)












