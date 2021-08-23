using System.Collections;
using System.Collections.Generic;
using UnityEngine;
// Nethereum
using Nethereum.Web3;
using Nethereum.ABI.FunctionEncoding.Attributes;
using Nethereum.Contracts.CQS;
using Nethereum.Util;
using Nethereum.Web3.Accounts;
using Nethereum.Hex.HexConvertors.Extensions;
using Nethereum.Contracts;
using Nethereum.Contracts.Extensions;
using System.Numerics;
using Nethereum.JsonRpc.UnityClient;
using Nethereum.ABI.Model;


public class Demo : MonoBehaviour
{



    //Deployment contract object definition
    //public partial class EIP20Deployment : EIP20DeploymentBase
    //{
    //    public EIP20Deployment() : base(BYTECODE) { }
    //    public EIP20Deployment(string byteCode) : base(byteCode) { }
    //}



    //public class EIP20DeploymentBase : ContractDeploymentMessage
    //{
    //    public static string BYTECODE = "608060405234801561001057600080fd5b506040516107843803806107848339810160409081528151602080840151838501516060860151336000908152808552959095208490556002849055908501805193959094919391019161006991600391860190610096565b506004805460ff191660ff8416179055805161008c906005906020840190610096565b5050505050610131565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106100d757805160ff1916838001178555610104565b82800160010185558215610104579182015b828111156101045782518255916020019190600101906100e9565b50610110929150610114565b5090565b61012e91905b80821115610110576000815560010161011a565b90565b610644806101406000396000f3006080604052600436106100ae5763ffffffff7c010000000000000000000000000000000000000000000000000000000060003504166306fdde0381146100b3578063095ea7b31461013d57806318160ddd1461017557806323b872dd1461019c57806327e235e3146101c6578063313ce567146101e75780635c6581651461021257806370a082311461023957806395d89b411461025a578063a9059cbb1461026f578063dd62ed3e14610293575b600080fd5b3480156100bf57600080fd5b506100c86102ba565b6040805160208082528351818301528351919283929083019185019080838360005b838110156101025781810151838201526020016100ea565b50505050905090810190601f16801561012f5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b34801561014957600080fd5b50610161600160a060020a0360043516602435610348565b604080519115158252519081900360200190f35b34801561018157600080fd5b5061018a6103ae565b60408051918252519081900360200190f35b3480156101a857600080fd5b50610161600160a060020a03600435811690602435166044356103b4565b3480156101d257600080fd5b5061018a600160a060020a03600435166104b7565b3480156101f357600080fd5b506101fc6104c9565b6040805160ff9092168252519081900360200190f35b34801561021e57600080fd5b5061018a600160a060020a03600435811690602435166104d2565b34801561024557600080fd5b5061018a600160a060020a03600435166104ef565b34801561026657600080fd5b506100c861050a565b34801561027b57600080fd5b50610161600160a060020a0360043516602435610565565b34801561029f57600080fd5b5061018a600160a060020a03600435811690602435166105ed565b6003805460408051602060026001851615610100026000190190941693909304601f810184900484028201840190925281815292918301828280156103405780601f1061031557610100808354040283529160200191610340565b820191906000526020600020905b81548152906001019060200180831161032357829003601f168201915b505050505081565b336000818152600160209081526040808320600160a060020a038716808552908352818420869055815186815291519394909390927f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925928290030190a350600192915050565b60025481565b600160a060020a03831660008181526001602090815260408083203384528252808320549383529082905281205490919083118015906103f45750828110155b15156103ff57600080fd5b600160a060020a038085166000908152602081905260408082208054870190559187168152208054849003905560001981101561046157600160a060020a03851660009081526001602090815260408083203384529091529020805484900390555b83600160a060020a031685600160a060020a03167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef856040518082815260200191505060405180910390a3506001949350505050565b60006020819052908152604090205481565b60045460ff1681565b600160209081526000928352604080842090915290825290205481565b600160a060020a031660009081526020819052604090205490565b6005805460408051602060026001851615610100026000190190941693909304601f810184900484028201840190925281815292918301828280156103405780601f1061031557610100808354040283529160200191610340565b3360009081526020819052604081205482111561058157600080fd5b3360008181526020818152604080832080548790039055600160a060020a03871680845292819020805487019055805186815290519293927fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef929181900390910190a350600192915050565b600160a060020a039182166000908152600160209081526040808320939094168252919091522054905600a165627a7a7230582084c618322109054a21a57e27075384a6172ab854e4b2c2d35062a964a6bf593f0029";

    //    public EIP20DeploymentBase() : base(BYTECODE) { }

    //    public EIP20DeploymentBase(string byteCode) : base(byteCode) { }

    //    [Parameter("uint256", "_initialAmount", 1)]

    //    public BigInteger InitialAmount { get; set; }

    //    [Parameter("string", "_tokenName", 2)]

    //    public string TokenName { get; set; }

    //    [Parameter("uint8", "_decimalUnits", 3)]

    //    public byte DecimalUnits { get; set; }

    //    [Parameter("string", "_tokenSymbol", 4)]

    //    public string TokenSymbol { get; set; }

    //}



    //[Function("transfer", "bool")]
    //public class TransferFunctionBase : FunctionMessage
    //{
    //    [Parameter("address", "_to", 1)]
    //    public string To { get; set; }
    //    [Parameter("uint256", "_value", 2)]
    //    public BigInteger Value { get; set; }
    //}



    //public partial class TransferFunction : TransferFunctionBase
    //{
    //}


    [Function("CreateLguModel")]
    public class CreateLguModelFunctionBase : FunctionMessage
    {
        [Parameter("string", "_name", 1)]
        public string Name { get; set; }
        [Parameter("uint", "_dna", 2)]
        public BigInteger Dna { get; set; }
    }

    public partial class CreateLguModelFunction : CreateLguModelFunctionBase
    {
    }



    //[Function("balanceOf", "uint256")]
    //public class BalanceOfFunction : FunctionMessage
    //{
    //    [Parameter("address", "_owner", 1)]
    //    public string Owner { get; set; }
    //}

    [Function("balanceOf", "uint256")]
    public class BalanceOfFunction : FunctionMessage
    {
        [Parameter("address", "_owner", 1)]
        public string Owner { get; set; }
    }

    [FunctionOutput]
    public class BalanceOfFunctionOutput : IFunctionOutputDTO
    {
        [Parameter("uint256", 1)]
        public int Balance { get; set; }
    }


    [Function("getModelsByOwner", "uint[]")]
    public class GetModelsByOwnerFunction : FunctionMessage
    {
        [Parameter("address", "_owner", 1)]
        public string Owner { get; set; }
    }

    [FunctionOutput]
    public class GetModelsByOwnerFunctionOutput : IFunctionOutputDTO
    {
        [Parameter("uint[]", 1)]
        public List<int> ModelIdArray { get; set; }
    }

    //[FunctionOutput]
    //public class BalanceOfFunctionOutput : IFunctionOutputDTO
    //{
    //    [Parameter("uint256", 1)]
    //    public int Balance { get; set; }
    //}

    //[Event("Transfer")]
    //public class TransferEventDTOBase : IEventDTO
    //{
    //    [Parameter("address", "_from", 1, true)]
    //    public virtual string From { get; set; }

    //    [Parameter("address", "_to", 2, true)]
    //    public virtual string To { get; set; }

    //    [Parameter("uint256", "_value", 3, false)]
    //    public virtual BigInteger Value { get; set; }
    //}

    //public partial class TransferEventDTO : TransferEventDTOBase
    //{
    //    public static EventABI GetEventABI()
    //    {
    //        return EventExtensions.GetEventABI<TransferEventDTO>();
    //    }
    //}

    [Event("NewLguModel")]
    public class NewLguModelEventDTOBase : IEventDTO
    {
        [Parameter("uint", "LguModelId", 1, false)]
        public virtual BigInteger LguModelId { get; set; }
        [Parameter("string", "name", 2, false)]
        public virtual string Name { get; set; }
        [Parameter("uint", "dna", 3, false)]
        public virtual BigInteger Dna { get; set; }
    }
    public partial class NewLguModelEventDTO : NewLguModelEventDTOBase
    {
        public static EventABI GetEventABI()
        {
            return EventExtensions.GetEventABI<NewLguModelEventDTO>();
        }
    }


    // Use this for initialization
    void Start()
    {

        StartCoroutine(DeployAndTransferToken());
    }


    //Sample of new features / requests
    public IEnumerator DeployAndTransferToken()
    {

        var url = "https://rinkeby.infura.io/v3/e9d2d0e0b2e849f6bc21d1b686f402ef";
        var privateKey = "0x622c91eb3cd1bf7a1efcc13cac20a435639be1dcf8115d1c256965765d13f4c5";
        var account = "0x3F7811a90330ADf80398D2dC285F93d2A39D97d8";
        var ContractAddress = "0xe9280ef5AEC4C47a2Da87539F444B7dbEfecd4C8";
        //initialising the transaction request sender

        //var transactionRequest = new TransactionSignedUnityRequest(url, privateKey);

        //var deployContract = new EIP20Deployment()
        //{
        //    InitialAmount = 10000,
        //    FromAddress = account,
        //    TokenName = "TST",
        //    TokenSymbol = "TST"
        //};

        ////deploy the contract
        //yield return transactionRequest.SignAndSendDeploymentContractTransaction<EIP20DeploymentBase>(deployContract);

        //if (transactionRequest.Exception != null)
        //{
        //    Debug.Log(transactionRequest.Exception.Message);
        //    yield break;
        //}

        //var transactionHash = transactionRequest.Result;
        //Debug.Log("Deployment transaction hash:" + transactionHash);

        //create a poll to get the receipt when mined
        //var transactionReceiptPolling = new TransactionReceiptPollingRequest(url);

        ////checking every 2 seconds for the receipt
        //yield return transactionReceiptPolling.PollForReceipt(transactionHash, 2);

        //var deploymentReceipt = transactionReceiptPolling.Result;

        //Debug.Log("Deployment contract address:" + deploymentReceipt.ContractAddress);




        ////Query request using our acccount and the contracts address (no parameters needed and default values)
        //var queryRequest = new QueryUnityRequest<BalanceOfFunction, BalanceOfFunctionOutput>(url, account);
        
        //yield return queryRequest.Query(new BalanceOfFunction() { Owner = account }, ContractAddress);
        
        ////Getting the dto response already decoded
        //var dtoResult = queryRequest.Result;
        //Debug.Log(dtoResult.Balance);


        // Query 2: getModelsByOwner
        var queryRequest2 = new QueryUnityRequest<GetModelsByOwnerFunction, GetModelsByOwnerFunctionOutput>(url, account);
        Debug.Log("Start BalanceOfFunction");
        yield return queryRequest2.Query(new GetModelsByOwnerFunction() { Owner = account }, ContractAddress);
        Debug.Log("End BalanceOfFunction");
        var dtoResult2 = queryRequest2.Result;
        for (int i=0; i < dtoResult2.ModelIdArray.Count; i++)
        {
            Debug.Log("ModelIdArray: " + dtoResult2.ModelIdArray[i]);
        }
        //Debug.Log(dtoResult2.ModelIdArray);


        // Transfer transaction
        Debug.Log("Transfer transaction start");
        var transactionTransferRequest = new TransactionSignedUnityRequest(url, privateKey);


        var transactionMessage = new CreateLguModelFunction
        {
            Name = "Create_From_unity_3",
            Dna = 987,
        };

        yield return transactionTransferRequest.SignAndSendTransaction(transactionMessage, ContractAddress);
        var transactionTransferHash = transactionTransferRequest.Result;

        var transactionReceiptPolling = new TransactionReceiptPollingRequest(url);
        yield return transactionReceiptPolling.PollForReceipt(transactionTransferHash, 2);
        var transferReceipt = transactionReceiptPolling.Result;
        Debug.Log("Transfer transaction finished");

        var transferEvent = transferReceipt.DecodeAllEvents<NewLguModelEventDTO>();
        Debug.Log("Transferd amount from event: " + transferEvent[0].Event.LguModelId);
        Debug.Log("Transferd amount from event: " + transferEvent[0].Event.Name);
        /////////////////////////////////////////////



        //var getLogsRequest = new EthGetLogsUnityRequest(url);
        //var eventTransfer = TransferEventDTO.GetEventABI();
        //yield return getLogsRequest.SendRequest(eventTransfer.CreateFilterInput(deploymentReceipt.ContractAddress, account));

        //var eventDecoded = getLogsRequest.Result.DecodeAllEvents<TransferEventDTO>();
        //Debug.Log("Transferd amount from get logs event: " + eventDecoded[0].Event.Value);

    }
}






















//public class StandardTokenDeployment : ContractDeploymentMessage
//{

//    public static string BYTECODE = "0x60606040526040516020806106f5833981016040528080519060200190919050505b80600160005060003373ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060005081905550806000600050819055505b506106868061006f6000396000f360606040523615610074576000357c010000000000000000000000000000000000000000000000000000000090048063095ea7b31461008157806318160ddd146100b657806323b872dd146100d957806370a0823114610117578063a9059cbb14610143578063dd62ed3e1461017857610074565b61007f5b610002565b565b005b6100a060048080359060200190919080359060200190919050506101ad565b6040518082815260200191505060405180910390f35b6100c36004805050610674565b6040518082815260200191505060405180910390f35b6101016004808035906020019091908035906020019091908035906020019091905050610281565b6040518082815260200191505060405180910390f35b61012d600480803590602001909190505061048d565b6040518082815260200191505060405180910390f35b61016260048080359060200190919080359060200190919050506104cb565b6040518082815260200191505060405180910390f35b610197600480803590602001909190803590602001909190505061060b565b6040518082815260200191505060405180910390f35b600081600260005060003373ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060005060008573ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600050819055508273ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925846040518082815260200191505060405180910390a36001905061027b565b92915050565b600081600160005060008673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600050541015801561031b575081600260005060008673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060005060003373ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000505410155b80156103275750600082115b1561047c5781600160005060008573ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828282505401925050819055508273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040518082815260200191505060405180910390a381600160005060008673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282825054039250508190555081600260005060008673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060005060003373ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828282505403925050819055506001905061048656610485565b60009050610486565b5b9392505050565b6000600160005060008373ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000505490506104c6565b919050565b600081600160005060003373ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600050541015801561050c5750600082115b156105fb5781600160005060003373ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282825054039250508190555081600160005060008573ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828282505401925050819055508273ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040518082815260200191505060405180910390a36001905061060556610604565b60009050610605565b5b92915050565b6000600260005060008473ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060005060008373ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060005054905061066e565b92915050565b60006000600050549050610683565b9056";

//    public StandardTokenDeployment() : base(BYTECODE) { }

//    [Parameter("uint256", "totalSupply")]
//    public BigInteger TotalSupply { get; set; }
//}


//[Function("balanceOf", "uint256")]
//public class BalanceOfFunction : FunctionMessage
//{
//    [Parameter("address", "_owner", 1)]
//    public string Owner { get; set; }
//}


//[Function("transfer", "bool")]
//public class TransferFunction : FunctionMessage
//{
//    [Parameter("address", "_to", 1)]
//    public string To { get; set; }

//    [Parameter("uint256", "_value", 2)]
//    public BigInteger TokenAmount { get; set; }
//}


//[Event("Transfer")]
//public class TransferEventDTO : IEventDTO
//{
//    [Parameter("address", "_from", 1, true)]
//    public string From { get; set; }

//    [Parameter("address", "_to", 2, true)]
//    public string To { get; set; }

//    [Parameter("uint256", "_value", 3, false)]
//    public BigInteger Value { get; set; }
//}


//public class Demo : MonoBehaviour
//{
//    private void Start()
//    {
//        //var url = "http://testchain.nethereum.com:8545";
//        var url = "https://rinkeby.infura.io/v3/e9d2d0e0b2e849f6bc21d1b686f402ef";
//        var privateKey = "622c91eb3cd1bf7a1efcc13cac20a435639be1dcf8115d1c256965765d13f4c5";
//        var account = new Account(privateKey);
//        var web3 = new Web3(account, url);


//        //var deploymentMessage = new StandardTokenDeployment
//        //{
//        //    TotalSupply = 100000
//        //};

//        //var deploymentHandler = web3.Eth.GetContractDeploymentHandler<StandardTokenDeployment>();
//        //var transactionReceipt = await deploymentHandler.SendRequestAndWaitForReceiptAsync(deploymentMessage);
//        //var contractAddress = transactionReceipt.ContractAddress;
//    }
//}
