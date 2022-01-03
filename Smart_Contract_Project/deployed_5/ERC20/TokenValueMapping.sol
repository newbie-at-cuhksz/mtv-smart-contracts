// SPDX-License-Identifier: MIT
pragma solidity>=0.4.24 <0.6.11;

import "./LguTokenERC20Base.sol";

contract TokenValueMapping is LguTokenERC20Base {
    
    struct RegionInfo {
        string name;
        uint256 base;
        uint256 weight;
    }
    
    uint256 private totalBonus = 200;
    
    uint256 private initialWeight = 1000;
    
    // the following two variables are not used, due to the bug of FISCO-BCOS
    uint256 private resetRegionWeightPeriod = 1 days;   // reset region weight every day
    uint256 private nextResetTime;
    
    RegionInfo[] private _regions;

    
    constructor() internal {
        nextResetTime = now + resetRegionWeightPeriod;
        
        /*
        _regions.push( RegionInfo("University Library", 20, initialWeight) );
        _regions.push( RegionInfo("TA", 15, initialWeight) );
        _regions.push( RegionInfo("Shaw", 10, initialWeight) );
        _regions.push( RegionInfo("Gym", 20, initialWeight) );
        */
        
        _regions.push( RegionInfo("NOWHERE",                    20, initialWeight) );
        _regions.push( RegionInfo("Administration Building",    20, initialWeight) );
        _regions.push( RegionInfo("University Library",         20, initialWeight) );
        _regions.push( RegionInfo("Student Center",             20, initialWeight) );
        _regions.push( RegionInfo("TA",                         20, initialWeight) );
        _regions.push( RegionInfo("Million Avenue",             20, initialWeight) );
        _regions.push( RegionInfo("TB",                         20, initialWeight) );
        _regions.push( RegionInfo("TC",                         20, initialWeight) );
        _regions.push( RegionInfo("TD",                         20, initialWeight) );
        _regions.push( RegionInfo("RA",                         20, initialWeight) );
        _regions.push( RegionInfo("RB",                         20, initialWeight) );
        _regions.push( RegionInfo("Shaw College East",          20, initialWeight) );
        _regions.push( RegionInfo("Shaw College West",          20, initialWeight) );
        _regions.push( RegionInfo("Zhixin Building",            20, initialWeight) );
        _regions.push( RegionInfo("GYM",                        20, initialWeight) );
        _regions.push( RegionInfo("Harmonia College",           20, initialWeight) );
        _regions.push( RegionInfo("Dligentia College",          20, initialWeight) );
        _regions.push( RegionInfo("Muse College",               20, initialWeight) );
        _regions.push( RegionInfo("Staff Quarters",             20, initialWeight) );
        _regions.push( RegionInfo("Chengdao Building",          20, initialWeight) );
        _regions.push( RegionInfo("Zhiren Building",            20, initialWeight) );
        _regions.push( RegionInfo("Letian Building",            20, initialWeight) );
        _regions.push( RegionInfo("Shaw International Conference Centre", 20, initialWeight) );
        _regions.push( RegionInfo("Start-up Zone",              20, initialWeight) );
        _regions.push( RegionInfo("Daoyuan Building",           20, initialWeight) );
        
    }
    
    modifier isRegionNameValid(string regionName) {
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
    
    function getRegionBase(string regionName) external view isRegionNameValid(regionName) returns (uint256) {
        for (uint i = 0; i < _regions.length; i++) {
            if (keccak256(abi.encodePacked(regionName)) == keccak256(abi.encodePacked( _regions[i].name ))) {
                return _regions[i].base;
            }
        }
        return 0;
    }
    
    function getRegionWeight(string regionName) external view isRegionNameValid(regionName) returns (uint256) {
        for (uint i = 0; i < _regions.length; i++) {
            if (keccak256(abi.encodePacked(regionName)) == keccak256(abi.encodePacked( _regions[i].name ))) {
                return _regions[i].weight;
            }
        }
        return 0;
    }
    
    // add new region or update an existing region base
    // we should avoid calling this function
    // delete region function is not provided yet
    function addNewRegion(string regionName, uint256 regionBase) external onlyOwner {
        for (uint i = 0; i < _regions.length; i++) {
            if (keccak256(abi.encodePacked(regionName)) == keccak256(abi.encodePacked( _regions[i].name ))) {
                _regions[i].base = regionBase;
                return;
            }
        }
        
        _regions.push( RegionInfo(regionName, regionBase, initialWeight) );
    }
    
    function resetRegionWeight() public onlyOwner {
        for (uint i = 0; i < _regions.length; i++) {
            _regions[i].weight = initialWeight;
        }
    }
    
    function getTokenNumPerUnitTime(string regionName) public view isRegionNameValid(regionName) returns (uint256) {
        uint256 totalWeight = 0;
        for (uint j = 0; j < _regions.length; j++) {
            totalWeight = totalWeight.add(_regions[j].weight);
        }
        
        for (uint i = 0; i < _regions.length; i++) {
            if (keccak256(abi.encodePacked(regionName)) == keccak256(abi.encodePacked( _regions[i].name ))) {
                uint256 regionBonus = totalBonus.mul(_regions[i].weight).div(totalWeight);      // totalBonus * regionWeight / totalWeight
                return _regions[i].base.add(regionBonus);
            }
        }
        
        return 0;
    }
    
    function grantTokenOnHookOnBlockchain(address account, uint256 timeSpan, string regionName) external isRegionNameValid(regionName) onlyOwner {
        
        // grant tokens
        uint256 amount = timeSpan.mul( getTokenNumPerUnitTime(regionName) );
        _mint(account, amount);
        
        // update region weights
        //uint256 weightIncrement = timeSpan.div(_regions.length - 1);
        uint256 weightIncrement = timeSpan;         // Since there are over 20 region, if users ask for token, say every 5 min, `weightIncrement` will always be 0
        for (uint i = 0; i < _regions.length; i++) {
            if (keccak256(abi.encodePacked(regionName)) != keccak256(abi.encodePacked( _regions[i].name ))){
                _regions[i].weight = _regions[i].weight.add(weightIncrement);
            }
        }
        
        // reset region weight if needed
        // (this is disabled due to the bug of FISCO-BCOS)
        // if (now >= nextResetTime) {
        //     resetRegionWeight();
        //     nextResetTime = now + resetRegionWeightPeriod;
        // }
    }

}
