# smart-contracts

开发环境及使用的工具/插件

## 1. Smart Contracts

包含两部分：

* ERC20 - 游戏内代币
* ERC721 - 编辑器NFT

开发环境：

* Remix IDE: https://remix.ethereum.org/

* [Remixd](https://remix-ide.readthedocs.io/en/latest/remixd.html) command (Remix IDE 连接本地文件夹):

    ```
    remixd -s <absolute-path-to-the-shared-folder> --remix-ide https://remix.ethereum.org
    
    remixd -s <absolute-path-to-the-shared-folder> --remix-ide http://remix.ethereum.org
    ```

* Compiler

    ```
    //SPDX-License-Identifier: MIT
    pragma solidity >=0.7.0 <0.9.0;
    // 实际编译使用v0.8.4
    
    // FISCO链
    // SPDX-License-Identifier: MIT
    pragma solidity>=0.4.24 <0.6.11;
    // 实际编译使用v0.4.25
    ```



## 2. Smart Contracts Interaction

### 2.1 Smart Contracts Interaction from Server

客户端 ==> **服务器 ==> 合约**

需实现服务器与合约交互的接口

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

