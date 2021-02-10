import telegrampy
import owoify
from owoify import Owoifator 
from telegrampy.ext import commands

bot=commands.Bot('')
@bot.command()
async def what(ctx):
	await ctx.send('Список команд: /owo [word] преобразует написанное вами слово в его няшную версию. Пример использования: /owo Hello >>> Hewwo')

@bot.command()
async def owo(ctx, args):
	owoifator = Owoifator()
	args=owoifator.owoify(args)
	await ctx.send(args+"(*^ω^)")

@bot.command()
async def понедельник(ctx):
	await ctx.send('https://ibb.co/cLLyCht')

@bot.command()
async def вторник(ctx):
	await ctx.send('https://ibb.co/bFYVqqg')

@bot.command()
async def среда(ctx):
	await ctx.send('https://ibb.co/M9D36DH')

@bot.command()
async def четверг(ctx):
	await ctx.send('https://ibb.co/LhyXHPk')

@bot.command()
async def пятница(ctx):
	await ctx.send('https://ibb.co/NVD63cd')
bot.run()
