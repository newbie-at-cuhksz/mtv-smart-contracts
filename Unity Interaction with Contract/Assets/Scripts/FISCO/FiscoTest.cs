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

        /*
         * Test Account:
         * 
         ** "address":"0xa8eea568452bd79502839fde0675347b47a54913",
         *  "publicKey":"0xa3ecb8b83cf8e81de7c4c81b21039a6268de7bfe4b08551c323b501573be2eae1d63ecc73cd084666cf18072dde7b9b371343547f14e6262b4ad377a82b64c35",
         ** "privateKey":"721ea4a6ee1bff772ae0de6af6bb499eb44ea97ae11f7c55d3c1450b4ffbd246",
         *  "userName":"admin_20210913",
         *  "type":0
         */

        this.privateKey = "0x721ea4a6ee1bff772ae0de6af6bb499eb44ea97ae11f7c55d3c1450b4ffbd246";     // need to add "0x" before privateKey
        // init: read binCode and ABI
        bool getAbiState = FileUtils.ReadFile("..\\Smart_Contract_Project\\deployed_FISCO_BCOS\\deployed_1_hello_world_v1\\HelloWorld.abi", out abi);
        bool getBinCodeState = FileUtils.ReadFile("..\\Smart_Contract_Project\\deployed_FISCO_BCOS\\deployed_1_hello_world_v1\\HelloWorld.bin", out binCode);


        //Debug.Log(binCode);
        //Debug.Log(abi);
    }

    
    public void GeneratorAccountTest()
    {
        var account = AccountUtils.GeneratorAccount("admin_20210913");
        var accountString = account.ToJson();
        Debug.Log(accountString);
    }


    public void GetBlockNumberTest()
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
        var contractService = new ContractService(BaseConfig.DefaultUrl, BaseConfig.DefaultRpcId, BaseConfig.DefaultChainId, BaseConfig.DefaultGroupId, privateKey);
        var txHash = contractService.DeployContract(binCode, abi);

        Debug.Log(txHash);
    }


    public void CallRequestTest()
    {
        var contractService = new ContractService(BaseConfig.DefaultUrl, BaseConfig.DefaultRpcId, BaseConfig.DefaultChainId, BaseConfig.DefaultGroupId, privateKey);
        string contractAddress = "0x60b364cab35c19678c6fa3d4a6cdf705a2adea89";
        string functionName = "get";
        var result = contractService.CallRequest(contractAddress, abi, functionName);
        var solidityAbi = new SolidityABI(abi);
        var outputList = solidityAbi.OutputDecode(functionName, result.Output);

        Debug.Log(outputList[0].Result.ToString());
    }


    public void SendTranscationWithReceiptDecodeTest(string _setToStr)
    {
        var contractService = new ContractService(BaseConfig.DefaultUrl, BaseConfig.DefaultRpcId, BaseConfig.DefaultChainId, BaseConfig.DefaultGroupId, privateKey);
        string contractAddress = "0x60b364cab35c19678c6fa3d4a6cdf705a2adea89";
        var inputsParameters = new[] { BuildParams.CreateParam("string", "n") };
        var paramsValue = new object[] { _setToStr };
        string functionName = "set";//调用合约方法
        ReceiptResultDto receiptResultDto = contractService.SendTranscationWithReceipt(abi, contractAddress, functionName, inputsParameters, paramsValue);

        var solidityAbi = new SolidityABI(abi);
        var inputList = solidityAbi.InputDecode(functionName, receiptResultDto.Input);

    }
}
