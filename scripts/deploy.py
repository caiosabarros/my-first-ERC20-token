from brownie import MyToken
from scripts.helpful_scripts import get_account

INITIAL_SUPPLY = 10000000000

def deploy_my_token(initial_supply=INITIAL_SUPPLY):
  account = get_account()
  my_token = MyToken.deploy(initial_supply,{"from":account})
  print(f"Contract deployed to {my_token.address}")

def total_ammount():
  account = get_account()
  token = MyToken[-1]
  total = token.totalSupply() #Since it is not a state change, I don't need to include {"from":account}
  print(f"The total supply is {total}") 

def main():
  deploy_my_token()
  total_ammount()
