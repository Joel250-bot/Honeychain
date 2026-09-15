# HoneyChain - System Architecture

## 1. Architecture Overview

HoneyChain is designed as a modular system consisting of:

1. IoT Data Simulation
2. Backend API
3. Database
4. AI/ML Engine
5. Blockchain
6. QR Verification
7. Frontend Dashboards
8. Authority Monitoring

The current prototype uses simulated IoT data. Real IoT hardware will
be integrated in a future version.

---

## 2. High-Level Architecture

```text
                         HONEYCHAIN
                              |
          +-------------------+-------------------+
          |                   |                   |
          v                   v                   v
     BEEKEEPER           LABORATORY          KVIC/ADMIN
          |                   |                   |
          v                   |                   |
    HIVE MANAGEMENT           |                   |
          |                   |                   |
          v                   |                   |
    IoT SIMULATOR             |                   |
          |                   |                   |
          +---------+---------+-------------------+
                    |
                    v
              FASTAPI BACKEND
                    |
          +---------+---------+
          |                   |
          v                   v
     POSTGRESQL             AI/ML
          |                   |
          |              +----+----+
          |              |         |
          |              v         v
          |           ALERTS   PREDICTION
          |              |
          +------+-------+
                 |
                 v
              HARVEST
                 |
                 v
               BATCH
                 |
           +-----+-----+
           |           |
           v           v
         SEAL      LAB TEST
           |           |
           +-----+-----+
                 |
                 v
             BLOCKCHAIN
                 |
                 v
             PROCESSING
                 |
                 v
              PACKAGE
                 |
                 v
                 QR
                 |
                 v
             CONSUMER