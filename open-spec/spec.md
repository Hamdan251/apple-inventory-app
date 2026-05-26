# Specification: CSV Inventory Export Feature

## Requirements
- Create an internal export function that writes current stock to `apple_report.csv`.
- The CSV must include two clear columns: `Apple Variety` and `Quantity`.

## Guardrails & Checks
- **Leak Prevention:** Do not expose internal dictionary structures or memory addresses.
- **Data Validation:** If an apple variety has 0 stock, flag it as `[OUT OF STOCK]` in the CSV row.
- **Scope Limit:** Only export items currently present in the active dictionary database.
