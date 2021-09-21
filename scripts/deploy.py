from brownie import MyToken
from scripts.helpful_scripts import get_account

INITIAL_SUPPLY = 10000000000

def deploy_my_token(initial_supply=INITIAL_SUPPLY):
  account = get_account()
  my_token = MyToken.deploy(initial_supply,{"from":account})
  print(f"Contract deployed to {my_token.address}")

def main():
  deploy_my_token()