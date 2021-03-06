import requests
import telepot
import configparser

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        chat_id = msg['chat']['id']
        text = msg['text']

        if text == "/help":
            bot.sendMessage(chat_id,'Hi, I\'m everfilter bot. \n if you send me an picture, '
                            'I\'ll give you everfiltering picture. \n Only jpg file is enable to use.')

    if content_type == 'photo':
        print('received a picture')
        bot.download_file(msg['photo'][-1]['file_id'], './file.jpg')
        with open('./file.jpg', 'rb') as f:
            r = requests.post('http://api.everfilter.me/filters/shinkai?nightscape=0',files={'media': f})
        with open('./everfilter_result.jpg', 'wb') as f:
            f.write(r.content)
        bot.sendMessage(chat_id,'please wait a few seconds')
        with open('./everfilter_result.jpg', mode="rb") as f_result:
            bot.sendPhoto(chat_id, f_result)


#bot = telepot.Bot("318673002:AAEd7Ezq5g6GKgYfw0etXBX8yL-wu16GXNo")
cfg = configparser.ConfigParser()
cfg.read('token.cfg')
bot = telepot.Bot(cfg['everfilter_bot']['token'])
print('Listening ...')
bot.message_loop({'chat': on_chat_message}, run_forever=True)
