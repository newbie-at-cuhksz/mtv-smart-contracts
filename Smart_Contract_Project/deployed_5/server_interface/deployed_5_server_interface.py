#!/usr/bin/env python
# -*- coding: utf-8 -*-


from client.contractnote import ContractNote
#from client.bcosclient import BcosClient
from client.bcosclienteth import BcosClientEth
import os
from eth_utils import to_checksum_address
from client.datatype_parser import DatatypeParser
from client.common.compiler import Compiler
from client.bcoserror import BcosException, BcosError
from client_config import client_config
import sys
import traceback


################################################
########### Interface: LguToken.sol ############

### func: directly grant user(`account`) `amount` of tokens
### (This function is not encouraged to be used, since it is not blockchain-style implementation)
### input:
###     `account`: str, user eth account address
###     `amount` : int, the amount of tokens to be granted to user
### output: 
###     bool, whether this transaction completes successfully
def LguToken_grantTokenDirectly1(account, amount):
    try:
        client = BcosClientEth(LguToken_ownerPrivateKey)

        args = [to_checksum_address(account), amount]
        receipt = client.sendRawTransactionGetReceipt(LguToken_address, LguToken_abi, "grantTokenDirectly1", args)
        #print("receipt:", receipt)
        client.finish()

        return True
    except:
        return False


### func: directly grant user(`account`) this number (timeSpan*valuePerTimeUnit) of tokens
### (This function is not encouraged to be used, since it is not blockchain-style implementation)
### input:
###     account : str, user eth account address
###     timeSpan : int
###     valuePerTimeUnit: int
### output: 
###     bool, whether this transaction completes successfully
def LguToken_grantTokenDirectly2(account, timeSpan, valuePerTimeUnit):
    try:
        client = BcosClientEth(LguToken_ownerPrivateKey)

        args = [to_checksum_address(account), timeSpan, valuePerTimeUnit]
        receipt = client.sendRawTransactionGetReceipt(LguToken_address, LguToken_abi, "grantTokenDirectly2", args)
        #print("receipt:", receipt)
        client.finish()

        return True
    except:
        return False


### func: grant user(`account`) tokens
### input:
###     `account`: str, user eth account address
###     `timeSpan` : int, unit time user stay in `regionName`
###     `regionName`: str (make sure the input is in `LguToken_regionList`)
### output: 
###     bool, whether this transaction completes successfully
def LguToken_grantTokenOnHookOnBlockchain(account, timeSpan, regionName):
    try:
        client = BcosClientEth(LguToken_ownerPrivateKey)

        args = [to_checksum_address(account), timeSpan, regionName]
        receipt = client.sendRawTransactionGetReceipt(LguToken_address, LguToken_abi, "grantTokenOnHookOnBlockchain", args)
        client.finish()

        return True
    except:
        return False


### func: user(userPrivateKey) spend `amount` of tokens
### *note: 类似`LguToken_CreateNft`该API不会检测用户是否有足够的token，
###        如果token不足，函数任会return true，但区块链上用户token数不会变化
###        (更多细节请参考note of `LguToken_CreateNft`)
### input: 
###     userPrivateKey: str, user's private key
###     amount: int, ammount of tokens to be spent
### output:
###     bool
def LguToken_spendTokenDirectly(userPrivateKey, amount):
    try:
        client = BcosClientEth(userPrivateKey)

        args = [amount]
        receipt = client.sendRawTransactionGetReceipt(LguToken_address, LguToken_abi, "spendTokenDirectly", args)
        client.finish()

        return True
    except:
        return False


### func: transfer `value` of tokens from `userPrivateKey` to `to`
### *note: 类似`LguToken_CreateNft`该API不会检测用户是否有足够的token，
###        如果token不足，函数仍会return true，但区块链上用户token数不会变化
###        (更多细节请参考note of `LguToken_CreateNft`)
### input:
###     userPrivateKey: the private key of the user, who wants to give out token
###     to: the address (public key) of the user, who receives the token
###     value: the amount of tokens to transfer
### output:
###     bool
def LguToken_transfer(userPrivateKey, to, value):
    try:
        client = BcosClientEth(userPrivateKey)

        args = [to_checksum_address(to), value]
        receipt = client.sendRawTransactionGetReceipt(LguToken_address, LguToken_abi, "transfer", args)
        client.finish()

        return True
    except:
        return False


### func: get number of tokens a user holds (`who`)
### input: 
###    `who`: str, address
### output: 
###    bool, whether this function completes successfully
###    int, token amount held by this user
def LguToken_balanceOf(who):
    try:
        client = BcosClientEth(dummy_privateKey)

        args = [to_checksum_address(who)]
        res = client.call(LguToken_address, LguToken_abi, "balanceOf", args)
        client.finish()
        return True, res[0]
    except:
        return False, -1


### func: get the token number per unit time in `regionName`
### input: 
##     `regionName`: str (make sure the input is in `LguToken_regionList`)
### output: 
###    bool, whether this function completes successfully
###    int, token value per unit time
def LguToken_getTokenNumPerUnitTime(regionName):
    try:
        client = BcosClientEth(dummy_privateKey)

        args = [regionName]
        res = client.call(LguToken_address, LguToken_abi, "getTokenNumPerUnitTime", args)
        client.finish()
        return True, res[0]
    except:
        return False, -1

### (DISCARDED) Please use the new API - `LguToken_getTokenNumPerUnitTime`
def LguToken_tokenNumPerUnitTime(regionName):
    return LguToken_getTokenNumPerUnitTime(regionName)


### func: get the weight of `regionName`
### input: 
###     `regionName`: str (make sure the input is in `LguToken_regionList`)
### output:
###     bool
###     int, the weight of `regionName`
def LguToken_getRegionWeight(regionName):
    try:
        client = BcosClientEth(dummy_privateKey)

        args = [regionName]
        res = client.call(LguToken_address, LguToken_abi, "getRegionWeight", args)
        client.finish()
        return True, res[0]
    except:
        return False, -1


### func: 区块链上，各个region的权重会根据该地区的得到token的数量而变化（即：越多人在某地区获得token，该地区的`LguToken_tokenNumPerUnitTime`数量越小）
###       此函数用于重置所有地区的权重
### output:
###     bool
def LguToken_resetRegionWeight():
    try:
        client = BcosClientEth(LguToken_ownerPrivateKey)

        args = []
        receipt = client.sendRawTransactionGetReceipt(LguToken_address, LguToken_abi, "resetRegionWeight", args)
        client.finish()

        return True
    except:
        return False


### func: get the total amount of tokens in this smart contract
### output:
###     bool
###     int, total amount of tokens in this smart contract
def LguToken_totalSupply():
    try:
        client = BcosClientEth(dummy_privateKey)

        args = []
        res = client.call(LguToken_address, LguToken_abi, "totalSupply", args)
        client.finish()
        return True, res[0]
    except:
        return False, -1


### func: the user (userPrivateKey) spend some tokens and create a NFT
### *note: 这个函数不会提前检查该用户是否有足够的token用于创造NFT，但智能合约会做检测:
###       - 如果token数目不足，函数仍会**return true**，但新的NFT不会被创造。
###         所以，在调用该接口前，应提前检测用户是否拥有足够的token，以保证用户体验
###         (return true/false 只表示我们的交易是否成功被发送至区块链，但区块链可以因token不足拒绝我们创造NFT的请求)
###       - 如果token数目充足，合约会自动扣除相应数目的token，无需服务器做任何额外的扣除操作
### input:
###     userPrivateKey: str, user's private key
###     nftName: str, 用户给NFT取的名字
###     nftContent: str, 模型文件的哈希值 (需要提前计算，计算方法见: https://github.com/newbie-at-cuhksz/mtv-smart-contracts/blob/main/Server_Contract_Interaction_py/MD5_py/nftContent_gen.py)
### output:
###     bool
def LguToken_CreateNft(userPrivateKey, nftName, nftContent):
    try:
        client = BcosClientEth(userPrivateKey)

        args = [nftName, nftContent]
        res = client.sendRawTransactionGetReceipt(LguToken_address, LguToken_abi, "CreateNft", args)
        client.finish()

        return True
    except:
        return False


### func: get how many tokens cost for a user to create a NFT
### output:
###     bool
###     int, number of tokens cost for a user to create a NFT
def LguToken_GetCreateNftFee():
    try:
        client = BcosClientEth(dummy_privateKey)

        args = []
        res = client.call(LguToken_address, LguToken_abi, "GetCreateNftFee", args)
        client.finish()
        return True, res[0]
    except:
        return False, -1


### func: set how many tokens cost for a user to create a NFT
### input:
###     newFee: int, number of tokens cost for a user to create a NFT
### output:
###     bool
def LguToken_SetCreateNftFee(newFee):
    try:
        client = BcosClientEth(LguToken_ownerPrivateKey)

        args = [newFee]
        res = client.sendRawTransactionGetReceipt(LguToken_address, LguToken_abi, "SetCreateNftFee", args)
        client.finish()
        return True
    except:
        return False
################################################



################################################
# 测试函数
def demo():
    # 以下为随机生成的ETH钱包
    user1_address = "0xE2fD835d8d064B672d16970B6739F177253F1499"
    user1_privateKey = "0x818352bbd9b3b1d66c44f278ad232e62cebfc2465dbf4deaae089617b3e24f84"

    user2_address = "0xc3b3131e171D8FBcB11A98a964D4dA97C284178c"
    user2_privateKey = "0x1ff515fe1d2326f1026ce679342233e00c45108b786a76f7bd8034c6aaf1722e"

    user3_address = "0x69A36F7252C46e7667dCaF45952cB4d5d983cBf5"
    user3_privateKey = "0x4030f93a771d4d711a5395fc515f65f41de1ae709d7f97df5212f9d962ed9557"

    LguToken_resetRegionWeight()
    print("reset Region Weight")

    isSuccess, amount = LguToken_totalSupply()
    print("==== total supply of tokens: %d ====" % amount)

    isSuccess, balance = LguToken_balanceOf(user1_address)
    print("User1: have %d tokens" % balance)

    LguToken_grantTokenDirectly1(user1_address, 10)
    print("grantTokenDirectly1: grant user1 10 tokens")

    isSuccess, balance = LguToken_balanceOf(user1_address)
    print("User1: have %d tokens" % balance)

    LguToken_grantTokenDirectly2(user1_address, 2, 4)
    print("grantTokenDirectly1: grant user1 (2*4) tokens")

    isSuccess, balance = LguToken_balanceOf(user1_address)
    print("User1: have %d tokens" % balance)

    isSuccess, amount = LguToken_getTokenNumPerUnitTime("University Library")
    print("Currently, user can get %d of token in University Library per minute" % amount)

    isSuccess, amount = LguToken_getRegionWeight("Shaw International Conference Centre")
    print("Currently, weight of Shaw International Conference Centre is %d" % amount)

    LguToken_grantTokenOnHookOnBlockchain(user1_address, 30, "University Library")
    print("grantTokenOnHookOnBlockchain: grant user1 stay in University Library for 30min")

    isSuccess, amount = LguToken_getTokenNumPerUnitTime("University Library")
    print("Currently, user can get %d of token in University Library per minute" % amount)

    isSuccess, amount = LguToken_getRegionWeight("Shaw International Conference Centre")
    print("Currently, weight of Shaw International Conference Centre is %d" % amount)

    isSuccess, balance = LguToken_balanceOf(user1_address)
    print("User1: have %d tokens" % balance)

    LguToken_spendTokenDirectly(user1_privateKey, 25)
    print("spendTokenDirectly: User1 spend 25 tokens directly")

    isSuccess, balance = LguToken_balanceOf(user1_address)
    print("User1: have %d tokens" % balance)

    isSuccess, balance = LguToken_balanceOf(user2_address)
    print("User2: have %d tokens" % balance)

    LguToken_transfer(user1_privateKey, user2_address, 5)
    print("User1 transfer 5 tokens to User2")

    isSuccess, balance = LguToken_balanceOf(user1_address)
    print("User1: have %d tokens" % balance)

    isSuccess, balance = LguToken_balanceOf(user2_address)
    print("User2: have %d tokens" % balance)

    isSuccess, amount = LguToken_totalSupply()
    print("==== total supply of tokens: %d ====" %amount)

    LguToken_resetRegionWeight()
    print("reset Region Weight")

    isSuccess, amount = LguToken_getRegionWeight("Shaw International Conference Centre")
    print("Currently, weight of Shaw International Conference Centre is %d" % amount)

    isSuccess, amount = LguToken_GetCreateNftFee()
    print("User need to spend %d of token to create a NFT" % amount)

    LguToken_SetCreateNftFee(amount + 2)
    print("Let's increase the NFT creation fee by 2")

    isSuccess, amount = LguToken_GetCreateNftFee()
    print("User need to spend %d of token to create a NFT" % amount)

    LguToken_CreateNft(user1_privateKey, "NFT-demo-01", "NFT-demo-01-content")
    print("User1 create a NFT")

    isSuccess, balance = LguToken_balanceOf(user1_address)
    print("User1: have %d tokens" % balance)


# 运行入口

# 声明全局变量
dummy_privateKey = "0x3c8ebf53a8b84f06a09f0207a314f5aed3d5a123c1539d3485f0afd7b36c77f6"  #全局变量，从区块链上读数据实际不需要私钥签名，但由于sdk限制，在此设定一个无用的私钥用于初始化client("address":"0xab5159fa9222e4787e53fb67394bf65c23d88ac9")

# 加载合约ABI - LguToken
abi_path_LguToken = "deployed_5_server_interface/LguToken.abi"
data_parser1 = DatatypeParser()
data_parser1.load_abi_file(abi_path_LguToken)
LguToken_abi = data_parser1.contract_abi                                                            #全局变量，在接口中被使用
LguToken_address = "0xa8f8be6d9abff36436c14add0ab59ec9cfbbe129"                                     #全局变量，在接口中被使用 (合约地址)
LguToken_ownerPrivateKey = "0xf7657dd26b5c63987c6fa586405023c694ae490c86feb44d68415df579b4219a"     #全局变量，在接口中被使用
LguToken_regionList = [
    "NOWHERE",
    "Administration Building",
    "University Library",
    "Student Center",
    "TA",
    "Million Avenue",
    "TB",
    "TC",
    "TD",
    "RA",
    "RB",
    "Shaw College East",
    "Shaw College West",
    "Zhixin Building",
    "GYM",
    "Harmonia College",
    "Dligentia College",
    "Muse College",
    "Staff Quarters",
    "Chengdao Building",
    "Zhiren Building",
    "Letian Building",
    "Shaw International Conference Centre",
    "Start-up Zone",
    "Daoyuan Building"
]

# 加载合约ABI - LguMetaverseEditor
abi_path_LguMetaverseEditor = "deployed_5_server_interface/LguMetaverseEditor.abi"
data_parser2 = DatatypeParser()
data_parser2.load_abi_file(abi_path_LguMetaverseEditor)
LguMetaverseEditor_abi = data_parser2.contract_abi                                                          #全局变量，在接口中被使用
LguMetaverseEditor_address = "0x7aa186962b1377d859a0b074a1dd3010e0b8aaec"                                   #全局变量，在接口中被使用 (合约地址)
LguMetaverseEditor_ownerPrivateKey = "0xf7657dd26b5c63987c6fa586405023c694ae490c86feb44d68415df579b4219a"   #全局变量，在接口中被使用


demo()
################################################
