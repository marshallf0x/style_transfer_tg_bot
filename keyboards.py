from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_transfer = InlineKeyboardButton('Transfer style', callback_data='get_pic_1')
inline_info = InlineKeyboardButton('Info', callback_data='info')
inline_dev = InlineKeyboardButton('Developer', callback_data='info_dev')

inline_kb = InlineKeyboardMarkup().add(inline_transfer).add(inline_info).add(inline_dev)