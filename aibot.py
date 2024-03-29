import discord #Importing the DISCORD MODULE  #`pip install py-cord`/ `pip install discord.py`
from discord.ext import commands #Importing the Commands section from the discord module.
import aiohttp #Built in AIOHTTP MODULE 
#GET YOUR API KEY FROM: https://rsa-api.xyz/
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents = intents) #Put all your other setup stuff here.
API_KEY = "YOUR API KEY HERE" #Defining the API KEY 
headervar = {"authorization": API_KEY}#This is the header. Which will be sent to verify your application's authenticity.
CUSTOMIZATION_URL = "https://v6.rsa-api.xyz/ai/customize" #The url used to customize the AI.
URL = "https://v6.rsa-api.xyz/ai/response" #Url of the API 
@bot.event #THe main Command.
async def on_message(message): #Bot receives the message.
	if message.author.bot: #Checks if the message is sent by a bot user. If it is then it will ignore it. 
		return
	if message.channel.id != 1232323234: #Use this in a INTEGER FORMAT Checks if the message is sent in this channel. Use this to avoid spam in all channels. #You can integrate your bot to a database and check if the message is in a channel which is in database. (Use that if you are making a public BOT)
		return
	try: #Try to do this
		datavar = {'msg':message.content, 'user_id':message.author.id}#--> Required ;You can add all the other non-important stuff as well...i.e Optional
		async with aiohttp.ClientSession(headers = headervar) as session: #This will send a request with the headers to the API
			async with session.get(url=URL, params = datavar) as reply: #This will receive an output and store it in "reply" var.
				output = await reply.json() #Converting the reply into python readable JSON Format
				msg = output["message"] #Getting the Response Out of it 
				await message.reply(msg) #Sending the response to the user as a reply to the person who sent the message.
	except: #If it fails, Then do this
		await message.reply("An erorr occured. Kindly contact an Admin") #If any error occurs (API not working or response time out, it will send this as the alternate reply.You can make it so that , create some error handler here.)
	
@bot.command()
async def setup(ctx):
	async with aiohttp.ClientSession(headers=headervar) as session:
		param_var = {"BotName":"Indigo", "BotMaster":"CannonBall Chris", "BotAge":69}#....You can find all customizations at: https://rsa-api.xyz > Documentation
		async with session.post(url=CUSTOMIZATION_URL, params = param_var) as sess:
			output = await sess.json()
			await ctx.send(output["message"])
#Use this command only once. THis command will help your bot to be registered on your api key in the db of api. So, you don't have to pass this information everytime. Its just one time only.

bot.run("ENTER YOUR TOKEN HERE")
