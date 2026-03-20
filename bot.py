import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "8576159430:AAHDuFL1CbUcsErAS6z1vt0yV65brj4ksl8"
ADMIN_ID = 7963952038

bot = telebot.TeleBot(BOT_TOKEN)
subscribers = set()

@bot.message_handler(commands=['start'])
def start(message):
    subscribers.add(message.chat.id)
    bot.send_message(message.chat.id, "✅ Ти підписався на розсилку!")
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("GET $50", url="https://qzino.click/50usdt"))
    text = (
        "💸 $50 for All New Players 💸\n\n"
        "Your bonus is already waiting 👇\n\n"
        "🎰 Start playing right away\n"
        "⚡ Fast payouts\n"
        "🔓 No KYC\n\n"
        "✌️ Big wins start with one spin."
    )
   bot.send_photo(message.chat.id, open("/app/image.png", "rb"), caption=text, reply_markup=markup)

@bot.message_handler(commands=['post'])
def post(message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        parts = message.text[6:].split("|")
        text = parts[0].strip()
        url = parts[1].strip()
        button_text = parts[2].strip() if len(parts) > 2 else "Перейти на сайт"
    except:
        bot.send_message(message.chat.id, "❌ Формат:\n/post Текст | https://сайт.com | Назва кнопки")
        return
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(button_text, url=url))
    count = 0
    for uid in subscribers:
        try:
            bot.send_message(uid, text, reply_markup=markup)
            count += 1
        except:
            pass
    bot.send_message(message.chat.id, f"✅ Надіслано {count} підписникам!")

@bot.message_handler(commands=['count'])
def count_cmd(message):
    if message.from_user.id != ADMIN_ID:
        return
    bot.send_message(message.chat.id, f"👥 Підписників: {len(subscribers)}")

bot.polling()
