import json
import sqlite3
import googlesheets as google

connection = sqlite3.connect('data.db')
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS admin_info (id INTEGER, save_text TEXT);')
# sql.execute('INSERT INTO admin_info (id, save_text) VALUES (1, "some_text");')
# connection.commit()


def save_comment():
    connection = sqlite3.connect('data.db')
    sql = connection.cursor()
    data = google.get_comment()[-1]
    data_list = json.dumps(data)
    sql.execute('UPDATE admin_info SET save_text = ? WHERE id = 1;', (data_list,))
    connection.commit()
    connection.close()


def check_comment():
    connection = sqlite3.connect('data.db')
    sql = connection.cursor()
    data = google.get_comment()[-1]
    data_list = json.dumps(data)
    get_db = sql.execute('SELECT save_text FROM admin_info;').fetchone()[0]
    if data_list == get_db:
        return True
    else:
        return False


