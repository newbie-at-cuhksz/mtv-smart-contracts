# HelloWorld.sol

A single file contract provided by FISCO BCOS console

## 1. Info

* Contract Address: 0x60b364cab35c19678c6fa3d4a6cdf705a2adea89
* Owner: 0xa8eea568452bd79502839fde0675347b47a54913

## 2. Process

* Compile in Remix IDE (get Bytecode and ABI) using compiler version **0.4.24**

* Deployed in C#

  ```c#
  public void DeployContractTest()
  {
      // init: read binCode and ABI
      bool getAbiState = FileUtils.ReadFile("..\\Smart_Contract_Project\\deployed_FISCO_BCOS\\deployed_1_hello_world_v1\\HelloWorld.abi", out abi);
      bool getBinCodeState = FileUtils.ReadFile("..\\Smart_Contract_Project\\deployed_FISCO_BCOS\\deployed_1_hello_world_v1\\HelloWorld.bin", out binCode);
  
      var contractService = new ContractService(BaseConfig.DefaultUrl, BaseConfig.DefaultRpcId, BaseConfig.DefaultChainId, BaseConfig.DefaultGroupId, privateKey);
      var txHash = contractService.DeployContract(binCode, abi);
  
      Debug.Log(txHash);
  }
  ```

  

---

我同时也尝试并通过以下方式编译/部署合约：

* 使用FISCO BCOS console编译（得到Bytecode 和 ABI）
* 使用FISCO BCOS console部署合约

以上方式皆通过编译、部署、合约交互测试

