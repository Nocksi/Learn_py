import config
from aiogram.types import *

a = 0
keyss = []
keyb = InlineKeyboardMarkup()
for i, j in config.LANGDICT.items():
    key = InlineKeyboardButton(j, callback_data=i)
    keyss.append(key)
    a+= 1;
    if a == 3:
        a = 0
        keyb.add(keyss[0], keyss[1], keyss[2])
        keyss = []