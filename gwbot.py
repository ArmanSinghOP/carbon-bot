import discord
from discord.ext import commands 
import datetime
import asyncio
import random

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("Bot is Ready")

@client.command()
@commands.has_role("★━━━━━━✧𒁷⏤͟͟͞✧〢OWNER✧━━━━━━★")
async def gstart(ctx, mins : int, * , prize: str):
    embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60)
    
    embed.add_field(name = "Ends at:", value = f"{end} UTC")
    embed.set_footer(text = "Participate Now!")

    my_msg = await ctx.send(embed = embed)


    await my_msg.add_reaction("🎉")

    await asyncio.sleep(mins)

    new_msg = await ctx.channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await ctx.send(f"Congratulations! {winner.mention} won {prize}")


client.run("")