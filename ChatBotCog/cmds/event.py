import discord
import os
from discord.ext import commands
from discord.ext.commands import errors
from core.classes import Cog_Extention
from cmds.main import Main

class Event(Cog_Extention):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(990649988474347600)
        await channel.send(f'{member} join')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(990650084125442058)
        await channel.send(f'{member} leave')

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ['hi', 'hello']
        for key in keyword:
            if (msg.content.find(key) != -1) and msg.author != self.bot.user:
                await msg.channel.send(f"<@{msg.author.id}> Hello!")
                break;
                ##await msg.author.send('hello.')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            await ctx.send("Please input parameter.")
            return 

        if isinstance(error, commands.errors.CommandNotFound):
            await ctx.send("command invalid.")
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("command loss parameter.")
        else:
            await ctx.send("command error")

    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        await msg.channel.send("Delete message author : " + str(msg.author))
        await msg.channel.send("Delete message content : " + str(msg.content))

    @Main.delete.error
    async def cmd_delete_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("command delete error.")

def setup(bot):
    bot.add_cog(Event(bot))