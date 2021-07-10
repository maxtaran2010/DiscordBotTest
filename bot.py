import game
import discord
from discord.ext import commands
from config.botData import settings

# тело бота------------------------------------------------------------
intents = discord.Intents.default()
intents.members = True
help_command = commands.DefaultHelpCommand(no_category='мои команды')
bot = commands.Bot(
    command_prefix=settings['prefix'],
    description=f'Для подробной информации напиши {settings["prefix"]}help <команда>',
    help_command=help_command,
    intents=intents
)
client = discord.Client()


# команды-------------------------------------------------------------
@bot.command()
async def edit(ctx):
    mess = await ctx.send('edit')
    await mess.add_reaction('🔪')


@bot.command()
async def game(ctx):
    message = await ctx.send('test')
    await message.add_reaction('❓')
    await message.add_reaction('⬆')
    await message.add_reaction('⬇')
    await message.add_reaction('➡')
    await message.add_reaction('⬅')
# эвенты--------------------------------------------------------------
@bot.event
async def on_ready():
    print(f'>name: {bot.user.name}<')
    print(f'>id: {bot.user.id}<')
    print(f'>ready for use<')
    print('''
    |  сдесь будут отоброжаться |
    V  ошибки и лог             V
    ''')


@bot.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji
    message = reaction.message.content
    usr = user.id
    if usr != 859114111940952105:
        if message == 'edit':
            if emoji == '🔪':
                await reaction.message.edit(content='ha!')
        if message == 'test':
            if emoji == '❓':
                await reaction.message.channel.send('''
ПОМОЩЬ
❓ - Показывает это сообщение
                ''')


@bot.event
async def on_reaction_remove(reaction, user):
    emoji = reaction.emoji
    message = reaction.message.content
    usr = user.id
    channel = reaction.message.channel
    message_data = reaction.message
    if usr != 859114111940952105:
        if message == 'ha!':
            if emoji == '🔪':
                await reaction.message.edit(content='edit')


@bot.event
async def on_member_join(member):
    await member.send(f"{member.mention}, добро пожаловать на сервер {member.guild.name}")


# запуск бота------------------------------------------------------------------
def main():
    bot.run(settings['token'])


main()
