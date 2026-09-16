// SPDX-License-Identifier: MIT
pragma solidity ^0.8.34;

contract HoneyChain {
    struct Batch {
        string batchId;
        string beekeeperId;
        string hiveId;
        string harvestId;
        uint256 quantity;
        uint256 createdAt;
    }

    struct Seal {
        string sealId;
        string batchId;
        uint256 assignedAt;
    }

    struct LabTest {
        string testId;
        string batchId;
        string result;
        uint256 testedAt;
    }

    struct Processing {
        string processingId;
        string batchId;
        string processorId;
        string status;
        uint256 processedAt;
    }

    struct Package {
        string packageId;
        string batchId;
        string sealId;
        uint256 quantity;
        uint256 createdAt;
    }

    mapping(string => Batch) private batches;
    mapping(string => Seal) private seals;
    mapping(string => LabTest) private labTests;
    mapping(string => Processing) private processings;
    mapping(string => Package) private packages;

    mapping(string => string) private batchLabTests;
    mapping(string => string) private batchProcessings;

    event BatchCreated(
        string batchId,
        string beekeeperId,
        string hiveId,
        string harvestId,
        uint256 quantity,
        uint256 createdAt
    );

    event SealAssigned(
        string sealId,
        string batchId,
        uint256 assignedAt
    );

    event LabVerified(
        string testId,
        string batchId,
        string result,
        uint256 testedAt
    );

    event ProcessingCompleted(
        string processingId,
        string batchId,
        string processorId,
        string status,
        uint256 processedAt
    );

    event PackageCreated(
        string packageId,
        string batchId,
        string sealId,
        uint256 quantity,
        uint256 createdAt
    );

    function createBatch(
        string memory batchId,
        string memory beekeeperId,
        string memory hiveId,
        string memory harvestId,
        uint256 quantity
    ) public {
        require(bytes(batchId).length > 0, "Invalid batch ID");
        require(batches[batchId].createdAt == 0, "Batch already exists");

        batches[batchId] = Batch(
            batchId,
            beekeeperId,
            hiveId,
            harvestId,
            quantity,
            block.timestamp
        );

        emit BatchCreated(
            batchId,
            beekeeperId,
            hiveId,
            harvestId,
            quantity,
            block.timestamp
        );
    }

    function assignSeal(
        string memory sealId,
        string memory batchId
    ) public {
        require(batches[batchId].createdAt != 0, "Batch not found");
        require(bytes(sealId).length > 0, "Invalid seal ID");
        require(seals[sealId].assignedAt == 0, "Seal already assigned");

        seals[sealId] = Seal(
            sealId,
            batchId,
            block.timestamp
        );

        emit SealAssigned(
            sealId,
            batchId,
            block.timestamp
        );
    }

    function recordLabVerification(
        string memory testId,
        string memory batchId,
        string memory result
    ) public {
        require(batches[batchId].createdAt != 0, "Batch not found");
        require(bytes(testId).length > 0, "Invalid test ID");
        require(labTests[testId].testedAt == 0, "Test already exists");

        labTests[testId] = LabTest(
            testId,
            batchId,
            result,
            block.timestamp
        );

        batchLabTests[batchId] = testId;

        emit LabVerified(
            testId,
            batchId,
            result,
            block.timestamp
        );
    }

    function recordProcessing(
        string memory processingId,
        string memory batchId,
        string memory processorId,
        string memory status
    ) public {
        require(batches[batchId].createdAt != 0, "Batch not found");
        require(
            processings[processingId].processedAt == 0,
            "Processing already exists"
        );

        processings[processingId] = Processing(
            processingId,
            batchId,
            processorId,
            status,
            block.timestamp
        );

        batchProcessings[batchId] = processingId;

        emit ProcessingCompleted(
            processingId,
            batchId,
            processorId,
            status,
            block.timestamp
        );
    }

    function createPackage(
        string memory packageId,
        string memory batchId,
        string memory sealId,
        uint256 quantity
    ) public {
        require(batches[batchId].createdAt != 0, "Batch not found");
        require(seals[sealId].assignedAt != 0, "Seal not found");

        require(
            keccak256(bytes(seals[sealId].batchId)) ==
            keccak256(bytes(batchId)),
            "Seal does not match batch"
        );

        require(bytes(packageId).length > 0, "Invalid package ID");

        require(
            packages[packageId].createdAt == 0,
            "Package already exists"
        );

        packages[packageId] = Package(
            packageId,
            batchId,
            sealId,
            quantity,
            block.timestamp
        );

        emit PackageCreated(
            packageId,
            batchId,
            sealId,
            quantity,
            block.timestamp
        );
    }

    function getBatch(
        string memory batchId
    ) public view returns (Batch memory) {
        require(
            batches[batchId].createdAt != 0,
            "Batch not found"
        );

        return batches[batchId];
    }

    function getSeal(
        string memory sealId
    ) public view returns (Seal memory) {
        require(
            seals[sealId].assignedAt != 0,
            "Seal not found"
        );

        return seals[sealId];
    }

    function getLabTest(
        string memory testId
    ) public view returns (LabTest memory) {
        require(
            labTests[testId].testedAt != 0,
            "Lab test not found"
        );

        return labTests[testId];
    }

    function getProcessing(
        string memory processingId
    ) public view returns (Processing memory) {
        require(
            processings[processingId].processedAt != 0,
            "Processing not found"
        );

        return processings[processingId];
    }

    function getPackage(
        string memory packageId
    ) public view returns (Package memory) {
        require(
            packages[packageId].createdAt != 0,
            "Package not found"
        );

        return packages[packageId];
    }

    function getBatchLabTestId(
        string memory batchId
    ) public view returns (string memory) {
        require(
            batches[batchId].createdAt != 0,
            "Batch not found"
        );

        require(
            bytes(batchLabTests[batchId]).length > 0,
            "Lab test not found"
        );

        return batchLabTests[batchId];
    }

    function getBatchProcessingId(
        string memory batchId
    ) public view returns (string memory) {
        require(
            batches[batchId].createdAt != 0,
            "Batch not found"
        );

        require(
            bytes(batchProcessings[batchId]).length > 0,
            "Processing not found"
        );

        return batchProcessings[batchId];
    }
}