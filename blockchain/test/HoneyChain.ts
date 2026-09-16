import { expect } from "chai";
import { network } from "hardhat";

describe("HoneyChain", function () {
  async function deployContract() {
    const { ethers } = await network.connect();
    const HoneyChain = await ethers.getContractFactory("HoneyChain");
    const honeyChain = await HoneyChain.deploy();
    await honeyChain.waitForDeployment();
    return honeyChain;
  }

  it("should create and retrieve a batch", async function () {
    const honeyChain = await deployContract();

    await honeyChain.createBatch(
      "HC-2026-00125",
      "BK-001",
      "HIVE-001",
      "HV-2026-001",
      125
    );

    const batch = await honeyChain.getBatch("HC-2026-00125");

    expect(batch.batchId).to.equal("HC-2026-00125");
    expect(batch.beekeeperId).to.equal("BK-001");
    expect(batch.hiveId).to.equal("HIVE-001");
    expect(batch.harvestId).to.equal("HV-2026-001");
    expect(batch.quantity).to.equal(125);
  });

  it("should assign a seal to a batch", async function () {
    const honeyChain = await deployContract();

    await honeyChain.createBatch(
      "HC-2026-00125",
      "BK-001",
      "HIVE-001",
      "HV-2026-001",
      125
    );

    await honeyChain.assignSeal(
      "S-84521",
      "HC-2026-00125"
    );

    const seal = await honeyChain.getSeal("S-84521");

    expect(seal.sealId).to.equal("S-84521");
    expect(seal.batchId).to.equal("HC-2026-00125");
  });

  it("should record laboratory verification", async function () {
    const honeyChain = await deployContract();

    await honeyChain.createBatch(
      "HC-2026-00125",
      "BK-001",
      "HIVE-001",
      "HV-2026-001",
      125
    );

    await honeyChain.recordLabVerification(
      "LAB-TEST-0042",
      "HC-2026-00125",
      "PASSED"
    );

    const test = await honeyChain.getLabTest(
      "LAB-TEST-0042"
    );

    expect(test.testId).to.equal("LAB-TEST-0042");
    expect(test.batchId).to.equal("HC-2026-00125");
    expect(test.result).to.equal("PASSED");
  });

  it("should record processing", async function () {
    const honeyChain = await deployContract();

    await honeyChain.createBatch(
      "HC-2026-00125",
      "BK-001",
      "HIVE-001",
      "HV-2026-001",
      125
    );

    await honeyChain.recordProcessing(
      "PROC-001",
      "HC-2026-00125",
      "PROC-001",
      "COMPLETED"
    );

    const processing = await honeyChain.getProcessing("PROC-001");

    expect(processing.processingId).to.equal("PROC-001");
    expect(processing.batchId).to.equal("HC-2026-00125");
    expect(processing.processorId).to.equal("PROC-001");
    expect(processing.status).to.equal("COMPLETED");
  });

  it("should create a package with the correct seal", async function () {
    const honeyChain = await deployContract();

    await honeyChain.createBatch(
      "HC-2026-00125",
      "BK-001",
      "HIVE-001",
      "HV-2026-001",
      125
    );

    await honeyChain.assignSeal(
      "S-84521",
      "HC-2026-00125"
    );

    await honeyChain.createPackage(
      "PKG-00001",
      "HC-2026-00125",
      "S-84521",
      50
    );

    const packageData = await honeyChain.getPackage("PKG-00001");

    expect(packageData.packageId).to.equal("PKG-00001");
    expect(packageData.batchId).to.equal("HC-2026-00125");
    expect(packageData.sealId).to.equal("S-84521");
    expect(packageData.quantity).to.equal(50);
  });

  it("should reject a package with a mismatched seal", async function () {
    const honeyChain = await deployContract();

    await honeyChain.createBatch(
      "HC-2026-00125",
      "BK-001",
      "HIVE-001",
      "HV-2026-001",
      125
    );

    await honeyChain.createBatch(
      "HC-2026-00126",
      "BK-002",
      "HIVE-002",
      "HV-2026-002",
      100
    );

    await honeyChain.assignSeal(
      "S-84521",
      "HC-2026-00125"
    );

    await expect(
      honeyChain.createPackage(
        "PKG-00002",
        "HC-2026-00126",
        "S-84521",
        50
      )
    ).to.be.revertedWith("Seal does not match batch");
  });

  it("should reject duplicate batch IDs", async function () {
    const honeyChain = await deployContract();

    await honeyChain.createBatch(
      "HC-2026-00125",
      "BK-001",
      "HIVE-001",
      "HV-2026-001",
      125
    );

    await expect(
      honeyChain.createBatch(
        "HC-2026-00125",
        "BK-002",
        "HIVE-002",
        "HV-2026-002",
        100
      )
    ).to.be.revertedWith("Batch already exists");
  });

  it("should reject a missing batch", async function () {
    const honeyChain = await deployContract();

    await expect(
      honeyChain.getBatch("HC-9999")
    ).to.be.revertedWith("Batch not found");
  });
});