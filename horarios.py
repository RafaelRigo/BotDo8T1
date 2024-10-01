import discord
from discord.ext import commands


class Horarios_e_datas(commands.Cog):
    @commands.command(
        name="horarios",
        brief="Um comando pra eu enviar a grade horária.",
        help="Use este comando para que eu envie a grade horária."
    )
    async def horarios(self, ctx):
        with open("gradehorária.png", "rb") as f:
            img = discord.File(f)
            await ctx.send(file=img)
    
    @commands.command(
        name="plantao",
        brief="Um comando para eu enviar os horários de plantão.",
        help="Use este comando para que eu envie os horários de plantão."
    )
    async def plantao(self, ctx):
        with open("plantão.png", "rb") as f:
            img = discord.File(f)
            await ctx.send(file=img)
    
    @commands.command(
        name='provas',
        brief='Um comando para eu enviar o calendário de provas',
        help='Use este comando para que eu envie o calendário de provas'
    )
    async def provas(self, ctx):
        try:
            with open('provas.png', 'rb') as f:
                img = discord.File(f)
                await ctx.send(file=img)
        except:
            await ctx.send('Não há nenhum calendário de provas no momento')
