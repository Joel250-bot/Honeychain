import { network } from "hardhat";

const { ethers } = await network.connect();

const HoneyChain = await ethers.getContractFactory("HoneyChain");
const honeyChain = await HoneyChain.deploy();

await honeyChain.waitForDeployment();

console.log("HoneyChain deployed to:", await honeyChain.getAddress());