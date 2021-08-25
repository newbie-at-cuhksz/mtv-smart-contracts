using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Nethereum.JsonRpc.UnityClient;

public class BlockNumber : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        //StartCoroutine(GetBlockNumber());
    }

    private IEnumerator GetBlockNumber()
    {
        //string url = "https://mainnet.infura.io/v3/9fe4e5215d2d43e8b756c0ab71ceb7fe";
        string url = "https://rinkeby.infura.io/v3/e9d2d0e0b2e849f6bc21d1b686f402ef";
        var blockNumberRequest = new EthBlockNumberUnityRequest(url);
        yield return blockNumberRequest.SendRequest();
        print(blockNumberRequest.Result.Value);
    }
}
