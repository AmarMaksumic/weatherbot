import random

from datetime import date, timedelta
from json_operators import read_json
from weather import get_forecast

async def get_weather_at(message, day):
  day = int(day)
  server_data = read_json('servers.json')
  text, temp, prov = await get_forecast(server_data[str(message.guild.id)]['def_location'], day)
  if text == 'none':
    await message.channel.send('No data for ' + str(date.today() + timedelta(days = int(day))))
  else:
    await message.channel.send(str(date.today() + timedelta(days = int(day))) + ': ' + str(text) + ' ' + str(temp) + '°F.')
    await message.channel.send('Provider: ' + prov)
    media = read_json('media.json')
    if str(text) in media['weather']:
      await message.channel.send(random.choice(media['weather'][str(text)]))

async def get_weather_now(message):
  server_data = read_json('servers.json')
  text, temp, prov = await get_forecast(server_data[str(message.guild.id)]['def_location'], 'now')
  if text == 'none':
    await message.channel.send('No data for right now')
  else:
    await message.channel.send('Weather right now: ' + str(text) + ', ' + str(temp) + '°F.')
    await message.channel.send('Provider: ' + prov)
    media = read_json('media.json')
    if str(text) in media['weather']:
      await message.channel.send(random.choice(media['weather'][str(text)]))

async def get_errored(message, command):
  media = read_json('media.json')
  await message.channel.send('i cannot ' + command)
  await message.channel.send(random.choice(media['wrong command']))

async def get_ds(message):
  media = read_json('media.json')
  await message.channel.send(random.choice(media['data structures']))

async def get_dummy(message):
  media = read_json('media.json')
  users_defaced = 0
  users_attempted = 0
  for user in message.mentions:
    print(str(user))
    if str(user) == "Shu-Wei(Wendy) Chen#2363":
      await message.channel.send('<@!' + str(message.author.id) + '> is the real dummy.')
      users_defaced += 1
    elif str(user) in media['dummy']:
      await message.channel.send('<@!' + str(message.mentions[users_attempted].id) + '> ' + random.choice(media['dummy'][str(user)]))
      users_defaced += 1
    users_attempted += 1
  if users_defaced == 0:
    await message.channel.send(random.choice(media['dummy']['generic']))

async def get_kpop(message):
  media = read_json('media.json')
  await message.channel.send('You should watch this MV!')
  await message.channel.send(random.choice(media['kpop']))

async def get_nap(message):
  media = read_json('media.json')
  await message.channel.send('I sayyyyyyyyy')
  await message.channel.send(random.choice(media['nap']))
