// SPDX-License-Identifier: MIT
pragma solidity>=0.4.24 <0.6.11;

// ref: https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol


import "./Safemath.sol";
import "./ERC721Base";


contract LguMetaverseEditor is ERC721Base {
    
    using SafeMath for uint256;

    event NewLguModel(uint LguModelId, string name, string content);

    struct LguModel {
        string name;
        string content;      // MD5 hash of model
    }
    
    LguModel[] public LguModels;


    // interaction with LguToken (ERC20)
    address _lguTokenContractAddr;     // ERC20
    
    function SetLguTokenContractAddr(address newAddr) external onlyOwner {
        _lguTokenContractAddr = newAddr;
    }

    function CreateLguModel(address _creator, string memory _name, string memory _content) public {
        require(
            msg.sender == owner() ||
            msg.sender == _lguTokenContractAddr
        );
        
        LguModels.push( LguModel(_name, _content) );
        uint id = LguModels.length - 1;

        _mint(_creator, id);

        emit NewLguModel(id, _name, _content);
    }
    
    
    modifier onlyOwnerOfModel(uint _modelId){
        require(msg.sender == ownerOf(_modelId));
        _;
    }

    
    function changeName(uint _modelId, string _newName) external onlyOwnerOfModel(_modelId) {
        LguModels[_modelId].name = _newName;
    }
    
    function getModelsByOwner(address _owner) external view returns(uint[] memory) {
        uint[] memory result = new uint[](balanceOf(_owner));
        uint counter = 0;
        for (uint i = 0; i < LguModels.length; i++) {
            if (ownerOf(i) == _owner) {
                result[counter] = i;
                counter++;
            }
        }
        return result;
    }

}
