# HoneyChain - System Requirements

## 1. Project Overview

HoneyChain is an integrated platform that combines IoT, AI/ML,
Blockchain and QR technology to improve honey production monitoring,
quality verification and supply-chain traceability.

The system connects beekeepers, hives, honey batches, laboratories,
processors, authorities and consumers through a common digital platform.

The current prototype will use simulated IoT data instead of physical
hardware. Real sensors can be integrated in a future version.

---

## 2. Problem Statement

The honey industry faces several challenges:

1. Counterfeit and adulterated honey can reduce consumer trust.
2. Consumers have limited ability to verify the origin and quality of honey.
3. Honey supply chains may lack complete traceability.
4. Beekeepers have limited access to continuous data-driven hive monitoring.
5. Authorities need better visibility into beekeepers, hives, production,
   laboratory testing and suspicious activities.
6. Beekeepers may have limited direct access to suitable markets and buyers.

HoneyChain addresses these challenges by connecting hive monitoring,
AI-based analysis, laboratory verification and blockchain-based
traceability.

---

## 3. Project Objectives

### 3.1 Hive Monitoring

The system shall monitor or simulate:

- Hive temperature
- Hive humidity
- Hive weight
- Hive activity

The system shall store historical hive data for analysis.

### 3.2 AI/ML Analysis

The system shall use AI/ML to:

- Detect unusual hive conditions.
- Generate alerts for abnormal patterns.
- Analyze hive activity.
- Predict honey production using available historical data.

The AI system should identify possible abnormal conditions and recommend
inspection. It should not be treated as a definitive medical or disease
diagnosis system.

### 3.3 Honey Traceability

The system shall provide unique digital identities for:

- Beekeepers
- Hives
- Harvests
- Honey batches
- Physical seals
- Laboratory tests
- Packages

The system shall maintain the relationship between these identities.

### 3.4 Laboratory Verification

The system shall allow authorized laboratories to:

- Receive or identify a honey batch.
- Verify the Batch ID and Seal ID.
- Record laboratory test information.
- Record PASS or FAIL results.
- Reference laboratory reports.

Laboratory testing is responsible for determining the physical quality or
adulteration status of the tested honey sample.

### 3.5 Chain of Custody

The system shall link the physical honey container with its digital
record using a Batch ID and a tamper-evident Seal ID.

If the seal presented during packaging does not match the seal recorded
during laboratory testing, the system shall flag the batch for further
inspection.

### 3.6 Blockchain Traceability

The system shall record important supply-chain events on blockchain.

Examples include:

- Batch creation
- Seal assignment
- Laboratory testing
- Laboratory approval
- Packaging verification
- Package creation
- Ownership or supply-chain transfers

Detailed sensor data and large documents shall remain in the database
or appropriate storage rather than being stored directly on blockchain.

### 3.7 QR Verification

Each approved retail package shall have a unique QR code.

Consumers shall be able to scan the QR code and view relevant information
such as:

- Package ID
- Batch ID
- Source hive
- Harvest information
- Laboratory verification status
- Seal verification status
- Supply-chain history

### 3.8 Authority/KVIC Monitoring

The system shall provide an authority dashboard through which authorized
users can view:

- Registered beekeepers
- Registered hives
- Hive conditions
- Honey production
- Honey batches
- Laboratory results
- AI alerts
- Suspicious or quarantined batches
- Regional production information

### 3.9 Marketplace

A future module shall connect beekeepers, cooperatives, processors and
buyers to improve market access.

The marketplace is not part of the initial MVP.

---

## 4. User Roles

### 4.1 Administrator

The administrator shall:

- Manage users.
- Manage system configuration.
- Manage authorized roles.
- Monitor the overall system.

### 4.2 Beekeeper

The beekeeper shall:

- Register and manage hives.
- View hive data.
- View AI alerts.
- View production predictions.
- Record harvests.
- View honey batch status.

### 4.3 Laboratory

The laboratory shall:

- View assigned batches.
- Verify Batch ID and Seal ID.
- Enter laboratory test results.
- Record PASS or FAIL status.
- Reference laboratory reports.

### 4.4 Processor

The processor shall:

- Receive approved batches.
- Verify Batch ID and Seal ID.
- Record processing activities.
- Create package records.

### 4.5 KVIC/Authority

The authority user shall:

- Monitor registered beekeepers and hives.
- Monitor honey production.
- Monitor laboratory verification.
- View AI alerts.
- Investigate suspicious batches.
- Monitor traceability information.

### 4.6 Consumer

The consumer shall:

- Scan a package QR code.
- View product traceability information.
- View laboratory verification status.
- Verify package and batch information.

---

## 5. Functional Requirements

The system shall provide:

### User Management

- User registration.
- User login.
- Role-based access control.
- User profile management.

### Hive Management

- Hive registration.
- Hive status management.
- Hive information viewing.
- Historical sensor data viewing.

### IoT Data

- Simulated sensor data generation.
- Sensor data transmission to the backend.
- Sensor data storage.
- Historical data retrieval.

### AI/ML

- Anomaly detection.
- Alert generation.
- Honey production prediction.
- Historical analysis.

### Harvest and Batch Management

- Harvest creation.
- Batch creation.
- Batch status management.
- Batch quantity tracking.

### Seal Management

- Unique Seal ID assignment.
- Batch-Seal relationship.
- Seal verification.
- Seal mismatch detection.

### Laboratory

- Laboratory registration.
- Test record creation.
- Test result management.
- Laboratory report reference.

### Processing and Packaging

- Processing record creation.
- Package creation.
- Package status management.
- Package-Batch relationship.

### Blockchain

- Important event recording.
- Transaction/hash reference storage.
- Traceability verification.

### QR

- QR generation.
- Package identification.
- Consumer verification.

### Authority Dashboard

- Production monitoring.
- Hive monitoring.
- Alert monitoring.
- Batch monitoring.
- Laboratory monitoring.

---

## 6. Non-Functional Requirements

### Security

The system shall provide:

- Authentication.
- Authorization.
- Password protection.
- Role-based access control.
- Secure API communication.
- Blockchain transaction integrity.

### Performance

The system should respond quickly to normal user requests and should
support multiple hives and users as the system grows.

### Scalability

The initial prototype shall support a small number of simulated hives,
but the architecture should allow future expansion to many hives.

### Reliability

Sensor data and important transaction information should be stored
reliably.

### Usability

The user interfaces should be simple and understandable for:

- Beekeepers
- Laboratory users
- Authority users
- Consumers

### Maintainability

The system shall use modular components so that IoT hardware can replace
the simulator in a future version without major changes to the backend.

---

## 7. MVP Scope

The first working prototype shall contain:

1. One or more simulated hives.
2. Simulated temperature, humidity, weight and activity data.
3. FastAPI backend.
4. PostgreSQL database.
5. AI anomaly detection.
6. Basic honey production prediction.
7. Harvest and batch creation.
8. Batch and Seal ID system.
9. Laboratory test records.
10. Blockchain traceability.
11. Package creation.
12. QR-based consumer verification.
13. Basic beekeeper dashboard.
14. Basic authority/KVIC dashboard.

---

## 8. Future Scope

Future versions may include:

- Real ESP32-based IoT hardware.
- Physical temperature and humidity sensors.
- Hive weight sensors.
- Camera-based bee activity monitoring.
- Computer vision.
- Weather API integration.
- Advanced AI/ML models.
- Mobile application.
- Large-scale authority deployment.
- Advanced marketplace.
- IoT gateway supporting multiple physical hives.

---

## 9. Important System Limitation

Blockchain does not physically test honey and cannot by itself guarantee
that the physical contents of a container have not been substituted.

HoneyChain therefore combines:

- Laboratory testing
- Tamper-evident physical seals
- Digital identities
- Controlled chain of custody
- Blockchain records
- QR verification

This makes unauthorized substitution easier to detect and provides a
verifiable digital history of the honey batch.