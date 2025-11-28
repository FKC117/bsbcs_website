# Happy : Supply Chain Management Platform ****

1. **Document Overview**
2. **Executive Summary**
3. **Purpose of the System**
4. **Scope of the System**
5. **Business Domain Background**
6. **Operational Context (Bangladesh FMCG Market Landscape)**
7. **User Role Overview (High-Level)**
8. **System Vision Statement**
9. **Stakeholders & Stakeholder Needs**
10. **High-Level System Goals & Objectives**
11. **Product Positioning**

---

# ---------------------------------------------------

# **1. DOCUMENT OVERVIEW**

# ---------------------------------------------------

This Software Requirements Specification (SRS) describes the complete functional, non-functional, business, and technical requirements for **Happy**, a multi-role, multi-layer sales and distribution management platform designed for Bangladesh’s FMCG and retail supply chain sector.

It follows a **Hybrid SRS Methodology** combining:

- **IEEE-830 formal documentation structure**,
- **Modern SaaS Product Specification**,
- **User Personas**,
- **Detailed Functional Requirements**,
- **Use Cases & User Stories**,
- **Process Flow Diagrams**,
- **Entity Interaction Models**,
- **End-to-End Lifecycle Descriptions**,
- **Operational Scenarios**,
- **Business Constraints**,
- **System Behaviour Definitions**.

# ---------------------------------------------------

# 2. EXECUTIVE SUMMARY

# ---------------------------------------------------

**Happy** is a centralized digital ecosystem that integrates and streamlines all layers of FMCG distribution in Bangladesh, connecting:

- **Super Admin & Admin** → top-level controllers
- **Dealers** → multi-company distributors
- **Sales Representatives (SR)** → order generators
- **Pickup Man** → warehouse stock receivers
- **Packing Man** → order consolidators
- **Delivery Man** → final-mile executors
- **Customer Care** → tele-order operators
- **Retailers** → the final customers who purchase and sell goods

The platform unifies:

- order processing
- warehouse stock management
- multi-company product catalog management
- real-time delivery operations
- profit, commission, and investment accounting
- route planning
- retailer engagement
- financial settlements

The system provides **full accountability**, **transparent inventory flow**, and **data-driven insights** for sustainable FMCG distribution management.

---

# ---------------------------------------------------

# 3. PURPOSE OF THE SYSTEM

# ---------------------------------------------------

The main purpose of **Happy** is to:

✔ Digitize and centralize Bangladesh’s physical FMCG distribution workflow

✔ Bring transparency to stock movement, order lifecycle, delivery attempts, and payments

✔ Empower Dealers, SRs, and Delivery Man with modern tools

✔ Enable Retailers to order conveniently through mobile

✔ Provide the Admin-level users with complete operational visibility

✔ Ensure profitability tracking from dealer, company, and Happy’s own perspective

✔ Standardize routes, service areas, and delivery behaviours.

✔ Enforce strict accountability across all field agents

✔ Automate daily operational challenges including:

- stock receiving
- packing flows
- dispatching
- deliveries
- returns
- damages
- due payments
- commissions
- withdrawal requests

---

# ---------------------------------------------------

# 4. SCOPE OF THE SYSTEM

# ---------------------------------------------------

## 4.1 In-Scope

The system will include:

### 🔹 **User Management & Access Control**

- Role-based access
- Multi-role permission matrix
- Workspace-level restrictions
- Per-dealer product visibility
- Company assignment & warehouse assignment

### 🔹 **Product & Inventory Lifecycle**

- Multi-company product catalog
- Warehouse stock in/out
- Batch-level tracking
- Expiry, variant pricing, damaged stocks
- Delivery-man inventory visibility
- Real-time stock adjustments

### 🔹 **End-to-End Order Management**

**Supported order types:**

1. Sales Representative Order
2. Delivery Man Custom Order
3. Ready Sell from Warehouse
4. Tele Order
5. Retailer Self Order

Includes:

- Custom pricing
- Negotiations
- Partially fulfilled orders
- Order revision
- Multi-SR merged packing
- Dispatch & delivery
- Due collections
- Return-to-warehouse
- Automatic next-day retry

### 🔹 **Financial & Profitability System**

- Dealer investment
- Dealer commission
- SR over commissions
- Happy’s own commissions
- Withdrawal request workflow
- Revenue, profit, and settlement reports

### 🔹 **Route & Area Management**

- Day-wise SR routes
- Fixed delivery-man routes
- Area → Union → Wards
- Dealer service area
- Retailer clustering

### 🔹 **Dashboards & Analytics**

- Real-time dashboards
- Top SRs
- Top retailers
- Top selling products
- Profit ratio
- Delivery success ratio

---

## 4.2 Out of Scope (Initial Version)

- IoT-based real-time vehicle tracking (future)
- Automated warehouse robotic systems (future)
- Integration with ERP systems (future)
- Bank API integration (future version may include)
- Multi-language support (future phase)

---

# ---------------------------------------------------

# 5. BUSINESS DOMAIN BACKGROUND

# ---------------------------------------------------

Bangladesh’s FMCG distribution relies heavily on:

- physical sales representatives
- territory-based dealer networks
- cash-heavy transactions
- manual tracking of stocks
- verbal negotiation-based pricing
- inconsistent delivery patterns
- paper-based order entries

### **Common problems observed in current real-world operations:**

| Problem | Impact |
| --- | --- |
| Manual order tracking | Loss of accountability & disputes |
| Lack of unified stock system | Over/under selling |
| Multiple order sources | Difficult reconciliation |
| Unplanned routes | Low delivery success rate |
| No standardized pricing | Conflicts during settlements |
| Cash/due management issues | Loss of revenue |
| No visibility of SR performance | Poor productivity |
| No transparency for dealers | Profit leakage |

**Happy** solves these with a **single unified digital platform**.

---

# ---------------------------------------------------

# 6. OPERATIONAL CONTEXT (FMCG MARKET)

# ---------------------------------------------------

### 6.1 Geographic Complexity

- Union/Upazila based dealer operations
- SRs must repeatedly visit assigned routes
- Delivery constraints based on area overpopulation/road access

### 6.2 Retail Behavior

- Retailers often negotiate prices
- Retailers demand credit (due)
- Retailers reorder frequently in small quantities

### 6.3 Multi-Company Dealers

Dealers in Bangladesh usually handle:

- 3–20 companies simultaneously
- multiple product lines
- different commission structures
- different expiry policies

### 6.4 Field Workforce

SRs, Deliverymen, Pickup Men, Packers — all operate manually, often:

- without records
- without accountability
- with communication gaps
- with no performance tracking

---

# ---------------------------------------------------

# 7. USER ROLE OVERVIEW (HIGH-LEVEL)

# ---------------------------------------------------

### **7.1 High-Level Role Hierarchy Diagram**

```
                       ┌──────────────────────┐
                       │     Super Admin      │
                       └──────────┬───────────┘
                                  │
                       ┌──────────┴───────────┐
                       │        Admin          │
                       └──────────┬────────────┘
                     Assigns / Manages:
                                  │
    ┌──────────────┬──────────────┼──────────────┬──────────────┬───────────────┐
    │              │              │              │               │               │
 Dealer       Sales Rep      Pickup Man      Packing Man     Delivery Man     Customer Care
    │                                 (Merged under Admin)                      │
    └────────────────────────────────────────────────────────────────────────────┘
                                  Retailer

```

---

# ---------------------------------------------------

# 8. SYSTEM VISION STATEMENT

# ---------------------------------------------------

**Happy** aims to become **Bangladesh’s most advanced, reliable, and scalable digital distribution management platform**, empowering all stakeholders with real-time data, structured workflows, transparent accountability, and financial clarity.

The long-term vision includes:

- Marketplace integration
- Automated warehouse management
- Credit scoring for retailers
- Advanced AI forecasting for demand
- ERP-like financial modules
- Multi-region operations

---

# ---------------------------------------------------

# 9. STAKEHOLDERS & STAKEHOLDER NEEDS

# ---------------------------------------------------

### **9.1 Stakeholder Groups & Their Interests**

| Stakeholder | Interests | Needs |
| --- | --- | --- |
| Super Admin | Complete system oversight | Security, visibility, control |
| Admin | Daily operations, user management | Tools to assign roles, view reports |
| Dealer | Profit, stock, SR performance | Clear stock, route & profit tracking |
| Sales Representative | Faster order taking | Easy mobile UI, real-time stock |
| Delivery Man | Smooth delivery workflow | Fixed routes, order visibility |
| Packing Man | Efficient packing | Merged SR orders per retailer |
| Pickup Man | Stock receiving | Variant pricing, expiry management |
| Customer Care | Tele-ordering | Fast manual order creation |
| Retailer | Self-ordering, dues | Transparent history & invoices |

---

# ---------------------------------------------------

# 10. HIGH-LEVEL SYSTEM GOALS & OBJECTIVES

# ---------------------------------------------------

### **10.1 Main Goals**

1. Digitize the entire distribution chain
2. Ensure 100% traceability of stock
3. Enforce route discipline
4. Centralize all types of orders
5. Provide real-time operational dashboards
6. Enable negotiation-ready orders
7. Maintain profit accounting for all actors
8. Offer reliable due and payment tracking

### **10.2 System-Wide Objectives**

- Reduce manual errors
- Increase daily order volume
- Improve delivery success rate
- Ensure accountability across roles
- Produce data-driven insights for strategic growth

---

# ---------------------------------------------------

# 11. PRODUCT POSITIONING

# ---------------------------------------------------

### **11.1 Target Users**

- FMCG dealers
- Distribution companies
- Direct-to-retailer supply chains
- Regional distributors

### **11.2 Market Differentiation**

Happy stands out through:

- Role-specific dashboards
- Dynamic multi-company product visibility
- Robust order life cycles
- Transparent SR and dealer performance
- Advanced profit modeling
- Real-time stock value calculations
- Per-role tightly controlled access

---

# ---------------------------------------------------

# **12. DETAILED USER PERSONAS**

# ---------------------------------------------------

This section describes the **operational personas** involved in Happy, detailing their needs, behaviors, frustrations, technological comfort, and motivations. These personas help shape system features aligned with real-world expectations.

---

## **12.1 Super Admin**

### **Profile**

- Master authority over entire system
- Oversees all Admins, Dealers, SRs, Warehouses
- High business & financial awareness

### **Goals**

- Maintain full control over user access & permissions
- Track system-wide financial performance
- Ensure operational transparency
- Enforce compliance and reduce abuse

### **Pain Points**

- Hard to validate field claims without system proof
- Fraudulent or manipulated stock entries
- Missing or incomplete documentation

### **Motivations**

- Ensure long-term sustainability of operations
- Maintain data integrity & security

---

## **12.2 Admin**

### **Profile**

- Operational controller of daily activities
- Manages users, areas, routes, orders, warehouses

### **Goals**

- Keep operations running smoothly
- Ensure every order is processed, packed, and delivered
- Validate delivery failures or disputes

### **Pain Points**

- Tracking thousands of small orders
- Verifying delivery man faults
- Manual stock reconciliation

### **Motivations**

- Increase operational efficiency
- Reduce conflicts between SR, Dealer, and Delivery Man

---

## **12.3 Dealer**

### **Profile**

- Manages multiple companies
- Oversees SRs, warehouse interactions, and profit

### **Goals**

- Track product-wise summary
- Assign SRs efficiently
- Maximize profit margin
- Make informed investment decisions

### **Pain Points**

- No transparency in SR performance
- Inventory mismatch between warehouse & actual deliveries
- Delayed payment settlements

### **Motivations**

- Grow dealer network
- Reduce operational losses

---

## **12.4 Sales Representative (SR)**

### **Profile**

- Field worker responsible for order generation
- Visits route-based retailers daily

### **Goals**

- Quickly place orders
- See available stocks
- Get best-selling product insights

### **Pain Points**

- Paper-based order writing
- Not knowing real stock instantly
- Retailer negotiation delays

### **Motivations**

- Higher over-commission
- Improved delivery success ratio
- Better retailer relationships

---

## **12.5 Pickup Man**

### **Profile**

- Receives stocks into warehouses
- Handles variants and custom expiry

### **Goals**

- Record proper in-warehouse entries
- Maintain accurate batches

### **Pain Points**

- Complex stock entries (variant price, expiry, damages)

### **Motivations**

- Zero entry error performance metric

---

## **12.6 Packing Man**

### **Profile**

- Packs orders per retailer
- Sees merged multi-SR orders

### **Goals**

- Pack fast
- Avoid mistakes in merged orders

### **Pain Points**

- Mismatching multi-SR orders
- Manual count verification

---

## **12.7 Delivery Man**

### **Profile**

- Delivers orders and creates custom manual orders

### **Goals**

- Efficient delivery
- Collect payment or due

### **Pain Points**

- Retailer negotiation causing delays
- SR overwritten order conflicts

### **Motivations**

- Successful delivery rate increases incentives

---

## **12.8 Customer Care**

### **Profile**

- Creates tele-orders manually for retailers

### **Goals**

- Fast order creation
- Avoid pricing mistakes

---

## **12.9 Retailer**

### **Profile**

- Final buyer
- Wants flexible pricing and credit options

### **Goals**

- Order easily
- Understand their profits
- Track due status

---

# ---------------------------------------------------

# **13. ROLE-BASED CAPABILITY MATRIX**

# ---------------------------------------------------

A structured permission view to illustrate who can perform what actions.

### **13.1 High-Level Role Matrix**

```markdown
┌─────────────────────┬────────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬──────────┐
│ Feature / Module     │ SuperAdmin │ Admin   │ Dealer  │   SR    │ Pickup  │ Packing │ Delivery│ Retailer │
├──────────────────────┼────────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼──────────┤
│ User Management       │   Full     │ Partial │  View   │  -      │   -     │   -     │   -     │    -     │
│ Product Catalog       │   Full     │ Full    │ Custom  │ View    │ View    │ View    │ View    │ View     │
│ Warehouse Management  │  Full      │ Full    │ View    │ -       │ Entry   │ Pack    │ Out     │ -        │
│ Order Placement       │  Create    │ Create  │ -       │ Create  │ -       │ -       │ Create  │ Create   │
│ Order Fulfillment     │  Full      │ Full    │ View    │ View    │ Entry   │ Pack    │ Deliver │ View     │
│ Delivery Management   │  Full      │ Full    │ Track   │ Track   │ -       │ -       │ Self    │ Track    │
│ Finance / Profit      │ Full       │ Full    │ Own     │ Own     │ -       │ -       │ Limited │ Own      │
│ Route Management      │ Full       │ Full    │ View    │ Edit    │ -       │ -       │ View    │ -        │
│ Dashboard & Analytics │ Full       │ Full    │ Partial │ Partial │ Limited │ Limited │ Limited │ Self     │
└──────────────────────┴────────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴──────────┘

```

---

# ---------------------------------------------------

# **14. ACTOR INTERACTION OVERVIEW (SYSTEM-WIDE)**

# ---------------------------------------------------

### **14.1 System Interaction Context Diagram**

```
                          ┌──────────────────┐
                          │  Super Admin     │
                          └───────┬──────────┘
                                  │
                         Manages System Rules
                                  │
                  ┌───────────────┴────────────────┐
                  │                                │
        ┌─────────▼──────────┐           ┌─────────▼───────────┐
        │        Admin        │           │       Dealer         │
        └─────────┬──────────┘           └─────────┬────────────┘
                  │ Assigns Users                 │
                  │                                │ Oversees Stock, Profit
          ┌───────▼─────────┐            ┌────────▼──────────┐
          │       SR         │            │  Pickup / Packing │
          └───────┬─────────┘            └────────┬──────────┘
          Places Orders                    Handles Warehouse In/Pack
                  │                                │
          ┌───────▼─────────┐            ┌─────────▼─────────┐
          │   Delivery Man   │──────────►│     Retailer       │
          └──────────────────┘  Deliver  └────────────────────┘

```

---

# ---------------------------------------------------

# **15. HIGH-LEVEL USE CASE DIAGRAMS**

# ---------------------------------------------------

### **15.1 Order Lifecycle Use Case Diagram**

```
                ┌─────────────────┐
                │   Sales Rep     │
                └───────┬─────────┘
                        │ Place Order
                        ▼
               ┌────────────────────┐
               │    Order System    │
               └───────┬────────────┘
                       │ Assign to Warehouse
                       ▼
             ┌──────────────────────┐
             │     Packing Man      │
             └──────┬───────────────┘
                    │ Pack
                    ▼
          ┌──────────────────────────┐
          │      Delivery Man        │
          └─────────┬───────────────┘
                    │ Deliver / Collect Due
                    ▼
      ┌──────────────────────────────┐
      │           Retailer           │
      └──────────────────────────────┘

```

---

# ---------------------------------------------------

# **16. EXTENDED USER JOURNEYS (WORKFLOW NARRATIVES)**

# ---------------------------------------------------

This section outlines **real-life operational scenarios** to demonstrate how each role interacts with the system in daily activities.

---

## **16.1 Journey: Sales Representative Places an Order**

1. SR logs into the app → sees their **assigned company products**
2. SR selects retailer from daily **route map**
3. SR views stock availability (real-time from warehouse)
4. SR adds products with **custom negotiated price**
5. SR submits order → retailer receives **push notification**
6. Order moves to **pending packing**
7. Dealer/Admin sees updated summary
8. Delivery Man sees stock allocated for delivery
9. SR sees delivery performance and over-commission

---

## **16.2 Journey: Delivery Man Delivers Order + Negotiation**

1. Delivery Man receives packed order
2. Visits retailer based on fixed route
3. Retailer negotiates quantity or price
4. Delivery Man modifies order (if allowed)
5. If partial delivery → updates system
6. Retailer makes full or due payment
7. Delivery Man submits delivery result
8. Inventory auto-updates with:
    - OUT
    - SOLD
    - RETURN IN
    - DAMAGES

---

## **16.3 Journey: Dealer Manages SR Performance**

1. Dealer enters SR profile
2. Views:
    - order history
    - conversion ratio
    - delivery ratio
    - top/bottom products
    - SR ranking
3. Adjusts SR assignment (areas, companies)
4. Reviews dealer profit summary
5. Submits withdrawal request

---

## **16.4 Journey: Packing Man Packs Multi-SR Orders**

1. Retailer X has 4 orders from 4 SRs
2. System **automatically merges** into one packing list
3. Packing Man selects a **basket**
4. Packs all items together
5. Marks packed → moves to dispatch

---

# ---------------------------------------------------

# **17. EARLY-PHASE SYSTEM CONSTRAINTS**

# ---------------------------------------------------

### **17.1 Operational Constraints**

- Multi-company dealers require **distinct pricing & commission rules**
- Some retailers have **daily, weekly, or irregular order cycles**
- Delivery Men CANNOT alter assigned routes
- SRs can modify ONLY day-wise routes

### **17.2 Functional Constraints**

- Inventory must update **in real-time**
- Order negotiation should preserve traceability
- Retailers must see profit based on dealer price

### **17.3 Technical Constraints**

- PostgreSQL for relational structures
- Redis for caching & queueing
- Scalable micro-modular backend structure
- Mobile-first experience for SR & Delivery Man
- Pack and pickup must support **variant/unit-level batches**

---

# **4. Functional Requirements (FR)**

This section defines *behavior*, *actions*, *system flows*, and *feature-specific rules* for each role.

Requirements are broken down into subsystems for clarity.

---

# **4.1 User & Role Management Module**

## **4.1.1 Overview**

The Happy Platform manages **9 user types**, each with distinct responsibilities and permissions.

Access control is achieved using **RBAC + Fine-grained Feature Permissions**.

**Roles:**

- Super Admin
- Admin
- Dealer
- Sales Representative (SR)
- Delivery Man
- Customer Care
- Retailer
- Pickup Man (merged into Admin)
- Packing Man (merged into Admin)

---

# **4.1.2 User Lifecycle Diagram**

```
             ┌──────────────┐
             │  User Create  │
             └──────┬───────┘
                    │
         ┌──────────▼──────────┐
         │ Role & Permission    │
         │ Assignment (RBAC)    │
         └──────────┬───────────┘
                    │
        ┌───────────▼────────────┐
        │ Profile Setup &         │
        │ Operational Mapping     │
        │ (Area, Dealer, Route…) │
        └───────────┬────────────┘
                    │
           ┌────────▼────────┐
           │   Active User   │
           └────────┬────────┘
                    │
                Deactivate
                    │
           ┌────────▼────────┐
           │   Archive User   │
           └──────────────────┘

```

---

# **4.1.3 User Module Functional Requirements**

### **FR-1: User Creation**

- Super Admin/Admin can create any user type.
- Mandatory fields: name, phone number, password, role, assigned warehouse/area (if required).

### **FR-2: Role Assignment**

- The system must assign a role at creation time.
- Permissions inherited from base role profile.
- Optionally includes custom feature-level overrides.

### **FR-3: User Listing**

- Users displayed by role-specific pages:
    - Dealer List
    - SR List
    - Deliveryman List
    - Retailer List
    - Customer Care
- Includes filters: area, company, warehouse, active/inactive.

### **FR-4: Role-specific Profile View**

Each role gets a customized view:

### **Dealer Profile**

- Assigned companies
- Assigned SRs
- Products list (with commission settings)
- Investment records
- Profit summary
- Withholding requests
- Inventory summary

### **SR Profile**

- Assigned companies
- Assigned dealers
- Assigned area & route list
- Order history
- Delivery success ratio
- Over commission summary

### **Delivery Man Profile**

- Assigned area & warehouse
- Delivered orders
- Delivery faults
- Daily route overview

### **Retailer Profile**

- Order history
- Due management
- Delivery success
- Payment attempt history

### **FR-5: User Status Control**

- Active / Inactive toggle.
- Inactive users cannot log in.

---

# **4.2 Company, Category & Product Management Module**

## **4.2.1 Overview**

The system supports multiple brands/companies under a dealer.

Each company has categories → products → product variants (optional: size, price, expiry).

---

## **4.2.2 Product Lifecycle Diagram**

```
Company
   │
   ├── Category
   │       │
   │       └── Products
   │                │
   │                └── Variants (price, qty, expiry)
   │
   └── Assigned Dealers → Assigned SRs

```

---

## **4.2.3 Functional Requirements**

### **FR-10: Company Management**

- Super Admin/Admin can:
    - Create company
    - Edit details
    - Assign dealers & SRs
    - Control commissions per dealer

### **FR-11: Product Creation**

- Fields:
    - Name
    - Company
    - Category
    - Buying Price
    - Selling Price
    - Expiry Handling Required
    - Minimum Stock Alert

### **FR-12: Dealer Commission Setup**

- Admin sets custom commission:
    - Percentage based
    - Amount per unit
    - Product-level, category-level, or company-level

### **FR-13: SR Order Price Customization**

- SR sees dealer price.
- SR can override the price (per order item) within allowed range.
- System logs:
    - min price allowed
    - SR override price
    - supervisor approval if needed

---

# **4.3 Warehouse & Inventory Module**

## **4.3.1 Overview**

Warehouse inventory comes from:

- Dealer stock entries by Pickup Man/Admin
- SR Orders → Packing → Delivery process
- Reverse stock processes (returns, cancellations)

The system maintains **real-time stock integrity**.

---

## **4.3.2 High-Level Inventory Flow Diagram**

```
                   Products
                       │
                       ▼
          ┌────────────────────────┐
          │      Warehouse Stock   │
          └────────────────────────┘
                │          │
      Pickup Entries     Stock Updates
                │          │
         ┌──────▼──────┐   │
         │ Stock In     │   │
         └──────┬──────┘   │
                │          │
                ▼          ▼
         Packing Stage   Delivery Stage
                │          │
                ▼          ▼
           Inventory Out   Sell / Return

```

---

## **4.3.3 Functional Requirements**

### **FR-20: Warehouse Management**

- Create/Edit warehouse information
- Assign:
    - Areas
    - Deliverymen
    - Pickupmen (Admin merged)

### **FR-21: Stock Entry (Pickup Man/Admin)**

- Pickup Man receives product batches from dealer:
    - Variant quantities
    - Pricing per variant
    - Expiry date per variant

System stores an **entry batch record** for traceability.

### **FR-22: View Warehouse Stock**

- Detailed stock view:
    - Product → variant → quantity → expiry
- Admin can:
    - Manually adjust stock (increase/decrease)
    - Edit expiry
    - Update variant price
    - Log adjustment reasons

### **FR-23: Stock Out Calculation**

Triggered when:

- Packing done
- Dispatch to deliveryman
- Retailer cancels (partial or full)
- Retailer edits value → adjust stock

### **FR-24: Reverse Stock**

Used when:

- Delivery failed
- Products returned
- Excess products sent back to warehouse

System automatically creates:

- **Return Batch Log**
- Updated stock levels

---

# **4.4 Route Management Module**

## **4.4.1 Overview**

Routes are essential for SR operations and Delivery Man operations.

### Differentiation:

- **SR Routes**: editable daily route
- **Delivery Routes**: fixed, cannot be edited by deliveryman

---

## **4.4.2 Functional Requirements**

### **FR-30: Create Routes**

Admin can define:

- Route Name
- Area → union → retailer clusters
- Allowed users:
    - Sales Representatives
    - Delivery Men

### **FR-31: Daily Route for SR**

- SR can modify only the current day's route.
- System logs:
    - Changes made
    - Start/end time
    - Distance covered (optional GPS integration)

### **FR-32: View Retailers on Map**

System shows:

- Nearby retailers
- Route stop points
- SR's live location (optional)
- Retailer last visit info

---

# **4.5 Order Management Module**

## **4.5.1 Overview**

Order types:

1. **SR Orders**
2. **Deliveryman Custom Orders**
3. **Ready Sell Orders** (warehouse)
4. **Tele Orders** (Customer Care)
5. **Retailer Self Orders** (App)

Orders proceed through stages:

```
Placed → Packed → Dispatched → Delivered → Paid (or Due)

```

---

## **4.5.2 Order Flow Diagram**

```
                        ┌────────────┐
                        │ Order Placed│
                        └─────┬──────┘
                              │
                      Validation Engine
                              │
                    ┌────────▼────────┐
                    │ Packing Required │
                    └─────┬──────┬────┘
                          │      │
                   Ready Sell   Normal Order
                          │      │
         ┌────────────────┘      └────────────────┐
         ▼                                         ▼
 Dispatch to Deliveryman                  Packing Stage
         │                                         │
         ▼                                         ▼
  Delivery Attempt ──────► Negotiation (Retailer) ──────► Checkout

```

---

## **4.5.3 Functional Requirements**

### **FR-40: Create Order (SR)**

- SR selects retailer
- Sees:
    - Product list (company filtered)
    - Stock availability
- Adds custom price per product
- Retailer + Dealer receive push notification

### **FR-41: Create Order (Delivery Man)**

- Delivery man can place order for a retailer during visit.
- Price override allowed.

### **FR-42: Ready Sell Order**

- From warehouse inventory
- No delivery charge
- No packing stage

### **FR-43: Tele Orders**

- Customer care creates orders manually
- Optional delivery charges

### **FR-44: Order Editing During Delivery**

Retailer can:

- Cancel fully
- Cancel partially
- Add products
- Change quantities
- Change values
    
    System recalculates:
    
- Out quantity
- Seller profit
- Dealer commission
- SR commission (if applicable)

### **FR-45: Due Management**

Retailer can:

- Pay partial or full later
- Due collection triggers:
    - Negotiation allowance
    - Re-calculation of profitability

### **FR-46: Failed Delivery Handling**

System flags:

- No-action orders
- Deliveryman faults
- Prepare orders for next day’s attempt

---

# **4.6 Packing & Dispatch Module**

## **4.6.1 Overview**

Packing Man sees unique consolidated retailer order.

### Example Scenario:

Retailer01 has orders from 4 SRs → each has multiple order attempts.

Packing Man sees:

👉 **ONE unified order to pack**.

---

## **4.6.2 Functional Requirements**

### **FR-50: Consolidated Order View**

- System merges all pending orders for a retailer
- Shows:
    - Total quantity per product
    - SR reference list

### **FR-51: Basket Assignment**

Packing man:

- Selects basket
- Packs all items in single batch
- Confirms packing to move stock to “Out”

### **FR-52: Dispatch to Delivery Man**

System:

- Assigns basket
- Sends notification to Delivery Man
- Updates inventory out record

---

# **4.7 Delivery Module**

## **4.7.1 Overview**

Delivery man receives dispatched baskets → delivers → collects payments → negotiates → logs outcomes.

---

## **4.7.2 Functional Requirements**

### **FR-60: Deliveryman Dashboard**

Shows:

- Today's route
- Assigned baskets
- Pending deliveries
- Due collection tasks

### **FR-61: Delivery Attempt Workflow**

Deliveryman chooses:

- Deliver as is
- Retailer negotiates → updates order
- Partial cancel
- Product addition
- Due creation

### **FR-62: Delivery Fault Tracking**

Admin can:

- See fault attempts
- Reverse actions
- Penalize or log warnings

---

# **4.8 Dealer Dashboard & Finance Module**

## **4.8.1 Overview**

Dealers see complete financial performance of their operations.

---

## **4.8.2 Functional Requirements**

### **FR-70: Investment Tracking**

Dealer can see:

- Total investment
- Stock valuation
- Incoming & outgoing stock
- Withdrawable balance

### **FR-71: Profit Summary**

- Product-wise profit
- Order-wise profit
- Company-wise profit
- SR performance impact
- Delivery cost adjustments

### **FR-72: SR Comparison Graphs**

- Best SRs
- Order-delivery ratios
- Commission earned
- Historical charts with date filters

### **FR-73: Withdrawal Requests**

- Dealer initiates withdrawal
- Admin reviews & approves

---

# **4.9 Reports & Dashboards Module**

## **4.9.1 Overview**

Admins see entire system analytics:

- Total orders
- Total retailers
- Delivery success rate
- Order value
- Due amount
- Top retailers
- Best selling products
- Best SRs

---

## **4.9.2 Dashboard Diagram**

```
                           DASHBOARD
                ┌────────────────────────────────┐
                │  Key KPIs                       │
                │  - Order Count                  │
                │  - Retailer Count               │
                │  - Delivery Success             │
                │  - Profit / Investment Summary  │
                └────────────────┬────────────────┘
                                 │
         ┌───────────────────────┼──────────────────────────┐
         ▼                       ▼                          ▼
 SR Performance           Product Analytics             Finance Metrics

```

---

# **4.10 Customer Care Module**

### **FR-80: Tele Order Management**

- Creating orders over phone
- Assigning delivery
- Price override
- Delivery charges addition

### **FR-81: Retailer Support Dashboard**

- Order history
- Due status
- Complaint resolution
- Issue tracking

---

# **5. NON-FUNCTIONAL REQUIREMENTS (NFR)**

Non-Functional Requirements define how the system must behave, covering reliability, performance, availability, scalability, maintainability, security, compliance, and usability.

---

# **5.1 Performance Requirements**

### **NFR-1: Response Time**

- 95% of API responses must be within **< 350ms** under normal load.
- Critical endpoints (order placement, stock updates) must respond in **< 250ms**.
- Dashboards with heavy aggregations must load within **< 2 seconds** using Redis caching.

### **NFR-2: Concurrency**

- System must support:
    - **5,000+ concurrent users**
    - **100,000+ daily order operations**
    - **High concurrency for inventory operations** with locking & transactional safety.

### **NFR-3: Real-time Updates**

- Order status changes (packed, dispatched, delivered, canceled) must propagate within **< 1 second** via WebSocket/FCM push.

---

# **5.2 Reliability & Availability**

### **NFR-4: Uptime**

- System must guarantee **99.5% availability** annually.

### **NFR-5: Fault Tolerance**

- System must implement:
    - Graceful degradation
    - Retry logic for communication failures
    - Dead-letter queues for failed background tasks

### **NFR-6: Database Reliability**

- PostgreSQL must run with:
    - Point-in-time recovery (PITR)
    - Automated daily backups
    - Write-Ahead Logging (WAL) archiving

---

# **5.3 Scalability Requirements**

### **NFR-7: Horizontal Scaling**

- Backend, Redis, Notification Service, API gateway must horizontally scale.

### **NFR-8: Micro-modular Architecture**

- Designed for module separation:
    - Inventory Service
    - Order Service
    - User Service
    - Finance Service
    - Notification Service
    - Reporting Service

Each can scale independently.

---

# **5.4 Maintainability**

### **NFR-9: Code Standards**

- Must follow:
    - Clean Architecture
    - ESLint/Prettier enforcement
    - SOLID principles
    - Proper folder grouping by module

### **NFR-10: Logging & Monitoring**

- Must implement:
    - Error Logging (Winston/Pino)
    - Aggregated logs in ELK/Grafana
    - Performance monitoring (Prometheus)

---

# **5.5 Usability Requirements**

### **NFR-11: User Interface Consistency**

- The system must use consistent components across:
    - Admin panel
    - Dealer panel
    - SR app
    - Delivery app
    - Retailer app

### **NFR-12: Mobile-first design**

- SR, Deliveryman, and Retailer interfaces must be:
    - Lightweight
    - Touch-friendly
    - Optimized for offline-first operations

---

# **5.6 Security Requirements**

### **NFR-13: Authentication**

- JWT + Refresh tokens
- Multi-session device tracking
- Device binding for SR/Deliveryman

### **NFR-14: Authorization**

- RBAC with granular ACL (role + feature flags)
- Example:
    - SR cannot edit company list
    - Dealer cannot edit inventory directly
    - Deliveryman cannot edit route

### **NFR-15: Data Encryption**

- Passwords hashed with **bcrypt (12–14 rounds)**
- HTTPS TLS 1.2+
- Sensitive data encrypted at rest

### **NFR-16: Audit Trails**

- All critical actions logged:
    - Stock edits
    - Order delivery/fault attempts
    - Price overrides
    - Withdrawals
    - Commission edits

### **NFR-17: Business Restrictions**

- Delete operations must follow:
    - Soft delete
    - No permanent delete for financial & stock entities

---

# **6. ARCHITECTURE DESIGN**

This section describes the overall internal structure of the system.

---

# **6.1 High-Level System Architecture Diagram**

```
                        ┌──────────────────────────┐
                        │        Client Apps        │
                        │  (Admin, Dealer, SR, etc) │
                        └───────────┬───────────────┘
                                    │ HTTPS
                          ┌─────────▼──────────┐
                          │   API Gateway       │
                          └─────────┬──────────┘
                                    │ Routes
               ┌────────────────────┼──────────────────────┐
               │                    │                      │
       ┌───────▼──────┐    ┌────────▼────────┐    ┌────────▼────────┐
       │ User Service  │    │ Order Service   │    │ Inventory Service│
       └───────┬──────┘    └────────┬────────┘    └────────┬────────┘
               │                    │                      │
               ▼                    ▼                      ▼
     ┌────────────────┐   ┌─────────────────┐    ┌───────────────────┐
     │ Postgres Users │   │ Postgres Orders │    │ Postgres Inventory │
     └────────────────┘   └─────────────────┘    └───────────────────┘
               │                    │                      │
               └──────────────┬─────┴─────┬──────────────┘
                              ▼           ▼
                          ┌──────────────────┐
                          │      Redis       │
                          │  Caching/Queues  │
                          └──────────────────┘

```

---

# **6.2 Architecture Style**

The system follows a **Modular Monolith** transitioning-ready architecture toward **Microservices**.

Modules include:

- User Management Module
- Inventory Module
- Order Module
- Payment & Finance Module
- Reporting Module
- Notification Module

Each module:

- Has own folder/logic
- Has own use cases
- Communicates via internal services
- Uses shared libraries for authentication & validation

---

# **6.3 Domain-Driven Design (DDD) Context Map**

```
[User Context] --------┐
                       │ Provides
[Inventory Context] ---┼------► Stock Info
                       │
[Order Context] -------┘ Requires

[Finance Context] <--------- Order Completion

[Reporting Context] <------- All Contexts

```

Bounded Contexts:

- User Context
- Dealer Context
- Product Context
- Stock/Inventory Context
- Order/Delivery Context
- Accounting Context

---

# **6.4 Infrastructure Layer**

### **Core technologies:**

- **Backend**: Node.js (TypeScript)
- **Database**: PostgreSQL
- **Cache & Queue**: Redis
- **Realtime**: WebSocket + Push notifications
- **CI/CD**: Docker + GitHub Actions
- **Cloud**: AWS (flexible)

---

# **7. SECURITY ARCHITECTURE**

---

# **7.1 Authentication Architecture**

```
Client → API → Auth Service → PostgreSQL / Redis

```

### JWT Flows:

- Access Token (short-lived)
- Refresh Token (long-lived)
- Device binding for SR/Delivery

---

# **7.2 Role-Based Access Control (RBAC) Diagram**

```
                   ┌─────────────────────┐
                   │        Role          │
                   └──────────┬──────────┘
                              │ 1..*
                       ┌──────▼──────┐
                       │Permissions  │
                       └──────┬──────┘
                              │ *..*
                       ┌──────▼────────┐
                       │ Feature Flags  │
                       └───────────────┘

```

Roles map to permissions → which map to feature flags.
Examples:

- SR: `order.create`, `route.view`, `inventory.deliveryView`
- Dealer: `commission.update`, `profit.view`
- Admin: All permissions

---

# **8. BUSINESS PROCESS WORKFLOWS & DIAGRAMS**

Below are major workflow diagrams used for compliance, audit, and engineering clarity.

---

# **8.1 Order Lifecycle – Detailed BPMN Diagram**

```
Start
 │
 ▼
Order Placed (SR/DM/Tele/Retailer)
 │
 ▼
Validate Stock ── No Stock? → Reject
 │
 ▼
Packing Required?
 ├──► Ready Sell → Dispatch
 │
 ▼
Packing Stage → Basket Assigned
 │
 ▼
Dispatch to Deliveryman
 │
 ▼
Delivery Attempt
 │
 ├── Successful Delivery → Payment / Due
 │
 ├── Partial Cancel → Adjust Inventory
 │
 ├── Full Cancel → Return Stock
 │
 └── No Action → Move to Next Day Attempt
 │
 ▼
Order Closed → Profit Distribution
 │
 ▼
End

```

---

# **8.2 Dealer Profit Calculation Flow**

```
Dealer Purchase Price
 + SR Override Margin
 + Delivery Charges (optional)
 - Happy Commission %
 --------------------------------
 = Dealer Profit

```

---

# **8.3 Inventory Movement Flow**

```
Stock IN (Pickup Entry / Return)
      │
      ▼
Warehouse Stock
      │
      ▼
Packing OUT
      │
      ▼
Delivery Man Inventory
      │
      ├── Sell → Inventory Sell Value
      ├── Cancel → Inventory Return
      └── Fault → Admin Correction

```

---

# **8.4 SR Route Workflow**

```
Daily Route Generated
      │
      ▼
SR Edits Route (Optional)
      │
      ▼
Retailer Visits
      │
      ▼
Order Placement
      │
      ▼
Summary Reports

```

---

# **6. Functional Requirements (Continued – Extended Deep Version)**

This section describes the detailed functional behavior of every subsystem involved in the Distributor Management & Sales Operations Platform. The emphasis is on **end-to-end operational workflows**, **role actions**, and **system rules** that govern correctness, reliability, and compliance.

---

# **6.5 Operational Workflow Requirements (End-to-End Business Flow)**

The system follows a strict operational pipeline:

### **Dealers → SRs (Sales Representatives) → Warehouse Packing → Delivery → Retailers**

This workflow ensures traceability, accountability, efficiency, and financial visibility across the business operations.

---

# **6.5.1 Dealer Operations Module Requirements**

### **6.5.1.1 Dealer Profile Management**

**The system shall:**

- Enable creation and management of dealer profiles with business details.
- Maintain KYC information such as trade license, NID/SSN, VAT registration.
- Allow dealers to be tagged to business zones, regions, territories, and routes.
- Track dealer credit limits, outstanding dues, and order history.

### **6.5.1.2 Dealer Credit Control**

The system shall:

- Enforce system-calculated **credit limit rules**.
- Block SRs from placing orders exceeding dealer credit.
- Allow finance/admin to override credit limits with approval workflow.

### **6.5.1.3 Dealer Product Pricing Rules**

The system shall:

- Maintain dealer-level pricing tiers.
- Support dynamic discounts based on volume slabs.
- Allow promotional pricing, seasonal offers, and campaign-based discounts.

### **6.5.1.4 Dealer Order Management**

The system shall:

- Allow SRs to place dealer orders on behalf of assigned dealers.
- Validate stock availability in assigned warehouse.
- Generate order summaries and expected delivery times.
- Trigger downstream workflow: **Packing Queue Entry**.

---

# **6.5.2 SR (Sales Representative) Operations Requirements**

### **6.5.2.1 SR Route & Coverage Management**

System shall:

- Assign SRs to routes (daily, weekly, custom).
- Enforce coverage rules: SR cannot place orders for unassigned dealers.
- Track SR performance metrics (sales volume, visit completion %, collections).

### **6.5.2.2 SR Order Placement Requirements**

System shall:

- Allow SRs to place orders through mobile/web.
- Validate order rules:
    - Dealer is active and within credit limit.
    - Products allowed under route/territory rules.
    - Promotions automatically applied.
- Log SR geolocation at the time of order placement.

### **6.5.2.3 SR Attendance & Activity Tracking**

System shall:

- Log daily attendance via mobile selfie + geotag.
- Verify GPS spoofing using:
    - Device integrity checks
    - Geo-fencing
    - Allowed radius validation
- Track field visits with:
    - Timestamp
    - Distance travelled
    - Covered retailers
    - Visit purpose & outcomes

### **6.5.2.4 SR Sales Dashboard**

Shall provide:

- Daily, weekly, monthly achievements
- Route performance vs. targets
- Commission breakdown
- Pending collections

---

# **6.5.3 Warehouse Packing Module Requirements**

### **6.5.3.1 Packing Queue Management**

System shall:

- Automatically push approved dealer orders to packing queue.
- Allow warehouse managers to:
    - Assign packers
    - Prioritize orders
    - Split items across packs if needed

### **6.5.3.2 Packing Validation**

System must enforce:

- Stock check with last-known quantity.
- FIFO handling for expiration-sensitive products.
- Barcode/QR scan per item for verification.
- Auto-detection of discrepancies.

If discrepancies occur:

- System shall allow packer to submit adjustment request.
- Supervisor must accept/decline adjustments.
- All decisions should trigger audit logs.

### **6.5.3.3 Packaging Completion Rules**

Upon completion:

- System creates:
    - Packing Slip
    - Batch ID
    - Delivery Handoff Ticket
- Moves order status to **"Ready for Dispatch"**.

---

# **6.5.4 Delivery Management Module Requirements**

### **6.5.4.1 Delivery Fleet Assignment**

System shall:

- Assign delivery orders to available riders/drivers.
- Optimize load distribution based on:
    - weight capacity
    - route mapping
    - delivery windows

### **6.5.4.2 Delivery Route Optimization**

System shall:

- Generate optimized delivery routes using:
    - Distance heuristics
    - Traffic data (if integrated)
    - Geo-clustering
- Provide GPS navigation for drivers (mobile app).

### **6.5.4.3 Delivery Validation Requirements**

Delivery staff must:

- Capture retailer signature OR OTP confirmation.
- Take a delivery photo (with timestamp + geolocation).
- Log return items (if any).
- Log payments collected.

### **6.5.4.4 Failed Delivery Workflow**

System must support:

- Failure reason categorization (e.g., retailer absent).
- Auto-reschedule logic.
- Return-to-warehouse process with reverse stock adjustment.

---

# **6.5.5 Retailer Management Module Requirements**

### **6.5.5.1 Retailer Profile Management**

System shall:

- Maintain business details, store type, product preferences.
- Map retailers to dealer & SR routes.
- Track purchase history and profitability.

### **6.5.5.2 Retailer Feedback & Issue Logging**

Retailers shall:

- Submit complaints
- Request product returns
- Ask for promotional materials

Issues must be routed to:

- SR
- Dealer
- Territory Manager
- Warehouse Manager (based on category)

---

# **6.6 Role-Based Access and Feature Control Requirements (RBAC)**

The system contains 8 core roles:

1. **Super Admin**
2. **Admin**
3. **Dealer**
4. **SR**
5. **Warehouse Manager**
6. **Packer**
7. **Delivery Staff**
8. **Retailer**

RBAC must be **fully configurable**, **permission-based**, and **feature-scoped**.

---

## **6.6.1 RBAC Functional Requirements**

### **6.6.1.1 Permission Hierarchy**

The platform shall support:

- **Global Permissions** (system-wide)
- **Module Permissions** (orders, packing, delivery)
- **Action Permissions** (create, update, delete, approve)
- **Field-Level Restrictions** (e.g., SR can't see dealer financial data)
- **Data Segmentation**:
    - region-based restrictions
    - route-based access
    - warehouse-based segmentation

### **6.6.1.2 Permission Assignment Rules**

System shall:

- Allow role→permission mapping
- Allow user→permission overrides
- Maintain permission groups for ease of configuration
- Log each permission change with:
    - who performed it
    - when
    - reason
    - affected users

### **6.6.1.3 Session Control & Security Rules**

System must:

- Revalidate permissions on each request
- Invalidate sessions upon permission changes
- Track user activities (audit logs)

---

# **6.7 Financial & Profitability Requirements**

### **6.7.1 Dealer Profitability Tracking**

System must compute:

- Dealer gross margin per product
- Dealer net margin after commissions, discounts, promotions
- SR commission impact
- Transportation charges

### **6.7.2 Company Profit Tracking**

System shall:

- Consolidate profit at:
    - Product level
    - Dealer level
    - Region level
    - SR level
    - Route level
- Provide profitability dashboards

### **6.7.3 Commission Rules Engine**

Supports:

- SR commission rules (slabs, targets, daily/weekly/monthly)
- Delivery staff incentives
- Dealer rebates
- Warehouse incentive for packing speed/accuracy

---

# **6.8 Business Rules (Extended)**

### **6.8.1 Ordering Rules**

- Orders cannot be placed for inactive dealers.
- Orders exceeding credit limits must be flagged.
- Stock availability must be validated before acceptance.

### **6.8.2 Multi-Warehouse Rules**

- SR is restricted to specific warehouse regions.
- Dealer is bound to specific primary warehouse.
- Inventory cannot cross warehouses without approval.

### **6.8.3 Data Integrity Rules**

- All financial data must be immutable.
- All stock movement requires dual-entry logs.
- All workflow states are versioned.

---

# **6.9 Error Handling & Exception Rules**

System must implement:

### **6.9.1 Operational Exceptions**

- Stock mismatch during packing
- Delivery failure exceptions
- Retailer rejection exceptions
- Payment mismatch exceptions

### **6.9.2 System Exceptions**

- Dead-letter queue handling for event failures
- Redis cache fallback to PostgreSQL
- Graceful degradation in module failures

### **6.9.3 User-Level Validation Errors**

- Friendly human-readable messages
- Multi-language support (if configured)

---

# **6.10 Workflow Diagrams (Included)**

### **6.10.1 High-Level Operational Workflow**

```
Dealer → SR Order → Warehouse Packing → Dispatch → Delivery → Retailer Receipt → Payment → Profit Consolidation

```

### **6.10.2 Detailed System Flow (ASCII UML)**

```
+---------+        +---------+         +-----------+        +-----------+       +-----------+
| Dealer  | -----> |   SR    | ----->  | Warehouse | -----> |  Delivery | ----> | Retailer  |
+---------+        +---------+         +-----------+        +-----------+       +-----------+
    ^                                                        |  Payment       |
    |                                                        +----------------+
    |                                                               |
    +------------- Profit & Accounting Engine <---------------------+

```

---

# **7. Non-Functional Requirements (NFR)**

## **7.1 Security Requirements**

Security is a foundational requirement for a multi-role, multi-warehouse, financially-sensitive distribution system. The system must comply with OWASP, CIS Benchmarks, and industry-standard backend hardening practices.

---

## **7.1.1 Authentication Requirements**

The system shall:

1. **Use JWT Access + Refresh tokens** for authentication.
2. Support **short-lived refresh tokens** for enhanced security.
3. Provide **secure cookie** and **HTTP-only** options for web authentication.
4. Enforce device-level verification for SR/Delivery apps:
    - Device ID binding
    - Optional biometric support
    - Jailbroken device detection
5. Allow **session revocation** from admin panel.
6. Automatically revoke tokens upon:
    - Role changes
    - Permission updates
    - Suspicious activity

---

## **7.1.2 Authorization Requirements**

The system must:

1. Enforce **RBAC (Role-Based Access Control)** at:
    - API level
    - Feature level
    - Data access level
    - Field-level visibility
2. Support **dynamic permission policies** stored in a database, not hard-coded.
3. Revalidate permissions every request using:
    - Redis cached permission map
    - Fallback PostgreSQL read
4. Prevent privilege escalation attacks by:
    - Explicit deny policies
    - Scope isolation
    - Route-based restrictions

---

## **7.1.3 Data Security Requirements**

Data must be protected in transit and at rest.

### **In Transit**

- TLS 1.2+ enforced
- HSTS enabled
- CORS restrictions by environment & domain

### **At Rest**

- PostgreSQL encrypted volumes
- Redis encrypted-in-memory (if supported)
- Encrypted S3 buckets for file storage

### **Critical Data Hashing / Encryption**

- Password hashing: Argon2id (preferred) or bcrypt
- Sensitive fields encryption:
    - Dealer financial info
    - SR location logs
    - Payment logs
    - Retailer invoices

---

## **7.1.4 API Security Requirements**

System must ensure:

1. Strict rate limiting per IP / User / Token.
2. Brute-force login protection.
3. SQL injection protection via ORM layer + validation.
4. XSS protection in all inputs.
5. CSRF protection where cookies are used.
6. Payload size limitations.
7. API signature validation for mobile clients (optional).

---

## **7.1.5 Logging & Security Audits**

System must log:

- All role/permission changes
- All financial operations
- All stock adjustments
- Login failures
- Sensitive data access attempts

Logs must be:

- Immutable
- Time-stamped
- Stored in tamper-proof storage

---

# **7.2 Performance Requirements**

## **7.2.1 Response Time Requirements**

The system shall meet the following:

| Action | Expected Response Time |
| --- | --- |
| Standard API requests | ≤ 200–300ms |
| Heavy queries | ≤ 800ms |
| Cached reads | ≤ 50–80ms |
| Mobile API endpoints | ≤ 150ms median |

---

## **7.2.2 Concurrency Requirements**

System must support:

- **10,000+ concurrent SR users**
- **Large warehouse operations** with hundreds of packers
- **High-volume dealer orders** during peak hours

Redis caching + read replicas will support concurrency.

---

## **7.2.3 Throughput Requirements**

System shall support:

- **1000 order placements per minute**
- **Up to 100k SKUs** in catalog
- **Up to 500k retailer records**
- **Real-time logs** for delivery events (high write-intensive module)

---

# **7.3 Availability & Reliability Requirements**

## **7.3.1 Target Availability**

The system must meet:

- **99.5% uptime** standard
- **Mission-critical modules** (auth, orders, packing) MUST remain operable even during partial degradation

---

## **7.3.2 Fault-Tolerance Requirements**

System must:

1. Use **PostgreSQL high availability** with replica nodes.
2. Leverage **Redis cluster mode** with failover.
3. Support **worker queues** with retry strategies.
4. Use **circuit breakers** in critical services.

---

## **7.3.3 Disaster Recovery Requirements**

Must support:

- Automated nightly DB backups
- Point-in-time recovery
- Multi-region data redundancy (optional)
- Recovery Time Objective (RTO): **< 2 hours**
- Recovery Point Objective (RPO): **< 15 minutes**

---

# **7.4 Scalability Requirements**

## **7.4.1 Horizontal Scaling**

System must support:

- Scaling API services horizontally via load balancer
- Scaling Redis cluster when read/write load increases
- Scaling PostgreSQL read replicas for analytics

---

## **7.4.2 Vertical Scaling**

Critical single-node components (e.g., queue workers, report generators) must:

- Support CPU/RAM expansion
- Auto-restart on crash states

---

## **7.4.3 Data Scaling**

System must handle:

- Millions of sales records
- Large inventory histories
- Multi-year logs
- Archival system for old data

---

# **7.5 Maintainability Requirements**

## **7.5.1 Code Maintainability**

The system must be:

- Fully modular
- Feature-based
- API versioned
- Enforced with linting & type-safety
- Covered by automated tests

---

## **7.5.2 Configurability**

The system must allow:

- Dynamic tax rules
- Adjustable credit limits
- Editable commission rules
- Flexible user permission configuration
- Multi-warehouse mapping updates

---

## **7.5.3 Documentation Requirements**

Documentation must include:

- API reference
- ERD
- Deployment guide
- System diagrams
- Failure recovery runbooks
- Monitoring dashboards

---

# **7.6 Usability Requirements**

## **7.6.1 Mobile User Experience (SR & Delivery Apps)**

Apps must support:

- Low-data mode
- Offline caching
- Background sync
- Fast load times
- Optimized UI for one-handed use

---

## **7.6.2 Web Admin Panel Usability**

Admin must experience:

- Fast searchable grids
- Exportable reports
- Permission-based UI visibility
- Drill-down dashboards with interactions
- Real-time alerts

---

# **7.7 Monitoring & Observability Requirements**

## **7.7.1 System Monitoring**

Mandatory monitoring includes:

- API latency
- Redis hit ratio
- Database slow queries
- CPU/RAM metrics
- Queue backlog levels
- Warehouse packing delays

---

## **7.7.2 Business-Level Monitoring**

System must support dashboards for:

- Daily sales
- SR attendance patterns
- Delivery performance
- Credit exposure
- Profitability
- Warehouse bottlenecks

---

## **7.7.3 Alerts & Notifications**

Alerts must trigger when:

- Error rate crosses threshold
- Stock mismatch occurs
- High-volume login failures happen
- DB replication lag grows
- Delivery delays exceed SLA

---

# **7.8 Compliance Requirements**

System must comply with:

- GDPR-equivalent data protection policies (user opt-in, data deletion)
- Local government tax compliance
- Audit log retention policies
- KYC requirements for dealers

---

# **7.9 Environmental Requirements**

System shall operate reliably in:

- Low-bandwidth mobile networks (SR/Delivery)
- High-load warehouse WiFi environments
- Cloud-native environments (AWS, GCP, Azure)

---

# **7.10 Non-Functional Diagrams**

### **7.10.1 High-Level System Architecture (ASCII)**

```
                +------------------------+
                |      API Gateway       |
                +-----------+------------+
                            |
                +-----------+------------+
                |   Node.js Backend      |
                +-----------+------------+
                            |
        ---------------------------------------------------
        |                    |                          |
+---------------+   +----------------+        +----------------------+
| PostgreSQL DB |   | Redis Cache    |        | Message Queue (MQ)  |
|  HA Cluster   |   |  Cluster Mode  |        |  Workers/Consumers  |
+---------------+   +----------------+        +----------------------+

```

---

# **8. System Architecture**

This section defines how the entire HAPPY ecosystem is structured.

It provides a **multi-layer, multi-module, scalable, secure architecture** suitable for long-term growth, multi-warehouse operations, and high concurrency.

---

# **8.1 Architecture Goals & Principles**

The system architecture must follow these engineering principles:

### **Scalability**

- Must support thousands of SRs and Delivery Men simultaneously.
- Must support increasing product catalogs and warehouses.

### **Maintainability**

- Modular, feature-based structure.
- Dependency isolation.
- Versioned APIs.

### **Performance**

- Redis caching for product, stock, pricing, permissions.
- Optimized PostgreSQL queries with proper indexing.

### **Security**

- Compliance with RBAC, JWT, encrypted storage.
- Tenant-like data isolation between dealers.

### **Resilience**

- Graceful error tolerance.
- Queue-based background processing.
- Failover-ready components.

---

# **8.2 High-Level Architecture Overview**

The HAPPY system is built with a **modular backend**, **real-time updates**, and **role-based access** layers.

### **High-Level Architectural Components**

1. **API Gateway / Load Balancer**
2. **Backend Services (Node.js + TypeScript)**
3. **PostgreSQL Cluster (Primary + Read Replicas)**
4. **Redis Cluster (Caching + Queues + Session)**
5. **Message Queue System (BullMQ / Redis Streams / RabbitMQ)**
6. **Admin Web Portal**
7. **SR & Delivery Mobile Apps**
8. **Dealer Portal**
9. **Retailer Mobile App/Web**
10. **Customer Care Console**
11. **Monitoring + Logging + Alerting Stack**
12. **Object Storage (S3)** for invoices, images, stock docs

---

# **8.3 Layered Architecture**

The system uses a **5-layer architecture**:

```
┌────────────────────────────────────────────────┐
│                Presentation Layer              │
│ (Web Admin UI, Dealer Portal, SR & DM Apps)    │
└────────────────────────────────────────────────┘
┌────────────────────────────────────────────────┐
│                 API Gateway Layer              │
│ (Routing, Throttling, Security, Versioning)    │
└────────────────────────────────────────────────┘
┌────────────────────────────────────────────────┐
│                   Backend Layer                 │
│ Controllers → Services → Repositories → Utils  │
└────────────────────────────────────────────────┘
┌────────────────────────────────────────────────┐
│          Data & Storage Layer                   │
│ PostgreSQL, Redis, S3, Queue Workers            │
└────────────────────────────────────────────────┘
┌────────────────────────────────────────────────┐
│           Observability & Ops Layer             │
│ Logging, Monitoring, Alerts, Dashboards         │
└────────────────────────────────────────────────┘

```

---

# **8.4 Detailed Backend Layer Architecture**

The backend follows the **Clean Architecture + DDD-inspired modular design**:

### **Controller Layer**

- Exposes endpoints
- Responsible for validation, DTO mapping, authentication checks

### **Service Layer**

- Contains business logic
- Handles workflows across entities
- Enforces role-based rules

### **Repository Layer**

- Interacts with PostgreSQL via Prisma ORM
- Executes optimized queries
- Maintains data integrity

### **Redis Integration Layer**

- Handling:
    - Caching (products, stock, dealers)
    - Sessions
    - Locking mechanisms (to prevent stock race conditions)

### **Worker Layer**

- Background jobs:
    - Report generation
    - Daily stock reconciliation
    - Low-stock alerts
    - Delivery retry scheduling
    - Tele-order follow-ups
    - Auto-retry failed operations

---

# **8.5 System Modules**

The full system is divided into 14 core modules:

---

## **8.5.1 User & Role Management Module**

Handles:

- User creation
- Role assignment
- Permission mapping
- Dealer-SR relation mapping
- Warehouse/Area/Route assignments

Key roles include:

Super Admin, Admin, Dealer, SR, Delivery Man, Retailer, Customer Care

---

## **8.5.2 Authentication & Authorization Module**

Key Functions:

- JWT Access Token
- JWT Refresh Token
- Device binding for SR & Delivery Man
- Two-factor optional for critical actions
- Enforced RBAC + Feature Control
- Admin impersonation (for log review)

---

## **8.5.3 Dealer Management Module**

Dealer Profile:

- Company mapping
- SR mapping
- Profit tracking
- Investment tracking
- Withdrawal request workflow
- Dealer-level dashboard
- Dealer-specific product commission logic

---

## **8.5.4 Sales Representative (SR) Module**

Handles:

- SR daily routes
- Order placing with custom price
- Nearby retailer detection via GPS
- Order history & summary
- Delivery tracking
- SR-level commission calculation

---

## **8.5.5 Delivery Man Module**

Functions:

- Assigned routes (non-editable)
- Warehouse → Retailer delivery workflow
- Order editing by retailer:
    - Partial cancel
    - Full cancel
    - Add-on product
- Due collection and negotiation
- Return stock handling
- Fault attempt tracking

---

## **8.5.6 Pickup & Packing Module**

Pickup Man:

- Receives stock from dealers
- Product batch management
- Variant expiry & price handling

Packing Man:

- Packs retailer baskets
- Merges multiple SR orders into one retail order
- Inventory deduction workflow
- Packing history logs

---

## **8.5.7 Retailer Management Module**

Retailer Portal Features:

- Create self-orders
- See profit per product
- Filter products by company/category
- View invoices & order history
- Pay due or maintain credit balance

Admin Features:

- Track due payments
- Retailer performance dashboard
- Retailer-level order insights

---

## **8.5.8 Order Management Module**

The most complex module:

Order Types:

1. SR Order
2. Delivery Man Order
3. Ready Sell Order (no delivery cost)
4. Tele Order
5. Retailer Self Order

Retailer Order Workflow:

- Basket merging logic
- Multi-SR order consolidation
- Price negotiation
- Due / partial payment
- Order state transitions:
    
    Created → Packed → Assigned → Delivered → Completed
    

---

## **8.5.9 Inventory & Warehouse Management Module**

Every warehouse tracks:

- Stock IN
- Stock OUT
- Sold quantity
- Damaged/returned quantity
- Assigned stock to Delivery Men

Stock Real-time Logs:

- Redis atomic locks
- Prevent overselling
- Prevent duplicate stock-out

Admin Utilities:

- Manual stock adjustments
- Warehouse value tracking
- Product expiry insights

---

## **8.5.10 Route & Area Module**

Routes assigned to:

- SR (Editable)
- Delivery Man (Admin only)

Entities:

- Region → District → Upazila → Union → Area
- Route chaining with geo-points
- Auto-suggestions for nearest retailers

---

## **8.5.11 Finance & Accounting Module**

Handles:

- Dealer profits
- Happy commission calculations
- Delivery charges
- SR over-commission
- Stock valuation
- Automated daily settlement reports

Dealer Withdrawal Workflow:

- Create request
- Admin review
- Approval / Rejection
- Ledger updates

---

## **8.5.12 Reporting Module**

Reports include:

- Order summary
- Product movement
- Dealer profitability
- SR performance
- Delivery performance
- Warehouse stock aging
- Retailer due tracking
- Month-end financial statements

---

## **8.5.13 Notification Module**

Channels:

- Push notifications (SR, Delivery Man, Retailer)
- Email (Admin, Dealer)
- SMS (Retailer orders)
- In-system notifications

Trigger Events:

- SR places order → Notify Dealer + Retailer
- Delivery attempt → Notify Retailer
- Withdrawal approval → Notify Dealer
- Stock threshold breach → Notify Admin

---

## **8.5.14 Customer Care Module**

Features:

- Tele order placement
- Order confirmation calls
- Editing orders before dispatch
- Retailer interaction history

---

# **8.6 Core System Data Flow Diagrams**

---

## **8.6.1 User Authentication Data Flow**

```
User → API Gateway → Auth Controller → Auth Service
      → PostgreSQL (verify credentials)
      → Generate JWT
      → Redis (store refresh token)
      → User

```

---

## **8.6.2 SR Order Placement Data Flow**

```
SR App
  ↓ (Product Request)
Redis Cache → (Stock + Product + Pricing)
  ↓
Backend → Validate Stock (PostgreSQL)
  ↓
Create Order (PostgreSQL)
  ↓
Notify Dealer & Retailer (Notification Service)
  ↓
Update SR Dashboard Summary

```

---

## **8.6.3 Delivery Workflow Data Flow**

```
Packing Completed → Assign to Delivery Man
  ↓
Delivery Man App → Start Route
  ↓
Retailer Negotiation → Modify Order Values
  ↓
Invoice Generated
  ↓
Stock OUT → Inventory Logs Updated
  ↓
Payment Collection / Due Management
  ↓
Delivery Marked Completed

```

---

## **8.6.4 Warehouse Stock Update Flow**

```
Dealer Sends Stock → Pickup Man Scans/Enters Data
  ↓
Backend → Batch Validation Logic
  ↓
Add to Warehouse Stock (PostgreSQL)
  ↓
Cache Updates (Redis)
  ↓
Admin Dashboard Stock Value Updates

```

---

# **8.7 Deployment Architecture**

Modern cloud-native deployment with autoscaling.

```
                   ┌───────────────────┐
                   │    Load Balancer  │
                   └─────────┬─────────┘
                             │
 ┌───────────────────────────┼──────────────────────────────┐
 │                           │                              │
 │                   Backend Server #1                Backend Server #2
 │                     (Node.js API)                     (Node.js API)
 └───────────────────────────┼──────────────────────────────┘
                             │
                   ┌─────────┴──────────┐
                   │   Redis Cluster    │
                   └─────────┬──────────┘
                             │
                   ┌─────────┴──────────┐
                   │ PostgreSQL Cluster │
                   └────────────────────┘

```

---

# **8.8 Technology Stack Summary**

| Component | Technology |
| --- | --- |
| Backend | Node.js + TypeScript |
| Database | PostgreSQL + Prisma |
| Cache | Redis Cluster |
| Storage | S3 |
| Queue | BullMQ / Redis Streams |
| Dashboard UI | React/Next.js |
| Mobile Apps | Flutter / React Native |
| CI/CD | GitHub Actions, Docker |
| Monitoring | Prometheus, Grafana, Loki |
| Logs | ELK Stack or CloudWatch |

---

# **8.9 Architectural Strengths**

### ✔ Highly Scalable

### ✔ Modular & Maintainable

### ✔ Secure (RBAC, JWT, Audit Logs)

### ✔ Optimized Inventory & Order Flow

### ✔ Real-time Notifications

### ✔ Enterprise-level Reporting Pipeline

### ✔ Offline-first SR/Delivery apps

---

# **8.0 SYSTEM ARCHITECTURE DESIGN (EXTENDED)**

---

## **8.1 High-Level Logical Architecture (Extended View)**

The system follows a **modular, domain-driven, service-oriented monolith** with selective microservice extraction points. The architecture is optimized for:

- High scalability
- High throughput
- Predictability under load
- Maintainability with modular boundaries
- Clear domain isolation for features
- Event-driven responsibilities for long-running workflows
- Vertical and horizontal scalability

### **8.1.1 Logical Layers**

```
┌────────────────────────────────────────────┐
│                Presentation API Layer      │
│ - REST Controller Modules                  │
│ - Request Validators                       │
│ - Authentication Guards                    │
└────────────────────────────────────────────┘
                │
                ▼
┌────────────────────────────────────────────┐
│            Application Service Layer       │
│ - Use Case Services                        │
│ - Domain Orchestrations                    │
│ - Event Dispatchers                        │
└────────────────────────────────────────────┘
                │
                ▼
┌────────────────────────────────────────────┐
│                Domain Layer                │
│ - Domain Models                             │
│ - Business Rules (Core Logic)               │
│ - Role/Feature Access Enforcement           │
└────────────────────────────────────────────┘
                │
                ▼
┌────────────────────────────────────────────┐
│             Infrastructure Layer           │
│ - PostgreSQL Repositories (Prisma)         │
│ - Redis Caching Layer                      │
│ - Job Queues (Optional)                    │
│ - Message/Event Broker (Optional)          │
│ - External Integrations                    │
└────────────────────────────────────────────┘

```

---

## **8.2 Deployment Architecture**

### **8.2.1 Recommended Deployment Stack**

| Layer | Recommended Technology |
| --- | --- |
| API Runtime | Node.js 20 LTS |
| Process Manager | PM2 / Dockerized Node |
| Reverse Proxy / Load Balancer | NGINX |
| Database | PostgreSQL 16 |
| Caching | Redis 7.x |
| Message Queue (Optional) | BullMQ / Kafka-lite workflow |
| Monitoring | Prometheus + Grafana |
| Logs | Loki / Elastic Stack |
| Authentication | JWT |
| Infrastructure | Docker + Kubernetes-ready |

---

# **9.0 MODULE ARCHITECTURE (Highly Detailed)**

This section breaks down each module, internal logic, workflows, and how modules communicate.

---

## **9.1 User & Access Control Module**

### **Purpose**

Provides role-based access, feature-based permissions, hierarchy mapping, and authentication/authorization enforcement.

### **Subcomponents**

- **Authentication Service**
- **Authorization Policy Engine**
- **Feature Flag Manager**
- **Role-Permission Registry**
- **User Account Service**

### **Extended Detail**

### **9.1.1 Authentication Flow**

```
Login → Validate Credentials → Issue Access Token → Store Session Metadata → RBAC Policy Injection → Continue Request

```

### **9.1.2 Role Hierarchy**

```
Admin
└── Dealer
     └── SR (Sales Representative)
          └── Packing Team
               └── Delivery Personnel
                    └── Retailer Portal

```

### **9.1.3 Permission Set Examples**

- dealer.manage.sr
- sr.manage.packing
- sr.collect.order
- packing.assign.delivery
- delivery.update.route
- retailer.place.order
- reports.dealer.dashboard
- reports.sr.performance

---

## **9.2 Dealer Management Module**

### **Purpose**

Manage dealers, territories, SR assignment, stock allocations, credit limits, commissions, and performance tracking.

### **Extended Design**

### **Dealer Functional Blocks**

- Dealer registration
- Territory mapping
- Wallet & credit limit accounting
- Commission earnings
- SR assignment logic

### **Dealer Workflow Diagram**

```
Dealer Creation → Assign Territory → Add SRs → Receive Stock → Sell to Retailers → Generate Revenue + Commission

```

---

## **9.3 Sales Representative Module**

### **Purpose**

Sales activity, order collection, visit logs, retailer mapping, performance analytics.

### **Extended Internal Functions**

- Route planning
- Retailer visit logging
- Incentive tracking
- Order sync (offline/online)

---

## **9.4 Packing Management Module**

### **Purpose**

Workflow from **Order Received → Packaging → Dispatch → Handover to Delivery Team**

### **Deep Technical Flow**

```
Order Queue Ingestion (Redis Stream)
    ↓
Packing Task Creation
    ↓
Assignment to Packing Team
    ↓
Quality Control Check
    ↓
Dispatch Confirmation
    ↓
Delivery Route Scheduling

```

---

## **9.5 Delivery Management Module**

### **Purpose**

Delivery routing, trip plans, handover, proof of delivery (POD), failed delivery loop, and settlement management.

### **Extended Logic Flows**

### **Route Optimization Flow**

```
Orders → Cluster by Geo → Optimize Route → Assign Delivery Agent → Dispatch → Live Tracking → POD

```

### **POD Capture**

- Image upload (optional)
- OTP-based confirmation
- Signature capture (optional)
- Cash Collection Tracking

---

## **9.6 Retailer Management Module**

- Retailer profile
- Order placement
- Credit account
- Purchase history
- Loyalty point tracking

---

# **10.0 CROSS-CUTTING ARCHITECTURE**

---

## **10.1 Caching Architecture (Redis)**

### **Caching Strategies**

- **Read-Through Cache** → For static data (roles, permissions, product catalog)
- **Write-Behind Cache** → For rate-limits and analytics counters
- **TTL-based Cache** → Temporary data (OTP, session tokens)
- **Distributed Locking** → Prevent race conditions in inventory updates

### **Recommended Redis Structures**

| Use Case | Redis Data Structure |
| --- | --- |
| OTP | String (TTL) |
| Rate Limits | INCR counters |
| Inventory Sync | Redlock + Hash |
| Leaderboards / KPIs | SortedSets |
| Order Queue | Streams |

---

## **10.2 Security Architecture**

### **Core Security Layers**

1. **Transport Security**
    - HTTPS-only
    - HSTS enabled
2. **Authentication**
    - JWT Access + Refresh Strategy
    - Rotation of refresh tokens
3. **Authorization**
    - RBAC + Feature Flagging
    - Context-based access control
4. **Data Security**
    - Parameterized SQL (Prisma)
    - Encrypted sensitive fields
5. **Operational Security**
    - Login throttling
    - Audit logging
    - Event alerts

---

# **11.0 EVENT-DRIVEN WORKFLOW ENGINE (Optional Advanced Component)**

This extends system scalability by offloading long-running tasks.

### **Events Examples**

- `order.created`
- `order.packed`
- `order.dispatched`
- `delivery.completed`
- `dealer.commission.generated`
- `retailer.credit.updated`

### **Event Flow Diagram**

```
API → Event Producer → Redis Streams → Consumer Workers → DB Updates → Notifications

```

---

# **12.0 SYSTEM WORKFLOW END-TO-END**

### **12.1 Dealer → SR → Packing → Delivery → Retailer Workflow (Full Engineering Overview)**

```
1. Dealer manages SRs
2. SR visits retailers & collects orders
3. Orders sent to Packing Queue (Redis)
4. Packing team prepares dispatch
5. Delivery team receives optimized routes
6. Retailer receives goods & confirms delivery
7. All profits, margins, incentive logs updated in reporting engine

```

---

# **13.0 DASHBOARD & REPORTING ENGINE (Extended)**

### **Dashboard Types**

- Dealer dashboard
- SR performance dashboard
- Packing queue dashboard
- Delivery live tracking dashboard
- Profit/Loss dashboard
- Retailer order analytics

### **KPIs Tracked**

- Daily/weekly sales
- SR attendance & performance score
- Delivery completion rate
- Packing team productivity
- Dealer’s profit margin analytics
- Stock movement reports
- Outstanding retailer dues

---

# **14.0 NON-FUNCTIONAL REQUIREMENTS (Extended)**

## **14.1 Performance**

- API response ≤ 200 ms for 80% calls
- Support 10k DAU scalable to 100k+
- Redis used for all heavy-read operations

## **14.2 Reliability**

- Zero data loss with PostgreSQL WAL
- Automatic failover (read replica)

## **14.3 Scalability**

- Stateless API (supports load balancing)
- Modular monolith → easy microservice migration

## **14.4 Maintainability**

- Strict TypeScript boundaries
- Domain-driven module separation

## **14.5 Security**

- JWT rotation
- Role-permission mapping
- DB encryption at rest

---

# **15.0 USE CASES & SCENARIOS**

This section defines primary and extended use cases for each role, including preconditions, triggers, normal flows, alternative flows, exceptions, and postconditions.

---

## **15.1 Use Case: Dealer Assigns SR**

- **Actor**: Dealer, Admin
- **Precondition**: Dealer must exist; SR must be registered
- **Trigger**: Admin/Dealer wants to assign SR to a specific area/company
- **Main Flow**:
    1. Login → Navigate to Dealer Profile
    2. Select “Assign SR” → Choose area, company
    3. System validates SR availability
    4. SR assigned successfully → Confirmation notification sent
- **Alternative Flow**:
    - SR already assigned → Prompt error
- **Postconditions**: SR now linked to dealer & area in DB; notifications sent
- **Diagrams**: Sequence diagram below

### **15.1.1 Sequence Diagram**

```
Dealer/Admin → System: requestAssignSR(SR_id, Area_id)
System → DB: validateSR(SR_id)
DB → System: SR_status
System → DB: assignSR(SR_id, Area_id)
System → Notification Service: sendAssignNotification(SR_id)
System → Dealer/Admin: confirmation

```

---

## **15.2 Use Case: SR Places Retailer Order**

- **Actor**: SR, Retailer
- **Precondition**: SR authenticated; retailer exists
- **Trigger**: SR collects orders at retailer location
- **Main Flow**:
    1. SR logs in → selects Retailer
    2. System displays products & stock availability
    3. SR adds products → custom price allowed
    4. Order confirmed → triggers inventory reserve
    5. Notification sent to Dealer & Packing Team
- **Alternative Flow**: Stock insufficient → prompt partial order
- **Postconditions**: Order stored, inventory reserved, notifications triggered

### **15.2.1 Sequence Diagram**

```
SR → System: createOrder(Retailer_id, Items[])
System → DB: checkStock(Items)
DB → System: StockStatus
System → DB: reserveStock(Order)
System → Notification Service: notifyDealerPacking(Order)
System → SR: confirmation

```

---

## **15.3 Use Case: Packing Man Packs Orders**

- **Actor**: Packing Man
- **Precondition**: Orders queued for packing
- **Trigger**: Daily packing session
- **Main Flow**:
    1. Login → View pending orders grouped by retailer
    2. Select basket → pack all items
    3. Confirm packed → triggers dispatch
- **Postconditions**: Orders marked as packed; delivery queue updated

---

## **15.4 Use Case: Delivery Man Delivers Orders**

- **Actor**: Delivery Man, Retailer
- **Precondition**: Orders packed & dispatched
- **Trigger**: Delivery route begins
- **Main Flow**:
    1. Login → View assigned route
    2. Deliver products → collect payments (full/due)
    3. Capture signature/POD if required
    4. Handle partial cancellations or additions by retailer
    5. Mark delivery complete → trigger profit calc & inventory update
- **Postconditions**: Inventory adjusted, notifications sent, commissions updated

---

# **16.0 CLASS DIAGRAM (Domain Model)**

```
┌─────────────┐
│   User      │
│-------------│
│+id:UUID     │
│+name:String │
│+role:Enum   │
│+areaId:UUID │
└─────┬───────┘
      │
      │ 1
      │
      │ M
┌───────────────┐
│   Order       │
│---------------│
│+id:UUID       │
│+type:Enum     │
│+status:Enum   │
│+dealerId:UUID │
│+srId:UUID     │
└─────┬─────────┘
      │ 1
      │
      │ M
┌───────────────┐
│  LineItem     │
│---------------│
│+id:UUID       │
│+productId:UUID│
│+qtyOrdered:Int│
│+qtyDelivered:Int│
└───────────────┘

```

**Notes**:

- User role differentiates Admin, Dealer, SR, Delivery, Retailer, etc.
- Orders contain multiple LineItems → supports polymorphic order types.

---

# **17.0 SEQUENCE DIAGRAMS**

### **17.1 Dealer Withdrawal Approval**

```
Dealer → System: requestWithdrawal(amount)
System → DB: validateProfit(Dealer_id, amount)
DB → System: status
System → Admin: approvalNotification
Admin → System: approveWithdrawal(id)
System → DB: updateWithdrawalStatus(Approved)
System → Dealer: notifyApproval

```

---

### **17.2 Inventory Update Post Delivery**

```
Delivery Man → System: completeDelivery(Order_id)
System → Inventory Service: adjustStock(LineItems)
Inventory Service → DB: decrementStock(LineItem)
Inventory Service → Event Queue: fireStockChangeEvent
DB → System: updateComplete
System → Notification: dealer/sr updated

```

---

# **18.0 OPERATIONAL GUIDELINES**

## **18.1 Deployment**

- Staging & Production separation
- CI/CD pipelines (GitHub Actions → Docker → Kubernetes)
- Rollbacks using container tags

## **18.2 Logging & Monitoring**

- **Logging**: All transactions, user actions, system events
- **Monitoring**: Prometheus → Alerts for failed jobs or slow API
- **Metrics**: Orders processed per hour, delivery success, packing efficiency, profit margins

## **18.3 Backup & Disaster Recovery**

- Daily PostgreSQL backups → Cloud Storage
- Point-in-Time Recovery enabled
- Redis snapshot backups for queues

## **18.4 Data Retention**

- Audit logs: 90 days
- Orders: Permanent
- Retailer & dealer financial data: 7 years (per local accounting compliance)

---

# **19.0 STATE DIAGRAM (Example: Order Lifecycle)**

```
[Placed] --> [Reserved]
[Reserved] --> [Packed]
[Packed] --> [Dispatched]
[Dispatched] --> [Delivered]
[Delivered] --> [Completed]
[Dispatched] --> [FailedDelivery] --> [Retry / Return]

```

---

# **20.0 EXCEPTIONS & ERROR HANDLING**

| Scenario | Error Handling |
| --- | --- |
| Stock Insufficient | Partial order, notify SR/Dealer |
| Delivery Failed | Auto Retry next day, log fault |
| Payment Pending | Allow due collection, update invoice |
| API Timeout | Retry 3x, fallback queue |

---

# **21.0 NOTIFICATIONS & ALERTS**

- Push: SR / Dealer
- SMS: Retailers (order confirmation / delivery)
- Email: Admin summaries
- Alert rules: low stock, failed deliveries, withdrawal approval

---

# **22.0 DATABASE DESIGN & SCHEMA**

The system uses **PostgreSQL** for ACID compliance and structured queries, **Redis** for caching, and **BullMQ** for event queues. Data models are optimized for FMCG workflows with batch handling, inventory deltas, multi-role traceability, and profit calculation.

---

## **22.1 Key Entities & Tables**

| Table | Primary Key | Description |
| --- | --- | --- |
| Users | id (UUID) | All system users: Super Admin, Admin, Dealer, SR, Delivery Man, Retailer, Customer Care |
| Roles | id (UUID) | RBAC roles with permissions JSONB |
| Companies | id (UUID) | FMCG companies/brands |
| Categories | id (UUID) | Product categories, hierarchical (Parent_id FK) |
| Products | id (UUID) | SKU-level product data; variants in JSONB |
| Warehouses | id (UUID) | Geo-tagged warehouses |
| Stocks | id (UUID) | Inventory per product per warehouse; tracks batch, price, expiry, variants |
| Orders | id (UUID) | Polymorphic: SR/Delivery/Ready/Tele/Retailer |
| LineItems | id (UUID) | Products per order with qty ordered/delivered |
| Routes | id (UUID) | Geo-points for SR/Delivery daily routes |
| Profits | id (UUID) | Dealer/SR/Happy commissions per order |
| Withdrawals | id (UUID) | Dealer withdrawal requests |
| AuditLogs | id (UUID) | System-wide logs for actions, compliance |

---

## **22.2 Entity-Relationship Diagram (ERD)**

**ERD Overview:**

```
Users (PK: id)
│
├─< Orders (srId/dealerId/retailerId)
│    │
│    └─< LineItems (productId, qtyOrdered, qtyDelivered)
│
├─< Routes (userId, date, points)
│
├─< Stocks (warehouseId, productId, batch)
│
└─< Withdrawals (dealerId, amount, status)

```

**Notes:**

- Many-to-many relationships:
    - Dealer ↔ Companies (junction table: DealerCompanies)
    - Dealer ↔ SRs (junction table: DealerSRs)
- JSONB used for **product variants**: `{size, price, expiry, batchId}`
- Partitioning: Orders and LineItems by `createdAt` for faster querying

---

## **22.3 Table Definitions & Attributes**

### **22.3.1 Users**

| Column | Type | Description |
| --- | --- | --- |
| id | UUID | PK |
| name | VARCHAR | Full name |
| email | VARCHAR | Unique |
| role | ENUM | SuperAdmin, Admin, Dealer, SR, Delivery, Retailer, Care |
| areaId | UUID | FK to Areas table |
| permissions | JSONB | Role-specific dynamic perms |
| createdAt | TIMESTAMP | Audit |
| updatedAt | TIMESTAMP | Audit |

---

### **22.3.2 Products**

| Column | Type | Description |
| --- | --- | --- |
| id | UUID | PK |
| name | VARCHAR | SKU Name |
| companyId | UUID | FK to Companies |
| categoryId | UUID | FK to Categories |
| variants | JSONB | Batch-level stock, price, expiry |
| createdAt | TIMESTAMP | Audit |
| updatedAt | TIMESTAMP | Audit |

---

### **22.3.3 Orders & LineItems**

| Column | Type | Description |
| --- | --- | --- |
| id | UUID | PK |
| type | ENUM | SR, Delivery, Ready, Tele, Retailer |
| status | ENUM | Pending, Packed, Dispatched, Delivered, Returned |
| dealerId | UUID | FK |
| srId | UUID | FK nullable |
| retailerId | UUID | FK |
| customPrice | DECIMAL | Optional override |
| createdAt | TIMESTAMP | Audit |
| updatedAt | TIMESTAMP | Audit |

**LineItems**: orderId FK, productId FK, qtyOrdered, qtyDelivered, batch info in JSONB

---

## **22.4 Indexing Strategy**

- **Users**: `role`, `areaId`
- **Products**: `companyId`, `categoryId`
- **Orders**: `status`, `dealerId`, `srId`, `createdAt` (partitioned)
- **Stocks**: `(warehouseId, productId)` unique, `(expiry)` for alerts
- **Profits**: `(orderId)` unique

**Analysis**: Indexes prioritize read-heavy dashboard queries and filtering by company/date/area. Partitioning improves large-scale order handling (~100k orders/day).

---

## **22.5 Data Flow Diagrams (DFD)**

### **22.5.1 Level 0 – System Context**

```
[Retailer] --> [Happy System] <-- [Dealer]
[SR] --> [Happy System] <-- [Packing/Delivery]
[Admin] --> [Happy System] --> [Notifications / Reports]
[External APIs: Maps, SMS, bKash]

```

---

### **22.5.2 Level 1 – Order Processing Flow**

```
SR/Retailer → Order Entry → Order Service
Order Service → Inventory Service: Reserve Stock
Inventory Service → DB: updateStocks
Order Service → Packing Queue → Packing Man → Dispatch
Dispatch → Delivery Man → Delivery
Delivery → Payment / Negotiation → Inventory & Profit Update → Notifications

```

---

### **22.5.3 Level 2 – Inventory Delta Flow**

```
Stock Entry (Pickup Man)
   ↓
Warehouse Stock Update
   ↓
Orders Reserved → Inventory Deducted
   ↓
Delivery → Sold / Returned → Inventory Adjusted
   ↓
Real-time Summary → Dealer/SR Dashboard

```

---

## **22.6 Trade-offs & Analysis**

- **JSONB for variants**: Flexible batch handling vs. query complexity → mitigated by materialized views
- **Partitioning Orders**: Improves performance but adds maintenance overhead
- **Audit logs in separate table**: Compliance vs. storage → use pruning & archiving

---