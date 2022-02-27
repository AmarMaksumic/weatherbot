import os 
import discord

from dotenv import load_dotenv
from msilib.schema import Error

from get import *
from set import set_def_location, set_members

intent = discord.Intents.default()
intent.members = True
client = discord.Client(intents = intent)

load_dotenv()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('.get'):
    command = message.content[5:]
    if command == 'data structures' or command == 'ds':
      await get_ds(message)
    elif command.startswith('dummy'):
      await get_dummy(message)
    elif command == 'kpop':
      await get_kpop(message)
    elif command == 'should i nap':
      await get_nap(message)
    elif command.isdigit():
      await get_weather_at(message, command)
    elif command != '':
      await get_errored(message, command)
    else:
      await get_weather_now(message)
  
  elif message.content.startswith('.set'):
    command = message.content[5:]
    if command.startswith('location'):
      await set_def_location(message)
    elif command == 'members':
      await set_members(message, client)
    else:
      await get_errored(message, command)
      
  elif message.content.startswith('.help'):
    embedVar = discord.Embed(
    title="Commands", description=".get [optional, day delta from now (integer)]", color=0x336EFF
            )
    await message.channel.send(embed=embedVar)

client.run(str(os.getenv('TOKEN')))