// SPDX-License-Identifier: MIT
pragma solidity>=0.4.24 <0.6.11;

import "./LguTokenERC20Base.sol";

contract TokenValueMapping is LguTokenERC20Base {
    mapping (string => uint256) internal _tokenValueMapping;
    string[] private LocationSet;
    
    constructor() internal {
        // init
        _tokenValueMapping ["TA"] = 1;
        _tokenValueMapping ["TB"] = 1;
        _tokenValueMapping ["TC"] = 1;
        _tokenValueMapping ["TD"] = 1;
        _tokenValueMapping ["University Library"] = 1;
        _tokenValueMapping ["Harmonia"] = 1;
        _tokenValueMapping ["Muse"] = 1;
        _tokenValueMapping ["Diligentia"] = 1;
        _tokenValueMapping ["Shaw"] = 1;
        
        LocationSet.push("TA");
        LocationSet.push("TB");
        LocationSet.push("TC");
        LocationSet.push("TD");
        LocationSet.push("University Library");
        LocationSet.push("Harmonia");
        LocationSet.push("Muse");
        LocationSet.push("Diligentia");
        LocationSet.push("Shaw");
    }
    
    modifier isKeyValid(string key) {         // is this modifier works??? NO...
        for (uint i = 0; i < LocationSet.length; i++) {
            if (keccak256(abi.encodePacked(key)) == keccak256(abi.encodePacked( LocationSet[i] ))) {
                _;
            }
        }
    }
    
    modifier isKeyInvalid(string key) {         // is this modifier works??? NO...
        for (uint i = 0; i < LocationSet.length; i++) {
            if (keccak256(abi.encodePacked(key)) == keccak256(abi.encodePacked( LocationSet[i] ))) {
                require(false);
            }
        }
        _;
    }
    
    function SetTokenValueMapping(string key, uint256 value) external isKeyValid(key) onlyOwner {
        _tokenValueMapping[key] = value;
    }
    
    function AddLocation(string key, uint256 value) external isKeyInvalid(key) onlyOwner {
        _tokenValueMapping [key] = value;
    }
}
