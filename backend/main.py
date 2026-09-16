from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from blockchain_service import (
    create_batch,
    get_batch,
    assign_seal,
    get_seal,
    record_lab_verification,
    get_lab_test,
    record_processing,
    get_processing,
    create_package,
    get_package,
    verify_package
)

app = FastAPI(title="HoneyChain API")


# -----------------------------
# Error handling
# -----------------------------

def handle_blockchain_error(error):
    message = str(error).lower()

    if "not found" in message:
        raise HTTPException(
            status_code=404,
            detail="Requested blockchain record was not found"
        )

    if "already exists" in message:
        raise HTTPException(
            status_code=409,
            detail="Blockchain record already exists"
        )

    if "already assigned" in message:
        raise HTTPException(
            status_code=409,
            detail="Seal is already assigned"
        )

    if "does not match" in message:
        raise HTTPException(
            status_code=400,
            detail="Blockchain relationship is invalid"
        )

    if "invalid" in message:
        raise HTTPException(
            status_code=400,
            detail="Invalid blockchain data"
        )

    raise HTTPException(
        status_code=500,
        detail="Blockchain operation failed"
    )


# -----------------------------
# Request models
# -----------------------------

class BatchRequest(BaseModel):
    batch_id: str
    beekeeper_id: str
    hive_id: str
    harvest_id: str
    quantity: int


class SealRequest(BaseModel):
    seal_id: str
    batch_id: str


class LabTestRequest(BaseModel):
    test_id: str
    batch_id: str
    result: str


class ProcessingRequest(BaseModel):
    processing_id: str
    batch_id: str
    processor_id: str
    status: str


class PackageRequest(BaseModel):
    package_id: str
    batch_id: str
    seal_id: str
    quantity: int


# -----------------------------
# Root endpoint
# -----------------------------

@app.get("/")
def root():
    return {
        "message": "HoneyChain API is running"
    }


# -----------------------------
# Batch endpoints
# -----------------------------

@app.post("/blockchain/batches")
def create_blockchain_batch(batch: BatchRequest):
    try:
        receipt = create_batch(
            batch.batch_id,
            batch.beekeeper_id,
            batch.hive_id,
            batch.harvest_id,
            batch.quantity
        )

        return {
            "message": "Batch created successfully",
            "batch_id": batch.batch_id,
            "transaction_hash": receipt["transactionHash"].hex()
        }

    except Exception as error:
        handle_blockchain_error(error)


@app.get("/blockchain/batches/{batch_id}")
def read_blockchain_batch(batch_id: str):
    try:
        return get_batch(batch_id)

    except Exception as error:
        handle_blockchain_error(error)


# -----------------------------
# Seal endpoints
# -----------------------------

@app.post("/blockchain/seals")
def create_blockchain_seal(seal: SealRequest):
    try:
        receipt = assign_seal(
            seal.seal_id,
            seal.batch_id
        )

        return {
            "message": "Seal assigned successfully",
            "seal_id": seal.seal_id,
            "batch_id": seal.batch_id,
            "transaction_hash": receipt["transactionHash"].hex()
        }

    except Exception as error:
        handle_blockchain_error(error)


@app.get("/blockchain/seals/{seal_id}")
def read_blockchain_seal(seal_id: str):
    try:
        return get_seal(seal_id)

    except Exception as error:
        handle_blockchain_error(error)


# -----------------------------
# Laboratory endpoints
# -----------------------------

@app.post("/blockchain/lab-tests")
def create_lab_test(test: LabTestRequest):
    try:
        receipt = record_lab_verification(
            test.test_id,
            test.batch_id,
            test.result
        )

        return {
            "message": "Laboratory verification recorded successfully",
            "test_id": test.test_id,
            "batch_id": test.batch_id,
            "result": test.result,
            "transaction_hash": receipt["transactionHash"].hex()
        }

    except Exception as error:
        handle_blockchain_error(error)


@app.get("/blockchain/lab-tests/{test_id}")
def read_lab_test(test_id: str):
    try:
        return get_lab_test(test_id)

    except Exception as error:
        handle_blockchain_error(error)


# -----------------------------
# Processing endpoints
# -----------------------------

@app.post("/blockchain/processing")
def create_processing(processing: ProcessingRequest):
    try:
        receipt = record_processing(
            processing.processing_id,
            processing.batch_id,
            processing.processor_id,
            processing.status
        )

        return {
            "message": "Processing recorded successfully",
            "processing_id": processing.processing_id,
            "batch_id": processing.batch_id,
            "processor_id": processing.processor_id,
            "status": processing.status,
            "transaction_hash": receipt["transactionHash"].hex()
        }

    except Exception as error:
        handle_blockchain_error(error)


@app.get("/blockchain/processing/{processing_id}")
def read_processing(processing_id: str):
    try:
        return get_processing(processing_id)

    except Exception as error:
        handle_blockchain_error(error)


# -----------------------------
# Package endpoints
# -----------------------------

@app.post("/blockchain/packages")
def create_blockchain_package(package: PackageRequest):
    try:
        receipt = create_package(
            package.package_id,
            package.batch_id,
            package.seal_id,
            package.quantity
        )

        return {
            "message": "Package created successfully",
            "package_id": package.package_id,
            "batch_id": package.batch_id,
            "seal_id": package.seal_id,
            "quantity": package.quantity,
            "transaction_hash": receipt["transactionHash"].hex()
        }

    except Exception as error:
        handle_blockchain_error(error)


@app.get("/blockchain/packages/{package_id}")
def read_blockchain_package(package_id: str):
    try:
        return get_package(package_id)

    except Exception as error:
        handle_blockchain_error(error)


# -----------------------------
# Consumer verification
# -----------------------------

@app.get("/verify/{package_id}")
def verify_blockchain_package(package_id: str):
    try:
        result = verify_package(package_id)

        if not result["seal_valid"]:
            raise HTTPException(
                status_code=400,
                detail="Package seal is invalid"
            )

        return result

    except HTTPException:
        raise

    except Exception as error:
        handle_blockchain_error(error)