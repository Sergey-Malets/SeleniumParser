from selenium_parser import parse_hh

#Update - кусок информации полученный нами от телеграма
from telegram import Update

#ApplicationBuilder - способ создать приложение с указанием настроек
from telegram.ext import ApplicationBuilder, MessageHandler, filters

#token - секретный ключ к вашему боту(получить у БотФазер)
app = ApplicationBuilder().token("5561145242:AAGRsxive9hif9oVcDQDx7lVV67hwoBPzZw").build()

#функция вызывается при получении смс
#ctx служебная информация
async def text_reply(upd: Update, _cxt):
    user_text = upd.message.text
    print(f"He: {user_text}")
    name = upd.message.from_user.full_name
    reply = f"Dear {name}, we reply you request: {user_text}"
    print(reply)
    await upd.message.reply_text(reply)
    job_count = parse_hh(user_text)
    await upd.message.reply_text(f"найдено {job_count} вакансий")


# Handler - обработчик сообщения
handler = MessageHandler(filters.TEXT, text_reply)
#MessageHandler для сообщений (...
#

# Прикрепляем обработчик к приложению
app.add_handler(handler)

# Запускаем приложение
app.run_polling()