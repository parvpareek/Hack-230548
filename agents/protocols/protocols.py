from uagents import Context, Model, Protocol
import typing
import os
from dotenv import load_dotenv
import requests

class CurrencyParams(Model):
    base_currency: str
    foreign_currency: str
    number: str

class RequestLimits(Model):
    msg: str

class ThresholdLimits(Model):
    max: float
    min: float

class RegistrationStatus(Model):
    msg: str
    

currency_protocol = Protocol()


@currency_protocol.on_message(CurrencyParams, replies=RequestLimits)
async def process_input(ctx: Context, sender: str, msg:CurrencyParams):

    ctx.logger.info(msg.base_currency)
    ctx.storage.set("base", msg.base_currency)

    ctx.storage.set('foreign', msg.foreign_currency)
    ctx.storage.set("number", msg.number)
    
    output_msg = f"Please Enter Values For {msg.foreign_currency}"
 
    await ctx.send(sender, RequestLimits(msg=output_msg))

@currency_protocol.on_message(ThresholdLimits, replies=RegistrationStatus)
async def process_limits(ctx: Context, sender: str, msg:ThresholdLimits):
    
    min = msg.min
    max = msg.max

    ctx.storage.set("min", min)
    ctx.storage.set("max", max)
    
    output_msg = f"Your inputs have been recorded! We will notify you if the rates go past the limits."

    ctx.storage.set("check", 1)
    ctx.storage.set("completed", True)
 
    await ctx.send(sender, RegistrationStatus(msg=output_msg))

@currency_protocol.on_interval(period=30, messages=None)
async def interval(ctx: Context):
    check = ctx.storage.get("check") or 0

 
    if check:
        
        load_dotenv()

        API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
        API_URL = f"http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}"
        
        number = ctx.storage.get("number")
        message = ""
        

        base = ctx.storage.get("base")

        foreign = ctx.storage.get("foreign")
        response = requests.get(API_URL + f"&{base}")
        
        data = response.json()
        min = ctx.storage.get("min")    
        max = ctx.storage.get("max")
        rate = data['rates'][foreign]
        print(rate)

        phone_number = "+919737012383"        

        WHATSAPP_API = os.getenv("WHATSAPP_API_KEY")
        if rate > max:
            message = f"The rate is {rate} above the limits set!"
            MESSAGE_API = f"https://api.callmebot.com/whatsapp.php?phone={number}&text={message}&apikey={WHATSAPP_API}"
            
            response = requests.get(MESSAGE_API)
            print(MESSAGE_API)
            print("UPARRR!")
            


        elif rate < min:
            message = f"The rate is {rate} and it is below the limits set!"  
            MESSAGE_API = f"https://api.callmebot.com/whatsapp.php?phone={number}&text={message}&apikey=3367362"
          
            response = requests.get(MESSAGE_API)
            print("NEECHE")

        else:
            message = "The rate is: {rate} Looks good, nothing's out of range"
            MESSAGE_API = f"https://api.callmebot.com/whatsapp.php?phone={number}&text={message}&apikey=3367362"
            response = requests.get(MESSAGE_API)

            ctx.logger.info(message)
            