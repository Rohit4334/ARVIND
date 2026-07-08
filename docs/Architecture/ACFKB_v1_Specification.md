# ARVIND Canonical Fraud Knowledge Base  
## ACFKB v1.0 Specification

Sprint: v0.4  
Owner: Rohit Sharma  
Partner & CTO: ChatGPT  

---

## 1. Purpose

The ARVIND Canonical Fraud Knowledge Base is the single source of truth for how ARVIND understands payment, card, customer, device, merchant, travel, authentication, and fraud data.

ARVIND does not analyse raw column names directly.

It first translates incoming data into a canonical fraud language using this knowledge base.

---

## 2. Core Principle

Every fraud decision must be:

- Explainable
- Reproducible
- Evidence-based
- Auditable
- Linked back to raw data

ARVIND does not just score transactions.

ARVIND builds evidence.

---

## 3. What Every Canonical Field Contains

Each canonical field is not just a column name.

Each field is a fraud intelligence object.

Every field should contain:

```text
field_id
display_name
category
subcategory
description
business_purpose
data_type
required_level
aliases
example_values
validation_rules
fraud_importance
supported_engines
relationships
risk_notes
ai_usage
future_usage