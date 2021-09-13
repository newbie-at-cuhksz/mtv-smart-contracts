# smart-contracts

开发环境及使用的工具/插件

## 1. Smart Contracts

* Remix IDE: https://remix.ethereum.org/

* [Remixd](https://remix-ide.readthedocs.io/en/latest/remixd.html) command (Remix IDE 连接本地文件夹):

    ```
    remixd -s <absolute-path-to-the-shared-folder> --remix-ide https://remix.ethereum.org
    ```

* Compiler

    ```
    //SPDX-License-Identifier: MIT
    pragma solidity >=0.7.0 <0.9.0;
    // 实际编译使用v0.8.4
    ```

### 已部署

1. **Deployed 1:** 

   * Rinkeby Testnet
   * **Contract Address**: 0xe9280ef5AEC4C47a2Da87539F444B7dbEfecd4C8

   * https://rinkeby.etherscan.io/address/0xe9280ef5AEC4C47a2Da87539F444B7dbEfecd4C8

   * **Owner of this contract**: 0x3F7811a90330ADf80398D2dC285F93d2A39D97d8



## 2. Unity Interaction with Contract

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
  * 导入该仓库的`FISCOBCOS.CSharpSdk`文件夹，部分代码需注释掉以消除报错

