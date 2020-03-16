#
#  Author: Panda
#  Date: 03/15/20
#
import analytics
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='::')


@bot.command(name='ge', help='You must put "quotations" around your item. ex: ::ge "abyssal whip"')
async def price_checker(ctx, item_name):
    price = analytics.get_item(item_name)
    response = 'The current price of ' + item_name + ' is: ' + str(price) + ' gp.'
    await ctx.channel.send(response)

bot.run(TOKEN)
