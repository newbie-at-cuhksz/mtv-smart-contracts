﻿using Nethereum.ABI.FunctionEncoding.Attributes;
using System;
using System.Collections.Generic;
using System.Text;

namespace FISCOBCOS.CSharpSdk.Dto
{

    public class SignatureListItemDto
    {
        /// <summary>
        /// 
        /// </summary>
        [Parameter("index")]
        public string Index { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("signature")]
        public string Signature { get; set; }
    }

    public class SignatureDto
    {
        /// <summary>
        /// 
        /// </summary>
          [Parameter("r")]
        public string R{ get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("s")]
        public string S { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("signature")]
        public string Signature { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("v")]
        public string V { get; set; }
    }

    public class TransactionsItemDto
    {
        /// <summary>
        /// 
        /// </summary>
        [Parameter("blockHash")]
        public string BlockHash { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("blockLimit")]
        public string BlockLimit { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("blockNumber")]
        public string BlockNumber { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("chainId")]
        public string ChainId { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("extraData")]
        public string ExtraData { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("from")]
        public string From { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("gas")]
        public string Gas { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("gasPrice")]
        public string GasPrice { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("groupId")]
        public string GroupId { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("hash")]
        public string Hash { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("input")]
        public string Input { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("nonce")]
        public string Nonce { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("signature")]
        public SignatureDto Signature { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("string", "to")]
        public string To { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("string", "transactionIndex")]
        public string TransactionIndex { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("string", "value")]
        public string Value { get; set; }
    }

    public class BlockByNumberDto
    {
        /// <summary>
        /// 
        /// </summary>
        [Parameter("string", "dbHash")]
        public string DbHash { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("string[]", "extraData")]
        public List<string> ExtraData { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("string", "gasLimit")]
        public string GasLimit { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("string", "gasUsed")]
        public string GasUsed { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("string", "hash")]
        public string Hash { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("string", "logsBloom")]
        public string LogsBloom { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("string", "number")]
        public string Number { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("string", "parentHash")]
        public string ParentHash { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("string", "receiptsRoot")]
        public string ReceiptsRoot { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("string", "sealer")]
        public string Sealer { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("sealerList")]
        public List<string> SealerList { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("signatureList")]
        public List<SignatureListItemDto> SignatureList { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("string", "stateRoot")]
        public string StateRoot { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("string", "timestamp")]
        public string Timestamp { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("transactions")]
        public List<TransactionsItemDto> Transactions { get; set; }
        /// <summary>
        /// 
        /// </summary>
        [Parameter("string", "transactionsRoot")]
        public string TransactionsRoot { get; set; }
    }
}
