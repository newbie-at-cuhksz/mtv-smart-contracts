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
### output: bool, whether this transaction completes successfully
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
    # except BcosException as e:
    #     print("execute demo_transaction failed ,BcosException for: {}".format(e))
    #     traceback.print_exc()
    # except BcosError as e:
    #     print("execute demo_transaction failed ,BcosError for: {}".format(e))
    #     traceback.print_exc()
    # except Exception as e:
    #     client.finish()
    #     traceback.print_exc()


### func: get the token number per unit time in `regionName`
### input: `regionName`, str
### output: int, token value per unit time
def Lgu_tokenNumPerUnitTime(regionName):
    try:
        client = BcosClientEth(dummy_privateKey)

        args = [regionName]
        res = client.call(LguToken_address, LguToken_abi, "tokenNumPerUnitTime", args)
        client.finish()
        return True, res
    except:
        return False, -1
################################################



# 测试函数
def demo():
    # 初始化以太坊钱包（以下公私钥由Metamask生成）
    #address:     0x820f3E244D73c5bF5c92A34Cc0B56E5912129f55
    #privateKey:  0x3e14b5b682d9768a1e37a39a6510e51b813b071c05c33b378157fbbb10c3a7ae
    user_address = "0x820f3E244D73c5bF5c92A34Cc0B56E5912129f55"
    user_privateKey = "0x3e14b5b682d9768a1e37a39a6510e51b813b071c05c33b378157fbbb10c3a7ae"

    #isSuccess = LguToken_grantTokenDirectly1(user_address, 30)
    isSuccess = False
    isSuccess, res = Lgu_tokenNumPerUnitTime("University Library")
    if isSuccess:
        print("tokenNumPerUnitTime of University Library: ", res[0])
        print( type(res[0]) )        #int
        print( type(res) )           #tuple



################################################
# 运行入口

# 声明全局变量
dummy_privateKey = "0x3c8ebf53a8b84f06a09f0207a314f5aed3d5a123c1539d3485f0afd7b36c77f6"  #全局变量，从区块链上读数据实际不需要私钥签名，但由于sdk限制，在此设定一个无用的私钥用于初始化client("address":"0xab5159fa9222e4787e53fb67394bf65c23d88ac9")

# 加载合约ABI - LguToken
abi_LguToken = "deployed_4_server_interface/LguToken.abi"
data_parser1 = DatatypeParser()
data_parser1.load_abi_file(abi_LguToken)
LguToken_abi = data_parser1.contract_abi                                                  #全局变量，在接口中被使用
LguToken_address = "0xad84fc9c84d327f33be15e49c0b32846d06cc3e9"                           #全局变量，在接口中被使用 (合约地址)
LguToken_ownerPrivateKey = "0x721ea4a6ee1bff772ae0de6af6bb499eb44ea97ae11f7c55d3c1450b4ffbd246"


# # 加载合约ABI - LguMetaverseEditor
# abi_LguMetaverseEditor = "deployed_4_server_interface/LguMetaverseEditor.abi"
# data_parser2 = DatatypeParser()
# data_parser2.load_abi_file(abi_LguMetaverseEditor)
# LguMetaverseEditor_abi = data_parser2.contract_abi                    #全局变量，在接口中被使用
# LguMetaverseEditor_address = "0x0cb70888c4c53f3a67ea0c7052ff64522b8218d6"

demo()
################################################
