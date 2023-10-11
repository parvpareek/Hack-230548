from protocols.protocols import *

from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
 
KARANC_ADDRESS = "agent1qw5cvefhhpz9epn06uj0zshljvdfkftw5j4demetnvtqjp73tzwx282am04"
 
user = Agent(
    name="user",
    port=8000,
    seed="user secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)
 
fund_agent_if_low(user.wallet.address())
 

 
# This on_interval agent function performs a request on a defined period
@user.on_interval(period=30, messages=CurrencyParams)
async def interval(ctx: Context):
    completed = ctx.storage.get("completed") or 0
 
    if not completed:
        base = input("Enter the base currency code e.g: INR, USD, GBP, JPY, EUR, etc: ")
        foreign = input("Enter the foregin currency code e.g: INR, USD, GBP, JPY, etc: ")
        number  = input("Enter your phone number where we can notify you: ")
        number = "91" + number

        await ctx.send(KARANC_ADDRESS, CurrencyParams(base_currency=base, foreign_currency=foreign, number=number))
 
@user.on_message(RequestLimits, replies=ThresholdLimits)
async def handle_request_limits(ctx: Context, sender: str, msg: RequestLimits):

    ctx.logger.info("Karan C:"  + msg.msg)    
    max = input(f"Enter the maximum rate: ")
    min = input(f"Enter the minimum rate: ")

    await ctx.send(KARANC_ADDRESS, ThresholdLimits(max=float(max), min=float(min)))

@user.on_message(RegistrationStatus)
async def handle_registration_response(ctx: Context, sender: str, status: RegistrationStatus):
    
    ctx.logger.info(status.msg)

if __name__ == "__main__":
    user.run()