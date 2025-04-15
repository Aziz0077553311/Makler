import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import time

# Токен вашего бота
token = '7653124309:AAE2O_kF6ZajJzSaQbwdqDKXYMMeLU5GdKw'
bot = telebot.TeleBot(token)

# Флаг для управления циклом
running = True

ads = [
    {
        "text": "1 xona 2 xona kilnin'gan yo'l domdan eski go'sht dyukon\nRuporasida 3 etaj 470ml tl 9308353584\nMakler xizmati bor",
        "images": ['photo1.jpg', 'photo2.jpg', 'photo3.jpg', 'photo4.jpg', 'photo5.jpg', 'photo6.jpg']
    },
    {
        "text": "2 xona 3 xona kilnin'gan 4 etaj narpayi uyda\nYo'l ustida tinchlik domi ipoteka ham bo'ladi 100m² 620ml",
        "images": ['photo7.jpg', 'photo8.jpg', 'photo9.jpg', 'photo10.jpg', 'photo11.jpg', 'photo12.jpg']
    },
    {
        "text": "1 xona 2 xona kilnin'gan 6 etaj 7 etaj dom left bor.\n22 maktab oldida 60m² 430ml ham ipoteka",
        "images": ['photo13.jpg', 'photo14.jpg', 'photo15.jpg', 'photo16.jpg', 'photo17.jpg', 'photo18.jpg']
    },
    {
        "text": "2 xona 2 etaj hamroz 23 maktab oldida jihozlari bilan 700ml.",
        "images": ['photo19.jpg', 'photo20.jpg', 'photo21.jpg', 'photo22.jpg', 'photo23.jpg', 'photo24.jpg']
    },
    {
        "text": "Srochnoiladi\n7 etajli uy sotilmoqda 1/2 xona kilnin'gan remonti o'rtacha.\nKvadarti katta trohxilisin dom.\nManzili 80 do'kon oldida.\nNarz 450 million kelishamiz.\nTel 9308353584 992787779.",
        "images": ['photo25.jpg', 'photo26.jpg', 'photo27.jpg', 'photo28.jpg', 'photo29.jpg', 'photo30.jpg']
    },
    {
        "text": "2 xona 2 etaj 80m² Yangi bozor oldida 600ml tl 9308353584 992787779.",
        "images": ['photo31.jpg', 'photo32.jpg', 'photo33.jpg', 'photo34.jpg', 'photo35.jpg', 'photo36.jpg']
    },
    {
        "text": "3 xona 4 etaj 7 m/p Jasorat 1 xonalar alohida 2 tarafda balkon ipoteka bo'ladi 650ml.",
        "images": ['photo37.jpg', 'photo38.jpg', 'photo39.jpg', 'photo40.jpg', 'photo41.jpg', 'photo42.jpg']
    },
    {
        "text": "Srochno uy sotiladi\n16 etajli dom 11-etaji 2 xona remonti toza ayrim narsalari qoladi.",
        "images": ['photo43.jpg', 'photo44.jpg', 'photo45.jpg', 'photo46.jpg', 'photo47.jpg', 'photo48.jpg']
    },
    {
        "text": "Uy srochni sotiladi\n4 etajli dom 4 etajda 3 xona remonti toza ayrim narsalari qoladi galereya.",
        "images": ['photo49.jpg', 'photo50.jpg', 'photo51.jpg', 'photo52.jpg', 'photo53.jpg', 'photo54.jpg']
    },
    {
        "text": "Srochni ijara beriladi. Shodlikda 13 maktab yaqin. 2 xonali 1 etaj\nRasmdaqi holatda\nOylaga beriladi 2 mln. Makler xizmati.",
        "images": ['photo55.jpg', 'photo56.jpg', 'photo57.jpg', 'photo58.jpg', 'photo59.jpg', 'photo60.jpg']
    }
]

def send_ad(chat_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("NAVOIY ARZON UYLAR ✅", url='https://t.me/Arzon_uylari'))
    markup.add(InlineKeyboardButton("1 XONALI UYLAR ✅", url='https://t.me/+OAbLerahLHM4NGEy'))
    markup.add(InlineKeyboardButton("2 XONALI UYLAR ✅", url='https://t.me/+0d1ikFWh7Ww1NTYy'))
    markup.add(InlineKeyboardButton("3-4 XONALI UYLAR ✅", url='https://t.me/+FX3nGqvgT64zOGJi'))
    markup.add(InlineKeyboardButton("XOVLILAR ✅", url='https://t.me/+vMyhdyq278FkOTky'))
    markup.add(InlineKeyboardButton("ADMIN ✅", url='https://t.me/Baxtiyor_makler'))
    
    try:
        with open('1.jpg', 'rb') as photo:
            bot.send_photo(chat_id, photo, reply_markup=markup)
    except FileNotFoundError:
        bot.send_message(chat_id, "❌ Файл '1.jpg' не найден!")

@bot.message_handler(commands=['start'])
def welcome(message):
    global running
    chat_id = message.chat.id
    running = True
    
    
    while running:  # Цикл работает, пока running == True
        send_ad(chat_id)
        for ad in ads:
            if not running:  # Проверка флага перед отправкой
                break
            try:
                media = [InputMediaPhoto(open(img, 'rb')) for img in ad['images']]
                bot.send_media_group(chat_id, media)
                bot.send_message(chat_id, ad['text'])
                time.sleep(15)  # Задержка 15 секунд
            except Exception as e:
                bot.send_message(chat_id, f"❌ Ошибка: {str(e)}")
                time.sleep(60)  # Ожидание перед повторной попыткой

@bot.message_handler(commands=['stop'])
def stop_bot(message):
    global running
    chat_id = message.chat.id
    running = False  # Устанавливаем флаг в False, чтобы остановить цикл
    bot.send_message(chat_id, "bot toxtatildi")

# Запуск бота
if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")
        time.sleep(10)  # Ожидание перед перезапуском