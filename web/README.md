# CNC Quote Studio — Web App

Open `web/index.html` in any modern browser. No installation, build tools, or backend required.

## Capabilities
- Part number, revision, customer and order quantity
- Material and scrap allowance; cycle-time and setup costing
- Additional per-part machining operations
- Inspection, outside processing, NRE and overhead
- Gross-margin pricing scenarios
- Save/load local JSON, export internal CSV, print/PDF

## Cost model
Material = quantity × material unit cost ÷ (1 − scrap fraction).
Machining = quantity × cycle minutes ÷ 60 × hourly rate.
Setup = setup hours × hourly rate.
Secondary operations = quantity × sum(hours per part × hourly rate).
Direct cost = material + machining + setup + operations + inspection + outside processing.
Overhead = direct cost × overhead rate.
Total cost = direct cost + overhead + NRE.
Selling price = total cost ÷ (1 − target gross margin).

Rates and inputs are illustrative. This is not a validated ERP or AS9100 record system. Review the quote before customer use. JSON and CSV contain confidential internal costs. Do not share them externally.

## Deployment
For GitHub Pages, configure Pages to deploy from the main branch and the `/docs` directory, or deploy the `web` folder with a static host. The repository does not currently include an automatic Pages publishing workflow.
