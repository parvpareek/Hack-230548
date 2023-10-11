from Karanc.protocols import *

from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
 
KARANC_ADDRESS = "agent1qw5cvefhhpz9epn06uj0zshljvdfkftw5j4demetnvtqjp73tzwx282am04"
 
user = Agent(
    name="user",
    port=8001,
    seed="user secret phrase",
    endpoint=["http://127.0.0.1:8001/submit"],
)
 
fund_agent_if_low(user.wallet.address())

input_params = None
limit_params = None

def setParams(base:str, foreign:str):

    input_params = CurrencyParams(base_currency=base, foreign_currency=foreign)

def setLimts(min:float, max:float):
    limit_params = ThresholdLimits(min, max)

 
# This on_interval agent function performs a request on a defined period
@user.on_interval(period=20, messages=CurrencyParams)
async def interval(ctx: Context):
    completed = ctx.storage.get("completed") or 0
 
    if not completed:
        await ctx.send(KARANC_ADDRESS, input_params)
 
@user.on_message(RequestLimits, replies=ThresholdLimits)
async def handle_registration_response(ctx: Context, sender: str, msg: RequestLimits):
    
    

    await ctx.send(KARANC_ADDRESS, limit_params)

def runUser():
    user.run()

"""if __name__ == "__main__":
    user.run()"""