import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='/', intents = discord.Intents.all())


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
async def fight(message):
    if pet['выносливость'] >=60 and pet['сила'] > 5:
        enemy = {
            'здоровье' : random.randint (1,100),
            'сила' : random.randint (1, 10),
            'защита' : random.randint (1, 5)
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
