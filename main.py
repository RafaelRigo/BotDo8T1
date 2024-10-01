import discord
import os
from discord.ext import commands
from pretty_help import DefaultMenu, PrettyHelp
from links import Links_importantes
from keep_alive import keep_alive
from commands import Comandos
from linksdeaulas import Links_de_aulas
from horarios import Horarios_e_datas

token = os.environ['token']

bot = commands.Bot(
    command_prefix='%',
    description="Um bot para a turma do 8T1"
)

ending_note = "Digite %help comando para ter mais informações de um comando.\nVocê também pode digitar %help categoria para ter mais informações de uma categoria."
nav = DefaultMenu("◀️", "▶️", "❌", active_time=60)
bot.help_command = PrettyHelp(navigation=nav, ending_note=ending_note, color=discord.Colour.blue(), index_title="Categorias de comandos")

@bot.event
async def on_ready():
    print("prontinho")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('You need to wait %.2f seconds to use this command again' % error.retry_after)
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Esse comando não existe! Use %help pra ver os comandos que você pode usar.")
    raise error


keep_alive()


def run():
    bot.add_cog(Horarios_e_datas(bot))
    bot.add_cog(Links_de_aulas(bot))
    bot.add_cog(Links_importantes(bot))
    bot.add_cog(Comandos(bot))
    bot.run(token)

if __name__ == "__main__":
    run()
