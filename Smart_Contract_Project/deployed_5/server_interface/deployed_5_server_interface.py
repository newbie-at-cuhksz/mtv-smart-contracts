#!/usr/bin/env python
# -*- coding: utf-8 -*-


from eth_account.account import Account
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


################################ 关于接口的注意事项 ################################
#
#   1. 每个API上方注释有详细的输入参数、返回值说明
#
#   2. 中文的注释都比较重要
#
#   3. 所有API的第一个返回值都为bool，它表示输入参数是否被成功递交给智能合约，
#      在 **参数类型** 不正确等情况发生时时，它会 return False
#
#   4. API **不会** 进行其他输入参数的鲁棒性验证，所有API都会尝试直接把输入的参数交给智能合约，并把智能合约的返回值交给我们。
#
#      当然，智能合约会检测出不合法的参数，或者不合理的请求。
#      比如，花费10个token，但账户里的token不足10个；
#           给一个不属于你的NFT改名...
#
#      当这些不合理的请求发生时，智能合约会拒绝该请求，合约里的数据不会发生变化。
#      不过问题在于，API不会告诉我们，我们的请求被拒绝了，
#      API的第一个返回值仍会为Ture（毕竟API已经成功把参数递交给智能合约，它的任务已经完成了），
#      我们不应该依赖API的第一个返回值来判断调用是否成功，
#      在调用API前，应提前做好鲁棒性检测，以保证更好的用户体验
#
#      （更详细的说明见对应API上方的注释）
#
#   5. 不是所有的API都需要/应该被数据服务器直接使用，这些API上方的注释里会被标注 --- "不被数据服务器直接调用"
#
######################################################################################


################################################################
###############     Interface: LguToken.sol     ################

### （不被数据服务器直接调用）
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


### （不被数据服务器直接调用）
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
###     userPrivateKey:     str, the private key of the user, who wants to give out token
###     to:                 str, the address (public key) of the user, who receives the token
###     value:              int, the amount of tokens to transfer
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


### （不被数据服务器直接调用）
### func: approve `value` amount of tokens to `spender`
### input:
###     userPrivateKey:     str, the private key of the user, who wants to give out token
###     spender:            str, address of user/contract get approved
###     value:              int, the amount of tokens
### output:
###     bool
def LguToken_approve(userPrivateKey, spender, value):
    try:
        client = BcosClientEth(userPrivateKey)

        args = [to_checksum_address(spender), value]
        receipt = client.sendRawTransactionGetReceipt(LguToken_address, LguToken_abi, "approve", args)
        client.finish()

        return True
    except:
        return False

### func: get number of tokens a user holds (`owner`)
### input: 
###    owner: str, address
### output: 
###    bool, whether this function completes successfully
###    int, token amount held by this user
def LguToken_balanceOf(owner):
    try:
        client = BcosClientEth(dummy_privateKey)

        args = [to_checksum_address(owner)]
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
###     nftName:        str, 用户给NFT取的名字
###     nftContent:     str, 模型文件的哈希值 (需要服务器提前计算，计算方法见: https://github.com/newbie-at-cuhksz/mtv-smart-contracts/blob/main/Server_Contract_Interaction_py/MD5_py/nftContent_gen.py)
### output:
###     bool
###     int, the newly created NFT ID
def LguToken_CreateNft(userPrivateKey, nftName, nftContent):
    try:
        client = BcosClientEth(userPrivateKey)

        args = [nftName, nftContent]
        receipt = client.sendRawTransactionGetReceipt(LguToken_address, LguToken_abi, "CreateNft", args)
        client.finish()

        # parse the receipt for event (NewLguModel),
        # and get the ID of newly created NFT
        newNftId = -1
        data_parser = DatatypeParser()
        logresult = data_parser.parse_event_logs(receipt["logs"])
        for log in logresult:
            if 'eventname' in log:
                if (log['eventname'] == "NewLguModel"):     # log['eventname'] should be a str
                    newNftId = log['eventdata'][0]          # log['eventdata'] should be a tuple, (NFT_ID, NFT_NAME, NFT_CONTENT), e.g. (11, 'event-test', 'event-test_C')

        return True, newNftId
    except:
        return False, -1


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


##################################################################
###########     Interface: LguMetaverseEditor.sol     ############

# 这个合约专门用于"体素编辑器"，即："体素编辑器"发布的模型为储存于本合约的NFT
# 目前，"宠物编辑器"发布的涂色不为NFT

# 关于NFT：每个NFT都有一个unique ID, 这个ID维护在区块链上。
#         每当有新的NFT被创造，新的 NFT ID 为当前最大(ID+1)。
#         即：NFT ID 由 0, 1, 2, 3... 顺序增长
#
#         我知道数据服务器也给每个模型(NFT)维护了一个模型ID用于数据同步，
#         值得一提的是，"区块链上的NFT ID" 和 "数据服务器的模型ID" 是可以inconsistent的
#         即：数据服务器的模型仅用于我们做数据同步，而区块链上的NFT ID用于显示在UI上，给玩家看.
#         这边怎么方便怎么来

### func: get number of NFTs a user holds (`owner`)
### input: 
###    owner: str, address
### output: 
###    bool, whether this function completes successfully
###    int, number of NFTs held by this user
def LguMetaverseEditor_balanceOf(owner):
    try:
        client = BcosClientEth(dummy_privateKey)

        args = [to_checksum_address(owner)]
        res = client.call(LguMetaverseEditor_address, LguMetaverseEditor_abi, "balanceOf", args)
        client.finish()
        return True, res[0]
    except:
        return False, -1


### func: change name of a NFT
### *note: 此API不会检测`modelId`是否属于发起改名的用户(`userPrivateKey`)
###        如果`modelId`不属于该用户，此函数仍return true，改名将不会发生在区块链上
###        (类似`LguToken_CreateNft`)
### input: 
###     userPrivateKey: str, user private key
###     modelId: int, the unique NFT ID owned by this user
###     newName: str, new name for this NFT
### output:
###     bool
def LguMetaverseEditor_changeName(userPrivateKey, modelId, newName):
    try:
        client = BcosClientEth(userPrivateKey)

        args = [modelId, newName]
        res = client.sendRawTransactionGetReceipt(LguMetaverseEditor_address, LguMetaverseEditor_abi, "changeName", args)
        client.finish()
        return True
    except:
        return False


### func: get the info (name and content) of the NFT indexed by `modelId`
### input:
###     modelId: int, the unique NFT ID owned by this user
### output:
###     bool, return "False" if the `modelId` does not exist (e.g. the `modelId` is too big and no NFT is associated with this ID yet)
###     str, name of this NFT
###     str, content of this NFT
def LguMetaverseEditor_LguModels(modelId):
    try:
        client = BcosClientEth(dummy_privateKey)

        args = [modelId]
        res = client.call(LguMetaverseEditor_address, LguMetaverseEditor_abi, "LguModels", args)
        client.finish()
        return True, res[0], res[1]
    except:
        return False, "", ""

### Another name of `LguMetaverseEditor_LguModels`, which is easier to understand in terms of function naming
def LguMetaverseEditor_getModelInfo(modelId):
    return LguMetaverseEditor_LguModels(modelId)


### func: get the owner address of a model
### input:
###     modelId: int, the unique NFT ID
### output:
###     bool,                       与`LguMetaverseEditor_getModelInfo`不同，如果`modelId`非法/太大，此函数仍return true
###     str, address of the owner   (如果`modelId`非法/太大，此处值为"0x0000000000000000000000000000000000000000")
def LguMetaverseEditor_ownerOf(modelId):
    try:
        client = BcosClientEth(dummy_privateKey)

        args = [modelId]
        res = client.call(LguMetaverseEditor_address, LguMetaverseEditor_abi, "ownerOf", args)
        client.finish()
        return True, res[0]
    except:
        return False, ""

### Another name of `LguMetaverseEditor_ownerOf`
def LguMetaverseEditor_LguModelToOwner(modelId):
    return LguMetaverseEditor_ownerOf(modelId)


### func: get a list of NFT IDs owned by user
### input: 
###     owner: str, address
### output: 
###     bool
###     tuple of int: list of NFT IDs owned by user
def LguMetaverseEditor_getModelsByOwner(owner):
    try:
        client = BcosClientEth(dummy_privateKey)

        args = [to_checksum_address(owner)]
        res = client.call(LguMetaverseEditor_address, LguMetaverseEditor_abi, "getModelsByOwner", args)
        client.finish()
        return True, res[0]
    except:
        return False, tuple()


### （不被数据服务器直接调用）
### func: transfer a NFT with ID `_tokenId` from `_from` to `_to`
### input:
###     userPrivateKey: str, user private key
###     _from:          str, address
###     _to:            str, address
###     _tokenId:       int
### *note:  通常情况下这里的`userPrivateKey`就是`_from`(公钥/地址)所对应的私钥，意为：用户把自己拥有的NFT-`_tokenId`，转移给`_to`
###         但是在某些情况下，`_from`可以不为`userPrivateKey`所对应的公钥，意为：用户把一个不属于自己的NFT-`_tokenId`，转移给`_to`。这种情况我们应该用不到
### output:
###     bool
def LguMetaverseEditor_transferFrom(userPrivateKey, _from, _to, _tokenId):
    try:
        client = BcosClientEth(userPrivateKey)

        args = [to_checksum_address(_from), to_checksum_address(_to), _tokenId]
        res = client.sendRawTransactionGetReceipt(LguMetaverseEditor_address, LguMetaverseEditor_abi, "transferFrom", args)
        client.finish()
        return True
    except:
        return False


### （不被数据服务器直接调用）
### func: approve an NFT to `spender`
### input:
###     userPrivateKey: str, user private key
###     _to:            str, address
###     _tokenId:       int
### output:
###     bool
def LguMetaverseEditor_approve(userPrivateKey, _to, _tokenId):
    try:
        client = BcosClientEth(userPrivateKey)

        args = [to_checksum_address(_to), _tokenId]
        res = client.sendRawTransactionGetReceipt(LguMetaverseEditor_address, LguMetaverseEditor_abi, "approve", args)
        client.finish()
        return True
    except:
        return False

##########################################################



##############################################################
###########     Interface: LguModelMarket.sol     ############

# 此合约用于实现：使用 LguToken 交易 LguMetaverseEditor(NFT) 的功能。
#
# MOTIVATION - 设计这个合约的原因：
#   自然，即使没有这个合约，用token交易NFT的功能也是可以实现的。
#   当两名用户商议好价格后，数据服务器执行：
#       LguToken_transfer(buyer_private_key, seller_addr, price)
#       LguMetaverseEditor_transferFrom(seller_private_key, seller_addr, buyer_addr, NftId)
#   即：我们的数据服务器充当一个中心化的中间商，帮用户完成一手交钱一手交货的手续
#
#   但是，既然token和NFT都是链上资产，这个交易手续就不适合由一个中心化的中间商来执行。
#   所以，我增加了这个合约，把上述的交易手续转移到链上进行。
#
# 合约功能 & 使用：
#   这个合约的设计初衷是想要实现一个去中心化的"淘宝网"，玩家可以上架、下架、交易NFT。
#   但是，上架、下架这些功能实际上我们在数据服务器上都已经实现过了。
#   所以，对于数据服务器来说，我们只借用本合约进行NFT交易，其余的上架/下架功能仍使用之前的“中心化”实现方式。
#   也就是说，尽管下方有许多新增的API，只有一个API（交易NFT）是会被数据服务器直接使用的。


### func: trade a NFT between two users
### *note: 严格来说，这不是一个合约接口，这个函数中调用了一系列合约API，从而实现交易NFT的功能。
###        也因此，与其他API不同，我在这个函数中做了“鲁棒性”测试
### input:
###     sellerPrivateKey:   str
###     buyerPrivateKey:    str
###     nftId:              int
###     price:              int
### output:
###     bool
def LguModelMarket_trade(sellerPrivateKey, buyerPrivateKey, nftId, price):
    # init
    sellerAddr = Account.from_key(sellerPrivateKey).address
    buyerAddr  = Account.from_key(buyerPrivateKey).address

    # robustness test: seller is this owner of `nftId`?
    isSuccess, nftOwner = LguMetaverseEditor_ownerOf(nftId)
    if (not isSuccess) or (nftOwner.lower() != sellerAddr.lower()):
        return False
    
    # robustness test: buyer has enough tokens?
    isSuccess, tokenAmount = LguToken_balanceOf(buyerAddr)
    if (not isSuccess) or (tokenAmount < price):
        return False
    
    # seller approve NFT
    isSuccess = LguMetaverseEditor_approve(sellerPrivateKey, LguModelMarket_address, nftId)
    if (not isSuccess):
        return False

    # seller open trade
    isSuccess, tradeId = LguModelMarket_openTrade(sellerPrivateKey, nftId, price)
    if (not isSuccess):
        return False
    
    # buyer approve tokens
    isSuccess = LguToken_approve(buyerPrivateKey, LguModelMarket_address, price)
    if (not isSuccess):
        return False

    # buyer execute trade
    isSuccess = LguModelMarket_executeTrade(buyerPrivateKey, tradeId)
    if (not isSuccess):
        return False

    return True


### （不被数据服务器直接调用）
### func: get trade info
### input:
###     _trade: int, trade id
### output:
###     bool
###     str, trade poster
###     int, trade NFT id
###     int, trade ERC20 price
###     ~~str, trade status~~
def LguModelMarket_getTrade(_trade):
    try:
        client = BcosClientEth(dummy_privateKey)

        args = [_trade]
        res = client.call(LguModelMarket_address, LguModelMarket_abi, "getTrade", args)
        client.finish()
        return True, res[0], res[1], res[2]
    except:
        return False, "", 0, 0


### （不被数据服务器直接调用）
### func: open a trade
### input:
###     userPrivateKey: str
###     _item:          int, NFT id to be selled
###     _price:         int
### output;
###     bool
###     int, trade id
def LguModelMarket_openTrade(userPrivateKey, _item, _price):
    try:
        client = BcosClientEth(userPrivateKey)

        args = [_item, _price]
        receipt = client.sendRawTransactionGetReceipt(LguModelMarket_address, LguModelMarket_abi, "openTrade", args)
        client.finish()

        # parse the receipt for trade id
        tradeId = -1
        data_parser = DatatypeParser()
        logresult = data_parser.parse_event_logs(receipt["logs"])
        for log in logresult:
            if 'eventname' in log:
                if (log['eventname'] == "TradeStatusChange"):     # log['eventname'] should be a str
                    tradeId = log['eventdata'][0]

        return True, tradeId
    except:
        return False, -1


### （不被数据服务器直接调用）
### func: execute a trade
### input:
###     userPrivateKey: str, buyer private key
###     _trade:         int, trade id
### output:
###     bool
def LguModelMarket_executeTrade(userPrivateKey, _trade):
    try:
        client = BcosClientEth(userPrivateKey)

        args = [_trade]
        res = client.sendRawTransactionGetReceipt(LguModelMarket_address, LguModelMarket_abi, "executeTrade", args)
        client.finish()
        return True
    except:
        return False


### （不被数据服务器直接调用）
### func: cancel a trade
### input:
###     userPrivateKey: str, original seller private key
###     _trade:         int, trade id to be cancelled
### output:
###     bool
def LguModelMarket_cancelTrade(userPrivateKey, _trade):
    try:
        client = BcosClientEth(userPrivateKey)

        args = [_trade]
        res = client.sendRawTransactionGetReceipt(LguModelMarket_address, LguModelMarket_abi, "cancelTrade", args)
        client.finish()
        return True
    except:
        return False

##############################################################



##########################################################
# 测试函数
def demo():
    # 以下为随机生成的ETH钱包
    user1_address = "0xE2fD835d8d064B672d16970B6739F177253F1499"
    user1_privateKey = "0x818352bbd9b3b1d66c44f278ad232e62cebfc2465dbf4deaae089617b3e24f84"

    user2_address = "0xc3b3131e171D8FBcB11A98a964D4dA97C284178c"
    user2_privateKey = "0x1ff515fe1d2326f1026ce679342233e00c45108b786a76f7bd8034c6aaf1722e"

    user3_address = "0x69A36F7252C46e7667dCaF45952cB4d5d983cBf5"
    user3_privateKey = "0x4030f93a771d4d711a5395fc515f65f41de1ae709d7f97df5212f9d962ed9557"

    print("=========== Test LguToken API ===========")

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

    LguToken_transfer(user1_privateKey, user2_address, 50)
    print("User1 transfer 50 tokens to User2")

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


    print("=========== Test LguMetaverseEditor API ===========")

    isSuccess, balance = LguToken_balanceOf(user1_address)
    print("User1: have %d tokens" % balance)

    isSuccess, balance = LguMetaverseEditor_balanceOf(user1_address)
    print("User1 has %d NFTs" % balance)

    isSuccess, nftList = LguMetaverseEditor_getModelsByOwner(user1_address)
    print("User1 has the following NFTs: ", nftList)

    isSuccess, newNftId = LguToken_CreateNft(user1_privateKey, "NFT-demo", "NFT-demo-content")
    print("User1 create a new NFT, whose ID is %d" % newNftId)

    isSuccess, balance = LguToken_balanceOf(user1_address)
    print("User1: have %d tokens" % balance)

    isSuccess, balance = LguMetaverseEditor_balanceOf(user1_address)
    print("User1 has %d NFTs" % balance)

    isSuccess, nftList = LguMetaverseEditor_getModelsByOwner(user1_address)
    print("User1 has the following NFTs: ", nftList)

    modelId = nftList[0]
    print("We know that NFT with ID %d is owned by User1" % modelId)
    print("We now let User1 do some operation to this NFT")

    isSuccess, ownerAddr = LguMetaverseEditor_LguModelToOwner(modelId)
    print("NFT-%d is owned by %s" % (modelId, ownerAddr))
    print("Is this address equals the address of User1? -", (ownerAddr.lower() == user1_address.lower()))

    isSuccess, modelName, modelContent = LguMetaverseEditor_getModelInfo(modelId)
    print("NFT-%d has info - name: %s; content: %s" % (modelId, modelName, modelContent))

    newName = modelName + "-update"
    LguMetaverseEditor_changeName(user1_privateKey, modelId, newName)
    print("User1 change the name of NFT-%d to \"%s\"" % (modelId, newName))

    isSuccess, modelName, modelContent = LguMetaverseEditor_getModelInfo(modelId)
    print("NFT-%d has info - name: %s; content: %s" % (modelId, modelName, modelContent))

    isSuccess, nftList = LguMetaverseEditor_getModelsByOwner(user2_address)
    print("User2 has the following NFTs: ", nftList)

    isSuccess, balance = LguToken_balanceOf(user1_address)
    print("User1: have %d tokens" % balance)

    isSuccess, balance = LguToken_balanceOf(user2_address)
    print("User2: have %d tokens" % balance)

    # LguMetaverseEditor_transferFrom(user1_privateKey, user1_address, user2_address, modelId)
    # print("User1 transfer NFT-%d to User2" % modelId)

    LguModelMarket_trade(user1_privateKey, user2_privateKey, modelId, 15)
    print("User1 sell NFT-%d to User2 at price 15" % modelId)

    isSuccess, balance = LguToken_balanceOf(user1_address)
    print("User1: have %d tokens" % balance)

    isSuccess, balance = LguToken_balanceOf(user2_address)
    print("User2: have %d tokens" % balance)

    isSuccess, nftList = LguMetaverseEditor_getModelsByOwner(user1_address)
    print("User1 has the following NFTs: ", nftList)

    isSuccess, nftList = LguMetaverseEditor_getModelsByOwner(user2_address)
    print("User2 has the following NFTs: ", nftList)

    isSuccess, ownerAddr = LguMetaverseEditor_LguModelToOwner(modelId)
    print("NFT-%d is owned by %s" % (modelId, ownerAddr))
    print("Is this address equals the address of User2? -", (ownerAddr.lower() == user2_address.lower()))


# 运行入口

# API配置初始化 / 声明全局变量
dummy_privateKey = "0x3c8ebf53a8b84f06a09f0207a314f5aed3d5a123c1539d3485f0afd7b36c77f6"  #全局变量，从区块链上读数据实际不需要私钥签名，但由于sdk限制，在此设定一个无用的私钥用于初始化client("address":"0xab5159fa9222e4787e53fb67394bf65c23d88ac9")

# 加载合约ABI - LguToken
abi_path_LguToken = "deployed_5_server_interface/LguToken.abi"
data_parser1 = DatatypeParser()
data_parser1.load_abi_file(abi_path_LguToken)
LguToken_abi = data_parser1.contract_abi                                                            #全局变量，在接口中被使用
LguToken_address = "0xe806418d6ef61fcc899a5054c05af39652dcf9de"                                     #全局变量，在接口中被使用 (合约地址)
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
LguMetaverseEditor_address = "0x6cc8180c529583fb80ab42b207d29d0a5450c0b6"                                   #全局变量，在接口中被使用 (合约地址)
LguMetaverseEditor_ownerPrivateKey = "0xf7657dd26b5c63987c6fa586405023c694ae490c86feb44d68415df579b4219a"   #全局变量，在接口中被使用

# 加载合约ABI - LguModelMarket
abi_path_LguModelMarket = "deployed_5_server_interface/LguModelMarket.abi"
data_parser3 = DatatypeParser()
data_parser3.load_abi_file(abi_path_LguModelMarket)
LguModelMarket_abi = data_parser3.contract_abi                                                              #全局变量，在接口中被使用
LguModelMarket_address = "0xd3fbd069290118507d448d3550c07108fd390219"                                       #全局变量，在接口中被使用 (合约地址)
LguModelMarket_ownerPrivateKey = "0xf7657dd26b5c63987c6fa586405023c694ae490c86feb44d68415df579b4219a"       #全局变量，在接口中被使用

demo()
################################################
