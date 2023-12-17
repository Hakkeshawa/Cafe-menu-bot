from telebot import TeleBot

import telebot

from telebot import types

key = '{your bot api}'

bot = telebot.TeleBot(key)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello, welcome to {your rest name}, order and eat great food! Type /menu to see menu")

@bot.message_handler(commands=['menu'])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    salads = types.KeyboardButton("Salads")
    meat = types.KeyboardButton("Meat")
    beverages = types.KeyboardButton("Beverages")
    snacks = types.KeyboardButton("Snacks")
    burger = types.KeyboardButton("Burgers")
    fish = types.KeyboardButton("Fish")
    pasta = types.KeyboardButton("Pasta")    
    markup.add(salads, meat, beverages, snacks, burger, fish, pasta)
    
    bot.send_message(message.chat.id, "Select option:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Salads")
def saladschoice(message):
    bot.send_message(message.chat.id, "Here's all our salads")
    button_ceasar = types.InlineKeyboardButton('Ceasar Salad', callback_data='Ceasar Salad')
    button_oliver = types.InlineKeyboardButton('Oliver Salad', callback_data='Oliver Salad')
    button_greek = types.InlineKeyboardButton('Greek Salad', callback_data='Greek Salad')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_ceasar)
    keyboard.add(button_oliver)
    keyboard.add(button_greek)
    bot.send_message(message.chat.id, text='Please pick up a salad you want!', reply_markup=keyboard)

@bot.message_handler(func=lambda message : message.text == "Meat")
def meatchoice(message):
    bot.send_message(message.chat.id, "Here's all our meat!")
    button_tbone = types.InlineKeyboardButton("T-Bone Steak", callback_data='T-Bone Steak')
    button_filet = types.InlineKeyboardButton("Filet Mignon", callback_data='Filet Mignon')
    button_ribeye = types.InlineKeyboardButton("Rib Eye", callback_data='Rib Eye')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_tbone)
    keyboard.add(button_filet)
    keyboard.add(button_ribeye)
    bot.send_message(message.chat.id, text="Please pick up a meat you want!", reply_markup=keyboard)

@bot.message_handler(func=lambda message : message.text == "Beverages")
def meatchoice(message):
    bot.send_message(message.chat.id, "Here's all our beverages!")
    button_coke = types.InlineKeyboardButton("Coca Cola", callback_data='Coca Cola')
    button_vine = types.InlineKeyboardButton("Vine", callback_data='Vine')
    button_whiskey = types.InlineKeyboardButton("Whiskey", callback_data='Whiskey')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_coke)
    keyboard.add(button_vine)
    keyboard.add(button_whiskey)
    bot.send_message(message.chat.id, text="Please pick up a beverage you want!", reply_markup=keyboard)

@bot.message_handler(func=lambda message : message.text == "Snacks")
def meatchoice(message):
    bot.send_message(message.chat.id, "Here's all our snacks!")
    button_onion = types.InlineKeyboardButton("Onion Rings", callback_data='Onion Rings')
    button_fries = types.InlineKeyboardButton("Fries", callback_data='Fries')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_onion)
    keyboard.add(button_fries)
    bot.send_message(message.chat.id, text="Please pick up a snack you want!", reply_markup=keyboard)

@bot.message_handler(func=lambda message : message.text == "Burgers")
def meatchoice(message):
    bot.send_message(message.chat.id, "Here's all our burgers!")
    button_cheeseb = types.InlineKeyboardButton("Cheeseburger", callback_data='Cheeseburger')
    button_hamb = types.InlineKeyboardButton("Hamburger", callback_data='Hamburge')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_cheeseb)
    keyboard.add(button_hamb)
    bot.send_message(message.chat.id, text="Please pick up a burger you want!", reply_markup=keyboard)

@bot.message_handler(func=lambda message : message.text == "Fish")
def meatchoice(message):
    bot.send_message(message.chat.id, "Here's all our fish!")
    button_tuna = types.InlineKeyboardButton("Tuna Steak", callback_data='Tuna Steak')
    button_sushi = types.InlineKeyboardButton("Sushi", callback_data='Sushi')
    button_dried = types.InlineKeyboardButton("Dried Fish", callback_data='Dried Fish')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_tuna)
    keyboard.add(button_sushi)
    keyboard.add(button_dried)
    bot.send_message(message.chat.id, text="Please pick up a fish you want!", reply_markup=keyboard)

@bot.message_handler(func=lambda message : message.text == "Pasta")
def meatchoice(message):
    bot.send_message(message.chat.id, "Here's all our pasta!")
    button_bolog = types.InlineKeyboardButton("Spaghetti Bolognaise", callback_data='Spaghetti Bolognaise')
    button_carb = types.InlineKeyboardButton("Carbonara", callback_data='Carbonara')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_bolog)
    keyboard.add(button_carb)
    bot.send_message(message.chat.id, text="Please pick up a meat you want!", reply_markup=keyboard)



bot.infinity_polling()