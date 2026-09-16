import { network } from "hardhat";

const { ethers } = await network.connect();

const HoneyChain = await ethers.getContractFactory("HoneyChain");
const honeyChain = await HoneyChain.deploy();

await honeyChain.waitForDeployment();

await honeyChain.createBatch(
  "HC-2026-00125",
  "BK-001",
  "HIVE-001",
  "HV-2026-001",
  125
);

const batch = await honeyChain.getBatch("HC-2026-00125");

console.log("Batch ID:", batch.batchId);
console.log("Beekeeper ID:", batch.beekeeperId);
console.log("Hive ID:", batch.hiveId);
console.log("Harvest ID:", batch.harvestId);
console.log("Quantity:", batch.quantity.toString());