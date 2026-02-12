# Vendor WHT Approval Engine (Odoo 16)

## Overview

Vendor WHT Approval Engine is an Odoo 16 custom module that introduces a structured Withholding Tax (WHT) control layer for Vendor Bills.

This module demonstrates ERP design thinking, accounting governance, and upgrade-safe customization without modifying Odoo core.

It provides:

- Automatic WHT calculation
- Approval workflow based on financial threshold
- Posting control enforcement
- Segregation of duties implementation
- REST API integration support

---

## Business Context

Withholding Tax (WHT) is a compliance mechanism where a company deducts tax before paying a vendor and remits it to the tax authority.

Example:

Invoice Total: 100,000  
WHT (3%): 3,000  
Net Payment: 97,000  

Improper handling may lead to:

- Compliance risk
- Financial misstatement
- Audit findings
- Fraud exposure

This module introduces governance controls aligned with financial risk management principles.

---

## Key Features

### 1. Automatic WHT Calculation
- Configurable WHT rate (default 3%)
- Auto-compute WHT amount
- Net payment calculation
- Applies only to Vendor Bills (`in_invoice`)

### 2. Approval Workflow
- Bills above threshold (e.g., 50,000) require Manager approval
- Enforced at model level (not only UI)
- Posting blocked until approved

### 3. Segregation of Duties
- Vendor WHT Officer
- Vendor WHT Manager
- Role-based access control

### 4. Upgrade-Safe Design
- No core modification
- Clean model inheritance
- Separation between document lifecycle and approval layer

### 5. REST API Endpoint

Endpoint:

POST /api/vendor_bill

Example request:

```json
{
  "vendor": "ABC Supplier",
  "amount": 100000
}
```

Example response:

```json
{
  "id": 45,
  "wht_amount": 3000
}
```

The API simulates external ERP integration while maintaining internal approval governance.

---

## Technical Design
### Extended Model

Model: `account.move`

Additional Fields:
- `x_wht_rate`
- `x_wht_amount`
- `x_approval_state`
- `x_is_approved`

### Approval Enforcement

Posting protection implemented via:

```python
action_post()
```

Approval method:

```python
action_approve()
```

UI restrictions are reinforced by server-side validation.

---

## Demonstration Flow

1. Create Vendor Bill
2. WHT auto-calculates
3. Send for approval
4. Manager approves
5. Post document
6. (Optional) Create via API

---

## Installation

1. Place module inside custom addons path
2. Update Apps list
3. Install `Demo Vendor WHT Engine`

Dependencies:
- `account`

---

## Design Principles

- Separation of concerns
- Integration-ready architecture
- Upgrade-safe customization

---

## Demo Access

The live demo environment can be accessed using the URL listed in the GitHub repository description above.
Please use the demo credentials provided below to log in.

### Available Users

**1. Administrator (Full Access)**
- Username: `admin`
- Password: `admin`

Use this account to:
- Install modules
- Configure settings
- Approve high-value Vendor Bills
- Access technical features

---

**2. Demo User (Standard Officer Role)**
- Username: `demo`
- Password: `demo`

Use this account to:
- Create Vendor Bills
- Trigger WHT calculation
- Submit documents for approval
- Test API-generated records

---

## Suggested Demo Flow

1. Login as `demo`
2. Create a Vendor Bill above threshold
3. Observe automatic WHT calculation
4. Submit for approval
5. Logout
6. Login as `admin`
7. Approve and post the document
8. Print WHT report

---

### Author

Phurin Nararat

Odoo Developer Demonstration Project