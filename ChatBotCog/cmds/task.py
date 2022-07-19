import discord
from discord.ext import commands
from core.classes import Cog_Extention
import json, asyncio, datetime

class Task(Cog_Extention):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0

        #async def interval():
            #await self.bot.wait_until_ready()
            #self.channel = self.bot.get_channel(989880595167445054)
            #while not self.bot.is_closed():
                #await self.channel.send("Hi i'm running!")
                #await asyncio.sleep(5) #second

        #self.bg_task = self.bot.loop.create_task(interval())

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(989880595167445054)
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime("%Y.%m.%d-%H:%M")
                with open('Setting.json', 'r', encoding = 'utf8') as file:
                    file_data = json.load(file)
                if now_time == file_data['time']:
                    self.counter == 1
                    await self.channel.send('Task Working!')
                    await asyncio.sleep(5) #second
                else:
                    await asyncio.sleep(5) #second
                    pass

        self.bg_task = self.bot.loop.create_task(time_task())


    @commands.command(name="set_channel", brief='Command set channel')
    async def set_channel(self, ctx, ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel:{self.channel.mention}')

    @commands.command(name="set_time", brief='Command set time')
    async def set_time(self, ctx, time):
        with open('Setting.json', 'r', encoding = 'utf8') as file:
            file_data = json.load(file)
            file_data['time'] = time

        with open('Setting.json', 'w', encoding = 'utf8') as file:
            json.dump(file_data, file, indent = 4)


def setup(bot):
    bot.add_cog(Task(bot))