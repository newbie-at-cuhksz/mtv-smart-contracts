// SPDX-License-Identifier: MIT
pragma solidity>=0.4.24 <0.6.11;


import "./TokenValueMapping.sol";


contract LguMetaverseEditorInterface {
    function CreateLguModel(address _creator, string memory _name, string memory _content) public;
}


contract LguToken is TokenValueMapping {
    
    // Remove in latter version
    function grantTokenDirectly1(address account, uint256 amount) external onlyOwner {
        _mint(account, amount);
    }
    
    // Remove in latter version
    function grantTokenDirectly2(address account, uint256 timeSpan, uint256 valuePerTimeUnit) external onlyOwner {
        uint256 amount = timeSpan.mul(valuePerTimeUnit);
        _mint(account, amount);
    }
    
    // in "TokenValueMapping",
    // function grantTokenOnHookOnBlockchain(address account, uint256 timeSpan, string location) external isRegionNameValid(location) onlyOwner;
    
    // Remove in latter version
    function spendTokenDirectly(uint256 amount) external {
        _burn(msg.sender, amount);
    }
    
    
    // interaction with LguMetaverseEditor
    LguMetaverseEditorInterface lguMetaverseEditorInterface;
    uint256 private _createNftFee = 10;

    function GetCreateNftFee() view external returns (uint256) {
        return _createNftFee;
    }
    
    function SetCreateNftFee(uint256 newFee) external onlyOwner {
        _createNftFee = newFee;
    }
    
    function SetNftAddr(address newAddr) external onlyOwner {
        lguMetaverseEditorInterface = LguMetaverseEditorInterface(newAddr);
    }
    
    function CreateNft(string _nftName, string _nftContent) external {
        _burn(msg.sender, _createNftFee);
        
        lguMetaverseEditorInterface.CreateLguModel(msg.sender, _nftName, _nftContent);
    }

}
