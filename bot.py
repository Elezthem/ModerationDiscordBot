import asyncio
import disnake
from disnake.ext import commands

from asyncio import sleep

import os

from config.table_create import tablecreate

import sqlite3

from config.settings import settings

connection = sqlite3.connect("server1.db") 
cursor = connection.cursor()

client = commands.Bot(command_prefix = '!', intents=disnake.Intents.all(), test_guilds=[1148955538080677959])
client.remove_command('help')

tablecreate()

@client.command()
@commands.has_permissions(administrator=True)
async def nick(inter, member: disnake.Member, nickname):
    await member.edit(nick=nickname)

@client.event
async def on_ready():
  guilds = len(client.guilds)
  info = "!"
  print(f"{client.user.name} запущен(а))".format(info)) #в командную строку идёт инфа о запуске
  while True:
    await client.change_presence(status = disnake.Status.dnd, activity = disnake.Activity(name = f'JOIN FOR JOIN CENTRAL', type = disnake.ActivityType.playing)) #Идёт инфа о команде помощи (префикс изменить)
    await asyncio.sleep(15)
    await client.change_presence(status = disnake.Status.dnd, activity = disnake.Activity(name = f'behind {len(client.guilds)} servers', type = disnake.ActivityType.watching)) #Инфа о количестве серверов, на котором находится бот.
    await asyncio.sleep(15)
    members = 0
    for guild in client.guilds:
      for member in guild.members:
        members += 1
    await client.change_presence(status = disnake.Status.idle, activity = disnake.Activity(name = f'behind {members} members', type = disnake.ActivityType.watching)) #Общее количество участников, за которыми следит бот (Находятся на серверах)
    await asyncio.sleep(15)

async def load_extension(): 
    for commands in settings['commands']:
        try:
            client.load_extension(commands)
        except Exception as e:
            print(f"Error loading commands: {e}") 

    for errors in settings['errors']:
        try:
            client.load_extension(errors)
        except Exception as e:
            print(f"Error loading errors: {e}") 
 
    for events in settings['events']:
        try:
            client.load_extension(events)
        except Exception as e:
            print(f"Error loading events: {e}")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    tablecreate()
    await load_extension()
    await client.start(settings["TOKEN"])


if __name__ == '__main__':
    client.loop.run_until_complete(main())
    
