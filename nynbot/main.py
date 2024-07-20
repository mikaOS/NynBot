import json 
import logging
import os 
import platform
import random
import sys
from typing import Final
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Context
from dotenv import load_dotenv
from discord import File
from greetings import Greetings
from Joke import Joke
import sys
from io import BytesIO
#from safebooru import rato
sys.path.append('/home/_mika/Documents/nynbot/Safebooru.py')

greetings = Greetings()
joke = Joke()
#rato = get_rato()

discord_intents: discord.Intents = discord.Intents.all()
discord_intents.message_content = True
client: client = discord.Client(intents=discord_intents)

response_intents = {

}

PREFIX = '1'

@client.event
async def on_message(message = discord.Message) -> None:
    if message.author == client.user:
        return None
    if not message.content.startswith(PREFIX):
        return None

    command = message.content[len(PREFIX):].lower()
    
    if command == 'ola':
        await message.channel.send(greetings.get_greeting())
        
    if command == 'meme':
        await message.channel.send()
    
    if command == 'joke':
        await message.channel.send (joke.get_joke())   
        
    if command == 'rato':
        await message.channel.send (rato.get_rato())
            
@client.event        
async def send_message(message: discord.Message, user_message: str) -> None:
    if not user_message:
        print ('Sai daqui glowie!')
        return
    if is_private := user_message [0] == '?':
        user_message = user_message [1:]
        
    try:
        response: str = get_response (user_message)
        await message.author.send if is_private else message.channel.send(response)    
    except Exception as e:
        print (e)

@client.event
async def on_ready():
    print('Hoje a janta é queijinho! ')
    
client.run('')