inventory = []

while True:
    print("\n========== INVENTORY MANAGEMENT SYSTEM ==========")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        product_id = input("Enter Product ID: ")

        found = False
        for item in inventory:
            if item["ID"] == product_id:
                found = True
                break

        if found:
            print("Product ID already exists.")
            continue

        name = input("Enter Product Name: ")

        while True:
            try:
                quantity = int(input("Enter Quantity: "))
                if quantity < 0:
                    print("Quantity cannot be negative.")
                    continue
                break
            except ValueError:
                print("Enter a valid quantity.")

        while True:
            try:
                price = float(input("Enter Price: "))
                if price < 0:
                    print("Price cannot be negative.")
                    continue
                break
            except ValueError:
                print("Enter a valid price.")

        inventory.append({
            "ID": product_id,
            "Name": name,
            "Quantity": quantity,
            "Price": price
        })

        print("Product added successfully.")

    elif choice == "2":
        if not inventory:
            print("Inventory is empty.")
        else:
            print("\n{:<10} {:<20} {:<10} {:<10}".format(
                "ID", "Name", "Quantity", "Price"))
            print("-" * 55)

            for item in inventory:
                print("{:<10} {:<20} {:<10} {:<10.2f}".format(
                    item["ID"],
                    item["Name"],
                    item["Quantity"],
                    item["Price"]
                ))

    elif choice == "3":
        search = input("Enter Product ID to search: ")

        found = False
        for item in inventory:
            if item["ID"] == search:
                print("\nProduct Found")
                print("ID       :", item["ID"])
                print("Name     :", item["Name"])
                print("Quantity :", item["Quantity"])
                print("Price    :", item["Price"])
                found = True
                break

        if not found:
            print("Product not found.")

    elif choice == "4":
        update = input("Enter Product ID to update: ")

        found = False
        for item in inventory:
            if item["ID"] == update:

                item["Name"] = input("Enter New Product Name: ")

                while True:
                    try:
                        item["Quantity"] = int(input("Enter New Quantity: "))
                        if item["Quantity"] < 0:
                            print("Quantity cannot be negative.")
                            continue
                        break
                    except ValueError:
                        print("Enter a valid quantity.")

                while True:
                    try:
                        item["Price"] = float(input("Enter New Price: "))
                        if item["Price"] < 0:
                            print("Price cannot be negative.")
                            continue
                        break
                    except ValueError:
                        print("Enter a valid price.")

                print("Product updated successfully.")
                found = True
                break

        if not found:
            print("Product ID not found.")

    elif choice == "5":
        delete = input("Enter Product ID to delete: ")

        found = False
        for item in inventory:
            if item["ID"] == delete:
                inventory.remove(item)
                print("Product deleted successfully.")
                found = True
                break

        if not found:
            print("Product ID not found.")

    elif choice == "6":
        print("Thank you for using Inventory Management System.")
        break

    else:
        print("Invalid choice. Please enter 1 to 6.")

