import discord
from discord.ext import commands


class Links_de_aulas(commands.Cog):
    '''Todos os links de aulas(não estão atualizados)'''
    @commands.command(
        name="b1plus",
        brief="Um comando para eu enviar o link do B1+.",
        help="Use este comando para fazer eu enviar o link do B1+."
    )
    async def _b1plus(self, ctx):
        await ctx.send("**Aqui está o link do B1+:**\nhttps://meet.google.com/cuo-mxfs-sqe")
    
    
    @commands.command(
        name="b1",
        brief="Um comando para eu enviar o link do B1.",
        help="Use este comando para fazer eu enviar o link do B1."
    )
    async def _b1(self, ctx):
        await ctx.send("**Aqui está o link do B1:**\nhhttps://meet.google.com/fiw-enje-gwv")
    
    @commands.command(
        name="a2",
        brief="Um comando para eu enviar o link do A2.",
        help="Use este comando para fazer eu enviar o link do A2."
    )
    async def _a2(self, ctx):
        await ctx.send("**Aqui está o link do A2:**\nhttps://meet.google.com/drj-sfxs-fpf")
    
    @commands.command(
        name="mat",
        brief="Um comando para eu enviar o link de matemática.",
        help="Use este comando para fazer eu enviar o link de matemática."
    )
    async def _mat(self, ctx):
        await ctx.send("**Aqui está o link de matemática:**\nhttps://meet.google.com/fcn-iqbc-yrw")
    
    @commands.command(
        name="cie",
        brief="Um comando para eu enviar o link de ciências.",
        help="Use este comando para fazer eu enviar o link de ciências."
    )
    async def _cie(self, ctx):
        await ctx.send("**Aqui está o link de ciências:**\nhttps://meet.google.com/vas-gpum-mry")
    
    @commands.command(
        name="psfilo",
        brief="Um comando para eu enviar o link de programa semente e filosofia.",
        help="Use este comando para fazer eu enviar o link de programa semente e filosofia."
    )
    async def _psfilo(self, ctx):
        await ctx.send("**Aqui está o link de programa semente e filosofia:**\nhttps://meet.google.com/ivn-mtwo-koy")
    
    @commands.command(
        name="art",
        brief="Um comando para eu enviar o link de artes.",
        help="Use este comando para fazer eu enviar o link de artes."
    )
    async def _art(self, ctx):
        await ctx.send("**Aqui está o link de artes:**\nhttps://meet.google.com/svr-atzb-sik")
    
    @commands.command(
        name="geo",
        brief="Um comando para eu enviar o link de geografia.",
        help="Use este comando para fazer eu enviar o link de geografia."
    )
    async def _geo(self, ctx):
        await ctx.send("**Aqui está o link de geografia:**\nhttps://meet.google.com/owe-pawd-rkt")
    
    @commands.command(
        name="hist",
        brief="Um comando para eu enviar o link de história.",
        help="Use este comando para fazer eu enviar o link de história."
    )
    async def _hist(self, ctx):
        await ctx.send("**Aqui está o link de história:**\nhttps://meet.google.com/qin-qkay-vka")
    
    @commands.command(
        name="port",
        brief="Um comando para eu enviar o link de português.",
        help="Use este comando para fazer eu enviar o link de português."
    )
    async def _port(self, ctx):
        await ctx.send("**Aqui está o link de português:**\nhttps://meet.google.com/ziu-vprs-acv")
    
    @commands.command(
        name="edf",
        brief="Um comando para eu enviar o link de educação física.",
        help="Use este comando para fazer eu enviar o link de educação física."
    )
    async def _edf(self, ctx):
        await ctx.send("**Aqui está o link de educação física:**\nhttps://meet.google.com/dpz-ktwc-och")