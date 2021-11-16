// SPDX-License-Identifier: MIT
pragma solidity>=0.4.24 <0.6.11;

import "./LguTokenERC20Base.sol";

contract TokenValueMapping is LguTokenERC20Base {
    
    struct RegionInfo {
        string name;
        uint256 base;
        uint256 weight;
    }
    
    uint256 totalBonus = 200;
    
    RegionInfo[] private _regions;

    
    constructor() internal {
        _regions.push( RegionInfo("University Library", 20, 100) );
        _regions.push( RegionInfo("TA", 15, 100) );
        _regions.push( RegionInfo("Shaw", 10, 100) );
        _regions.push( RegionInfo("Gym", 20, 100) );
    }
    
    modifier isRegionNameValid(string regionName) {         // is this modifier works??? 
        bool tmp = false;
        for (uint i = 0; i < _regions.length; i++) {
            if (keccak256(abi.encodePacked(regionName)) == keccak256(abi.encodePacked( _regions[i].name ))) {
                tmp = true;
                break;
            }
        }
        
        require(tmp);
        _;
    }

}
