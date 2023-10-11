from uagents import Context, Model, Protocol
import typing
import requests

class CurrencyParams(Model):
    base_currency: str
    foreign_currency: str

class RequestLimits(Model):
    msg: str

class ThresholdLimits(Model):
    min: float
    max: float

class RegistrationStatus(Model):
    msg: str
    

currency_protocol = Protocol()


@currency_protocol.on_message(CurrencyParams, replies=RequestLimits)
async def process_input(ctx: Context, sender: str, msg:CurrencyParams):
    
    base = msg.base_currency
    foreign = msg.foreign_currency

    ctx.storage.set("base", base)
    ctx.storage.set("foreign", foreign)
    
    output_msg = "Please Enter Values For "

    for cur in foreign:
        output_msg += f" {cur}"
 
    await ctx.send(sender, RequestLimits(msg=output_msg))

@currency_protocol.on_message(ThresholdLimits, replies=RegistrationStatus)
async def process_limits(ctx: Context, sender: str, msg:CurrencyParams):
    
    min = msg.base_currency
    max = msg.foreign_currency

    ctx.storage.set("min", min)
    ctx.storage.set("max", max)
    
    output_msg = f"Your inputs have been recorded! We will notify you if the rates go past the limits."

    ctx.storage.set("check", 1)
    ctx.storage.set("completed", True)
 
    await ctx.send(sender, RegistrationStatus(msg=output_msg))

@currency_protocol.on_interval(period=30)
async def interval(ctx: Context):
    check = ctx.storage.get("check") or 0
 
    if check:
        
        API_KEY = "0de13419226f14163d3100b80323dfc8"
        API_URL = f"http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}"

        base = ctx.storage.get("base")
        foreing = ctx.storage.get("foreign")
        response = requests.get(API_URL + f"&{base}")

        if response.status_code == 200:
            data = response.json()
            max = ctx.storage.get("max")
            min = ctx.storage.get("min")

            rate = data['rates']['foreign']

            if rate > max:
                #Send Alert
                print()

            elif rate < min:
                #send alert
                print()
            