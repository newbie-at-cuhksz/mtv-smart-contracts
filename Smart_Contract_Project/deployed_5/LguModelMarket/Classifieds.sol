// SPDX-License-Identifier: MIT
pragma solidity>=0.4.24 <0.6.11;

/*
 * ref: https://ethereum.org/en/developers/tutorials/how-to-implement-an-erc721-market/
 *      https://github.com/HQ20/contracts/blob/master/contracts/classifieds/Classifieds.sol
 */

import "./Ownable.sol";

contract IERC20 {
    function transferFrom(address from, address to, uint256 value) external returns (bool);
}

contract IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
}


 /**
 * @title Classifieds
 * @notice Implements the classifieds board market. The market will be governed
 * by an ERC20 token as currency, and an ERC721 token that represents the
 * ownership of the items being traded. Only ads for selling items are
 * implemented. The item tokenization is responsibility of the ERC721 contract
 * which should encode any item details.
 */
contract Classifieds is Ownable {
    event TradeStatusChange(uint256 ad, bytes32 status);

    IERC20 currencyToken;
    IERC721 itemToken;

    struct Trade {
        address poster;
        uint256 item;
        uint256 price;
        bytes32 status; // Open, Executed, Cancelled
    }

    mapping(uint256 => Trade) public trades;

    uint256 tradeCounter;

    //constructor (address _currencyTokenAddress, address _itemTokenAddress)
    constructor ()
        public
    {
        // set address of ERC20 and ERC721 contracts later
        //currencyToken = IERC20(_currencyTokenAddress);
        //itemToken = IERC721(_itemTokenAddress);
        tradeCounter = 0;
    }

    function setERC20Addr (address _currencyTokenAddress) external onlyOwner {
        currencyToken = IERC20(_currencyTokenAddress);
    }

    function setERC721Addr (address _itemTokenAddress) external onlyOwner {
        itemToken = IERC721(_itemTokenAddress);
    }


    /**
     * @dev Returns the details for a trade.
     * @param _trade The id for the trade.
     */
    function getTrade(uint256 _trade)
        public
        view
        returns(address, uint256, uint256, bytes32)
    {
        Trade memory trade = trades[_trade];
        return (trade.poster, trade.item, trade.price, trade.status);
    }

    /**
     * @dev Opens a new trade. Puts _item in escrow.
     * @param _item The id for the item to trade.
     * @param _price The amount of currency for which to trade the item.
     */
    function openTrade(uint256 _item, uint256 _price)
        public
    {
        itemToken.transferFrom(msg.sender, address(this), _item);
        trades[tradeCounter] = Trade({
            poster: msg.sender,
            item: _item,
            price: _price,
            status: "Open"
        });
        tradeCounter += 1;
        emit TradeStatusChange(tradeCounter - 1, "Open");
    }

    /**
     * @dev Executes a trade. Must have approved this contract to transfer the
     * amount of currency specified to the poster. Transfers ownership of the
     * item to the filler.
     * @param _trade The id of an existing trade
     */
    function executeTrade(uint256 _trade)
        public
    {
        Trade memory trade = trades[_trade];
        require(trade.status == "Open", "Trade is not Open.");
        currencyToken.transferFrom(msg.sender, trade.poster, trade.price);
        itemToken.transferFrom(address(this), msg.sender, trade.item);
        trades[_trade].status = "Executed";
        emit TradeStatusChange(_trade, "Executed");
    }

    /**
     * @dev Cancels a trade by the poster.
     * @param _trade The trade to be cancelled.
     */
    function cancelTrade(uint256 _trade)
        public
    {
        Trade memory trade = trades[_trade];
        require(
            msg.sender == trade.poster,
            "Trade can be cancelled only by poster."
        );
        require(trade.status == "Open", "Trade is not Open.");
        itemToken.transferFrom(address(this), trade.poster, trade.item);
        trades[_trade].status = "Cancelled";
        emit TradeStatusChange(_trade, "Cancelled");
    }
}
