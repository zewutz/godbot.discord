import discord
from discord.ext import commands

class Embed(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="licee")
    async def licee(self,ctx):
        embed=discord.Embed(title="Liceu", description="Alegeti liceul din lista de mai jos.", color=discord.Color.red())
        embed.add_field(name='Colegiul Național "Moise Nicoară" Arad', value="Select :pencil:", inline=False)
        embed.add_field(name="Liceul Pedagogic „Dimitrie Țichindeal” ", value="Select :teacher:", inline=False)
        embed.add_field(name="Colegiul Național „Elena Ghiba Birta” Arad", value="Select :gear:", inline=False)
        embed.add_field(name="Colegiul Economic Arad", value="Select :money_with_wings:", inline=False)
        embed.add_field(name="Liceul National de Informatica", value="Select :computer:", inline=False)
        embed.add_field(name="Liceul de Artă „Sabin Drăgoi”", value="Select :artist:", inline=False)
        embed.add_field(name="Liceul Teoretic „Adam Müller-Guttenbrunn”", value="Select :flag_de:", inline=False)
        embed.add_field(name="Colegiul Tehnic „Aurel Vlaicu” Arad", value="Select :dart:", inline=False)
        embed.add_field(name="Liceul Tehnologic de Industrie Alimentară", value="Select :herb:", inline=False)
        embed.set_footer(text="Daca liceul tau nu se afla in lista, poti lasa o sugestie pe canalul #sugestii  ca acesta sa fie adaugat.")
        await ctx.send(embed=embed)


    @commands.command(name="clasa")
    async def clase(self,ctx):
        embed=discord.Embed(title="Clasa", description="Alegeti clasa din lista de mai jos.", color=discord.Color.blue())
        embed.add_field(name='Clasa a IX-a', value="Select ", inline=False)
        embed.add_field(name="Clasa a X-a", value="Select ", inline=False)
        embed.add_field(name="Clasa a XI-a", value="Select ", inline=False)
        embed.add_field(name="Clasa a XII-a", value="Select ", inline=False)
        embed.set_footer(text=" ")
        await ctx.send(embed=embed)

    @commands.command(name="sex")
    async def sex(self,ctx):
        embed=discord.Embed(title="Sex", description="Alegeti sexul din lista de mai jos.", color=discord.Color.orange())
        embed.add_field(name='Baiat :cry:', value="Select ", inline=False)
        embed.add_field(name="Fata", value="Select ", inline=False)
        embed.add_field(name="Custom", value="Select ", inline=False)
        embed.set_footer(text="")
        await ctx.send(embed=embed)

    @commands.command(name="varsta")
    async def varsta(self,ctx):
        embed=discord.Embed(title="Varsta", description="Alegeti varsta din lista de mai jos.", color=discord.Color.orange())
        embed.add_field(name='14-15 ani', value="Select ", inline=False)
        embed.add_field(name="16-17 ani", value="Select ", inline=False)
        embed.add_field(name="18-19 ani", value="Select ", inline=False)
        embed.set_footer(text="Daca varsta ta nu se afla in lista de mai sus, poti lasa o sugestie pe canalul #sugestii ca aceasta sa fie adaugata.")
        await ctx.send(embed=embed)

    @commands.command(name="hobbys")
    async def hobbys(self,ctx):
        embed=discord.Embed(title="Hobby-uri/Activitati", description="Alegeti hobby-urile din lista de mai jos.", color=discord.Color.orange())
        embed.add_field(name='Sport', value="Select ", inline=False)
        embed.add_field(name="Arta", value="Select ", inline=False)
        embed.add_field(name="In progress", value="Select ", inline=False)
        embed.set_footer(text="Daca hobby-ul tau nu se afla in lista de mai sus, poti lasa o sugestie pe canalul #sugestii ca acesta sa fie adaugata.")
        await ctx.send(embed=embed)

    #! CULORI

def setup(client):
    client.add_cog(Embed(client))
