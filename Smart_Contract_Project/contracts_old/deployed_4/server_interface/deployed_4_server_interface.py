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
##      bool, whether this transaction completes successfully
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


### func: grant user(`account`) tokens
### input:
###     `account`: str, user eth account address
###     `timeSpan` : int, unit time user stay in `regionName`
###     `regionName`: str
### output: 
##      bool, whether this transaction completes successfully
def LguToken_grantTokenOnHookOnBlockchain(account, timeSpan, regionName):
    try:
        client = BcosClientEth(LguToken_ownerPrivateKey)

        args = [to_checksum_address(account), timeSpan, regionName]
        receipt = client.sendRawTransactionGetReceipt(LguToken_address, LguToken_abi, "grantTokenOnHookOnBlockchain", args)
        client.finish()

        return True
    except:
        return False


### func: get number of tokens a user holds (`who`)
### input: 
##     `who`: str, address
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
##     `regionName`: str (can only be "University Library", "TA", "Shaw", "Gym" at this point)
### output: 
###    bool, whether this function completes successfully
###    int, token value per unit time
def LguToken_tokenNumPerUnitTime(regionName):
    try:
        client = BcosClientEth(dummy_privateKey)

        args = [regionName]
        res = client.call(LguToken_address, LguToken_abi, "tokenNumPerUnitTime", args)
        client.finish()
        return True, res[0]
    except:
        return False, -1
################################################



################################################
# ????????????
def demo():
    # ?????????????????????????????????????????????Metamask?????????
    #address:     0x820f3E244D73c5bF5c92A34Cc0B56E5912129f55
    #privateKey:  0x3e14b5b682d9768a1e37a39a6510e51b813b071c05c33b378157fbbb10c3a7ae
    user_gary_address = "0x820f3E244D73c5bF5c92A34Cc0B56E5912129f55"
    user_gary_privateKey = "0x3e14b5b682d9768a1e37a39a6510e51b813b071c05c33b378157fbbb10c3a7ae"


    isSuccess = False
    isSuccess, res = LguToken_tokenNumPerUnitTime("University Library")
    if isSuccess:
        print("tokenNumPerUnitTime of University Library: ", res)

    isSuccess = False
    isSuccess, res = LguToken_tokenNumPerUnitTime("TA")
    if isSuccess:
        print("tokenNumPerUnitTime of TA: ", res)

    isSuccess = False
    isSuccess, res = LguToken_balanceOf(user_gary_address)
    if isSuccess:
        print("This user holds **", res, "** tokens")

    if LguToken_grantTokenOnHookOnBlockchain(user_gary_address, 30, "University Library"):
        print("This user is granted with tokens successfully")

    isSuccess = False
    isSuccess, res = LguToken_balanceOf(user_gary_address)
    if isSuccess:
        print("This user holds **", res, "** tokens")


    isSuccess = False
    isSuccess, res = LguToken_tokenNumPerUnitTime("University Library")
    if isSuccess:
        print("tokenNumPerUnitTime of University Library: ", res)

    isSuccess = False
    isSuccess, res = LguToken_tokenNumPerUnitTime("TA")
    if isSuccess:
        print("tokenNumPerUnitTime of TA: ", res)


# ????????????

# ??????????????????
dummy_privateKey = "0x3c8ebf53a8b84f06a09f0207a314f5aed3d5a123c1539d3485f0afd7b36c77f6"  #??????????????????????????????????????????????????????????????????????????????sdk?????????????????????????????????????????????????????????client("address":"0xab5159fa9222e4787e53fb67394bf65c23d88ac9")

# ????????????ABI - LguToken
abi_LguToken = "deployed_4_server_interface/LguToken.abi"
data_parser1 = DatatypeParser()
data_parser1.load_abi_file(abi_LguToken)
LguToken_abi = data_parser1.contract_abi                                                  #????????????????????????????????????
LguToken_address = "0xad84fc9c84d327f33be15e49c0b32846d06cc3e9"                           #???????????????????????????????????? (????????????)
LguToken_ownerPrivateKey = "0x721ea4a6ee1bff772ae0de6af6bb499eb44ea97ae11f7c55d3c1450b4ffbd246"


# # ????????????ABI - LguMetaverseEditor
# abi_LguMetaverseEditor = "deployed_4_server_interface/LguMetaverseEditor.abi"
# data_parser2 = DatatypeParser()
# data_parser2.load_abi_file(abi_LguMetaverseEditor)
# LguMetaverseEditor_abi = data_parser2.contract_abi                    #????????????????????????????????????
# LguMetaverseEditor_address = "0x0cb70888c4c53f3a67ea0c7052ff64522b8218d6"

demo()
################################################
