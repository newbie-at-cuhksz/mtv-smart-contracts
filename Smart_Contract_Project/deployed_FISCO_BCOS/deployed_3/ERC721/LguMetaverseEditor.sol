// SPDX-License-Identifier: MIT
pragma solidity>=0.4.24 <0.6.11;


import "./ownable.sol";
import "./safemath.sol";
import "./erc721.sol";


contract LguMetaverseEditor is Ownable, ERC721 {
    
    using SafeMath for uint256;
    using SafeMath32 for uint32;
    using SafeMath16 for uint16;
    
    event NewLguModel(uint LguModelId, string name, string content);
    

    struct LguModel {
        string name;
        string content;
    }
    
    LguModel[] public LguModels;
    
    mapping (uint => address) public LguModelToOwner;
    mapping (address => uint) ownerLguModelCount;
    
    
    function CreateLguModel(string memory _name, string memory _content) public onlyOwner {
        LguModels.push( LguModel(_name, _content) );
        uint id = LguModels.length - 1;
        LguModelToOwner[id] = msg.sender;
        ownerLguModelCount[msg.sender] = ownerLguModelCount[msg.sender].add(1);
        emit NewLguModel(id, _name, _content);
    }
    
    

    modifier onlyOwnerOfModel(uint _modelId){
        require(msg.sender == LguModelToOwner[_modelId]);
        _;
    }
    
    
    // function withdraw() external onlyOwner {
    //     //address payable _owner = payable(address(uint160(owner())));
    //     address _owner = owner();
    //     _owner.transfer(address(this).balance);
    // }
    
    function changeName(uint _modelId, string _newName) external onlyOwnerOfModel(_modelId) {
        LguModels[_modelId].name = _newName;
    }
    
    function getModelsByOwner(address _owner) external view returns(uint[] memory) {
        uint[] memory result = new uint[](ownerLguModelCount[_owner]);
        uint counter = 0;
        for (uint i = 0; i < LguModels.length; i++) {
            if (LguModelToOwner[i] == _owner) {
                result[counter] = i;
                counter++;
            }
        }
        return result;
    }
    
    
    // ERC721 implements
    mapping (uint => address) modelApprovals;
    
    function balanceOf(address _owner) external view returns (uint256) {
        return ownerLguModelCount[_owner];
    }
    
    function ownerOf(uint256 _tokenId) external view returns (address) {
        return LguModelToOwner[_tokenId];
    }
    
    function _transfer(address _from, address _to, uint256 _tokenId) private {
        ownerLguModelCount[_to] = ownerLguModelCount[_to].add(1);
        ownerLguModelCount[msg.sender] = ownerLguModelCount[msg.sender].sub(1);
        LguModelToOwner[_tokenId] = _to;
        emit Transfer(_from, _to, _tokenId);
    }
    
    function transferFrom(address _from, address _to, uint256 _tokenId) external payable {
        require ( LguModelToOwner[_tokenId] == msg.sender || modelApprovals[_tokenId] == msg.sender );
        _transfer(_from, _to, _tokenId);
    }
    
    function approve(address _approved, uint256 _tokenId) external payable onlyOwnerOfModel(_tokenId) {
        modelApprovals[_tokenId] = _approved;
        emit Approval(msg.sender, _approved, _tokenId);
    }
}

