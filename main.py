import discord
import os
client =discord.Client()
@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.conent.startwith('/ls clan'):
        await message.channel.send('Banu Haqim Brujah Gangrel Hecata Lasombra Malkavian The Ministry Nosferatu Ravnos Salubri Toreador Tremere Tzimisce Ventrue Caitiff Thin-blood')

client.run('')