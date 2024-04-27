import discord
import os
import random
from discord.ext import commands
import requests
bot = commands.Bot(command_prefix='/', intents = discord.Intents.all())

@bot.command('mem')
async def mem(foto):
    x = random.randint(1,101)
    if x >=1 and x <= 20:
        with open(f'images/mem1.jpg', 'rb') as f:
            picture = discord.File(f)
        await foto.send(file = picture)
    if x >21 and x <= 90:
        with open(f'images/mem2.jpg', 'rb') as f:
            picture = discord.File(f)
        await foto.send(file = picture)
    if x >91 and x <= 100:
            with open(f'images/mem3.jpg', 'rb') as f:
                picture = discord.File(f)
            await foto.send(file = picture)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


bot.run('')
