import json
from web3 import Web3

RPC_URL = "http://127.0.0.1:8545"

CONTRACT_ADDRESS = "0xa513E6E4b8f2a923D98304ec87F64353C4D5C853"

ABI_PATH = "../blockchain/artifacts/contracts/HoneyChain.sol/HoneyChain.json"

w3 = Web3(Web3.HTTPProvider(RPC_URL))

with open(ABI_PATH, "r") as file:
    contract_data = json.load(file)

contract = w3.eth.contract(
    address=CONTRACT_ADDRESS,
    abi=contract_data["abi"]
)

account = w3.eth.accounts[0]


# -----------------------------
# Batch
# -----------------------------

def create_batch(
    batch_id,
    beekeeper_id,
    hive_id,
    harvest_id,
    quantity
):
    tx = contract.functions.createBatch(
        batch_id,
        beekeeper_id,
        hive_id,
        harvest_id,
        quantity
    ).transact({
        "from": account
    })

    return w3.eth.wait_for_transaction_receipt(tx)


def get_batch(batch_id):
    batch = contract.functions.getBatch(
        batch_id
    ).call()

    return {
        "batch_id": batch[0],
        "beekeeper_id": batch[1],
        "hive_id": batch[2],
        "harvest_id": batch[3],
        "quantity": batch[4],
        "created_at": batch[5]
    }


# -----------------------------
# Seal
# -----------------------------

def assign_seal(seal_id, batch_id):
    tx = contract.functions.assignSeal(
        seal_id,
        batch_id
    ).transact({
        "from": account
    })

    return w3.eth.wait_for_transaction_receipt(tx)


def get_seal(seal_id):
    seal = contract.functions.getSeal(
        seal_id
    ).call()

    return {
        "seal_id": seal[0],
        "batch_id": seal[1],
        "assigned_at": seal[2]
    }


# -----------------------------
# Laboratory
# -----------------------------

def record_lab_verification(
    test_id,
    batch_id,
    result
):
    tx = contract.functions.recordLabVerification(
        test_id,
        batch_id,
        result
    ).transact({
        "from": account
    })

    return w3.eth.wait_for_transaction_receipt(tx)


def get_lab_test(test_id):
    lab_test = contract.functions.getLabTest(
        test_id
    ).call()

    return {
        "test_id": lab_test[0],
        "batch_id": lab_test[1],
        "result": lab_test[2],
        "tested_at": lab_test[3]
    }


def get_batch_lab_test_id(batch_id):
    return contract.functions.getBatchLabTestId(
        batch_id
    ).call()


# -----------------------------
# Processing
# -----------------------------

def record_processing(
    processing_id,
    batch_id,
    processor_id,
    status
):
    tx = contract.functions.recordProcessing(
        processing_id,
        batch_id,
        processor_id,
        status
    ).transact({
        "from": account
    })

    return w3.eth.wait_for_transaction_receipt(tx)


def get_processing(processing_id):
    processing = contract.functions.getProcessing(
        processing_id
    ).call()

    return {
        "processing_id": processing[0],
        "batch_id": processing[1],
        "processor_id": processing[2],
        "status": processing[3],
        "processed_at": processing[4]
    }


def get_batch_processing_id(batch_id):
    return contract.functions.getBatchProcessingId(
        batch_id
    ).call()


# -----------------------------
# Package
# -----------------------------

def create_package(
    package_id,
    batch_id,
    seal_id,
    quantity
):
    tx = contract.functions.createPackage(
        package_id,
        batch_id,
        seal_id,
        quantity
    ).transact({
        "from": account
    })

    return w3.eth.wait_for_transaction_receipt(tx)


def get_package(package_id):
    package = contract.functions.getPackage(
        package_id
    ).call()

    return {
        "package_id": package[0],
        "batch_id": package[1],
        "seal_id": package[2],
        "quantity": package[3],
        "created_at": package[4]
    }


# -----------------------------
# Complete Package Verification
# -----------------------------

def verify_package(package_id):
    package = get_package(package_id)

    batch = get_batch(
        package["batch_id"]
    )

    seal = get_seal(
        package["seal_id"]
    )

    seal_valid = (
        seal["batch_id"] == package["batch_id"]
    )

    lab_test = None
    processing = None

    try:
        lab_test_id = get_batch_lab_test_id(
            package["batch_id"]
        )

        lab_test = get_lab_test(
            lab_test_id
        )

    except Exception:
        lab_test = None

    try:
        processing_id = get_batch_processing_id(
            package["batch_id"]
        )

        processing = get_processing(
            processing_id
        )

    except Exception:
        processing = None

    verification_status = (
        "VERIFIED"
        if seal_valid
        else "INVALID"
    )

    return {
        "verification_status": verification_status,
        "package": package,
        "batch": batch,
        "seal": seal,
        "lab_test": lab_test,
        "processing": processing,
        "seal_valid": seal_valid
    }


# -----------------------------
# Connection Test
# -----------------------------

if __name__ == "__main__":
    print(
        "Blockchain connected:",
        w3.is_connected()
    )

    print(
        "Contract address:",
        CONTRACT_ADDRESS
    )

    print(
        "Account:",
        account
    )