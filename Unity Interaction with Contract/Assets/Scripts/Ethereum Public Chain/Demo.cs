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
    /*
     * Sample ERC20 transfer
     */

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



    /*
     * contract LguMetaverseBase
     * function CreateLguModel(string memory _name, uint _dna) public
     */
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


    /*
     * Sample ERC20 balanceOf
     */

    //[Function("balanceOf", "uint256")]
    //public class BalanceOfFunction : FunctionMessage
    //{
    //    [Parameter("address", "_owner", 1)]
    //    public string Owner { get; set; }
    //}
    //[FunctionOutput]
    //public class BalanceOfFunctionOutput : IFunctionOutputDTO
    //{
    //    [Parameter("uint256", 1)]
    //    public int Balance { get; set; }
    //}


    /*
     * contract LguMetaverseBase (ERC721)
     * function balanceOf(address _owner) override external view returns (uint256)
     */
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


    /*
     * contract LguMetaverseBase (ERC721)
     * function getModelsByOwner(address _owner) external view returns(uint[] memory)
     */
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





    /*
     * contract LguMetaverseBase
     * event NewLguModel(uint LguModelId, string name, uint dna);
     */

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



    /*
     * contract LguMetaverseBase
     * function transferFrom(address _from, address _to, uint256 _tokenId) override external payable
     */
    [Function("transferFrom")]
    public class TransferFromFunctionBase : FunctionMessage
    {
        [Parameter("address", "_from", 1)]
        public string From { get; set; }
        [Parameter("address", "_to", 2)]
        public string To { get; set; }
        [Parameter("uint256", "_tokenId", 3)]
        public BigInteger TokenId { get; set; }
    }
    public partial class TransferFromFunction : TransferFromFunctionBase
    {
    }

    [Event("Transfer")]
    public class TransferFromEventDTOBase : IEventDTO
    {
        [Parameter("address", "_from", 1, true)]
        public virtual string From { get; set; }
        [Parameter("address", "_to", 2, true)]
        public virtual string To { get; set; }

        [Parameter("uint256", "_tokenId", 3, true)]
        public virtual BigInteger TokenId { get; set; }
    }
    public partial class TransferFromEventDTO : TransferFromEventDTOBase
    {
        public static EventABI GetEventABI()
        {
            return EventExtensions.GetEventABI<TransferFromEventDTO>();
        }
    }






    string url = "https://rinkeby.infura.io/v3/e9d2d0e0b2e849f6bc21d1b686f402ef";
    //string privateKey = "0x622c91eb3cd1bf7a1efcc13cac20a435639be1dcf8115d1c256965765d13f4c5";
    //string account = "0x3F7811a90330ADf80398D2dC285F93d2A39D97d8";                    // public key OR address of the account
    string ContractAddress = "0xe9280ef5AEC4C47a2Da87539F444B7dbEfecd4C8";


    //Sample of new features / requests
    public IEnumerator Query_getModelsByOwner(string _account)
    {
        // Query sample
        //var queryRequest = new QueryUnityRequest<BalanceOfFunction, BalanceOfFunctionOutput>(url, account);
        //yield return queryRequest.Query(new BalanceOfFunction() { Owner = account }, ContractAddress);
        ////Getting the dto response already decoded
        //var dtoResult = queryRequest.Result;
        //Debug.Log(dtoResult.Balance);



        // Query 2: getModelsByOwner
        //Query request using our acccount and the contracts address (no parameters needed and default values)
        Debug.Log("Start: GetModelsByOwnerFunction");

        var queryRequest2 = new QueryUnityRequest<GetModelsByOwnerFunction, GetModelsByOwnerFunctionOutput>(url, _account);
        yield return queryRequest2.Query(new GetModelsByOwnerFunction() { Owner = _account }, ContractAddress);
        
        Debug.Log("Finish: GetModelsByOwnerFunction");

        Debug.Log("Report model id owned by this account: " + _account);
        string reportMsg = "ModelIdArray: ";

        var dtoResult2 = queryRequest2.Result;
        for (int i=0; i < dtoResult2.ModelIdArray.Count; i++)
        {
            reportMsg = reportMsg + dtoResult2.ModelIdArray[i] + ", ";
        }
        Debug.Log(reportMsg);
    }

    
    public IEnumerator Transaction_CreateLguModel(string _privateKey, string _name, int _dna)
    {
        // Transfer transaction
        Debug.Log("Start: CreateLguModelFunction");
        var transactionTransferRequest = new TransactionSignedUnityRequest(url, _privateKey);

        var transactionMessage = new CreateLguModelFunction
        {
            Name = _name,
            Dna = _dna,
        };

        yield return transactionTransferRequest.SignAndSendTransaction(transactionMessage, ContractAddress);
        var transactionTransferHash = transactionTransferRequest.Result;

        var transactionReceiptPolling = new TransactionReceiptPollingRequest(url);
        yield return transactionReceiptPolling.PollForReceipt(transactionTransferHash, 2);
        var transferReceipt = transactionReceiptPolling.Result;

        var transferEvent = transferReceipt.DecodeAllEvents<NewLguModelEventDTO>();
        Debug.Log("CreateLguModel from event: " + transferEvent[0].Event.LguModelId);
        Debug.Log("CreateLguModel from event: " + transferEvent[0].Event.Name);
        Debug.Log("CreateLguModel from event: " + transferEvent[0].Event.Dna);

        Debug.Log("Finish: CreateLguModelFunction");
    }

    public IEnumerator Transaction_TransferFrom(string _privateKey, string _from, string _to, BigInteger _tokenId)
    {
        // Transfer transaction
        Debug.Log("Start: TransferFromFunction");
        var transactionTransferRequest = new TransactionSignedUnityRequest(url, _privateKey);

        var transactionMessage = new TransferFromFunction
        {
            From = _from,
            To = _to,
            TokenId = _tokenId,
        };

        yield return transactionTransferRequest.SignAndSendTransaction(transactionMessage, ContractAddress);
        var transactionTransferHash = transactionTransferRequest.Result;

        var transactionReceiptPolling = new TransactionReceiptPollingRequest(url);
        yield return transactionReceiptPolling.PollForReceipt(transactionTransferHash, 2);
        var transferReceipt = transactionReceiptPolling.Result;

        var transferEvent = transferReceipt.DecodeAllEvents<TransferFromEventDTO>();
        Debug.Log("TransferFromEventDTO from event: " + transferEvent[0].Event.TokenId);
        

        Debug.Log("Finish: TransferFromFunction");
    }

    public void OnClickGetModelsByOwner(string _account)
    {
        StartCoroutine(Query_getModelsByOwner(_account));
    }

    public void OnClickCreateLguModel(string _privateKey, string _name, int _dna)
    {
        StartCoroutine(Transaction_CreateLguModel(_privateKey, _name, _dna));
    }

    public void OnClickTransferFrom(int _tokenId)
    {
        string privateKey = "0x622c91eb3cd1bf7a1efcc13cac20a435639be1dcf8115d1c256965765d13f4c5";
        string from = "0x3F7811a90330ADf80398D2dC285F93d2A39D97d8";
        string to =   "0xd268bc736A187b4E59EdA5e787d0f1a61A97a1fF";

        StartCoroutine(Transaction_TransferFrom(privateKey, from, to, _tokenId));
    }
}
