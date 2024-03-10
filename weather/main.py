#MODULES
import os
from keep_alive import keep_alive
import discord
import requests
import json
from weather import *


#STARTER
api_key = 'key'
client = discord.Client()
command_prefix = '$w'


#MAIN
@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(command_prefix):
        if len(message.content.replace(command_prefix, '')) >= 1:
            location = message.content.replace(command_prefix, '').lower()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial'
            try:
                data = parse_data(json.loads(requests.get(url).content)['main'])
                await message.channel.send(embed=weather_message(data, location))
            except KeyError:
                await message.channel.send(embed=error_message(location))


#SHUSH
keep_alive()
my_secret = os.environ['token']
client.run(my_secret)
