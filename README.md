## Smart Contract Project

Remix IDE: https://remix.ethereum.org/

Remixd command:

```
remixd -s <absolute-path-to-the-shared-folder> --remix-ide https://remix.ethereum.org

remixd -s D:\repo_Chen-Gary\lgu-metaverse-nft --remix-ide https://remix.ethereum.org

remixd -s D:\repo_Chen-Gary\lgu-metaverse-nft\Smart_Contract_Project\contracts --remix-ide https://remix.ethereum.org
```



```
//SPDX-License-Identifier: MIT
pragma solidity >=0.7.0 <0.9.0;
```

**Contract Address** (Rinkeby Testnet): 0xe9280ef5AEC4C47a2Da87539F444B7dbEfecd4C8

https://rinkeby.etherscan.io/address/0xe9280ef5AEC4C47a2Da87539F444B7dbEfecd4C8

**Owner of this contract**: 0x3F7811a90330ADf80398D2dC285F93d2A39D97d8



## Unity Interaction with Contract

* Unity 2019.4.5f1

* [Nethereum](https://github.com/Nethereum/Nethereum) - net461dllsAOT - v3.5.0

  (Follow this [post](https://medium.com/coinmonks/part-1-using-nethereum-in-unity-54e62f7e65d5) to import Nethereum to Unity2019.4.5f1 project)

* [Infura](https://infura.io/)













---

SCRIPTS

The 'scripts' folder contains example async/await scripts for deploying the 'Storage' contract.
For the deployment of any other contract, 'contractName' and 'constructorArgs' should be updated (along with other code if required). 
Scripts have full access to the web3.js and ethers.js libraries.

To run a script, right click on file name in the file explorer and click 'Run'. Remember, Solidity file must already be compiled.

Output from script will appear in remix terminal.
