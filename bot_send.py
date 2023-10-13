import telebot
import time
import googlesheets, database


bot = telebot.TeleBot('6408658506:AAGBX2zOQmPKhO6akF1hxqNFaNJhhs3jXf0')

chat_id = '-4007892162'



def send_data_to_telegram():
    response = googlesheets.get_comment()
    headers = response[0]
    record = response[-1]
    message = ""
    for header, value in zip(headers[2:], record[2:]):
        message += f"<b>{header}</b> {value}\n"
    message = message.replace("::", ":").replace(": :", ":").strip()
    print(message)
    bot.send_message(chat_id, message, parse_mode='HTML')



while True:
    tester = database.check_comment()
    if tester:
        time.sleep(5)
    else:
        database.save_comment()
        send_data_to_telegram()








