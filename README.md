# Practical-Off-Chain-Smart-Contract-Execution

A methodology to improve blockchain throughput and reduce gas fees by executing smart contracts off-chain.

<img width="836" alt="image" src="https://github.com/akshatjain1004/Practical-Off-Chain-Smart-Contract-Execution/assets/86458423/25c0b3e0-5310-42f6-b0d1-6e776cc1e176">

--------------------------------------------------------------------------------------------------------
We quantify the performance in terms of gas fees and execution time.

<img width="450" alt="image" src="https://github.com/akshatjain1004/Practical-Off-Chain-Smart-Contract-Execution/assets/86458423/ac6e41f5-90ec-47fd-8c41-f8d5d623b402">
<img width="450" alt="image" src="https://github.com/akshatjain1004/Practical-Off-Chain-Smart-Contract-Execution/assets/86458423/ccb9f418-5c11-48e9-96c6-207a033193ff">

--------------------------------------------------------------------------------------------------------
# Execution Details
## Execution Platform
Remix

## Necessary Dependencies
1. Remixd
2. Hardhat
3. Python- Web3

## Steps
1. cd into the folder blockchain project by command `cd blockchain_project`
2. Connect your localhost to the remix platform to import the files. For this, start a connection using remixd library.
3. Start a local blockchain testnet using the hardhat library in npm.
4. Now deploy the solidity contract `name.sol` on the local testnet using the remix platform.
5. Now, run the file `client.py` in a separate terminal. This is representative of the client, who interacts with the executor from the pool of operators.
6. Finally, run the two files `operator1.py` and `operator2.py` in separate terminals representative of the pool of operators.
7. The client can give commands to the executor, chosen from the two operators and can even change the executor.
8. Refer to `report.pdf` for in depth analysis .
