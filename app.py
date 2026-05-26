import csv

# Baseline inventory
inventory = {"Honeycrisp": 50, "Gala": 32, "Granny Smith": 15}

def show_inventory():
    print("\n--- Current Apple Stock ---")
    for apple, count in inventory.items():
        print(f"{apple}: {count} boxes")

# VIBE CODED FEATURE: Fast, unplanned CSV export
def export_to_csv():
    # The AI just assumed the file name and structure without asking
    with open('report.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Apple", "Count"]) # Quick headers
        for apple, count in inventory.items():
            writer.writerow([apple, count])
    print("\n[Vibe Code] Exported to report.csv successfully!")

# NEW FEATURE: Calculate total boxes and display summary alert
def show_total_summary():
    total_boxes = sum(inventory.values())
    alert_border = "=" * 50
    print(f"\n{alert_border}")
    print(f"📦 INVENTORY SUMMARY ALERT")
    print(f"{alert_border}")
    print(f"Total Apple Boxes in Stock: {total_boxes} boxes")
    print(f"Varieties: {len(inventory)}")
    for apple, count in inventory.items():
        print(f"  • {apple}: {count} boxes")
    print(f"{alert_border}\n")

if __name__ == "__main__":
    show_inventory()
    export_to_csv() # Automatically runs the export
    show_total_summary() # Display summary alert
