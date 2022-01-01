import nextcord as discord
from nextcord.ext import commands
from nextcord.ui import view
import asyncio

intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix= ".", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("HolyFrag.pl"))
    print('Bot Gotowy do Pracy!')

class Przyciski(discord.ui.View):
  def __init(self):
    super().__init__(timeout=None)
    self.value = None

  @discord.ui.button(label="Zweryfikuj", style=discord.ButtonStyle.green)
  async def role(self, button: discord.ui.Button, interaction: discord.Interaction):
    rola = discord.utils.get(interaction.user.guild.roles, id=919316008181825618)
    zrola = discord.utils.get(interaction.user.guild.roles, id=926937402629586954)
    await interaction.user.add_roles(rola)
    await interaction.user.remove_roles(zrola)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Zweryfikowano :white_check_mark:", ephemeral=True)
    self.value = True

class wojPrzyciski(discord.ui.View):
  def __init(self):
    super().__init__(timeout=None)
    self.value = None

  @discord.ui.button(label="Zachodnio-Pomorskie", style=discord.ButtonStyle.grey)
  async def arole(self, button: discord.ui.Button, interaction: discord.Interaction):
    zach = discord.utils.get(interaction.user.guild.roles, id=919316008181825618)
    await interaction.user.add_roles(zach)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="Wielkopolskie", style=discord.ButtonStyle.grey)
  async def brole(self, button: discord.ui.Button, interaction: discord.Interaction):
    wiel = discord.utils.get(interaction.user.guild.roles, id=919623004600807444)
    await interaction.user.add_roles(wiel)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="Warminsko-Mazurskie", style=discord.ButtonStyle.grey)
  async def crole(self, button: discord.ui.Button, interaction: discord.Interaction):
    warm = discord.utils.get(interaction.user.guild.roles, id=919623002751119370)
    await interaction.user.add_roles(warm)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="Świętokrzyskie", style=discord.ButtonStyle.grey)
  async def drole(self, button: discord.ui.Button, interaction: discord.Interaction):
    swie = discord.utils.get(interaction.user.guild.roles, id=919623001794814042)
    await interaction.user.add_roles(swie)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="Śląskie", style=discord.ButtonStyle.grey)
  async def erole(self, button: discord.ui.Button, interaction: discord.Interaction):
    slas = discord.utils.get(interaction.user.guild.roles, id=919623001056632903)
    await interaction.user.add_roles(slas)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="Pomorskie", style=discord.ButtonStyle.grey)
  async def frole(self, button: discord.ui.Button, interaction: discord.Interaction):
    pomo = discord.utils.get(interaction.user.guild.roles, id=919623000532324402)
    await interaction.user.add_roles(pomo)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="Podlaskie", style=discord.ButtonStyle.grey)
  async def grole(self, button: discord.ui.Button, interaction: discord.Interaction):
    podl = discord.utils.get(interaction.user.guild.roles, id=919622999596994572)
    await interaction.user.add_roles(podl)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="Podkarpackie", style=discord.ButtonStyle.grey)
  async def hrole(self, button: discord.ui.Button, interaction: discord.Interaction):
    podk = discord.utils.get(interaction.user.guild.roles, id=919622999265656832)
    await interaction.user.add_roles(podk)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="Opolskie", style=discord.ButtonStyle.grey)
  async def irole(self, button: discord.ui.Button, interaction: discord.Interaction):
    opol = discord.utils.get(interaction.user.guild.roles, id=919622989627129866)
    await interaction.user.add_roles(opol)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="Mazowieckie", style=discord.ButtonStyle.grey)
  async def jrole(self, button: discord.ui.Button, interaction: discord.Interaction):
    mazo = discord.utils.get(interaction.user.guild.roles, id=919622986829541467)
    await interaction.user.add_roles(mazo)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="Małopolskie", style=discord.ButtonStyle.grey)
  async def krole(self, button: discord.ui.Button, interaction: discord.Interaction):
    malo = discord.utils.get(interaction.user.guild.roles, id=919622987337048074)
    await interaction.user.add_roles(malo)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="Łódzkie", style=discord.ButtonStyle.grey)
  async def lrole(self, button: discord.ui.Button, interaction: discord.Interaction):
    lodz = discord.utils.get(interaction.user.guild.roles, id=919622984656896030)
    await interaction.user.add_roles(lodz)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="Lubuskie", style=discord.ButtonStyle.grey)
  async def mrole(self, button: discord.ui.Button, interaction: discord.Interaction):
    lubu = discord.utils.get(interaction.user.guild.roles, id=919622981955760221)
    await interaction.user.add_roles(lubu)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="Lubelskie", style=discord.ButtonStyle.grey)
  async def nrole(self, button: discord.ui.Button, interaction: discord.Interaction):
    lube = discord.utils.get(interaction.user.guild.roles, id=919622513632362556)
    await interaction.user.add_roles(lube)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="Kujawsko-Pomorskie", style=discord.ButtonStyle.grey)
  async def orole(self, button: discord.ui.Button, interaction: discord.Interaction):
    kuja = discord.utils.get(interaction.user.guild.roles, id=919622511749103649)
    await interaction.user.add_roles(kuja)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="Dolnośląskie", style=discord.ButtonStyle.grey)
  async def urole(self, button: discord.ui.Button, interaction: discord.Interaction):
    doln = discord.utils.get(interaction.user.guild.roles, id=919622506611109999)
    await interaction.user.add_roles(doln)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

class wiekPrzyciski(discord.ui.View):
  def __init(self):
    super().__init__(timeout=None)
    self.value = None

  @discord.ui.button(label="+12", style=discord.ButtonStyle.grey)
  async def aarole(self, button: discord.ui.Button, interaction: discord.Interaction):
    w12 = discord.utils.get(interaction.user.guild.roles, id=919622511283552277)
    await interaction.user.add_roles(w12)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="+14", style=discord.ButtonStyle.grey)
  async def barole(self, button: discord.ui.Button, interaction: discord.Interaction):
    w14 = discord.utils.get(interaction.user.guild.roles, id=919622510910246982)
    await interaction.user.add_roles(w14)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="+16", style=discord.ButtonStyle.grey)
  async def carole(self, button: discord.ui.Button, interaction: discord.Interaction):
    w16 = discord.utils.get(interaction.user.guild.roles, id=919622509647765535)
    await interaction.user.add_roles(w16)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="+18", style=discord.ButtonStyle.grey)
  async def darole(self, button: discord.ui.Button, interaction: discord.Interaction):
    w18 = discord.utils.get(interaction.user.guild.roles, id=919622509370949692)
    await interaction.user.add_roles(w18)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="+20", style=discord.ButtonStyle.grey)
  async def earole(self, button: discord.ui.Button, interaction: discord.Interaction):
    w20 = discord.utils.get(interaction.user.guild.roles, id=919622508355940353)
    await interaction.user.add_roles(w20)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="+22", style=discord.ButtonStyle.grey)
  async def farole(self, button: discord.ui.Button, interaction: discord.Interaction):
    w22 = discord.utils.get(interaction.user.guild.roles, id=919622507936485387)
    await interaction.user.add_roles(w22)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True

  @discord.ui.button(label="+24", style=discord.ButtonStyle.grey)
  async def garole(self, button: discord.ui.Button, interaction: discord.Interaction):
    w24 = discord.utils.get(interaction.user.guild.roles, id=919622507231846400)
    await interaction.user.add_roles(w24)
    await interaction.response.send_message(":white_check_mark: Pomyślnie Nadano :white_check_mark:", ephemeral=True)
    self.value = True
  


@client.command()
async def weryfikacja(ctx):
  if(not ctx.author.guild_permissions.ban_members):
    await ctx.send(f"{ctx.author.mention} Nie posiadasz wystarczających uprawinień!")
    await asyncio.sleep(10)
    await ctx.channel.purge(limit=2)
    return
  view = Przyciski()
  embed=discord.Embed(color=0xff0000)
  embed.add_field(name="Klikając przycisk, akceptujesz powyższy regulamin oraz zostaniesz zweryfikowany :white_check_mark:", value="----------------------------------------------------------------------------", inline=True)
  embed.set_footer(text="HolyFrag.pl © 2022")
  await ctx.send(embed=embed, view=view)
  await view.wait()

@client.command()
async def woj(ctx):
  if(not ctx.author.guild_permissions.ban_members):
    await ctx.send(f"{ctx.author.mention} Nie posiadasz wystarczających uprawinień!")
    await asyncio.sleep(10)
    await ctx.channel.purge(limit=2)
    return
  view = wojPrzyciski()
  embed=discord.Embed(color=0xff0000)
  embed.add_field(name="Klikając przycisk, możesz wybrać swoje województwo", value="----------------------------------------------------------------------------------------------", inline=True)
  embed.set_footer(text="HolyFrag.pl © 2022")
  await ctx.send(embed=embed, view=view)
  await view.wait()

@client.command()
async def wie(ctx):
  if(not ctx.author.guild_permissions.ban_members):
    await ctx.send(f"{ctx.author.mention} Nie posiadasz wystarczających uprawinień!")
    await asyncio.sleep(10)
    await ctx.channel.purge(limit=2)
    return
  view = wiekPrzyciski()
  embed=discord.Embed(color=0xff0000)
  embed.add_field(name="Klikając przycisk, możesz wybrać swój wiek", value="--------------------------------------------------------------", inline=True)
  embed.set_footer(text="HolyFrag.pl © 2022")
  await ctx.send(embed=embed, view=view)
  await view.wait()


@client.command(aliases=['c'])
async def clear(ctx, amount=11):
  if(not ctx.author.guild_permissions.ban_members):
    await ctx.send(f"{ctx.author.mention} Nie posiadasz wystarczających uprawinień!")
    await asyncio.sleep(10)
    await ctx.channel.purge(limit=2)
    return
  ammount= amount+1
  if amount > 101:
    await ctx.send(f"{ctx.author.mention} Nie możesz wyczyścić więcej niż 100 wiadomości!")
    await asyncio.sleep(10)
    await ctx.channel.purge(limit=1)
  else:
      await asyncio.sleep(5)
      await ctx.channel.purge(limit=amount)
      await asyncio.sleep(2)
      await ctx.send(f"{ctx.author.mention} Usunięto wiadomości!")
      await asyncio.sleep(10)
      await ctx.channel.purge(limit=1)
    
