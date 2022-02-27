from asyncore import write
from http import server
from json_operators import read_json, write_json
from weather import is_loc_valid

async def set_def_location(message):
  location = message.content[14:]
  if (location == ''):
    await message.channel.send('No location entered.')
  else:
    await message.channel.send('Setting location to: ' + location + '.')
    if (await is_loc_valid(location)): 
      guild_id = str(message.guild.id)
      guild_name = str(message.guild.name)
      server_data = read_json('servers.json')
      print(server_data)
      if not guild_id in server_data:
        server_data[guild_id] = {}
      server_data[guild_id]['def_location'] = location
      write_json(server_data, 'servers.json')
      print('Set default location in ' + guild_id
            + ' (name: ' + guild_name + ') to '
            + location)
      await message.channel.send('Set default location in ' + guild_id
            + ' (name: ' + guild_name + ') to '
            + location)
    else:
      await message.channel.send(location + ' is not a valid location.')

async def set_members(message, client):
  guild_id = str(message.guild.id)
  guild = client.get_guild(message.guild.id)
  members = guild.members
  members_data = read_json('members.json')
  if not guild_id in members_data:
    members_data[guild_id] = []
  for member in members:
    if not ( str(member.name) + '#' + str(member.discriminator) ) in members_data[guild_id]:
      members_data[guild_id].append(str(member.name) + '#' + str(member.discriminator))
  write_json(members_data, 'members.json')