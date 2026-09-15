# HoneyChain - Database Design

## 1. Database

HoneyChain will use PostgreSQL as the primary relational database.

The database stores detailed application, hive, sensor, laboratory,
traceability and user information.

Blockchain will store only important verification and traceability
events. Detailed sensor data will remain in PostgreSQL.

---

## 2. Main Entities

The database contains the following major entities:

- User
- Beekeeper
- Hive
- Sensor Data
- AI Alert
- Harvest
- Honey Batch
- Seal
- Laboratory
- Laboratory Test
- Processor
- Processing
- Package
- Blockchain Record

---

## 3. Entity Relationships

```text
USER
 |
 | 1:1
 v
BEEKEEPER
 |
 | 1:M
 v
HIVE
 |
 | 1:M
 v
SENSOR_DATA
 |
 v
AI_ALERT


HIVE
 |
 | 1:M
 v
HARVEST
 |
 | 1:M
 v
BATCH
 |
 +---------> SEAL
 |
 +---------> LAB_TEST
 |
 +---------> PROCESSING
 |
 +---------> PACKAGE
                    |
                    v
                    QR