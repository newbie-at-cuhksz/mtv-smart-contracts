from eth_account import Account
import secrets

priv = secrets.token_hex(32)
private_key = "0x" + priv

print ("SAVE BUT DO NOT SHARE THIS:", private_key)      # 私钥：注意在调用合约接口时，私钥需要有"0x"前缀
acct = Account.from_key(private_key)
print("Address:", acct.address)                         # 公钥
