//SPDX-License-Identifier: MIT
//https://betterprogramming.pub/developing-a-smart-contract-by-using-re mix-ide-81ff6f44ba2f
pragma solidity >=0.7.0 <0.9.0; 

contract EVoting 
{
    struct Voter 
    {
        bool hasVoted;
        address voterAddress;
    }

    struct Candidate 
    {
        string name;
        uint votes;
    }

    Candidate[] public candidates;
    mapping(address => Voter) public voters;

    constructor(string[] memory _candidateNames) 
    {
        for (uint i = 0; i < _candidateNames.length; i++) 
        {
            candidates.push(Candidate(_candidateNames[i], 0));
        }
    }

    function vote(uint _candidateIndex) public 
    {
        require(!voters[msg.sender].hasVoted, "Already voted");
        require(_candidateIndex < candidates.length, "Invalid candidate index");

        voters[msg.sender].hasVoted = true;
        voters[msg.sender].voterAddress = msg.sender;
        candidates[_candidateIndex].votes++;
    }

    function getCandidateVotes(uint _candidateIndex) public view returns (uint) 
    {
        return candidates[_candidateIndex].votes;
    }

    function getCandidateName(uint _candidateIndex) public view returns (string memory) 
    {
        return candidates[_candidateIndex].name;
    }
}