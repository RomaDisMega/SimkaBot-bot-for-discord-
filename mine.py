import disnake
from disnake.ext import commands

bot = commands.InteractionBot(intents = disnake.Intents.all())

@bot.event
async def on_ready():
    print("Simka bot готов к работе!")
    await bot.change_presence(activity=disnake.Activity(name="pydroid 3",type=disnake.ActivityType.competing, state="солями"), status=disnake.Status.idle)

@bot.slash_command(name="хелп", description="Команды, и другое, ну короче хелп")
async def help(inter):
    await inter.send("`/хелп — это помощь\n/калькулятор — считывает числа (пример: 2+2=4)\n/инфо — выводит информацию о сервере\n/кот — добавляет к сообщению =^ᴥ^=\n/текст — повторяет набранный пользователем текст`")
    
@bot.slash_command(name="калькулятор", description="калькулятор. больше не очём говорить")
async def calc(inter, пример: str):
  try:
    await inter.response.defer()  
    await inter.send(eval(пример))
  except Exception as e:
    await inter.send(f"Ошибка! {e}")

@bot.slash_command(name="инфо", description="инфо о сервере")
async def server_info(ctx):
    guild = ctx.guild
    members = guild.members
    num_user = sum(not member.bot for member in members)
    num_bot = sum(member.bot for member in members)
    voice_channels = len(guild.voice_channels)
    text_channels = len(guild.text_channels)
    await ctx.send(f"`На сервере {guild.name} есть {text_channels} текстовых каналов и {voice_channels} голосовых каналов. И {num_user} людей, {num_bot} ботов, а всего {len(members)} участников/ботов`")
    
@bot.slash_command(name="кот", description="добавяет к сообщению =^ᴥ^=")
async def cat(inter, сообщение: str = None):
    if сообщение != None:
        await inter.send(сообщение + " =^ᴥ^=")
    else:
        await inter.send("=^ᴥ^=")

@bot.slash_command(name="текст", description="повторяет написаный пользователем текст")
async def ping(inter, сообщение: str):
    channel = inter.channel
    await channel.send(сообщение)

@bot.slash_command(name="бот", description="выводит информацию о боте")
async def infb(inter):
    await inter.send("`Информация о Simka\nДата начала разработки — 11.11.23\nСсылка приглашение — *тут могла бы быть ваша реклама*`")
    
@bot.slash_command(name="участник", description="выводит информацию о участнике")
async def infm(inter, участник: disnake.Member = None):
    if участник == None:
        await inter.send(f"Информация о {inter.author.name}")
    elif участник:
        await inter.send(f"Информация о {участник}")

@bot.slash_command(name="кик", description="кикает участника")
async def kik(inter, участник: disnake.Member):
       await участник.kick()
       await inter.send(f"Участник {участник.mention} был выгнан модератором {inter.author.name}")
            
@bot.slash_command(name="бан", description="БаН.")
async def bn(inter, участник: disnake.Member, время):
    await участник.ban()
    await inter.send(f"Участник {участник.name} был забанен модератором {inter.author.name}!")

bot.run('