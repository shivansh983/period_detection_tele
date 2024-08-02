import os
import telegram.ext
import telebot
import calendar as cl

BOT_TOKEN = '5782007803:AAEzVj3Jr3ia0mgD2ZUpGX2AUtzKJIXOUaA'

bot = telebot.TeleBot(BOT_TOKEN)
user_register_dict = {}


#start
@bot.message_handler(commands=['start', 'hello'])
def start(message):
    bot.reply_to(message, "welcome! i am rose.\nand you are ?")
    user_register_dict[message.chat.id] = {}
    name= message.text
    name= str.title(name)
    bot.register_next_step_handler(message , start_step2)
    

    
def start_step2(message):
    user_register_dict[message.chat.id]['name'] = message.text
    bot.reply_to(message , 'now enter your starting date in mon/date/year format')
    
    
    bot.register_next_step_handler(message , start_step3)
    
def start_step3(message):    
    user_register_dict[message.chat.id]['date'] = message.text
    bot.reply_to(message , 'how many days your periods last')
    user_register_dict[message.chat.id] = {}
    days= message.text
    days = int(days)   
    bot.register_next_step_handler(message , start_step4)
    
def start_step4(message):    
    user_register_dict[message.chat.id]['days'] = message.text
    bot.reply_to(message , 'your average length of cycles?\n it is 28 days in most cases or in usual cases.')
    user_register_dict[message.chat.id] = {}
    avg= message.text
    avg= int(avg)
    bot.register_next_step_handler(message , start_step5)
    
def start_step5(message):    
    
    user_register_dict[message.chat.id]['average'] = message.text
    bot.reply_to (message , '{average + days}')
    bot.register_next_step_handler(message , start_step4)        
    

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()        
