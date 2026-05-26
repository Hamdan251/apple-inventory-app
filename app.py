inventory = {"Honeycrisp": 50, "Gala": 32, "Granny Smith": 15}

def show_inventory():
    print("\n--- Current Apple Stock ---")
    for apple, count in inventory.items():
        print(f"{apple}: {count} boxes")

if __name__ == "__main__":
    show_inventory()
