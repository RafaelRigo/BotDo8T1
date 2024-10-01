import discord
from discord.ext import commands

class Links_importantes(commands.Cog):
    '''Todos os outros links importantes que não são de aula'''
    @commands.command(
        name="sugestoes",
        brief="Um comando para eu enviar o link do forms de sugestões.",
        help="Não está funcionando"
    )
    async def _sugestoes(self, ctx):
        await ctx.send("**Aqui está o link do formulário de sugestões:**não tem")
    
    