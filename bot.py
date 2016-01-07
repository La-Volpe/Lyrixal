import telebot
import utilities
with open ("key.txt", "r") as key:
    token =  key.read().strip()
API_TOKEN = token

bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['help', 'start'])
def send_message(message):
    bot.reply_to(message, """/lyric [artist name]-[songe name]
    /find [Artist Name] - [Song Name]
    Example:
    /lyric Slipknot-Snuff""")

@bot.message_handler(commands=['lyric'])
def get_lyrics(message):
    raw = message.text
    if len(raw) < 7 :
        bot.reply_to(message, "Oops! You didn't say anything! Try /help to learn more.")
    else:
        info = raw[5: len(raw)]
        info = info.split("-")
        artist = info[0]
        song = info[1]
        xml = utilities.fetch_lyrics(artist, song)
        lyric = utilities.parser(xml, "Lyric")
        if song.lower().strip() = 'roshani':
            with open('sina.txt', 'r') as sina:
                roshani = sina.read().strip()
            bot.reply_to(message, roshani)
        else:
            bot.reply_to(message, lyric)
@bot.message_handler(commands=['find'])
def find(message):
    raw = message.text
    if len(raw) < 6 :
        bot.reply_to(message, "Oops! You didn't say anything! Try /help to learn more.")
    else:
        info = raw[5: len(raw)]
        info = info.split("-")
        artist = info[0]
        song = info[1]
        _json = utilities.fetch_from_wiki(artist, song)
        response = utilities.response(_json)
        if song == 'Roshani' or song == 'roshani' or song == ' roshani' or song == ' Roshani':
            with open('sina.txt', 'r') as sina:
                roshani = sina.read().strip()
            bot.reply_to(message, roshani)
        else:
            bot.reply_to(message, response)

# Buncha Easter eggs below
# They are starting to outgrow the main functionality!
MehdiSticker = 'BQADBAADDAIAAsY-4gABkYqH6Pg8d3UC'
JavadSticker = 'BQADBAADLgQAApv7sgABhbe8T1HBWC4C'
MohsenSticker = 'BQADBAADfwkAAhRfVQOHXHZgd1N9-gI'
SinaSticker = 'BQADBAADhAQAApv7sgABfrYz202X0VUC'
MahyarSticker = 'BQADBAADiwkAAhRfVQN3IC-BPzbIlQI'

@bot.message_handler(commands=['easter', 'eggs', 'eastereggs'])
def javad(message):
    bot.reply_to(message, """/javad
    /mehdi or /facepalm
    /mohsen
    /sina
    /mahyar""")


@bot.message_handler(commands=['javad','Javad'])
def javad(message):
    bot.send_sticker(message.chat.id, JavadSticker)

@bot.message_handler(commands=['Mehdi','mehdi','facepalm'])
def facepalm(message):
    bot.send_sticker(message.chat.id, MehdiSticker)

@bot.message_handler(commands=['mohsen', 'Mohsen'])
def keephydrated(message):
    bot.send_sticker(message.chat.id, MohsenSticker)

@bot.message_handler(commands=['sina','Sina'])
def keephydrated(message):
    bot.send_sticker(message.chat.id, SinaSticker)

@bot.message_handler(commands=['Mahyar','mahyar'])
def keephydrated(message):
    bot.send_sticker(message.chat.id, MahyarSticker)
#@bot.message_handler(func=lambda message: True, content_types=['sticker'])
#def getid(message):
#    fileid = message.sticker.file_id
#    bot.reply_to(message, fileid)


bot.polling()

while True:
    pass
