
import discord
from discord.ext import client
import asyncio
import random

@client.event
async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

async def on_message(self, message):
        if message.content.startswith('!editme'):
            msg = await message.channel.send('10')
            await asyncio.sleep(3.0)
            await msg.edit(content='40')

async def on_message_edit(self, before, after):
        msg = f'**{before.author}** edited their message:\n{before.content} -> {after.content}'
        await before.channel.send(msg)

async def mem(ctx):
        with open('images/meme1.jpg', 'rb') as f:
            # Memorizziamo il file della libreria di Discord convertito in questa variabile!
            picture = discord.File(f)
    # Possiamo quindi inviare questo file come parametro!
        await ctx.send(file=picture)

async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$aiuto'):
        x = random.randint(1,3)
        if x == 1:
                await message.channel.send("evitare lo spreco di cibo")
        elif x == 2:
                await message.channel.send("ridurre l'uso della plastica")
        elif x == 3:
              await message.channel.send("ridurre il consumo di acqua")
              
    else:
        await message.channel.send(message.content)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
client.run("TOKEN")
