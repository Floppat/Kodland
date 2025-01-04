import telebot
import config
import random
import datetime

import telebot

API_TOKEN = config.token

bot = telebot.TeleBot(API_TOKEN)

class Human():
    def __init__(self, name, surname, age,knowledge=20,stamina=100, hunger=0):
        self.name = name
        self.surname = surname
        self.age = age
        self.knowledge = knowledge
        self.stamina = stamina
        self.hunger = hunger
    
    def info(self):
        return (f'--- information about human {self.name} ---\n'
                f'    | name: {self.name}\n'
                f'    | surname: {self.surname}\n'
                f'    | age: {self.age}\n'
                f'    | knowledge: {self.knowledge}\n'
                f'    | stamina: {self.stamina}\n'
                f'    | hunger: {self.hunger}')
            
    def sleep(self):
        self.stamina = 100
        print(f"{self.name}, ohayo! ^^'")
    def eat(self):
        self.hunger = 0
        print(f'{self.name}, run for you life. run to dining room. Sucess! you got a one serving. lucky')

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """привет! я повторяю слова за тобой!
                                помимо этого у меня есть несколько других команд:
                                /info - автор
                                /random - рандомное число в диапазоне от 1 до 10
                                /poll - опрос 
                                /after_NY - время прошндшее после нового года
                                /human [name] [surname] [age] - создаёт человека ч данными именем фамилией и возврастом. дальнейший функционал в будущих версиях""")


@bot.message_handler(commands = 'info')
def info(message):
    bot.reply_to(message, 'привет! я учебный бот программиста Floppat на GitHub')

@bot.message_handler(commands = 'random')
def info(message):
    bot.reply_to(message, random.randint(1, 10))

@bot.message_handler(commands=["poll"])
def create_poll(message):
    bot.send_message(message.chat.id, "What we gonna do tomorrow?")
    answer_options = ["go to Park", "draw cat", "just chilling", "do some sport exercises"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="We gonna",
        options=answer_options,
        # если я хочу не простой опрос а викторину:
        # type="poll",
        # correct_option_id=2,
        is_anonymous=True,
    )

@bot.message_handler(commands=["after_NY"])
def NY_left(message):
    t1 = datetime.datetime.now()
    t2 = datetime.datetime(2025,1,1)
    bot.send_message(message.chat.id,str(t1-t2))

@bot.message_handler(commands=["human"])
def human(message):
    args = telebot.util.extract_arguments(message.text).split()
    print(args)
    human = Human(args[0],args[1],args[2])
    bot.send_message(message.chat.id,f'human {human.name} created')
    bot.send_message(message.chat.id,human.info())
    
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
