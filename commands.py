import discord
from discord.ext import commands


class Comandos(commands.Cog):
    '''Os comandos que não tem categoria'''
    @commands.command(
        name="site",
        brief="Um comando para eu enviar o link do meu site.",
        help="Use este comando para que eu envie o link do meu site!"
    )
    async def _site(self, ctx):
        await ctx.send("**Meu site:**\nhttps://bot-do-7t1.rafaelrigo.repl.co/")