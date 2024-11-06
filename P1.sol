//SPDX-License-Identifier: MIT
//https://betterprogramming.pub/developing-a-smart-contract-by-using-re mix-ide-81ff6f44ba2f

pragma solidity >=0.7.0 <0.9.0; 
contract SimpleBank {
    struct client_account{
        int client_id;	
        address client_address; 
        uint client_balance_in_ether;	
    }
    client_account[] clients; 
    int clientCounter;
    address payable manager;
    modifier onlyManager() 
    {
        require(msg.sender == manager, "Only manager can call this!");
        _;
    }
    modifier onlyClients() 
    { 
        bool isclient = false;	
        for(uint i=0;i<clients.length;i++)
        {	
            if(clients[i].client_address == msg.sender)
            { 
                isclient = true; 
            }
        }   
        require(isclient, "Only clients can call this!"); 
        _;
    }
    constructor() {
        clientCounter = 0; 
    }
    receive() external payable { } 
    function setManager(address managerAddress) public returns(string memory)
    { 
        manager = payable(managerAddress);
        return ""; 
    }
    function joinAsClient() public payable returns(string memory)
    {
        clients.push(client_account(clientCounter++, msg.sender, address(msg.sender).balance)); 
        return ""; 
    }
    function deposit() public payable onlyClients
    { 
        payable(address(this)).transfer(msg.value);
    }
    function withdraw(uint amount) public payable onlyClients
    { 
        payable(msg.sender).transfer(amount * 1 ether); 
    }
    function sendInterest() public payable onlyManager
    { 
        for(uint i=0;i<clients.length;i++)
        { 
            address initialAddress = clients[i].client_address;     
            payable(initialAddress).transfer(1 ether);

        }
    }
    function getContractBalance() public view returns(uint)
    {
        return address(this).balance;
    }
}
