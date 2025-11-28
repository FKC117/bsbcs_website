Step 1: Order Creation (In the Field)
The process begins when a Sales Representative (SR) visits a retailer on their assigned route.

+------------------+          +-----------------+
| Sales Rep (SR)   |          |   Retailer      |
| (uses mobile app)|--------->| (at their shop) |
+------------------+          +-----------------+
        |
        | 1. SR checks real-time stock & prices.
        | 2. Negotiates with Retailer.
        | 3. Places order on behalf of the Retailer.
        ▼
+------------------+
|   Order Placed   |
| (in Happy System)|
+------------------+

Step 2: Order Consolidation (In the System)
The system receives the order and prepares it for the warehouse. If multiple SRs have placed orders for the same retailer, the system automatically merges them.

+------------------+      +------------------+      +------------------+
|  Order from SR 1 |      |  Order from SR 2 |      |  Order from SR 3 |
+------------------+      +------------------+      +------------------+
         |                       |                       |
         └─────────────┬───────────────┘
                       ▼
            +----------------------+
            |   Happy Platform     |
            | (Merges all orders   |
            | for one Retailer)    |
            +----------------------+
                       │
                       │ 1. Validates stock and dealer credit.
                       │ 2. Creates a single, unified packing list.
                       ▼
            +----------------------+
            |  Warehouse           |
            |  (Packing Queue)     |
            +----------------------+

Step 3: Packing (In the Warehouse)
A warehouse worker packs the consolidated order.

+----------------------+
|  Packing Man         |
| (in warehouse)       |
+----------------------+
         |
         | 1. Gets unified packing list.
         | 2. Scans items and packs them into a basket.
         | 3. Confirms packing is complete.
         ▼
+----------------------+
|   Basket Packed &    |
|   Ready for Dispatch |
+----------------------+


Step 4: Dispatch & Delivery
The packed basket is assigned to a Delivery Man for delivery.

+----------------------+
| Delivery Man         |
| (receives basket)    |
+----------------------+
         |
         | 1. Follows an optimized route.
         | 2. Visits the retailer's location.
         | 3. Hands over the goods.
         ▼
+----------------------+
|   Retailer           |
| (receives order)     |
+----------------------+
         |
         | 1. Confirms delivery.
         | 2. Makes payment (full or partial/due).
         | 3. May negotiate or return items on the spot.
         ▼
+----------------------+
|   Order Completed    |
| (or Partially Done)  |
+----------------------+

Step 5: Financial Settlement
The system calculates profits and commissions for all stakeholders.

+----------------------+
|   Happy Platform     |
+----------------------+
         |
         | 1. Calculates Dealer's profit.
         | 2. Calculates SR's commission.
         | 3. Updates dealer's withdrawable balance.
         | 4. Tracks all financial transactions.
         ▼
+------------------+   +------------------+   +------------------+
| Dealer's Account |   | SR's Account     |   | Happy's Account  |
| (Profit credited)|   | (Commission)     |   | (Platform Fee)   |
+------------------+   +------------------+   +------------------+

