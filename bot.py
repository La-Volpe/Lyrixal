import telebot
import utilities
API_TOKEN = "120683812:AAHtpwKIZJgw44Hjn9Q35Vmq2h94NRxg0SM"
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['help', 'start'])
def send_message(message):
    bot.reply_to(message, """Use /get [artist name]-[songe name]
    Example: /get Slipknot-Snuff""")
@bot.message_handler(commands=['get'])
def get_lyrics(message):
    raw = message.text
    if len(raw) < 5 :
        bot.reply_to(message, "Oops! You didn't say anything! Try /help to learn more.")
    else:
        info = raw[5: len(raw)]
        info = info.split("-")
        artist = info[0]
        song = info[1]
        xml = utilities.fetch_lyrics(artist, song)
        lyric = utilities.parser(xml, "Lyric")
        bot.send_message(message.chat.id, lyric)
bot.polling()

while True:
    pass