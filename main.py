import discord
from discord.ext import commands
import time
from keras.models import load_model
import numpy as np
from PIL import Image, ImageOps
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


def detect(image, model):
    np.set_printoptions(suppress=True)
    model = load_model(model, compile=False)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction)
    score = prediction[0][index]
    return index, score


@bot.command('info')
async def cmd_info(ctx: commands.Context):
    await ctx.send('я бот, который может определить какая планета солнеченой системы изображена на картинке')

@bot.command('image')
async def cmd_image(ctx: commands.Context):
    if not ctx.message.attachments:
        await ctx.reply('вы не прекрепили изображение')
        return
    for item in ctx.message.attachments:
        if item.filename.split('.')[-1] not in ('png','jpg','jpeg'):
            await ctx.reply('я принимаю только картинки')
            return
        filename = f'{ctx.message.author.global_name}__{time.time()}.png'
        await item.save('images/'+ filename)
        last_msg = await ctx.reply("картинка получена, ожидайте результата")
        index, score = detect('images/'+filename, 'keras_model.h5')
        if index == 0 and score > 0.7:
            await ctx.send('Это арбуз')
        elif index == 1 and score > 0.7:
            await ctx.send('Это дыня')
        elif index == 2 and score > 0.7:
            await ctx.send('Это кабачок')
        else:
            await ctx.send('не понял')
        await last_msg.delete()
        return
bot.run('')
