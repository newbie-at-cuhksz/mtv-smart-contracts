// SPDX-License-Identifier: MIT
pragma solidity>=0.4.24 <0.6.11;


import "./TokenValueMapping.sol";


contract LguMetaverseEditorInterface {
    function CreateLguModel(string memory _name, string memory _content) public;
}


contract LguToken is TokenValueMapping {
    
    function grantToken(address account, uint256 amount) external onlyOwner {
        _mint(account, amount);
    }
    
    function grantTokenOnHook(address account, uint256 timeSpan, uint256 valuePerTimeUnit) external onlyOwner {
        uint256 amount = timeSpan.mul(valuePerTimeUnit);
        _mint(account, amount);
    }
    
    function grantTokenOnHookOnBlockchain(address account, uint256 timeSpan, string location) external isKeyValid(location) onlyOwner {
        uint256 amount = timeSpan.mul( _tokenValueMapping[location] );
        _mint(account, amount);
    }
    
    
    // interaction with LguMetaverseEditor
    LguMetaverseEditorInterface lguMetaverseEditorInterface;
    uint256 private _createNftFee = 10;

    function GetCreateNftFee() view external returns (uint256) {
        return _createNftFee;
    }
    
    function SetNftAddr(address newAddr) external onlyOwner {
        lguMetaverseEditorInterface = LguMetaverseEditorInterface(newAddr);
    }
    
    function SetCreateNftFee(uint256 newFee) external onlyOwner {
        _createNftFee = newFee;
    }
    
    function CreateNft(string _nftName, string _nftContent) external {
        require(_createNftFee <= _balances[msg.sender]);
        
        _burn(msg.sender, _createNftFee);
        
        lguMetaverseEditorInterface.CreateLguModel(_nftName, _nftContent);
    }

}
