// SPDX-License-Identifier: MIT
pragma solidity>=0.4.24 <0.6.11;

/* 
 * ERC20 ref
 * https://eips.ethereum.org/EIPS/eip-20
 * (old version sample implemantaion of ERC20) https://github.com/OpenZeppelin/openzeppelin-contracts/blob/9b3710465583284b8c4c5d2245749246bb2e0094/contracts/token/ERC20/ERC20.sol
 * https://ethereum.org/en/developers/docs/standards/tokens/erc-20/
 * https://docs.openzeppelin.com/contracts/2.x/api/token/erc20
 */
 
//import "./Ownable.sol";  // already set in TokenValueMapping
import "./Safemath.sol";
import "./IERC20.sol";
import "./TokenValueMapping.sol";


contract LguMetaverseEditorInterface {
    function CreateLguModel(string memory _name, string memory _content) public;
}


contract LguToken is IERC20, TokenValueMapping {
    using SafeMath for uint256;
    
    mapping (address => uint256) private _balances;

    mapping (address => mapping (address => uint256)) private _allowed;
    
    uint256 private _totalSupply;
    
    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }
    
    function balanceOf(address owner) public view returns (uint256) {
        return _balances[owner];
    }
    
    function allowance(
        address owner,
        address spender
    )
        public
        view
        returns (uint256)
    {
        return _allowed[owner][spender];
    }
    
    function transfer(address to, uint256 value) public returns (bool) {
        require(value <= _balances[msg.sender]);
        require(to != address(0));
        
        _balances[msg.sender] = _balances[msg.sender].sub(value);
        _balances[to] = _balances[to].add(value);
        emit Transfer(msg.sender, to, value);
        return true;
    }
    
    function approve(address spender, uint256 value) public returns (bool) {
        require(spender != address(0));

        _allowed[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }
    
    function transferFrom(
        address from, 
        address to, 
        uint256 value
    ) 
        public 
        returns (bool) 
    {
        require(value <= _balances[from]);
        require(value <= _allowed[from][msg.sender]);
        require(to != address(0));
        
        _balances[from] = _balances[from].sub(value);
        _balances[to] = _balances[to].add(value);
        _allowed[from][msg.sender] = _allowed[from][msg.sender].sub(value);
        emit Transfer(from, to, value);
        return true;
    }
    
    function increaseAllowance(
        address spender, 
        uint256 addedValue
    ) 
    public 
    returns (bool) 
    {
        require(spender != address(0));
        
        _allowed[msg.sender][spender] = (
            _allowed[msg.sender][spender].add(addedValue));
        emit Approval(msg.sender, spender, _allowed[msg.sender][spender]);
        return true;
    }
    
    function decreaseAllowance(
        address spender, 
        uint256 subtractedValue
    ) 
    public 
    returns (bool) 
    {
        require(spender != address(0));
        
        _allowed[msg.sender][spender] = (
            _allowed[msg.sender][spender].sub(subtractedValue));
        emit Approval(msg.sender, spender, _allowed[msg.sender][spender]);
        return true;
    }
    
    function _mint(address account, uint256 amount) internal {
        require(account != 0);
        _totalSupply = _totalSupply.add(amount);
        _balances[account] = _balances[account].add(amount);
        emit Transfer(address(0), account, amount);
    }
    
    function _burn(address account, uint256 amount) internal {
        require(account != 0);
        require(amount <= _balances[account]);
        
        _totalSupply = _totalSupply.sub(amount);
        _balances[account] = _balances[account].sub(amount);
        emit Transfer(account, address(0), amount);
    }
    
    function _burnFrom(address account, uint256 amount) internal {
        require(amount <= _allowed[account][msg.sender]);
        
        _allowed[account][msg.sender] = _allowed[account][msg.sender].sub(
            amount);
        _burn(account, amount);
    }
    
    
    // Customized below
    // function grantToken(address account, uint256 amount) external onlyOwner {
    //     _mint(account, amount);
    // }
    
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
