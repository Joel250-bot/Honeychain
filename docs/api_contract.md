# HoneyChain API Contract

## 1. Purpose

This document defines the API communication standards between the HoneyChain modules.

The backend API acts as the central communication layer between:

- IoT Simulator
- AI/ML Module
- Blockchain Module
- Frontend
- QR Verification
- Database
- KVIC Dashboard

---

## 2. API Standards

- Protocol: HTTP/HTTPS
- Architecture: REST
- Data Format: JSON
- Authentication: JWT
- Database: PostgreSQL
- Time Format: ISO 8601 UTC
- Temperature Unit: °C
- Humidity Unit: %
- Weight Unit: kg
- Activity Score: 0–100

---

## 3. Identifier Convention

Internal database records use UUIDs.

Human-readable public identifiers are used by the system:

- Beekeeper: `BK-001`
- Hive: `HIVE-001`
- Harvest: `HV-2026-001`
- Batch: `HC-2026-00125`
- Seal: `S-84521`
- Lab Test: `LAB-TEST-0042`
- Package: `PKG-00001`

The backend resolves public codes to internal database IDs.

---

# 4. Authentication APIs

## Register

`POST /auth/register`

### Request

```json
{
  "name": "John",
  "email": "john@example.com",
  "password": "password",
  "role": "beekeeper"
}