import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

from backend.app.database import engine, Base, SessionLocal
from backend.app.models.models import User, Hive, SensorReading, AIResult, HoneyBatch, BlockchainBlock
from backend.app.ai.model_service import ai_service
from backend.app.blockchain.ledger import create_genesis_block, add_event_block, verify_ledger_integrity
from backend.app.services.qr_service import generate_qr_code_base64


def test_full_workflow():
    print("==================================================")
    print("Testing HoneyChain E2E System Workflow")
    print("==================================================")

    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # 1. Verify Beekeepers & Hives
        beekeepers_count = db.query(User).count()
        hives_count = db.query(Hive).count()
        print(f"[OK] Database Users: {beekeepers_count}, Hives: {hives_count}")

        # 2. Test AI Anomaly Detection & Yield Prediction
        normal_analysis = ai_service.analyze_hive_condition(34.0, 65.0, 42.0, 85.0)
        print(f"[OK] AI Normal Condition Check: Status={normal_analysis['anomaly_status']}, Score={normal_analysis['anomaly_score']}, Yield={normal_analysis['predicted_honey_kg']}kg")
        assert normal_analysis['anomaly_status'] == 'normal', "Expected normal status"

        abnormal_analysis = ai_service.analyze_hive_condition(44.0, 92.0, 31.0, 18.0)
        print(f"[OK] AI Abnormal Condition Check: Status={abnormal_analysis['anomaly_status']}, Score={abnormal_analysis['anomaly_score']}, Alert='{abnormal_analysis['alert_message']}'")
        assert abnormal_analysis['anomaly_status'] == 'abnormal', "Expected abnormal status"

        # 3. Test Blockchain Genesis & Verification
        create_genesis_block(db)
        verification = verify_ledger_integrity(db)
        print(f"[OK] Blockchain Ledger Integrity: Valid={verification['is_valid']}, Status='{verification['status_message']}'")
        assert verification['is_valid'] is True, "Blockchain verification failed!"

        # 4. Test QR Code Generation
        qr = generate_qr_code_base64("http://localhost:5173/verify/HONEY-2026-0001")
        print(f"[OK] QR Code Base64 Generated (Length: {len(qr)} chars)")
        assert qr.startswith("data:image/png;base64,"), "Invalid QR code format"

        print("\nSUCCESS: ALL E2E WORKFLOW TESTS PASSED PERFECTLY!")

    finally:
        db.close()


if __name__ == "__main__":
    test_full_workflow()
