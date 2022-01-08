from bitcoin import *
from eth_account import Account
import secrets

my_private_key = random_key()
print("Private Key: %s\n" % my_private_key)

public_key = privtopub(my_private_key)
print(public_key)
address = pubtoaddr(public_key)
print(address)

priv = secrets.token_hex(32)
private_key = "0x" + priv
print ("SAVE BUT DO NOT SHARE THIS:", private_key)
acct = Account.from_key(private_key)
print("Address:", acct.address)