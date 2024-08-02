
import datetime
import telebot

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
    bot.register_next_step_handler(message , reply)    
    
def reply(message):
    bot.reply_to(message , 'hello {name} would u like to know your periods date,\n if yes than u can use :-\n/period date')
    
    
@bot.message_handler(commands=['period'])    
def take_dates(message):
    bot.reply_to(message, 'now enter your starting date in date/month/year format(for ex:- 24/12/2022)')
    bot.register_next_step_handler(message, take_days)
    
def take_days(message):    
    chat_id = message.chat.id
    if chat_id not in user_register_dict:
        user_register_dict[chat_id] = {}
    user_register_dict[chat_id]['date'] = message.text
    start_date = datetime.datetime.strptime(message.text, '%d/%m/%Y')  
    bot.reply_to(message, 'how many days your periods last')
    bot.register_next_step_handler(message, take_avg, start_date)

def take_avg(message, start_date):    
    chat_id = message.chat.id
    user_register_dict[chat_id]['days'] = message.text
    period = int(message.text)
    bot.reply_to(message , 'your average length of cycles?\n it is 28 days in most cases or in usual cases.')
    bot.register_next_step_handler(message, result, start_date, period)

def result(message,start_date,period):
    chat_id = message.chat.id
    user_register_dict[chat_id]['average'] = message.text
    start_date = datetime.datetime.strptime(user_register_dict[chat_id]['date'], '%d/%m/%Y')
    period = int(user_register_dict[chat_id]['days'])
    avg = int(user_register_dict[chat_id]['average'])
    period_date = start_date + datetime.timedelta(avg-period)
    bot.send_message(chat_id, 'Period date is {}'.format(period_date.strftime("%d/%m/%Y"))) 

         

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()        
