
import discord
import random
import os

from discord.ext import commands
from discord.utils import get


bot = commands.Bot(command_prefix="c.")
randomthing = 0
players = {}



@bot.event
async def on_ready():
    print("connected and ready to use")
@bot.command(pass_context=True)
async def cmds(ctx):
    await ctx.send('''NOT UPDATED\n\n\n\n\n\nc. is the prefix\n\nscript - reads bee movie script\nbee - puts a random bee movie character on screen\na - put a question after a and it will answer | usage c.a <question>\njoin - joins your voice channel\nrename - renames the target | usage c.rename <user> <new name>''')


@bot.command(pass_context=True)
async def read (ctx, *, arg):
    message = await ctx.send (arg, tts=True)
    message_id = message.id
    await message.edit(content="Reading...")
    print("command read | " + arg)

bot.voting_enabled = False

pollmessage = ''

@bot.command()
async def pollstart(ctx, arg1, arg2, arg3, arg4, *, arg5):
    bot.pollvoting_enabled = True
    global pollmessage
    pollmessage = await ctx.send('Question:  ' + arg5 + '?\n' + '1 = ' + arg1 + '\n2 = ' + arg2 + '\n3 = ' + arg3 + '\n4 = ' + arg4)
    await pollmessage.add_reaction('1️⃣')
    await pollmessage.add_reaction('2️⃣')
    await pollmessage.add_reaction('3️⃣')
    await pollmessage.add_reaction('4️⃣')

@bot.event
async def on_reaction_add(reaction, user):
    pass

        




onereaction = 0

tworeaction = 0

threereaction = 0

fourreaction = 0


@bot.event
async def on_raw_reaction_add(payload):
    if payload.emoji.name == "1️⃣":
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        reaction = get(message.reactions, emoji=payload.emoji.name)
        if reaction and reaction.count > 1:
            global onereaction
            onereaction = reaction.count - 1
    if payload.emoji.name == "2️⃣":
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        reaction = get(message.reactions, emoji=payload.emoji.name)
        if reaction and reaction.count > 1:
            global tworeaction
            tworeaction = reaction.count - 1
    if payload.emoji.name == "3️⃣":
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        reaction = get(message.reactions, emoji=payload.emoji.name)
        if reaction and reaction.count > 1:
            global threereaction
            threereaction = reaction.count - 1
    if payload.emoji.name == "4️⃣":
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        reaction = get(message.reactions, emoji=payload.emoji.name)
        if reaction and reaction.count > 1:
            global fourreaction
            fourreaction = reaction.count - 1

pollwinner = ''

@bot.command()
async def pollend(ctx):
    bot.voting_enabled = False
    pollwinner = 'Nobody, Its a tie!'
    if onereaction > tworeaction and threereaction and fourreaction:
        pollwinner = '1'
    elif tworeaction > onereaction and threereaction and fourreaction:
        pollwinner = '2'
    elif threereaction > onereaction and tworeaction and fourreaction:
        pollwinner = '3'
    elif fourreaction > onereaction and tworeaction and threereaction:
        pollwinner = '4'


    await ctx.send(str(onereaction) + 'vote(s) for 1\n' + str(tworeaction) + 'vote(s) for 2\n' + str(threereaction) + 'vote(s) for 3\n' + str(fourreaction) + 'vote(s) for 4\nand the winner is... ' + str(pollwinner))


@bot.command()
async def pollstatus(ctx):
    if bot.voting_enabled:
        await ctx.send('enabled')
    else:
        await ctx.send('not enabled wait until later')
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    print("command join")

@bot.command()
async def updates(ctx):
    await ctx.send('all updates https://ExpertEssentialMegabyte.harrypotter10.repl.co')


@bot.command()
async def pollresults(ctx):
    await ctx.send('---')

@bot.command()
async def rename(ctx, user: discord.Member, *,newName = ""):
    temp = user.display_name
    await user.edit(nick=newName)
    await ctx.send(ctx.message.author.mention + " changed " + str(user.name) + "'s name to " + newName)
    print("command rename | " + temp + " | " + newName)

@bot.command()
async def ban(ctx, user: discord.Member, *,reason = ""):
    channel = await user.create_dm()
    await channel.send(reason)
    await user.ban(reason='barry benson hates u also...' + reason)
    await ctx.send(ctx.message.author.mention + " banned " + str(user.name) + "because barry bensen is always watching and " + reason)
    print("command ban | " + 'user' + " | " + reason)


@bot.command()
async def kick(ctx, user: discord.Member, *,reason = ""):
    channel = await user.create_dm()
    await channel.send(reason)
    await user.ban(reason='barry benson hates u also...' + reason)
    await ctx.send(ctx.message.author.mention + " banned " + str(user.name) + "because barry bensen is always watching and " + reason)
    await user.unban(reason='barry likes you again :)')
    print("command kick | " + 'user' +" | "+ reason)

@bot.command()
async def unban(ctx, user: discord.Member, *, reason = ""):
    channel = await user.create_dm()
    await channel.send(reason)
    await user.unban(reason='barry likes you again :)')
    print ("command unban | " + 'user' + " | " + reason)





@bot.command(pass_context=True)
async def bee (ctx):
    randomImage = random.randint(1, 4)
    if randomImage == 1:
        await ctx.send(file=discord.File("index.jpg"))
    if randomImage == 2:
        await ctx.send(file=discord.File("index2.jpg"))
    if randomImage == 3:
        await ctx.send(file=discord.File("index3.jpg"))
    if randomImage == 4:
        await ctx.send(file=discord.File("buffbee.jpg"))
        print("command bee")
@bot.command(pass_context=True)
async def script (ctx):
    message = await ctx.send('''Bee Movie Script - Dialogue Transcript

  
According to all known laws
of aviation,

  
there is no way a bee
should be able to fly.

  
Its wings are too small to get
its fat little body off the ground.

  
The bee, of course, flies anyway

  
because bees don't care
what humans think is impossible.

  
Yellow, black. Yellow, black.
Yellow, black. Yellow, black.

  
Ooh, black and yellow!
Let's shake it up a little.

  
Barry! Breakfast is ready!

  
Ooming!

  
Hang on a second.

  
Hello?

  
- Barry?
- Adam?

  
- Oan you believe this is happening?
- I can't. I'll pick you up.

  
Looking sharp.

  
Use the stairs. Your father
paid good money for those.

  
Sorry. I'm excited.

  
Here's the graduate.
We're very proud of you, son.

  
A perfect report card, all B's.

  
Very proud.

  
Ma! I got a thing going here.

  
- You got lint on your fuzz.
- Ow! That's me!

  
- Wave to us! We'll be in row 118,000.
- Bye!

  
Barry, I told you,
stop flying in the house!

  
- Hey, Adam.
- Hey, Barry.

  
- Is that fuzz gel?
- A little. Special day, graduation.

  
Never thought I'd make it.

  
Three days grade school,
three days high school.

  
Those were awkward.

  
Three days college. I'm glad I took
a day and hitchhiked around the hive.

  
You did come back different.

  
- Hi, Barry.
- Artie, growing a mustache? Looks good.

  
- Hear about Frankie?
- Yeah.

  
- You going to the funeral?
- No, I'm not going.

  
Everybody knows,
sting someone, you die.

  
Don't waste it on a squirrel.
Such a hothead.

  
I guess he could have
just gotten out of the way.

  
I love this incorporating
an amusement park into our day.

  
That's why we don't need vacations.

  
Boy, quite a bit of pomp...
under the circumstances.

  
- Well, Adam, today we are men.
- We are!

  
- Bee-men.
- Amen!

  
Hallelujah!''',tts=True)
    message_id = message.id
    await message.edit(content="Reading Bee Movie Script...")
    print("command script")
@bot.command(pass_context=True)
async def a (ctx):
    randomNumber = random.randint(1, 100)
    randomNumber2 = random.randint(1, 3)
    if randomNumber < 20:
        if randomNumber2 == 3:
            await ctx.send('ya like jazz')
        if randomNumber2 == 2:
            await ctx.send('why?')
        if randomNumber2 == 1:
            await ctx.send('shut up')
    elif randomNumber < 58:
        await ctx.send ('yes')
    elif randomNumber < 86:
        await ctx.send('no')
    elif randomNumber < 100:
        await ctx.send('maybe')
    print("command Q&A")

@bot.event
async def on_command_error(ctx, error):
    print(f"An error occured: {str(error)}")

bot.run(os.environ['bottoken'])
