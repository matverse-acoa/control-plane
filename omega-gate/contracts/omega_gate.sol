// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract OmegaGate {
    event DecisionAnchored(
        bytes32 indexed proofHash,
        string decision,
        string reason,
        uint256 timestamp
    );

    function anchorDecision(bytes32 proofHash, string calldata decision, string calldata reason) external {
        emit DecisionAnchored(proofHash, decision, reason, block.timestamp);
    }
}
