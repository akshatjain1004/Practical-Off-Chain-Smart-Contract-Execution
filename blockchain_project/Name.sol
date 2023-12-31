// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


contract RandomExecutor  {
    uint256 public balance = 100;
    uint256 public index = 0;
    string[] public operatorIds;
    string public executor;
    string public message = "";
    bool public flag=false;
    constructor() {
        operatorIds = ["1", "2", "3"];
        executor = operatorIds[index];
    }
    function setRandomExecutor() public {
        require(operatorIds.length > 0, "No operator ids available");

        // Generate a pseudo-random number based on the current timestamp and block hash
        // uint256 randomValue = uint256(keccak256(abi.encodePacked(block.timestamp, blockhash(block.number - 1))));


        if (index == 0) {
            index = 2;
        } else if (index == 2) {
            index = 1;
        } else if (index == 1) {
            index = 0;
        } else {
            // update the index using randomness
            index = 2;
        }

        // // Update the executor with the operator at the new index
        executor = operatorIds[index];
    }


    // function setRandomExecutor() public{
    //     index= index+1;
    //     require(operatorIds.length > index, "No operator ids available");
        
    //     executor = operatorIds[index];
    // }
    function getString() public view returns (string memory) {
        return message;
    }
    function getFlag() public view returns (bool) {
        return flag;
    }
    function getExecutor() public  view returns (string memory) {
        return executor;
    }
    function setString(string calldata newMessage) public  {
        flag= true;
        message = newMessage;
    }
    function getBalance() public view returns (uint256) {
        return  balance;
    }

    function processMessage(string calldata input) public{
        bytes32 trueHash = keccak256(bytes("True"));
        bytes32 falseHash = keccak256(bytes("False"));
        bytes32 inputHash = keccak256(bytes(input));
        if (inputHash==trueHash) {
            balance += 5;
        } else if (inputHash==falseHash) {
            balance -= 2;
        }
        flag= false;
    }

}
