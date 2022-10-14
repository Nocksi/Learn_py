from googletrans import Translator
import aiogram
import sqlite3
from aiogram import types
import config
import klav
transl = Translator()

bot = aiogram.Bot(token=config.TOKEN)

dp = aiogram.Dispatcher(bot)
con = sqlite3.connect('baza.db')
print('база загружена')

@dp.message_handler(commands=['start'])
async def process_start_command(message: aiogram.types.Message):

    mycursor = con.cursor()

    sql = "SELECT * FROM users WHERE id = ?"
    adr = (str(message.from_user.id),)
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    print(myresult)
    if myresult is None or myresult == [] or myresult == ():
        mycursor = con.cursor()
        sql = "INSERT INTO users (id, lang) VALUES (?, ?)"
        val = (str(message.from_user.id), "en")
        mycursor.execute(sql, val)
        con.commit()
        await message.reply("Привет! Я бот - переводчик", reply_markup=klav.keyb)
    else:
        await message.reply("Привет! Я бот - переводчик", reply_markup=klav.keyb)

    await message.reply(config.STARTMSG)


@dp.message_handler(commands=['choose'])
async def process_start_command(message: aiogram.types.Message):
    await message.reply(config.CHOOSEMSG, reply_markup=klav.keyb)


@dp.callback_query_handler(lambda c: c.data)
async def process_callback_kb1btn1(callback_query: aiogram.types.CallbackQuery):
    if callback_query.data in config.LANGUES:

        lang = callback_query.data

        mycursor = con.cursor()
        sql = "UPDATE users SET lang = ? WHERE id = ?"
        val = (lang, str(callback_query.from_user.id))

        mycursor.execute(sql, val)
        await bot.send_message(callback_query.from_user.id, "Язык изменён на  " + config.LANGDICT[lang] +
                               ". Для смены языка используйте комманду /choose")

@dp.message_handler()
async def echo_message(msg: types.Message):
    print(2343)
    mycursor = con.cursor()
    sql = "SELECT * FROM users WHERE id = ?"
    adr = (msg.from_user.id,)
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    lang = myresult[0][1]
    word = transl.translate(msg.text, dest=lang).text
    # a = str(str(msg.from_user.id) + str(myresult))

    await bot.send_message(msg.from_user.id, word)

if __name__ == '__main__':
    aiogram.executor.start_polling(dp)