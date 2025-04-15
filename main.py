import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import time
import os

token = '7653124309:AAE2O_kF6ZajJzSaQbwdqDKXYMMeLU5GdKw'
bot = telebot.TeleBot(token)

# Удаляем webhook, если был установлен ранее
bot.remove_webhook()

running = True

ads = [
    {
        "text": "1 xona 2 xona kilnin'gan yo'l domdan eski go'sht dyukon\nRuporasida 3 etaj 470ml tl 9308353584\nMakler xizmati bor",
        "images": ['photo1.jpg', 'photo2.jpg', 'photo3.jpg', 'photo4.jpg', 'photo5.jpg', 'photo6.jpg']
    },
    # ... boshqa e'lonlar ...
]

def send_ad(chat_id):
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

@bot.message_handler(commands=['start'])
def welcome(message):
    global running
    chat_id = message.chat.id
    running = True

    send_ad(chat_id)

    while running:
        for ad in ads:
            if not running:
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

@bot.message_handler(commands=['stop'])
def stop_bot(message):
    global running
    running = False
    bot.send_message(message.chat.id, "✅ Bot to'xtatildi")

if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"❌ Botda xatolik: {e}")
            time.sleep(10)
