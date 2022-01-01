// SPDX-License-Identifier: MIT
pragma solidity>=0.4.24 <0.6.11;


/**
 * @title ERC721 Non-Fungible Token Standard basic interface
 * @dev see https://github.com/ethereum/EIPs/blob/master/EIPS/eip-721.md
 */
interface ERC721 {

  event Transfer(
    address indexed from,
    address indexed to,
    uint256 indexed tokenId
  );
  event Approval(
    address indexed owner,
    address indexed approved,
    uint256 indexed tokenId
  );
  event ApprovalForAll(
    address indexed owner,
    address indexed operator,
    bool approved
  );

  function balanceOf(address owner) external view returns (uint256 balance);
  function ownerOf(uint256 tokenId) external view returns (address owner);
  
  function approve(address to, uint256 tokenId) external;
  function getApproved(uint256 tokenId)
    external view returns (address operator);
  
  function setApprovalForAll(address operator, bool _approved) external;
  function isApprovedForAll(address owner, address operator)
    external view returns (bool);
  
  function transferFrom(address from, address to, uint256 tokenId) external;
  // function safeTransferFrom(address from, address to, uint256 tokenId)
  //   external;

  // function safeTransferFrom(
  //   address from,
  //   address to,
  //   uint256 tokenId,
  //   bytes data
  // )
  //   external;
}
