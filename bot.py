import telebot
import utilities
with open ("key.txt", "r") as key:
    token =  key.read().strip()
API_TOKEN = token

bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['help', 'start'])
def send_message(message):
    bot.reply_to(message, """Use /lyric [artist name]-[songe name]
    Example: /lyric Slipknot-Snuff""")
@bot.message_handler(commands=['lyric'])
def get_lyrics(message):
    raw = message.text
    if len(raw) < 6 :
        bot.reply_to(message, "Oops! You didn't say anything! Try /help to learn more.")
    else:
        info = raw[5: len(raw)]
        info = info.split("-")
        artist = info[0]
        song = info[1]
        xml = utilities.fetch_lyrics(artist, song)
        lyric = utilities.parser(xml, "Lyric")
        bot.reply_to(message, lyric)
MehdiSticker = 'BQADBAADDAIAAsY-4gABkYqH6Pg8d3UC'
JavadSticker = 'BQADBAADLgQAApv7sgABhbe8T1HBWC4C'
@bot.message_handler(commands=['javad'])
def javad(message):
    bot.send_sticker(message.chat.id, JavadSticker)

@bot.message_handler(commands=['mehdi','facepalm'])
def facepalm(message):
    bot.send_sticker(message.chat.id, MehdiSticker)     

@bot.message_handler(commands=['mohsen'])
def keephydrated(message):
    bot.send_message(message.chat.id, "I want you\n\r\n\r\n\rTo #KeepHydrated!")  
    
 
#@bot.message_handler(func=lambda message: True, content_types=['sticker'])
#def getid(message):
#    fileid = message.sticker.file_id
#    bot.reply_to(message, fileid)
    

bot.polling()

while True:
    pass
