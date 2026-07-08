# ARVIND Architecture

## Overview

ARVIND is a modular Fraud Intelligence Platform designed to support explainable fraud investigation workflows.

The platform is built around a simple principle:

> ARVIND does not only score transactions. ARVIND builds evidence.

---

## Architecture Flow

```text
CSV Upload
    ↓
Data Intelligence Engine
    ↓
Schema Intelligence
    ↓
Canonical Fraud Knowledge Base
    ↓
Fraud Rule Library
    ↓
Fraud Rule Engine
    ↓
Evidence Engine
    ↓
Fraud Service
    ↓
Case Management Engine
    ↓
Investigation Workspace
    ↓
Executive Dashboard

Core Modules
1. UI Layer

Location:

ui/

Responsible for:

Application pages
Reusable UI components
Header
Executive KPI cards
Status badges
Investigation cards
2. Data Ingestion

Location:

ingestion/

Responsible for:

Reading uploaded CSV files
Profiling data
Calculating data quality
Preparing raw data for schema mapping
3. Canonical Layer

Location:

canonical/

Responsible for:

Canonical Fraud Knowledge Base
Field definitions
Alias mapping
Fraud Rule Library
Schema mapping

This layer allows ARVIND to understand different PSP-style datasets.

4. Intelligence Layer

Location:

intelligence/

Responsible for:

Fraud rule execution
Evidence generation
Future behavioural intelligence
Future statistical intelligence
Future AI investigation logic
5. Service Layer

Location:

services/

Responsible for orchestration.

Main services:

fraud_service.py
case_service.py

The service layer connects data, rules, evidence, and case management.

Key Design Decisions
Canonical Fraud Knowledge Base

ARVIND does not rely on fixed CSV column names.

Instead, uploaded fields are mapped to canonical fraud fields such as:

Transaction Amount
Card BIN
AVS Result
CVV Result
Customer Email
Device Fingerprint
Transaction Country

This makes ARVIND adaptable to different payment data structures.

Fraud Rule Library

Rules are defined as metadata rather than being hardcoded directly into logic.

Each rule includes:

Rule name
Severity
Risk points
Business reason
Evidence type
Required fields
Recommended investigation

This makes the rule engine easier to expand.

Evidence Engine

Every triggered rule becomes a structured evidence object.

Evidence includes:

Source engine
Finding
Severity
Confidence
Business reason
Recommended investigation

This enables explainable fraud decisions.

Case Management

Analysed transactions are converted into fraud investigation cases.

Each case includes:

Case ID
Case status
Case priority
Assigned analyst
Final decision
Evidence
Analyst notes

This reflects how fraud operations teams actually work.

Current Capabilities

Version 0.10 includes:

CSV upload
Data profiling
Data quality scoring
Schema intelligence
Canonical fraud mapping
Rule library
Rule engine
Evidence engine
Case management
Investigation workspace
Executive dashboard
Multi-analyst notes
Future Architecture

Future modules are designed to plug into the same evidence pipeline.

Planned modules:

Browser Intelligence
Device Intelligence
Email Intelligence
Phone Intelligence
Shopper Fingerprint
Corporate Intelligence
Statistical Intelligence
AI Investigator
Voice Verification
PDF Investigation Reports

Each future engine should produce structured evidence that can be consumed by the Case Management and AI layers.

Design Philosophy

ARVIND follows these principles:

Explainability over black-box scoring
Evidence-first fraud decisions
Modular architecture
Human-centred investigation workflows
Extendable design for future intelligence engines
Version

Current Release:

ARVIND v0.10
Foundation Release