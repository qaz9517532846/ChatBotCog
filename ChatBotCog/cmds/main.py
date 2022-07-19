import discord
from discord.ext import commands
from core.classes import Cog_Extention

class Main(Cog_Extention):

    @commands.command(name="ping", brief='Command Ping')
    async def ping(self, ctx):
        await ctx.send(self.bot.latency)

    @commands.command(name="say", brief='Command repeate message')
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command(name="delete", brief='Command delete message')
    async def delete(self, ctx, num:int):
        await ctx.channel.purge(limit = num + 1)

    @commands.command(name="reviewallmsg", brief='review num history message')
    async def reviewallmsg(self, ctx, num:int):
        his_msg = ""
        async for message in ctx.channel.history(limit = num + 1):
            his_msg += (message.content + '\n')
        await ctx.send(his_msg)

    @commands.command(name="reviewallauther", brief='review num history message auther')
    async def reviewallauther(self, ctx, num:int):
        his_msg = ""
        async for message in ctx.channel.history(limit = num + 1):
            his_msg += (str(message.author) + '\n')
        await ctx.send(his_msg)

    @commands.group(name="Group", brief='group and subcommand')
    async def subcmd(self, ctx):
        pass

    @subcmd.command(name="apple", brief='sub command apple')
    async def apple(self, ctx):
        await ctx.send("Sub Command apple")

    @subcmd.command(name="axe", brief='sub command axe')
    async def axe(self, ctx):
        await ctx.send("Sub Command axe")

    @subcmd.command(name="gun", brief='sub command gun')
    async def gun(self, ctx):
        await ctx.send("Sub Command gun")



def setup(bot):
    bot.add_cog(Main(bot))