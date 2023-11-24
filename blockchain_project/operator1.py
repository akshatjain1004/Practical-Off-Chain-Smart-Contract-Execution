from tee import TrustedExecutionEnvironment

operator_id="1"
tee1= TrustedExecutionEnvironment()
from web3 import Web3

# Connect to the JavaScript VM (in-browser Ethereum virtual machine)
w3 = Web3(Web3.WebsocketProvider('ws://localhost:8545'))

# Replace with your contract's address and ABI
contract_address = "0x5FbDB2315678afecb367f032d93F642f64180aa3"
contract_address= Web3.to_checksum_address(contract_address)
contract_abi = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "input",
				"type": "string"
			}
		],
		"name": "processMessage",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "setRandomExecutor",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "newMessage",
				"type": "string"
			}
		],
		"name": "setString",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "balance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "executor",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "flag",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getBalance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getExecutor",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getFlag",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getString",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "index",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "message",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "operatorIds",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

# Load the contract
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

while True:
    executor= contract.functions.getExecutor().call()
    if(str(executor)==operator_id):
        isChange= contract.functions.getFlag().call()
        if(isChange):
            message= contract.functions.getString().call()
            ans= tee1.public(message)
            if(ans==True):
                contract.functions.processMessage("True").transact({'from': w3.eth.accounts[0]})
                balance= contract.functions.getBalance().call()
                print(balance)
                print("Balance Increased")
            else:
                contract.functions.processMessage("False").transact({'from': w3.eth.accounts[0]})
                balance= contract.functions.getBalance().call()
                print(balance)
                print("Balance Decreased")
        # print("Here")
    # Your Python script can interact with the contract now
        # message = input("Enter a message ('Change' to change executor): ")
        # contract.functions.setString(message).transact({'from': w3.eth.accounts[0]})
        

    # result = contract.functions.getString().call()
    # print(f"Retrieved message: {result}")
