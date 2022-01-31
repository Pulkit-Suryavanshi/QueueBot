import discord
import os
from replit import db
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

client = discord.Client()

queue=[]
i=0

@client.event
async def on_ready():
  print('We have logged in as {0.user} '.format(client))
  #pulkit testing security:
  for guild in client.guilds:
    print(guild)
    print(guild.id)
  role1 = discord.utils.get("Security level 01")#S is the name of this
  print(role1)
  #pulkit testing security end:
  
@client.event
async def on_message(message) : 
  if message.author == client.user:
    return
   
  if message.content.startswith('!ping'):
    await message.channel.send('Pong!')
    name=message.author.name
    await message.channel.send('Hey'+ message.author.mention)

  #Join
  if message.content.startswith('!join'):
    name=message.author.mention
    #db[""] = name
    if(name in queue):
      await message.channel.send(message.author.mention+" already in queue")
    else:
      queue.append(message.author.mention)
      position = len(queue)
      await message.channel.send(message.author.mention+" has been added to the queue on position: "+str(position)+"\n please stay in the voice channel while you're waiting")

  #Leave
  if message.content.startswith('!leave'):
    name=message.author.mention
    if(name not in queue):
      await message.channel.send(message.author.mention+" already removed")
    else:
      queue.remove(name)
      await message.channel.send(message.author.mention+" has been removed from the queue")


  #Next
  if message.content.startswith('!next'):
    
    if queue:
      n=queue.pop(0)
      await message.channel.send(n+" is next")
    else:
      await message.channel.send("The queue is empty")


  #Display
  if message.content.startswith('!display'):
    if queue:
      await message.channel.send("Students in the Queue are:")
      for i in range(0,len(queue)):
        await message.channel.send(str(i+1)+" : "+queue[i])
      #await message.channel.send(queue)
    else:
      await message.channel.send("The queue is empty")
  
  #to empty the list
  if message.content.startswith('!empty'):
    with queue.mutex:
      queue.queue.clear()
    await message.channel.send("Queue is empty")

  #help
  if message.content.startswith('!help'):
    await message.channel.send("!join - To Join the Queue\n!leave - To leave the Queue\n!display - To display the Queue\n!next (Only Instructors) - To see the next person in the Queue")

  if message.content.startswith('!role'):
    await message.channel.send("Hi "+message.author.mention+", You have role: "+str(message.author.roles[1])) #gives role as Security Level 01

#keep_alive()
my_secret = os.environ['token1']
client.run(my_secret)

