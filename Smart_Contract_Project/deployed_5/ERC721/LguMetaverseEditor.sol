// SPDX-License-Identifier: MIT
pragma solidity>=0.4.24 <0.6.11;

// ref: https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol

//import "./Ownable.sol";
import "./Safemath.sol";
//import "./IERC721.sol";


contract LguMetaverseEditor is ERC721Base {
    
    using SafeMath for uint256;

    event NewLguModel(uint LguModelId, string name, string content);

    struct LguModel {
        string name;
        string content;      // MD5 hash of model
    }
    
    LguModel[] public LguModels;
    
    mapping (uint => address) public LguModelToOwner;
    mapping (address => uint) ownerLguModelCount;
    

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
        LguModelToOwner[id] = _creator;
        ownerLguModelCount[_creator] = ownerLguModelCount[_creator].add(1);
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
    mapping (uint => address) _modelApprovals;
    
    // Mapping from owner to operator approvals
    mapping(address => mapping(address => bool)) private _operatorApprovals;
    
    function balanceOf(address _owner) external view returns (uint256) {
        return ownerLguModelCount[_owner];
    }
    
    function ownerOf(uint256 _tokenId) public view returns (address) {
        return LguModelToOwner[_tokenId];
    }
    
    function _transfer(address _from, address _to, uint256 _tokenId) private {
        ownerLguModelCount[_to] = ownerLguModelCount[_to].add(1);
        ownerLguModelCount[msg.sender] = ownerLguModelCount[msg.sender].sub(1);
        LguModelToOwner[_tokenId] = _to;
        emit Transfer(_from, _to, _tokenId);
    }
    
    function transferFrom(address _from, address _to, uint256 _tokenId) external {
        require ( _isApprovedOrOwner(msg.sender, _tokenId), "ERC721: transfer caller is not owner nor approved" );
        
        _transfer(_from, _to, _tokenId);
    }
    
    // function safeTransferFrom(address _from, address _to, uint256 _tokenId) public {
    //     safeTransferFrom(_from, _to, _tokenId, "");
    // }
    
    // function safeTransferFrom(address _from, address _to, uint256 _tokenId, bytes data) external payable {
    //     require(_isApprovedOrOwner(msg.sender, _tokenId), "ERC721: transfer caller is not owner nor approved");
    //     _safeTransfer(_from, _to, _tokenId, data);
    // }
    
    // function _safeTransfer(address from, address to, uint256 tokenId, bytes memory _data) internal {
    //     _transfer(from, to, tokenId);
    //     require(_checkOnERC721Received(from, to, tokenId, _data), "ERC721: transfer to non ERC721Receiver implementer"); // _checkOnERC721Received() not implemented
    // }
    

    function _approve (address _to, uint256 _tokenId) internal {
        _modelApprovals[_tokenId] = _to;
        emit Approval(msg.sender, _to, _tokenId);
    }
    
    function approve(address to, uint256 tokenId) external {
        address owner = ownerOf(tokenId);
        require(to != owner, "ERC721: approval to current owner");
        
        require(
            msg.sender == owner || isApprovedForAll(owner, msg.sender),
            "ERC721: approve caller is not owner nor approved for all"
        );
        
        _approve(to, tokenId);
    }
    
    function getApproved(uint256 tokenId) public view returns (address) {
        require(_exists(tokenId), "ERC721: approved query for nonexistent token");

        return _modelApprovals[tokenId];
    }
    
    function setApprovalForAll(address operator, bool approved) public {
        require(operator != msg.sender, "ERC721: approve to caller");

        _operatorApprovals[msg.sender][operator] = approved;
        emit ApprovalForAll(msg.sender, operator, approved);
    }
    
    function isApprovedForAll(address owner, address operator) public view returns (bool) {
        return _operatorApprovals[owner][operator];
    }
    


    function _exists(uint256 tokenId) internal view returns (bool) {
        return LguModelToOwner[tokenId] != address(0);
    }
    
    function _isApprovedOrOwner(address spender, uint256 tokenId) internal view returns (bool) {
        require(_exists(tokenId), "ERC721: operator query for nonexistent token");
        address owner = ownerOf(tokenId);
        return (spender == owner || getApproved(tokenId) == spender || isApprovedForAll(owner, spender));
    }
}
