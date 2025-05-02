## OFI Feature Construction

This project computes **Order Flow Imbalance (OFI)** features from high-frequency order book data. It helps quantify short-term buying vs. selling pressure in financial markets — a core signal in many market microstructure and predictive models.

---

## How is OFI Calculated?

For each timestamp (row in the dataset), OFI is computed by comparing the **current** and **previous** values of bid and ask **price** and **size**.

### Bid-side Logic:
- If the **bid price goes up**, buyers are more aggressive → **add current bid size**
- If the **bid price stays the same**, change = current size - previous size
- If the **bid price goes down**, buyers are retreating → **subtract current bid size**

### Ask-side Logic:
- If the **ask price goes up**, sellers are retreating → **subtract current ask size**
- If the **ask price stays the same**, change = current size - previous size
- If the **ask price goes down**, sellers are more aggressive → **add current ask size**