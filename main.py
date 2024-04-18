import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='/', intents = discord.Intents.all())

pet = {
    'health': 100,
    'strength': 1,
    'defence': 1
}
@bot.command('help')
async def help(message):
    await message.send('/train')
    await message.send('/feed')
    await message.send('/fight')
    await message.send('/help')
@bot.command('train')
async def train(message):
    pet['strength'] +=2
    pet['health'] -=10
    await message.send('ваш питомец прошёл изнуртельные тренировки')
    await message.send(str(pet))

@bot.command('feed')
async def feed(message):
    pet['health'] += 20
    await message.send('ваш питомец хорошо поел')
    await message.send(str(pet))

@bot.command('fight')
async def fight(message):
    enemy = {
        'health' : random.randint (1,100),
        'strength' : random.randint (1, 10),
        'defence' : random.randint (1, 10)
    }
    await message.send('вы атакуете врага')
    while enemy['health'] >= 0 and pet['health'] >= 0:
        pet['health'] -= enemy['strength'] - pet['defence']
        enemy['health'] -= pet['strength'] - enemy['defence']
        await message.send('ваш питомец:' +str(pet))
        await message.send('ваш враг:' +str(enemy))
    if enemy['health'] > pet['health']:
        await message.send('вы проиграли!')
    else:
        await message.send('вы выиграли!')
@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'дикий {member.name} появился {discord.utils.format_dt(member.joined_at)}')
bot.run('')
