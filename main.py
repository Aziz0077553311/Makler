import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import threading
import time
import os

token = '7653124309:AAE2O_kF6ZajJzSaQbwdqDKXYMMeLU5GdKw'
bot = telebot.TeleBot(token)

# Webhookni o'chirish
bot.remove_webhook()

ads = [
    {
        "text": "1 xona 2 xona kilnin'gan yo'l domdan eski go'sht dyukon\nRuporasida 3 etaj 470ml tl 9308353584\nMakler xizmati bor",
        "images": ['photo1.jpg', 'photo2.jpg', 'photo3.jpg', 'photo4.jpg', 'photo5.jpg', 'photo6.jpg']
    },
    # ... boshqa e'lonlar ...
]

active_users = set()

def send_buttons(chat_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("NAVOIY ARZON UYLAR ✅", url='https://t.me/Arzon_uylari'))
    markup.add(InlineKeyboardButton("1 XONALI UYLAR ✅", url='https://t.me/+OAbLerahLHM4NGEy'))
    markup.add(InlineKeyboardButton("2 XONALI UYLAR ✅", url='https://t.me/+0d1ikFWh7Ww1NTYy'))
    markup.add(InlineKeyboardButton("3-4 XONALI UYLAR ✅", url='https://t.me/+FX3nGqvgT64zOGJi'))
    markup.add(InlineKeyboardButton("XOVLILAR ✅", url='https://t.me/+vMyhdyq278FkOTky'))
    markup.add(InlineKeyboardButton("ADMIN ✅", url='https://t.me/Baxtiyor_makler'))

    if os.path.exists('1.jpg'):
        with open('1.jpg', 'rb') as photo:
            bot.send_photo(chat_id, photo, reply_markup=markup)
    else:
        bot.send_message(chat_id, "❌ Fayl '1.jpg' topilmadi!")

def ad_loop(chat_id):
    while chat_id in active_users:
        for ad in ads:
            if chat_id not in active_users:
                break
            try:
                media = []
                for img_path in ad['images']:
                    if os.path.exists(img_path):
                        with open(img_path, 'rb') as f:
                            media.append(InputMediaPhoto(f.read()))
                    else:
                        bot.send_message(chat_id, f"❌ Rasm topilmadi: {img_path}")
                        break
                if media:
                    bot.send_media_group(chat_id, media)
                    bot.send_message(chat_id, ad['text'])
                time.sleep(15)
            except Exception as e:
                bot.send_message(chat_id, f"❌ Xatolik: {str(e)}")
                time.sleep(60)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    if chat_id not in active_users:
        active_users.add(chat_id)
        send_buttons(chat_id)
        threading.Thread(target=ad_loop, args=(chat_id,)).start()
        bot.send_message(chat_id, "✅ Reklama boshladi!")
    else:
        bot.send_message(chat_id, "ℹ️ Sizda allaqachon reklama ishlayapti.")

@bot.message_handler(commands=['stop'])
def stop(message):
    chat_id = message.chat.id
    if chat_id in active_users:
        active_users.remove(chat_id)
        bot.send_message(chat_id, "✅ Reklama to‘xtatildi.")
    else:
        bot.send_message(chat_id, "ℹ️ Sizda reklama ishlamayapti.")

if __name__ == '__main__':
    print("🚀 Bot ishga tushdi...")
    bot.polling(none_stop=True)
