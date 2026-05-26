import csv

# Baseline inventory (Notice Granny Smith is 0 to test our spec rules!)
inventory = {"Honeycrisp": 50, "Gala": 32, "Granny Smith": 0}

def show_inventory():
    print("\n--- Current Apple Stock ---")
    for apple, count in inventory.items():
        print(f"{apple}: {count} boxes")

# SPEC-DRIVEN FEATURE: Built strictly following open-spec/spec.md guardrails
def export_spec_compliant_csv():
    file_name = 'apple_report.csv' # Explicitly named per spec requirements
    
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Apple Variety", "Quantity"]) # Clean headers per spec
        
        for apple, count in inventory.items():
            # SPEC GUARDRAIL VALIDATION: Flag out of stock items clearly
            if count == 0:
                writer.writerow([f"{apple} [OUT OF STOCK]", count])
            else:
                writer.writerow([apple, count])
                
    print(f"\n[Spec Code] Clean export saved securely to {file_name}!")

if __name__ == "__main__":
    show_inventory()
    export_spec_compliant_csv()