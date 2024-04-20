import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='/', intents = discord.Intents.all())

coins = 0
win = 10
lose = 1
pet = {
    'здоровье': 100,
    'сила': 2,
    'защита': 1,
    'выносливость': 100
}
@bot.command('guide')
async def guide(message):
    await message.send('каждый день (до использования команды /sleep) вы можете 2 раза потренироватся, затем 1 раз поесть.')
    await message.send('за день можно 2 раза потренироватся, или 1 раз потренироватся и 1 раз подратся')
    await message.send('совет: лучше перед боем не тренероватся, ведь будет меньше здоровья, а поесть вы не сможете')
    await message.send('тактика про: каждый день 2 раза тренироваться и 1 раз есть, после того как набралось 10 атаки на следущий день идти в бой')
    await message.send('пока функций мало, но надеюсь игра вам понравится!')
@bot.command('cmd')
async def cmd(message):
    await message.send('попробуйте /train  (+сила; -здоровье; -выносливость)')
    await message.send('попробуйте /feed  (+здоровье; +выносливость)')
    await message.send('попробуйте /fight  (-здоровье (ведь это же битва))')
    await message.send('попробуйте /sleep  (полное восстановление выносливости)')
    await message.send('попробуйте /cmd')
    await message.send('попробуйте /guide  (ввод в игру)')
    await message.send('попробуйте /shop  (покупка артефактов)')
@bot.command('shop')
async def shop(message):
    await message.send('/s400;   400 монет    5 защиты')   
    await message.send('/s800;   800 монет   10 защиты') ##########################################################################################################################
    await message.send('/s1200;  1200 монет  15 защиты')
    await message.send('/s1600;  1600 монет  20 защиты')
    await message.send('/s2000;  2000 монет  25 защиты')
@bot.command('s400')
global coins
async def s400(message):
    if coins >= 400:
        coins = coins - 400
        pet['защита'] = 5
        await message.send('остаток денег:') 
        await message.send(coins)
        await message.send(str(pet))
    else:
        await message.send('денег не хватает') 
        await message.send(str(pet))
@bot.command('s800')
global coins
async def s800(message):
    if coins >= 800:
        coins = coins - 800
        pet['защита'] = 10
        await message.send('остаток денег:') 
        await message.send(coins)
        await message.send(str(pet))
    else:
        await message.send('денег не хватает') 
        await message.send(str(pet))
@bot.command('s1200')
global coins
async def s1200(message):
    if coins >= 1200:
        coins = coins - 1200
        pet['защита'] = 15
        await message.send('остаток денег:') 
        await message.send(coins)
        await message.send(str(pet))
    else:
        await message.send('денег не хватает') 
        await message.send(str(pet))
@bot.command('s1600')
global coins
async def s1600(message):
    if coins >= 1600:
        coins = coins - 1600
        pet['защита'] = 20
        await message.send('остаток денег:') 
        await message.send(coins)
        await message.send(str(pet))
    else:
        await message.send('денег не хватает') 
        await message.send(str(pet))
@bot.command('s2000')
global coins
async def s2000(message):
    if coins >= 2000:
        coins = coins - 2000
        pet['защита'] = 25
        await message.send('остаток денег:') 
        await message.send(coins)
        await message.send(str(pet))
    else:
        await message.send('денег не хватает') 
        await message.send(str(pet))
@bot.command('train')
async def train(message):
    if pet['здоровье'] >=20 and pet['выносливость'] >= 40:
        pet['сила'] +=2
        pet['здоровье'] -=10
        pet['выносливость'] -=40
        await message.send('ваш питомец прошёл изнуртельные тренировки')
        await message.send(str(pet))
    else:
        await message.send('ваш питомец слишком устал/голоден для тренеровок')
        await message.send(str(pet))

@bot.command('feed')
async def feed(message):
    if pet['здоровье'] <= 80:
        pet['здоровье'] += 20
        pet['выносливость'] += 10
        await message.send('ваш питомец хорошо поел')
        await message.send(str(pet))
    else:
        await message.send('ваш питомец не хочет есть')
        await message.send(str(pet))

@bot.command('fight')
global lose,coins, win
async def fight(message):
    if pet['выносливость'] >=60 and pet['сила'] > lose:
        enemy = {
            'здоровье' : random.randint (1,100),
            'сила' : random.randint (lose, win),
            'защита' : random.randint (1, lose)
        }
        pet['выносливость'] -=60
        await message.send('вы атакуете врага')
        while enemy['здоровье'] >= 0 and pet['здоровье'] >= 0:
            pet['здоровье'] -= enemy['сила'] - pet['защита']
            enemy['здоровье'] -= pet['сила'] - enemy['защита']
            await message.send('ваш питомец:' +str(pet))
            await message.send('ваш враг:' +str(enemy))
        if enemy['здоровье'] > pet['здоровье']:
            await message.send('вы проиграли!')
        else:
            await message.send('вы выиграли!')
            await message.send('вы заработали:')
            coins = coins + 100
            win = win + 2
            lose = lose + 2
            await message.send(coins)
            await message.send('монет')
            await message.send('вы выиграли. противник стал посильнее.')
    else:
        await message.send('сперва вашему питомцу следует восстановить силы')
@bot.command('sleep')
async def sleep(message):
    if pet['выносливость'] <40:  
        pet['выносливость'] = 100
        await message.send('ваш питомец хорошо поспал')
        await message.send(str(pet))
    else:
        await message.send('ваш питомец ещё не устал')
bot.run('')
