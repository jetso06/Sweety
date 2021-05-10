#MODULES
import os
from keep_alive import keep_alive
import discord
from discord.ext import commands, tasks
from itertools import cycle
import random


#STARTER
client = commands.Bot(command_prefix = '$')
status = cycle(['with chaka','with manga','with thenga','with thalachorú','with alavalathy','with kirmi kadi','with pottan','with mandan','Doodh ka dhula','Chor-police','with sasura','like Khatarnak','like Sikander','caz Ghar ki murgi daal barabar','caz Door ke dhol suhavne lagte hain','with khichdi','with Pataka','but...Ungli mat kar','caz Ullu bana diya','caz Jiski lathi uski bhais','caz Bagal main bachcha shahar main dhindora','caz Dal nahi gali','with Fattu','with Bindaas','with Ghanta','with Vella','with Pataka','with Pakau','with Dhinchak','with OVER'])


#READY
@client.event
async def on_ready():
    change_status.start()
    print('Online as:    {0.user}'.format(client))


#STATUS
@tasks.loop(seconds=3)
async def change_status():
    await client.change_presence(status=discord.Status.idle,activity=discord.Game(next(status)))


#$ping
@client.command()#ep3b
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency*1000)}ms')


#$8ball
@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As i see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.',]
    import random#by myself
    await ctx.send(f'Questions: {question}\nAnswer: {random.choice(responses )}')#ep3e


#$pp
@client.command()
async def pp(ctx, user: discord.User = None):
    if user==None:
        user = ctx.message.author
    await ctx.send(user.avatar_url_as())


#SHUSH
keep_alive()
my_secret = os.environ['token']    
client.run(my_secret)
