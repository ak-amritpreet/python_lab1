def calculate_bill(cleaned, filled, xray):
    subtotal = 0
    
    if cleaned == 'y':
        subtotal += 60
    
    if filled == 'y':
        subtotal += 200
    
    if xray == 'y':
        subtotal += 100
    
    tax = subtotal * 0.15
    total = subtotal + tax
    
    if total > 300:
        total *= 0.9
    elif total > 200:
        total *= 0.95
    
    return (subtotal, tax, total)


print("Melanie Dental Clinic")
print("---------------------")

name = input("Enter patient's name: ")
cleaned = input("Was cleaning performed? (y/n): ")
filled = input("Was cavity-filling performed? (y/n): ")
xray = input("Was X-Ray performed? (y/n): ")

subtotal, tax, total = calculate_bill(cleaned, filled, xray)

print("---------------------")
print(f"Receipt for patient name: {name}")
print("---------------------")
print(f"Subtotal: ${subtotal}")
print(f"Tax: ${tax}")
print("---------------------")
print(f"Total: ${total}")
