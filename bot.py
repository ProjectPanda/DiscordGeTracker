#
#  Author: Panda
#  Date: 03/15/20
#
import item_search
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='::')


@bot.command(name='ge')
async def price_checker(ctx, item_name):
    price = item_search.get_price(item_name)
    small_icon = item_search.get_small_icon(item_name)
    large_icon = item_search.get_large_icon(item_name)

    embed = discord.Embed(
        title='',
        description='This is a desc.',
        color=discord.Color.orange()
    )

    embed.set_footer(text='Live GE Prices using the Zenyte API')
    embed.set_image(url='')
    embed.set_thumbnail(url=large_icon)
    embed.set_author(name=item_name, icon_url=small_icon)
    embed.add_field(name='Current Price', value=price, inline=False)
    embed.add_field(name='5 Day Change', value='Field Value', inline=True)
    embed.add_field(name='10 Day Change', value='Field Value', inline=True)
    embed.add_field(name='30 Day Change', value='Field Value', inline=True)

    await ctx.channel.send(embed=embed)

bot.run(TOKEN)
