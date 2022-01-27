from os import name
import discord
from discord import user
from discord import client
from discord.ext import commands 
import asyncio
import random
import datetime
from discord.ext.commands.bot import Bot

intents = discord.Intents.all()
intents.members= True

bot = commands.Bot(command_prefix=".", intents=intents)
bot.remove_command("help")

f = open("rules.txt","r")
rules = f.readlines()


@bot.event
async def on_ready():
    #setting Playing status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=" on TWO NOOB GAMERZ!"))
    print("Bot is Ready")

@bot.event
async def on_member_join(member):
    guild = bot.get_guild(719231017772384296)
    channel = guild.get_channel(719596350089723915)
    await channel.send(f'Welcome to the server {member.mention}!:partying_face:')
    
@bot.command()       #test working Status
async def test(ctx):
    await ctx.send("Bot is Working Fine!")

@bot.command()       #ping everyone role  
@commands.has_role("★━━━━━━✧𒁷⏤͟͟͞✧〢OWNER✧━━━━━━★")
async def pingeveryone(ctx):
    await ctx.send("@everyone " + ctx.author.mention + " pinged!")

@bot.command(aliases=['rules'])        #rules for Server 
async def rule(ctx,*,number):
    await ctx.send(rules[int(number)-1])

@bot.command(aliases=["fp"])
async def fanpass(ctx,*,n):
    await ctx.send(fp[int(n)-1])

@bot.command(aliases=['yt','youtube channel','yt channel'])      #youtube channel
async def youtube(ctx):
    embed = discord.Embed(title = "<:tngyt:878502873900679218> Our Youtube Channel <:tngyt:878502873900679218>", description = "https://www.youtube.com/channel/UC0zAoqtgdHfE_y-1dFoJz8A", color = ctx.author.color)
    await ctx.send(embed=embed)

@bot.command(aliases=['insta'])       #insta page
async def instagram(ctx):
    embed = discord.Embed(title = "<:tnginsta:878501876197392444>Our Instagram<:tnginsta:878501876197392444>", description = "https://instagram.com/ig_unitedsouls", color = ctx.author.color)
    await ctx.send(embed=embed)

@bot.command(aliases=['purge','c'])       #clear messages
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit = amount+1)

@bot.command()                               #kick members
@commands.has_permissions(kick_members = True) 
async def kick(ctx,member : discord.Member,*,reason= "No reason Provided!"):
    await member.send("You have Been Kicked From The TWO NOOB GAMERZ, because:"+reason)
    await ctx.send(member.name + " has Been Kicked From The TWO NOOB GAMERZ, because:"+reason)
    await member.kick(reason=reason)

@bot.command()                    #ban members
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "No reason Provided!"):
    await member.send("You have Been banned From The TWO NOOB GAMERZ, because:"+reason)
    await ctx.send(member.name + " has Been banned From The TWO NOOB GAMERZ, because:"+reason)
    await member.ban(reason=reason) 

@bot.command()                   #unban members
@commands.has_permissions(ban_members = True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member_name,member_disc):

            await ctx.guild.unban(user)
            await ctx.send(member_name +" has been unbanned!")
            return

    await ctx.send(member+" was not found!")

@bot.command()                  #mute members
@commands.has_permissions(kick_members=True)
async def mute(ctx,member : discord.Member):
    muted_role = ctx.guild.get_role(738334545560076310)

    await member.add_roles(muted_role)

    await ctx.send(member.mention + " has been muted!")
    
@bot.command()                  #unmute members
@commands.has_permissions(kick_members=True)
async def unmute(ctx,member : discord.Member):
    muted_role = ctx.guild.get_role(738334545560076310)

    await member.remove_roles(muted_role)
    await ctx.send(member.mention + " has been unmuted!")

@bot.command()                  #socials
async def socials(ctx):
    embed = discord.Embed(title = "Our Socials!!" , description = "Follow Us To get Updated!!" , color = discord.Colour.green())
    embed.add_field(name = "<:tngyt:878502873900679218> Our Youtube Channel <:tngyt:878502873900679218>", value = "https://www.youtube.com/channel/UC0zAoqtgdHfE_y-1dFoJz8A" , inline= True )
    embed.add_field(name = "<:tnginsta:878501876197392444>Our Instagram<:tnginsta:878501876197392444>", value = "https://instagram.com/ig_unitedsouls" , inline= False)
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):           #help
    embed = discord.Embed(title = "Help Page" , description = f"My prefix For the server is `.`" , color = ctx.author.color)
    embed.add_field(name = "💬**General Commands**", value = "`Socials`,`youtube`,`instagram`,`rule`" , inline= False )
    embed.add_field(name = "🛠️**Moderation Commands**", value = "`ban`,`unban`,`kick`,`mute`,`unmute`,`pingeveryone`,`clear`" , inline= False)
    embed.add_field(name = "🎭Miscellaneous", value = "`about`,`test`")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/878177140439388170/880711607557169202/Free_Sample_By_Wix.jpg")
    embed.set_footer (icon_url="https://cdn.discordapp.com/attachments/878177140439388170/878177192645890098/1629444115634.jpg", text = "Managed by MᴏʀᴛᴀʟOP!")
    await ctx.send(embed=embed)

@bot.command() 
async def about(ctx):             #about bot
    embed = discord.Embed(title = "Carbon Bot" , Description = "A Bot Made for Special Works Which Also Have Many Moderation Commands As well!" , color = ctx.author.color)
    embed.add_field(name = "**Information**", value = "**Developer**: MᴏʀᴛᴀʟOP#9251 | **Python**: Python 3.8.5")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/878177140439388170/880711607557169202/Free_Sample_By_Wix.jpg")
    embed.set_footer (icon_url="https://cdn.discordapp.com/attachments/878177140439388170/878177192645890098/1629444115634.jpg", text = "Managed by MᴏʀᴛᴀʟOP!")
    await ctx.send(embed=embed)

@bot.command()                 #giveaway 
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
    users.pop(users.index(bot.user))

    winner = random.choice(users)

    await ctx.send(f"Congratulations! {winner.mention} won {prize}")

@bot.command(aliases=[""])
async def guild(ctx):            #ff guild
    embed = discord.Embed(title="Guild Info", description="Here's the list of our official Guilds", color=ctx.author.color) 
    embed.add_field(name="ՄɴɪᴛᴇᴅᯓՏᴏᴜʟs", value="Type `.guildus` For More Info", inline=False)
    embed.add_field(name="Guild ID", value="1001130095", inline=False)
    embed.add_field(name="Tɴɢ★Aʀᴍʏ", value="Type `.guildtng` For More Info", inline=False)
    embed.add_field(name="Guild ID", value="1007353986", inline=True)
    await ctx.send(embed = embed )

@bot.command()               #united souls guild
async def guildus(ctx): 
    embed = discord.Embed(title="ՄɴɪᴛᴇᴅᯓՏᴏᴜʟs", description="A Friendly Guild For Friends And Non-Friendly For Haters!", color=ctx.author.color)
    embed.add_field(name="Guild ID", value="1001130095", inline=True)
    embed.add_field(name="Glory", value="20 Lakh+", inline=True)
    embed.add_field(name="Requirements", value="Lvl 65+ | Atleast Diamond Rank | Rank Squad KD - 4+", inline=False)
    embed.set_image(url ="https://cdn.discordapp.com/attachments/878177140439388170/881784631383453706/IMG_20210830_114309.jpg")
    embed.add_field(name="Managed By", value="<@479623407869231122> DM Him For Inquiring anything more about guild or about recruitment", inline=False)
    embed.set_footer(text="Join For Booyah!!", icon_url="https://cdn.discordapp.com/attachments/878177140439388170/881792524728020992/IMG_20210830_121826.jpg")
    await ctx.send(embed=embed)
 
@bot.command()               #tng guild
async def guildtng(ctx):    
    embed = discord.Embed(title="TNG★E-Sᴘᴏʀᴛs", description="", color= ctx.author.color)
    embed.add_field(name="Guild ID", value="1003380081", inline=True)
    embed.add_field(name="Glory", value="11 Lakh+", inline=True)
    embed.add_field(name="Requirements", value="Lvl 60+ | Daily 80 Glory Must!", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/878177140439388170/886858084910268486/IMG_20210913_114717.jpg")
    embed.add_field(name="Manged By", value="<@719230548517847091> DM Him For Inquiring anything more about guild or about recruitment", inline=True)
    embed.set_footer(text="Join For Booyah!", icon_url="https://cdn.discordapp.com/attachments/878177140439388170/881792390149578752/1630306046446.jpg")
    await ctx.send(embed=embed)
    
@bot.command(aliases=["tournament"])
async def t(ctx,*,ch):
    if ch=="fp" or ch=="fanpass":
        await ctx.send("Here are the links for the Fan Pass tournament of this week!\nHope You Consider playing in the tournament!\nhttps://bit.ly/fplinkstng")
    elif ch=="free":
        await ctx.send("Links Will be available soon!")
    else:
        await ctx.send("Please put a valid command `.t <fp/fanpass/free>`")



bot.run("Nzc0MTcxNjc1NjE2MDgzOTY5.X6T5jg.9_jbCFD9YfuNP6tMednaYf6Na_w")
