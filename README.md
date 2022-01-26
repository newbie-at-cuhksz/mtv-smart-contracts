# CUHKSZ Metaverse Smart Contracts

开发环境及使用的工具/插件

## 0. FISCO-BCOS区块链部署

服务器环境：**CentOS 7.6**

官方文档：

* [快速搭链](https://fisco-bcos-documentation.readthedocs.io/zh_CN/latest/docs/installation.html)
* [WeBASE中间件部署](https://webasedoc.readthedocs.io/zh_CN/latest/docs/WeBASE/install.html)



## 1. Smart Contracts

包含以下部分：

* `LguToken`: **ERC20**, 游戏内代币
* `LguMetaverseEditor`: **ERC721**, （体素）编辑器NFT
* `LguModelMarket`: 实现使用`LguToken`交易`LguMetaverseEditor` (NFT) 的功能

开发环境：

* Remix IDE: https://remix.ethereum.org/

* [Remixd](https://remix-ide.readthedocs.io/en/latest/remixd.html) command (Remix IDE 连接本地文件夹):

    ```
    remixd -s <absolute-path-to-the-shared-folder> --remix-ide https://remix.ethereum.org
    
    remixd -s <absolute-path-to-the-shared-folder> --remix-ide http://remix.ethereum.org
    ```

* Compiler

    ```
    // FISCO链
    // SPDX-License-Identifier: MIT
    pragma solidity>=0.4.24 <0.6.11;
    // 实际编译使用v0.4.25
    ```



## 2. Smart Contracts Interaction

### 2.1 Smart Contracts Interaction from Server

客户端 ==> **服务器 ==> 合约**

服务器与合约交互的接口使用以下文档/工具实现：

* [官方文档](https://fisco-bcos-documentation.readthedocs.io/zh_CN/latest/docs/sdk/python_sdk/index.html)
* 服务器环境配置见[Server_Contract_Interaction_py/README.md](Server_Contract_Interaction_py/README.md)
* Python

### 2.2 Unity Interaction with Contract (弃用)

客户端直接与合约交互

* Unity 2019.4.5f1

* [Nethereum](https://github.com/Nethereum/Nethereum) - net461dllsAOT - v3.5.0

  * Follow this [post](https://medium.com/coinmonks/part-1-using-nethereum-in-unity-54e62f7e65d5) to import Nethereum to Unity2019.4.5f1 project

  * 这个插件会与编辑器部分存档功能使用的JsonDotNet插件 ("Newtonsoft.Json.dll") 冲突，在导入插件前删除原先的JsonDotNet文件夹即可，原先的存档功能不会受到影响

    ```c#
    // 编辑器存档功能使用以下namespace
    using Newtonsoft.Json.Converters;
    using Newtonsoft.Json;
    ```

* [Infura](https://infura.io/)

* FISCO-BCOS - C# sdk: https://github.com/FISCO-BCOS/csharp-sdk

  * 该SDK基于Nethereum实现
  * 导入该仓库的`FISCOBCOS.CSharpSdk`文件夹，部分代码需注释掉以消除报错（参考[这个仓库](https://github.com/Chen-Gary/csharp-sdk)的修改）

