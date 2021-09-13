using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using FISCOBCOS.CSharpSdk.Core;
using FISCOBCOS.CSharpSdk;
using FISCOBCOS.CSharpSdk.Dto;
using FISCOBCOS.CSharpSdk.Utis;
using Nethereum.Hex.HexConvertors.Extensions;
using Nethereum.Util;
using FISCOBCOS.CSharpSdk.Utils;
using System;
//using System.Globalization;




public class FiscoTest : MonoBehaviour
{
    public string privateKey = "";
    string binCode = "";
    string abi = "";


    private void Start()
    {
        // init
        this.privateKey = "0x3a6bf2c49579ac5f35691a686c47c8ae564a7a25f41bcda9196d5c84ef67cda0";
        bool getAbiState = FileUtils.ReadFile("D:\\repo_Chen-Gary\\csharp-sdk\\Src\\FISCOBCOS.CSharpSdk.Test\\TestData\\HelloWorld.abi", out abi);
        bool getBinCodeState = FileUtils.ReadFile("D:\\repo_Chen-Gary\\csharp-sdk\\Src\\FISCOBCOS.CSharpSdk.Test\\TestData\\HelloWorld.bin", out binCode);

        //Debug.Log(binCode);
        //Debug.Log(abi);

        //CallRequestTest();
        //Debug.Log("SendTranscationWithReceiptDecodeTest");
        //SendTranscationWithReceiptDecodeTest();
        //CallRequestTest();
        //DeployContractTest();
        //GetBlockNumberTest();
        //GeneratorAccountTest();

    }

    
    private void GeneratorAccountTest()
    {
        var account = AccountUtils.GeneratorAccount("adminUser");
        var accountString = account.ToJson();
        Debug.Log(accountString);
    }


    private void GetBlockNumberTest()
    {
        //BaseService baseService = new BaseService("http://120.78.207.251:8645", 1, 1, 3);
        //BaseService baseService = new BaseService("http://120.78.207.251:8545", 1);
        BaseService baseService = new BaseService(BaseConfig.DefaultUrl, 1);
        //BaseService baseService = new BaseService("http://49.235.72.8:8545", 1, 1, 2);

        var blockNum = baseService.GetBlockNumber();

        Debug.Log("blockNum = " + blockNum);
    }

    public void DeployContractTest()
    {
        string abi2 = "";
        string binCode2 = "";
        bool getAbiState = FileUtils.ReadFile("D:\\repo_Chen-Gary\\csharp-sdk\\Src\\FISCOBCOS.CSharpSdk.Test\\TestData\\DefaultTest.abi", out abi2);
        bool getBinCodeState = FileUtils.ReadFile("D:\\repo_Chen-Gary\\csharp-sdk\\Src\\FISCOBCOS.CSharpSdk.Test\\TestData\\DefaultTest.bin", out binCode2);

        var contractService = new ContractService(BaseConfig.DefaultUrl, BaseConfig.DefaultRpcId, BaseConfig.DefaultChainId, BaseConfig.DefaultGroupId, privateKey);
        var txHash = contractService.DeployContract(binCode2, abi2);

        Debug.Log(txHash);
    }

    public void CallRequestTest()
    {
        var contractService = new ContractService(BaseConfig.DefaultUrl, BaseConfig.DefaultRpcId, BaseConfig.DefaultChainId, BaseConfig.DefaultGroupId, privateKey);
        string contractAddress = "0x54c721bdaa99fb3b47b18498da7c373e37e2327d";
        string functionName = "get";
        var result = contractService.CallRequest(contractAddress, abi, functionName);
        var solidityAbi = new SolidityABI(abi);
        var outputList = solidityAbi.OutputDecode(functionName, result.Output);

        Debug.Log(outputList[0].Result.ToString());
    }


    public void SendTranscationWithReceiptDecodeTest()
    {
        var contractService = new ContractService(BaseConfig.DefaultUrl, BaseConfig.DefaultRpcId, BaseConfig.DefaultChainId, BaseConfig.DefaultGroupId, privateKey);
        string contractAddress = "0x54c721bdaa99fb3b47b18498da7c373e37e2327d";
        var inputsParameters = new[] { BuildParams.CreateParam("string", "n") };
        var paramsValue = new object[] { "Hello, 20210911, 你好" };
        string functionName = "set";//调用合约方法
        ReceiptResultDto receiptResultDto = contractService.SendTranscationWithReceipt(abi, contractAddress, functionName, inputsParameters, paramsValue);

        var solidityAbi = new SolidityABI(abi);
        var inputList = solidityAbi.InputDecode(functionName, receiptResultDto.Input);

    }
}
