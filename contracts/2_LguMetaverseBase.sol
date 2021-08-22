// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0 <0.9.0;

import "./1_ownable.sol";
import "./safemath.sol";

contract LguMetaverseBase is Ownable {
    
    using SafeMath for uint256;
    using SafeMath32 for uint32;
    using SafeMath16 for uint16;
    
    event NewLguModel(uint LguModelId, string name, uint dna);
    
    //uint dnaDigits = 16;
    //uint dnaModulus = 10 ** dnaDigits;
    //uint cooldownTime = 1 days;
    
    struct LguModel {
        string name;
        uint dna;
    }
    
    LguModel[] public LguModels;
    
    mapping (uint => address) public LguModelToOwner;
    mapping (address => uint) ownerLguModelCount;
    
    
    // This function should be "internal"
    function CreateLguModel(string memory _name, uint _dna) public {
        LguModels.push( LguModel(_name, _dna) );
        uint id = LguModels.length - 1;
        LguModelToOwner[id] = msg.sender;
        ownerLguModelCount[msg.sender] = ownerLguModelCount[msg.sender].add(1);
        emit NewLguModel(id, _name, _dna);
    }
    
    // function _generateRandomDna(string memory _str) private view returns (uint);
    // function createRandomZombie(string memory _name) public;
}
