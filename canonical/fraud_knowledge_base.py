"""
===========================================================
ARVIND
Adaptive Risk & Verification Intelligence
for Next-generation Detection
===========================================================

Module:
Fraud Knowledge Base

Purpose:
Defines ARVIND's Canonical Fraud Knowledge Base used by
Schema Intelligence, Rule Engine, Behaviour Engine, Statistics,
Scoring, and AI Investigation.

Owner:
Canonical Data Layer

Sprint:
v0.4

Author:
Rohit Sharma
Partner & CTO: ChatGPT

===========================================================
"""


ACFKB_VERSION = "1.0"


FRAUD_KNOWLEDGE_BASE = {
    # =====================================================
    # TRANSACTION FIELDS
    # =====================================================

    "transaction_id": {
        "display_name": "Transaction ID",
        "category": "Transaction",
        "subcategory": "Identifier",
        "description": "Unique identifier for the transaction.",
        "business_purpose": "Used to track, deduplicate and investigate transactions.",
        "data_type": "string",
        "required_level": "critical",
        "aliases": [
            "transaction_id", "txn_id", "tx_id", "payment_id",
            "auth_id", "authorization_id", "order_id", "booking_id"
        ],
        "example_values": ["TXN123456", "AUTH98765"],
        "validation_rules": ["Must not be empty", "Should be unique"],
        "fraud_importance": "critical",
        "supported_engines": [
            "schema_intelligence", "rule_engine", "ai_engine", "case_management"
        ],
        "relationships": ["transaction_timestamp", "transaction_amount"],
        "risk_notes": "Duplicate transaction IDs may indicate data quality issues or repeated processing.",
        "ai_usage": "Used to reference the transaction in investigation summaries.",
        "future_usage": "Can link to PSP, issuer processor or case management systems."
    },

    "transaction_timestamp": {
        "display_name": "Transaction Timestamp",
        "category": "Transaction",
        "subcategory": "Time",
        "description": "Date and time when the transaction was attempted or authorised.",
        "business_purpose": "Used for velocity, timing, out-of-hours and travel consistency checks.",
        "data_type": "datetime",
        "required_level": "critical",
        "aliases": [
            "transaction_date", "transaction_time", "txn_date", "txn_time",
            "auth_time", "auth_date", "created_at", "payment_date", "date_of_transaction"
        ],
        "example_values": ["2026-07-06 12:30:00"],
        "validation_rules": ["Must be parseable as date/time"],
        "fraud_importance": "critical",
        "supported_engines": [
            "schema_intelligence", "rule_engine", "behavioural_engine",
            "statistical_engine", "travel_engine", "ai_engine"
        ],
        "relationships": ["transaction_amount", "transaction_country", "date_of_travel"],
        "risk_notes": "Unusual transaction timing can support account takeover or misuse detection.",
        "ai_usage": "Used to explain timing and velocity risk.",
        "future_usage": "Can support real-time streaming fraud detection."
    },

    "transaction_amount": {
        "display_name": "Transaction Amount",
        "category": "Transaction",
        "subcategory": "Value",
        "description": "Monetary value of the transaction.",
        "business_purpose": "Used for high-value, outlier, velocity and exposure analysis.",
        "data_type": "decimal",
        "required_level": "critical",
        "aliases": [
            "amount", "txn_amount", "txn_amt", "transaction_value",
            "payment_amount", "purchase_amount", "auth_amount",
            "total_amount", "charge_amount", "value"
        ],
        "example_values": ["120.50", "3900.00"],
        "validation_rules": ["Must be numeric", "Must be greater than or equal to zero"],
        "fraud_importance": "critical",
        "supported_engines": [
            "schema_intelligence", "rule_engine", "statistical_engine",
            "scoring_engine", "ai_engine"
        ],
        "relationships": ["currency", "merchant_name", "customer_id"],
        "risk_notes": "Large deviations from historical spend can indicate fraud or misuse.",
        "ai_usage": "Used to explain financial exposure and transaction severity.",
        "future_usage": "Can support loss forecasting and financial impact modelling."
    },

    "currency": {
        "display_name": "Currency",
        "category": "Transaction",
        "subcategory": "Value",
        "description": "Currency used for the transaction.",
        "business_purpose": "Used for FX, country and spend analysis.",
        "data_type": "string",
        "required_level": "high",
        "aliases": ["currency", "ccy", "txn_currency", "transaction_currency", "payment_currency"],
        "example_values": ["GBP", "EUR", "USD"],
        "validation_rules": ["Should be ISO currency code where possible"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "rule_engine", "statistical_engine", "ai_engine"],
        "relationships": ["transaction_amount", "transaction_country"],
        "risk_notes": "Unexpected currency may indicate cross-border risk or unusual behaviour.",
        "ai_usage": "Used to explain currency mismatch or travel-related context.",
        "future_usage": "Can support FX fraud and exposure analysis."
    },

    "transaction_status": {
        "display_name": "Transaction Status",
        "category": "Transaction",
        "subcategory": "Authorisation",
        "description": "Outcome of the transaction attempt.",
        "business_purpose": "Used to identify approvals, declines, reversals and repeated failures.",
        "data_type": "string",
        "required_level": "critical",
        "aliases": [
            "status", "txn_status", "transaction_status", "payment_status",
            "auth_status", "authorisation_status", "authorization_status", "result"
        ],
        "example_values": ["Approved", "Declined", "Reversed"],
        "validation_rules": ["Should map to approved, declined, reversed or unknown"],
        "fraud_importance": "critical",
        "supported_engines": ["schema_intelligence", "rule_engine", "statistical_engine", "ai_engine"],
        "relationships": ["decline_reason", "transaction_timestamp"],
        "risk_notes": "Multiple declines followed by approval may suggest card testing or attack behaviour.",
        "ai_usage": "Used to explain transaction outcome and decline patterns.",
        "future_usage": "Can support approval rate optimisation."
    },

    "decline_reason": {
        "display_name": "Decline Reason",
        "category": "Transaction",
        "subcategory": "Authorisation",
        "description": "Reason provided for a declined transaction.",
        "business_purpose": "Used to understand card testing, insufficient funds, CVV mismatch or issuer declines.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": [
            "decline_reason", "decline_code", "failure_reason", "response_code",
            "auth_response", "issuer_response", "reason_code"
        ],
        "example_values": ["CVV mismatch", "Insufficient funds", "Do not honour"],
        "validation_rules": ["Can be empty for approved transactions"],
        "fraud_importance": "high",
        "supported_engines": ["schema_intelligence", "rule_engine", "ai_engine"],
        "relationships": ["transaction_status", "cvv_result", "avs_result"],
        "risk_notes": "Repeated CVV or AVS failures can support fraud suspicion.",
        "ai_usage": "Used to explain why a transaction failed.",
        "future_usage": "Can be normalised by PSP response code mapping."
    },

    # =====================================================
    # CARD FIELDS
    # =====================================================

    "card_token": {
        "display_name": "Card Token",
        "category": "Card",
        "subcategory": "Identifier",
        "description": "Tokenised card identifier used instead of raw card number.",
        "business_purpose": "Used as the anchor for Shopper Fingerprint Intelligence.",
        "data_type": "string",
        "required_level": "critical",
        "aliases": [
            "card_token", "payment_token", "card_id", "card_number_token",
            "pan_token", "tokenised_card", "tokenized_card"
        ],
        "example_values": ["card_tok_12345"],
        "validation_rules": ["Must not contain full raw PAN"],
        "fraud_importance": "critical",
        "supported_engines": [
            "schema_intelligence", "behavioural_engine",
            "statistical_engine", "scoring_engine", "ai_engine"
        ],
        "relationships": ["email_domain", "device_fingerprint", "chargeback_history"],
        "risk_notes": "Multiple unrelated identities using the same card may indicate misuse or compromise.",
        "ai_usage": "Used to explain Shopper Fingerprint consistency or mismatch.",
        "future_usage": "Can support graph-based identity intelligence."
    },

    "card_bin": {
        "display_name": "Card BIN",
        "category": "Card",
        "subcategory": "Issuer Identification",
        "description": "First 6-8 digits identifying the card issuer.",
        "business_purpose": "Used to identify issuer, issuing country, scheme, product and BIN risk.",
        "data_type": "string",
        "required_level": "high",
        "aliases": [
            "bin", "card_bin", "issuer_bin", "iin",
            "issuer_identification_number", "card_iin"
        ],
        "example_values": ["400000", "510000"],
        "validation_rules": ["Must be numeric", "Length should be 6 to 8 digits"],
        "fraud_importance": "critical",
        "supported_engines": [
            "schema_intelligence", "rule_engine", "behavioural_engine",
            "statistical_engine", "ai_engine"
        ],
        "relationships": ["card_issuing_country", "card_issuer_name", "card_scheme", "card_type"],
        "risk_notes": "BIN mismatch with transaction country or customer history can increase risk.",
        "ai_usage": "Used to explain issuer and country mismatch risk.",
        "future_usage": "Can connect to external BIN intelligence providers."
    },

    "card_issuing_country": {
        "display_name": "Card Issuing Country",
        "category": "Card",
        "subcategory": "Issuer Geography",
        "description": "Country where the card was issued.",
        "business_purpose": "Used for country mismatch and cross-border risk analysis.",
        "data_type": "string",
        "required_level": "high",
        "aliases": [
            "card_country", "issuer_country", "issuing_country",
            "card_issuing_country", "bin_country"
        ],
        "example_values": ["GB", "US", "IN"],
        "validation_rules": ["Should be country code or country name"],
        "fraud_importance": "high",
        "supported_engines": ["schema_intelligence", "rule_engine", "behavioural_engine", "ai_engine"],
        "relationships": ["card_bin", "transaction_country", "billing_country"],
        "risk_notes": "Issuer country mismatch may be valid for travel but suspicious without context.",
        "ai_usage": "Used to explain geographic mismatch.",
        "future_usage": "Can support country risk scoring."
    },

    "card_scheme": {
        "display_name": "Card Scheme",
        "category": "Card",
        "subcategory": "Network",
        "description": "Card network or scheme.",
        "business_purpose": "Used for network-specific rules and dispute handling.",
        "data_type": "string",
        "required_level": "high",
        "aliases": ["scheme", "card_scheme", "network", "card_network", "payment_method"],
        "example_values": ["Visa", "Mastercard", "Amex", "Diners"],
        "validation_rules": ["Should map to known card network"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "rule_engine", "ai_engine"],
        "relationships": ["card_bin", "payment_method", "liability_shift"],
        "risk_notes": "Different schemes may have different fraud and chargeback rules.",
        "ai_usage": "Used to explain scheme-specific authentication or chargeback context.",
        "future_usage": "Can support scheme rule libraries."
    },

    "card_type": {
        "display_name": "Card Type",
        "category": "Card",
        "subcategory": "Product",
        "description": "Whether the card is credit, debit, prepaid or corporate.",
        "business_purpose": "Used for card product risk and corporate card interpretation.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["card_type", "credit_debit", "funding_source", "payment_card_type"],
        "example_values": ["Credit", "Debit", "Prepaid", "Corporate"],
        "validation_rules": ["Should map to known card type"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "rule_engine", "ai_engine"],
        "relationships": ["card_product", "card_scheme", "card_bin"],
        "risk_notes": "Prepaid or unusual card type may change risk interpretation.",
        "ai_usage": "Used in card product explanations.",
        "future_usage": "Can support issuer-product risk analytics."
    },

    "card_issuer_name": {
        "display_name": "Card Issuer Name",
        "category": "Card",
        "subcategory": "Issuer",
        "description": "Name of the issuing bank or institution.",
        "business_purpose": "Used for issuer-level performance, risk and authorisation behaviour.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["issuer", "issuer_name", "card_issuer", "issuing_bank", "bank_name"],
        "example_values": ["Barclays", "Chase", "HSBC"],
        "validation_rules": ["Free text accepted"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "statistical_engine", "ai_engine"],
        "relationships": ["card_bin", "card_issuing_country"],
        "risk_notes": "Issuer-level decline or fraud trends may matter operationally.",
        "ai_usage": "Used to explain issuer context.",
        "future_usage": "Can support issuer performance dashboards."
    },

        "card_last4": {
        "display_name": "Card Last 4 Digits",
        "category": "Card",
        "subcategory": "Identifier",
        "description": "Last four digits of the card number.",
        "business_purpose": "Used for analyst reference, customer verification and card identification.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": [
            "card_last4",
            "card_last_4",
            "last4",
            "last_4",
            "card_last_digits",
            "pan_last4"
        ],
        "example_values": ["3301", "4421"],
        "validation_rules": ["Should be 4 digits"],
        "fraud_importance": "medium",
        "supported_engines": [
            "schema_intelligence",
            "rule_engine",
            "ai_engine",
            "case_management"
        ],
        "relationships": ["card_token", "card_bin", "cardholder_name"],
        "risk_notes": "Card last 4 is not sufficient for fraud detection alone but helps investigation and verification.",
        "ai_usage": "Used to reference the card safely in investigation summaries.",
        "future_usage": "Can support cardholder call verification workflows."
    },

    # =====================================================
    # CUSTOMER / IDENTITY FIELDS
    # =====================================================

    "customer_email": {
        "display_name": "Customer Email",
        "category": "Customer",
        "subcategory": "Identity",
        "description": "Email address linked to the customer or user.",
        "business_purpose": "Used for identity, domain, corporate and Shopper Fingerprint analysis.",
        "data_type": "string",
        "required_level": "high",
        "aliases": [
            "email", "customer_email", "user_email", "shopper_email",
            "billing_email", "email_address", "payer_email"
        ],
        "example_values": ["name@company.com"],
        "validation_rules": ["Should contain @"],
        "fraud_importance": "critical",
        "supported_engines": [
            "schema_intelligence", "behavioural_engine",
            "rule_engine", "ai_engine"
        ],
        "relationships": ["email_domain", "corporate_id", "card_token"],
        "risk_notes": "Unrelated email domains using same card can indicate misuse.",
        "ai_usage": "Used to explain identity mismatch or corporate consistency.",
        "future_usage": "Can connect to email reputation and domain age checks."
    },

    "email_domain": {
        "display_name": "Email Domain",
        "category": "Customer",
        "subcategory": "Identity",
        "description": "Domain part of the email address after @.",
        "business_purpose": "Used to detect corporate identity clusters and unrelated users.",
        "data_type": "string",
        "required_level": "high",
        "aliases": ["email_domain", "domain", "customer_domain", "shopper_domain"],
        "example_values": ["deloitte.com", "gmail.com"],
        "validation_rules": ["Can be derived from customer_email"],
        "fraud_importance": "critical",
        "supported_engines": [
            "schema_intelligence", "behavioural_engine",
            "scoring_engine", "ai_engine"
        ],
        "relationships": ["customer_email", "corporate_id", "card_token"],
        "risk_notes": "Same corporate domain may reduce risk; unrelated domains may increase risk.",
        "ai_usage": "Used for Shopper Fingerprint explanations.",
        "future_usage": "Can support corporate domain trust models."
    },

    "first_name": {
        "display_name": "First Name",
        "category": "Customer",
        "subcategory": "Identity",
        "description": "Customer or cardholder first name.",
        "business_purpose": "Used for identity consistency checks.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["first_name", "firstname", "given_name", "customer_first_name"],
        "example_values": ["John", "Priya"],
        "validation_rules": ["Free text accepted"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "behavioural_engine", "ai_engine"],
        "relationships": ["last_name", "cardholder_name", "passenger_name"],
        "risk_notes": "Name mismatch may support identity risk when combined with other signals.",
        "ai_usage": "Used in identity consistency explanation.",
        "future_usage": "Can support fuzzy name matching."
    },

    "last_name": {
        "display_name": "Last Name",
        "category": "Customer",
        "subcategory": "Identity",
        "description": "Customer or cardholder last name.",
        "business_purpose": "Used for identity consistency checks.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["last_name", "lastname", "surname", "family_name", "customer_last_name"],
        "example_values": ["Smith", "Sharma"],
        "validation_rules": ["Free text accepted"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "behavioural_engine", "ai_engine"],
        "relationships": ["first_name", "cardholder_name", "passenger_name"],
        "risk_notes": "Name mismatch may support identity risk when combined with other signals.",
        "ai_usage": "Used in identity consistency explanation.",
        "future_usage": "Can support fuzzy name matching."
    },

    "cardholder_name": {
        "display_name": "Cardholder Name",
        "category": "Customer",
        "subcategory": "Identity",
        "description": "Name printed or associated with the payment card.",
        "business_purpose": "Used to compare payer, traveller and card identity.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["cardholder_name", "card_holder_name", "name_on_card", "card_name"],
        "example_values": ["John Smith"],
        "validation_rules": ["Free text accepted"],
        "fraud_importance": "high",
        "supported_engines": ["schema_intelligence", "behavioural_engine", "travel_engine", "ai_engine"],
        "relationships": ["passenger_name", "customer_email", "card_token"],
        "risk_notes": "Mismatch between cardholder and passenger may be normal in corporate travel but should be contextualised.",
        "ai_usage": "Used to explain identity and travel consistency.",
        "future_usage": "Can support fuzzy matching and corporate booking policies."
    },

    # =====================================================
    # CORPORATE FIELDS
    # =====================================================

    "employee_id": {
        "display_name": "Employee ID",
        "category": "Corporate",
        "subcategory": "Employee",
        "description": "Unique identifier for the employee or corporate user.",
        "business_purpose": "Used to link corporate card activity to a known employee profile.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": [
            "employee_id",
            "emp_id",
            "staff_id",
            "user_id",
            "traveller_id",
            "traveler_id"
        ],
        "example_values": ["EMP12345"],
        "validation_rules": ["Free text accepted"],
        "fraud_importance": "high",
        "supported_engines": [
            "schema_intelligence",
            "behavioural_engine",
            "corporate_rules",
            "ai_engine"
        ],
        "relationships": ["corporate_id", "customer_email", "card_token"],
        "risk_notes": "Employee ID helps distinguish legitimate corporate/shared-card behaviour from suspicious identity mismatch.",
        "ai_usage": "Used to explain corporate user consistency.",
        "future_usage": "Can support employee-level spending and behavioural profiles."
    },

    "company_name": {
        "display_name": "Company Name",
        "category": "Corporate",
        "subcategory": "Company",
        "description": "Name of the corporate customer or employer.",
        "business_purpose": "Used to understand corporate account context.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": [
            "company_name",
            "company",
            "organisation_name",
            "organization_name",
            "employer_name",
            "client_name"
        ],
        "example_values": ["Deloitte", "Wise", "Perk"],
        "validation_rules": ["Free text accepted"],
        "fraud_importance": "medium",
        "supported_engines": [
            "schema_intelligence",
            "behavioural_engine",
            "ai_engine"
        ],
        "relationships": ["corporate_id", "email_domain", "corporate_profile"],
        "risk_notes": "Company context can reduce false positives for corporate travel and shared-card behaviour.",
        "ai_usage": "Used to explain corporate relationship context.",
        "future_usage": "Can support corporate entity risk profiling."
    },

    "corporate_id": {
        "display_name": "Corporate ID",
        "category": "Corporate",
        "subcategory": "Account",
        "description": "Identifier for the corporate customer or company.",
        "business_purpose": "Used to group employees, cards and policies under a corporate account.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["corporate_id", "company_id", "client_id", "account_id", "organisation_id", "organization_id"],
        "example_values": ["CORP12345"],
        "validation_rules": ["Free text accepted"],
        "fraud_importance": "high",
        "supported_engines": ["schema_intelligence", "behavioural_engine", "corporate_rules", "ai_engine"],
        "relationships": ["corporate_profile", "email_domain", "employee_id"],
        "risk_notes": "Corporate context can reduce false positives for shared card usage.",
        "ai_usage": "Used to explain corporate identity cluster.",
        "future_usage": "Can support corporate policy engines."
    },

    "corporate_profile": {
        "display_name": "Corporate Profile",
        "category": "Corporate",
        "subcategory": "Account",
        "description": "Corporate profile or business account classification.",
        "business_purpose": "Used for policy, spending and identity grouping.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["corporate_profile", "profile_name", "company_profile", "business_profile"],
        "example_values": ["Deloitte UK Travel"],
        "validation_rules": ["Free text accepted"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "behavioural_engine", "ai_engine"],
        "relationships": ["corporate_id", "email_domain"],
        "risk_notes": "Corporate profile helps explain legitimate shared-card or delegated booking behaviour.",
        "ai_usage": "Used in corporate context explanations.",
        "future_usage": "Can support policy-based risk decisions."
    },

    # =====================================================
    # MERCHANT FIELDS
    # =====================================================

    "merchant_id": {
        "display_name": "Merchant ID",
        "category": "Merchant",
        "subcategory": "Identifier",
        "description": "Unique merchant identifier.",
        "business_purpose": "Used for merchant behaviour, risk and trend analysis.",
        "data_type": "string",
        "required_level": "high",
        "aliases": ["merchant_id", "mid", "merchant_account", "merchant_identifier"],
        "example_values": ["MID12345"],
        "validation_rules": ["Free text accepted"],
        "fraud_importance": "high",
        "supported_engines": ["schema_intelligence", "rule_engine", "behavioural_engine", "statistical_engine", "ai_engine"],
        "relationships": ["merchant_name", "merchant_category_code", "merchant_country"],
        "risk_notes": "First-time or high-risk merchant activity can increase risk.",
        "ai_usage": "Used in merchant behaviour explanation.",
        "future_usage": "Can support merchant reputation scoring."
    },

    "merchant_name": {
        "display_name": "Merchant Name",
        "category": "Merchant",
        "subcategory": "Identity",
        "description": "Name of the merchant.",
        "business_purpose": "Used for merchant recognition and behavioural comparison.",
        "data_type": "string",
        "required_level": "high",
        "aliases": ["merchant", "merchant_name", "merchant_nm", "merchant_desc", "merchant_description"],
        "example_values": ["Apple Store", "British Airways"],
        "validation_rules": ["Free text accepted"],
        "fraud_importance": "high",
        "supported_engines": ["schema_intelligence", "rule_engine", "behavioural_engine", "ai_engine"],
        "relationships": ["merchant_id", "merchant_category_code"],
        "risk_notes": "New merchant or unusual merchant category may increase risk.",
        "ai_usage": "Used to explain merchant familiarity or novelty.",
        "future_usage": "Can support merchant clustering."
    },

    "merchant_category_code": {
        "display_name": "Merchant Category Code",
        "category": "Merchant",
        "subcategory": "MCC",
        "description": "Merchant category code describing merchant type.",
        "business_purpose": "Used for high-risk category rules and corporate policy checks.",
        "data_type": "string",
        "required_level": "high",
        "aliases": ["mcc", "mcc_code", "merchant_category_code", "merchant_category", "merchant_cat_code"],
        "example_values": ["5812", "4511", "5732"],
        "validation_rules": ["Usually four digits"],
        "fraud_importance": "critical",
        "supported_engines": ["schema_intelligence", "rule_engine", "behavioural_engine", "corporate_rules", "ai_engine"],
        "relationships": ["merchant_name", "merchant_id"],
        "risk_notes": "Certain MCCs such as electronics, gambling or money transfer may carry higher risk.",
        "ai_usage": "Used to explain merchant category risk.",
        "future_usage": "Can support industry-specific risk policy."
    },

    # =====================================================
    # GEOGRAPHY / BILLING
    # =====================================================

    "transaction_country": {
        "display_name": "Transaction Country",
        "category": "Transaction",
        "subcategory": "Geography",
        "description": "Country where the transaction occurred.",
        "business_purpose": "Used for geographic mismatch, travel and country-risk analysis.",
        "data_type": "string",
        "required_level": "high",
        "aliases": ["transaction_country", "txn_country", "payment_country", "country", "merchant_country"],
        "example_values": ["GB", "US", "DE"],
        "validation_rules": ["Should be country code or country name"],
        "fraud_importance": "high",
        "supported_engines": ["schema_intelligence", "rule_engine", "behavioural_engine", "travel_engine", "ai_engine"],
        "relationships": ["card_issuing_country", "billing_country", "departure_country", "destination_country"],
        "risk_notes": "New country may be suspicious unless supported by travel context.",
        "ai_usage": "Used to explain geographic behaviour.",
        "future_usage": "Can connect to country risk scoring."
    },

    "billing_postcode": {
        "display_name": "Billing Postcode",
        "category": "Billing",
        "subcategory": "Address",
        "description": "Postal or ZIP code from billing address.",
        "business_purpose": "Used for AVS and billing identity checks.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["postcode", "post_code", "zip", "zip_code", "billing_postcode", "billing_zip"],
        "example_values": ["SE10 0AA", "10001"],
        "validation_rules": ["Free text accepted due to international formats"],
        "fraud_importance": "high",
        "supported_engines": ["schema_intelligence", "rule_engine", "ai_engine"],
        "relationships": ["billing_country", "avs_result", "avs_score"],
        "risk_notes": "Postcode mismatch may increase risk, especially for US transactions.",
        "ai_usage": "Used in AVS and billing mismatch explanations.",
        "future_usage": "Can support address normalisation."
    },

    "billing_country": {
        "display_name": "Billing Country",
        "category": "Billing",
        "subcategory": "Address",
        "description": "Billing address country.",
        "business_purpose": "Used for AVS and geographic consistency checks.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["billing_country", "bill_country", "address_country"],
        "example_values": ["GB", "US"],
        "validation_rules": ["Should be country code or country name"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "rule_engine", "ai_engine"],
        "relationships": ["billing_postcode", "transaction_country", "card_issuing_country"],
        "risk_notes": "Billing country mismatch may increase risk when combined with other signals.",
        "ai_usage": "Used in geographic mismatch explanations.",
        "future_usage": "Can support address reputation checks."
    },

    # =====================================================
    # DEVICE / BROWSER / OS
    # =====================================================

    "device_fingerprint": {
        "display_name": "Device Fingerprint",
        "category": "Device",
        "subcategory": "Identifier",
        "description": "Unique or semi-unique device fingerprint.",
        "business_purpose": "Used for device recognition and Shopper Fingerprint analysis.",
        "data_type": "string",
        "required_level": "high",
        "aliases": ["device_fingerprint", "fingerprint", "fp", "device_id", "device_hash", "FrigerPrint"],
        "example_values": ["fp_abc123"],
        "validation_rules": ["Free text accepted"],
        "fraud_importance": "critical",
        "supported_engines": ["schema_intelligence", "behavioural_engine", "scoring_engine", "ai_engine"],
        "relationships": ["browser", "operating_system", "card_token", "customer_email"],
        "risk_notes": "New device can increase risk, especially with identity or country mismatch.",
        "ai_usage": "Used to explain device consistency or anomaly.",
        "future_usage": "Can support device reputation and graph analysis."
    },

    "device_type": {
        "display_name": "Device Type",
        "category": "Device",
        "subcategory": "Device Profile",
        "description": "Type of device used.",
        "business_purpose": "Used to identify behavioural changes between phone, laptop, tablet etc.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["device", "device_type", "device_category", "platform_type"],
        "example_values": ["Phone", "Laptop", "Tablet"],
        "validation_rules": ["Should map to known device types where possible"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "behavioural_engine", "ai_engine"],
        "relationships": ["device_fingerprint", "browser", "operating_system"],
        "risk_notes": "Device type changes may support behavioural anomaly detection.",
        "ai_usage": "Used in device behaviour summaries.",
        "future_usage": "Can support emulator or automation detection."
    },

    "browser": {
        "display_name": "Browser",
        "category": "Browser",
        "subcategory": "Client Environment",
        "description": "Internet browser used for the transaction.",
        "business_purpose": "Used for behavioural device intelligence.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["browser", "internet_browser", "web_browser", "browser_name"],
        "example_values": ["Chrome", "Safari", "Firefox"],
        "validation_rules": ["Free text accepted"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "behavioural_engine", "ai_engine"],
        "relationships": ["browser_version", "device_fingerprint", "operating_system"],
        "risk_notes": "Unexpected browser change may be suspicious when combined with other changes.",
        "ai_usage": "Used to explain browser behaviour.",
        "future_usage": "Can support browser reputation and automation detection."
    },

    "browser_version": {
        "display_name": "Browser Version",
        "category": "Browser",
        "subcategory": "Client Environment",
        "description": "Version of the browser used.",
        "business_purpose": "Used to detect browser downgrade or unusual client behaviour.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["browser_version", "browser_ver", "browser_release", "browser_build"],
        "example_values": ["139.0", "114.0"],
        "validation_rules": ["Free text accepted"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "behavioural_engine", "ai_engine"],
        "relationships": ["browser", "device_fingerprint"],
        "risk_notes": "Sudden downgrade from recent browser version to old version may indicate suspicious device change.",
        "ai_usage": "Used in browser downgrade explanation.",
        "future_usage": "Can compare against latest stable versions."
    },

    "operating_system": {
        "display_name": "Operating System",
        "category": "Operating System",
        "subcategory": "Client Environment",
        "description": "Operating system used during transaction.",
        "business_purpose": "Used for behavioural device intelligence.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["os", "operating_system", "operating_system_name", "platform"],
        "example_values": ["Windows", "iOS", "Android", "macOS"],
        "validation_rules": ["Free text accepted"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "behavioural_engine", "ai_engine"],
        "relationships": ["operating_system_version", "device_fingerprint", "browser"],
        "risk_notes": "Unexpected OS change may indicate a new or compromised device.",
        "ai_usage": "Used to explain OS behaviour changes.",
        "future_usage": "Can support rooted/jailbroken device signals."
    },

    "operating_system_version": {
        "display_name": "Operating System Version",
        "category": "Operating System",
        "subcategory": "Client Environment",
        "description": "Version of the operating system.",
        "business_purpose": "Used to detect OS downgrade or unusual device environment.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["os_version", "operating_system_version", "platform_version"],
        "example_values": ["Windows 11", "iOS 18"],
        "validation_rules": ["Free text accepted"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "behavioural_engine", "ai_engine"],
        "relationships": ["operating_system", "device_fingerprint"],
        "risk_notes": "OS downgrade may indicate suspicious environment change.",
        "ai_usage": "Used to explain OS anomaly.",
        "future_usage": "Can compare against normal upgrade patterns."
    },

    # =====================================================
    # AUTHENTICATION / VERIFICATION
    # =====================================================

    "avs_result": {
        "display_name": "AVS Result",
        "category": "Verification",
        "subcategory": "Address Verification",
        "description": "Address verification result.",
        "business_purpose": "Used to validate billing address, especially for US transactions.",
        "data_type": "string",
        "required_level": "high",
        "aliases": ["avs", "avs_result", "avs_response", "avs_resp", "address_verification_result"],
        "example_values": ["Match", "No Match", "Partial Match"],
        "validation_rules": ["Should map to match, partial, no match, unavailable"],
        "fraud_importance": "critical",
        "supported_engines": ["schema_intelligence", "rule_engine", "scoring_engine", "ai_engine"],
        "relationships": ["avs_score", "billing_postcode", "billing_country"],
        "risk_notes": "AVS failure is particularly relevant for US-issued cards and US customers.",
        "ai_usage": "Used to explain address verification risk.",
        "future_usage": "Can support country-specific AVS rules."
    },

    "avs_score": {
        "display_name": "AVS Score",
        "category": "Verification",
        "subcategory": "Address Verification",
        "description": "Normalised score representing AVS strength.",
        "business_purpose": "Used to quantify address verification strength.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["avs_score", "avs_code", "avs_match_score"],
        "example_values": ["Y", "N", "A", "Z"],
        "validation_rules": ["Provider-specific values should be normalised"],
        "fraud_importance": "high",
        "supported_engines": ["schema_intelligence", "rule_engine", "scoring_engine", "ai_engine"],
        "relationships": ["avs_result", "billing_postcode"],
        "risk_notes": "Weak AVS result may increase risk when combined with other indicators.",
        "ai_usage": "Used to explain AVS scoring.",
        "future_usage": "Can support PSP-specific AVS code dictionaries."
    },

    "cvv_result": {
        "display_name": "CVV Result",
        "category": "Verification",
        "subcategory": "Card Verification",
        "description": "Result of CVV verification.",
        "business_purpose": "Used to validate card security code.",
        "data_type": "string",
        "required_level": "high",
        "aliases": ["cvv", "cvv_result", "cvv_match", "cvc_result", "cvc_match", "security_code_result"],
        "example_values": ["Matched", "Not Matched", "Unavailable"],
        "validation_rules": ["Should map to matched, not matched, unavailable"],
        "fraud_importance": "critical",
        "supported_engines": ["schema_intelligence", "rule_engine", "scoring_engine", "ai_engine"],
        "relationships": ["transaction_status", "decline_reason"],
        "risk_notes": "CVV mismatch can indicate card testing or unauthorised card use.",
        "ai_usage": "Used to explain card verification risk.",
        "future_usage": "Can support issuer response normalisation."
    },

    "three_ds_enabled": {
        "display_name": "3DS Enabled",
        "category": "Authentication",
        "subcategory": "3DS",
        "description": "Whether 3DS was enabled or available.",
        "business_purpose": "Used to assess authentication strength.",
        "data_type": "boolean",
        "required_level": "medium",
        "aliases": ["3ds_enabled", "three_ds_enabled", "is_3ds", "secure_3d_enabled"],
        "example_values": ["True", "False"],
        "validation_rules": ["Should map to true or false"],
        "fraud_importance": "high",
        "supported_engines": ["schema_intelligence", "rule_engine", "ai_engine"],
        "relationships": ["three_ds_version", "three_ds_eci", "liability_shift"],
        "risk_notes": "Absence of 3DS may increase risk depending on region and exemption.",
        "ai_usage": "Used to explain authentication strength.",
        "future_usage": "Can support SCA exemption analytics."
    },

    "three_ds_version": {
        "display_name": "3DS Version",
        "category": "Authentication",
        "subcategory": "3DS",
        "description": "Version of 3D Secure used.",
        "business_purpose": "Used to understand authentication protocol and friction.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["3ds_version", "three_ds_version", "3d_secure_version"],
        "example_values": ["2.1", "2.2"],
        "validation_rules": ["Free text accepted"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "rule_engine", "ai_engine"],
        "relationships": ["three_ds_enabled", "three_ds_eci", "three_ds_challenged"],
        "risk_notes": "Older or failed 3DS behaviour may matter in authentication risk.",
        "ai_usage": "Used in authentication explanation.",
        "future_usage": "Can support protocol performance dashboards."
    },

    "three_ds_eci": {
        "display_name": "3DS ECI Value",
        "category": "Authentication",
        "subcategory": "3DS",
        "description": "Electronic Commerce Indicator value from 3DS.",
        "business_purpose": "Used to determine authentication result and liability context.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["eci", "eci_value", "3ds_eci", "three_ds_eci", "authentication_eci"],
        "example_values": ["05", "06", "07"],
        "validation_rules": ["Provider-specific values should be normalised"],
        "fraud_importance": "high",
        "supported_engines": ["schema_intelligence", "rule_engine", "scoring_engine", "ai_engine"],
        "relationships": ["liability_shift", "three_ds_enabled"],
        "risk_notes": "ECI value can affect liability and fraud interpretation.",
        "ai_usage": "Used to explain liability and authentication outcome.",
        "future_usage": "Can support scheme-specific ECI interpretation."
    },

    "liability_shift": {
        "display_name": "Liability Shift",
        "category": "Authentication",
        "subcategory": "3DS",
        "description": "Whether fraud liability shifted due to authentication.",
        "business_purpose": "Used for fraud exposure and chargeback risk assessment.",
        "data_type": "boolean",
        "required_level": "medium",
        "aliases": ["liability_shift", "liability_shifted", "fraud_liability_shift", "shifted_liability"],
        "example_values": ["True", "False"],
        "validation_rules": ["Should map to true or false"],
        "fraud_importance": "critical",
        "supported_engines": ["schema_intelligence", "rule_engine", "scoring_engine", "ai_engine"],
        "relationships": ["three_ds_eci", "three_ds_enabled", "chargeback_history"],
        "risk_notes": "No liability shift can increase financial exposure.",
        "ai_usage": "Used to explain financial and chargeback exposure.",
        "future_usage": "Can support dispute liability analysis."
    },

    # =====================================================
    # TRAVEL FIELDS
    # =====================================================

    "passenger_name": {
        "display_name": "Passenger Name",
        "category": "Travel",
        "subcategory": "Traveller",
        "description": "Name of passenger or traveller.",
        "business_purpose": "Used to compare traveller with cardholder and corporate user.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["passenger", "passenger_name", "traveller_name", "traveler_name", "pax_name"],
        "example_values": ["John Smith"],
        "validation_rules": ["Free text accepted"],
        "fraud_importance": "high",
        "supported_engines": ["schema_intelligence", "travel_engine", "behavioural_engine", "ai_engine"],
        "relationships": ["cardholder_name", "customer_email", "corporate_id"],
        "risk_notes": "Passenger mismatch may be normal in business travel but requires context.",
        "ai_usage": "Used to explain travel identity consistency.",
        "future_usage": "Can support fuzzy traveller matching."
    },

    "carrier_code": {
        "display_name": "Carrier Code",
        "category": "Travel",
        "subcategory": "Airline",
        "description": "Airline or carrier code.",
        "business_purpose": "Used for route, airline and travel behaviour analysis.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["carrier", "carrier_code", "airline_code", "supplier_code"],
        "example_values": ["BA", "LH", "AF"],
        "validation_rules": ["Usually 2-character airline code but flexible"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "travel_engine", "ai_engine"],
        "relationships": ["departure_airport", "destination_airport", "date_of_travel"],
        "risk_notes": "Unusual carrier may support travel anomaly analysis.",
        "ai_usage": "Used in travel itinerary explanation.",
        "future_usage": "Can support supplier and airline risk analysis."
    },

    "date_of_travel": {
        "display_name": "Date of Travel",
        "category": "Travel",
        "subcategory": "Itinerary",
        "description": "Date when travel is due to occur.",
        "business_purpose": "Used to determine whether foreign transactions are consistent with travel.",
        "data_type": "date",
        "required_level": "medium",
        "aliases": ["travel_date", "date_of_travel", "departure_date", "flight_date"],
        "example_values": ["2026-08-24"],
        "validation_rules": ["Must be parseable as date"],
        "fraud_importance": "high",
        "supported_engines": ["schema_intelligence", "travel_engine", "rule_engine", "ai_engine"],
        "relationships": ["transaction_timestamp", "departure_airport", "destination_airport"],
        "risk_notes": "Travel date can explain otherwise unusual country activity.",
        "ai_usage": "Used to explain whether geography is consistent with travel.",
        "future_usage": "Can support itinerary-aware fraud models."
    },

    "departure_airport": {
        "display_name": "Departure Airport",
        "category": "Travel",
        "subcategory": "Route",
        "description": "Origin airport for flight itinerary.",
        "business_purpose": "Used for route and travel consistency analysis.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["departure_airport", "origin_airport", "from_airport", "dep_airport"],
        "example_values": ["LHR", "JFK"],
        "validation_rules": ["Usually IATA airport code but flexible"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "travel_engine", "ai_engine"],
        "relationships": ["destination_airport", "date_of_travel"],
        "risk_notes": "Route context may explain cross-border card activity.",
        "ai_usage": "Used in route consistency explanation.",
        "future_usage": "Can support route risk scoring."
    },

    "destination_airport": {
        "display_name": "Destination Airport",
        "category": "Travel",
        "subcategory": "Route",
        "description": "Destination airport for flight itinerary.",
        "business_purpose": "Used for route and travel consistency analysis.",
        "data_type": "string",
        "required_level": "medium",
        "aliases": ["destination_airport", "arrival_airport", "to_airport", "arr_airport"],
        "example_values": ["CDG", "DXB"],
        "validation_rules": ["Usually IATA airport code but flexible"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "travel_engine", "ai_engine"],
        "relationships": ["departure_airport", "date_of_travel", "transaction_country"],
        "risk_notes": "Destination can explain transaction country changes.",
        "ai_usage": "Used in travel geography explanation.",
        "future_usage": "Can support route risk scoring."
    },

    "hotel_check_in": {
        "display_name": "Hotel Check In",
        "category": "Hotel",
        "subcategory": "Accommodation",
        "description": "Indicates whether hotel check-in exists or hotel was booked.",
        "business_purpose": "Used to understand full travel context.",
        "data_type": "boolean",
        "required_level": "low",
        "aliases": ["hotel_check_in", "hotel_booked", "hotel_yn", "accommodation_booked"],
        "example_values": ["Y", "N", "True", "False"],
        "validation_rules": ["Should map to true or false"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "travel_engine", "ai_engine"],
        "relationships": ["date_of_travel", "destination_airport"],
        "risk_notes": "Hotel booking may support legitimacy of travel-related spend.",
        "ai_usage": "Used in travel context explanation.",
        "future_usage": "Can support hotel fraud intelligence."
    },

    "flight_and_hotel_booked": {
        "display_name": "Flight and Hotel Both Booked",
        "category": "Travel",
        "subcategory": "Package",
        "description": "Indicates whether both flight and hotel are booked.",
        "business_purpose": "Used to understand travel completeness and legitimacy.",
        "data_type": "boolean",
        "required_level": "low",
        "aliases": ["flight_and_hotel", "flight_hotel_booked", "package_booking", "flight_and_hotel_booked"],
        "example_values": ["Y", "N"],
        "validation_rules": ["Should map to true or false"],
        "fraud_importance": "medium",
        "supported_engines": ["schema_intelligence", "travel_engine", "ai_engine"],
        "relationships": ["hotel_check_in", "date_of_travel", "destination_airport"],
        "risk_notes": "Complete travel context can reduce false positives.",
        "ai_usage": "Used in travel legitimacy explanation.",
        "future_usage": "Can support package travel risk models."
    },

    # =====================================================
    # RISK / HISTORY FIELDS
    # =====================================================

    "chargeback_history": {
        "display_name": "Chargeback History",
        "category": "Risk",
        "subcategory": "Historical Risk",
        "description": "Historical chargeback count or indicator linked to card, customer or merchant.",
        "business_purpose": "Used to understand previous dispute or fraud risk.",
        "data_type": "integer",
        "required_level": "medium",
        "aliases": ["chargeback_history", "chargebacks", "chargeback_count", "previous_chargebacks"],
        "example_values": ["0", "2"],
        "validation_rules": ["Should be numeric if count-based"],
        "fraud_importance": "critical",
        "supported_engines": ["schema_intelligence", "rule_engine", "behavioural_engine", "scoring_engine", "ai_engine"],
        "relationships": ["card_token", "customer_email", "merchant_id"],
        "risk_notes": "Prior chargebacks increase risk and may influence call priority.",
        "ai_usage": "Used to explain historical risk.",
        "future_usage": "Can support chargeback prediction."
    },

    "previous_fraud_flag": {
        "display_name": "Previous Fraud Flag",
        "category": "Risk",
        "subcategory": "Historical Risk",
        "description": "Indicates whether the entity has previous confirmed or suspected fraud.",
        "business_purpose": "Used for historical fraud context.",
        "data_type": "boolean",
        "required_level": "medium",
        "aliases": ["previous_fraud", "fraud_history", "previous_fraud_flag", "known_fraud"],
        "example_values": ["True", "False"],
        "validation_rules": ["Should map to true or false"],
        "fraud_importance": "critical",
        "supported_engines": ["schema_intelligence", "rule_engine", "scoring_engine", "ai_engine"],
        "relationships": ["card_token", "customer_email", "merchant_id", "device_fingerprint"],
        "risk_notes": "Previous confirmed fraud strongly increases risk.",
        "ai_usage": "Used to explain prior fraud evidence.",
        "future_usage": "Can support entity reputation scoring."
    }
}


def get_all_fields() -> dict:
    """
    Returns the full ARVIND Fraud Knowledge Base.
    """
    return FRAUD_KNOWLEDGE_BASE


def get_field(field_id: str) -> dict | None:
    """
    Returns one canonical field by field_id.
    """
    return FRAUD_KNOWLEDGE_BASE.get(field_id)


def get_fields_by_category(category: str) -> dict:
    """
    Returns all fields belonging to a specific category.
    """
    return {
        field_id: metadata
        for field_id, metadata in FRAUD_KNOWLEDGE_BASE.items()
        if metadata["category"].lower() == category.lower()
    }


def get_required_fields(required_level: str = "critical") -> dict:
    """
    Returns fields by required level.
    """
    return {
        field_id: metadata
        for field_id, metadata in FRAUD_KNOWLEDGE_BASE.items()
        if metadata["required_level"].lower() == required_level.lower()
    }


def get_alias_map() -> dict:
    """
    Creates a reverse lookup from alias to canonical field_id.

    Example:
    txn_amt -> transaction_amount
    issuer_bin -> card_bin
    """
    alias_map = {}

    for field_id, metadata in FRAUD_KNOWLEDGE_BASE.items():
        for alias in metadata["aliases"]:
            alias_map[alias.lower()] = field_id

    return alias_map