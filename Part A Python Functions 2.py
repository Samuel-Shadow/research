def custumerBooking():
    form_of_id = input("Form of ID (Passport, driver's license): ")
    id = input("ID Number: ")
    name = input("Passenger Name: ")
    ticket_ID = 20000
    ticket_ID += 1
    print("Ticket ID:", ticket_ID)
    return id
    return ticket_ID

def ferry_service_total():
    custumerBooking()
    total_cost = 0
    while True:
        service_name = input("Enter the service name (or 'done' to finish): ")
        if service_name.lower() == 'done':
            break
        try:
            price = float(input(f"Enter the price for {service_name}: "))
            max_price = float(input(f"Enter the maximum amount you can pay for {service_name}: "))
            if price <= max_price:
                total_cost += price
            else:
                print(f"The price for {service_name} exceeds your maximum amount. Service not added.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the price.")
    
    return total_cost

total = ferry_service_total()
print(f"The total cost of the services requested is: ${total:.2f}")

def booking_approval(id, ticket_ID):
    ferry_service_total(total)
    status = "Pending"
    first_three_id = id[:3]
    last_two_ticket = ticket_ID[-2:]
    result = first_three_id + last_two_ticket

    print("Total:", total)
    print("Status: ", status)
    print("Approval Referenece Number:", result)
booking_approval()

def display_booking():
    print(custumerBooking())
    print(ferry_service_total())
    print(booking_approval())
display_booking()