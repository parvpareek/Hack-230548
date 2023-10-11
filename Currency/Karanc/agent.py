from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
from Karanc.protocols import currency_protocol
 
karanc = Agent(
    name="karanc",
    port=8001,
    seed="karanc phrase",
    endpoint=["http://127.0.0.1:8001/submit"],
)
 
fund_agent_if_low(karanc.wallet.address())
 
print(karanc.address)
karanc.include(currency_protocol)

def runAgent():
    karanc.run()