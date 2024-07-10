from tronpy import Tron
from tronpy.providers import HTTPProvider
client = Tron(HTTPProvider(api_key="API_KEY_HERE"))
balance = client.get_account_balance(str('TRON_ADDRESS_HERE'))
totalTRONPower = client.get_account_resource('TRON_ADDRESS_HERE')["tronPowerLimit"]  #Total TRON Power 
usedTRONPower = client.get_account_resource('TRON_ADDRESS_HERE')["tronPowerLimit"] # Used TRON Power
unusedTRONPower = totalTRONPower - usedTRONPower
print ("Unfrozen Balance in TRX: ", balance) 
print ("Total Staked TRX v2: ", totalTRONPower)
print ("Unused Tron Power: ", unusedTRONPower)
print ("Total TRX Account Balance: ", balance + totalTRONPower)