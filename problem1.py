print("\n\nSHOPPING CART CALCULATOR")
print("========================================")

def calculate_item_total(quantity, unit_price):
    return quantity * unit_price

def apply_bulk_discount(total, quantity):
    if quantity >= 10:
        discount = 10
    elif quantity >= 5:
        discount = 5
    else:
        discount = 0
    return round(total * discount / 100, 2)

def calculate_tax(subtotal, tax_rate):
    return subtotal * tax_rate / 100

def is_eligible_for_free_shipping(subtotal):
    if subtotal >= 50:
        return True
    else:
        return False

def process_order(item_name, quantity, unit_price, tax_rate):
    item_total = calculate_item_total(quantity, unit_price)
    bulk_discount_amount = apply_bulk_discount(item_total, quantity)
    subtotal = item_total - bulk_discount_amount
    tax_amount = calculate_tax(subtotal, tax_rate)
    after_tax = subtotal + tax_amount    #final total
    shipping_eligibility = is_eligible_for_free_shipping(subtotal)
    amount_needed_for_free_shipping = 0 if shipping_eligibility else 50 - subtotal

    print(f"Order Receipt for: {item_name}")
    print(f"  Quantity: {quantity} @ ${unit_price:.2f} each")
    print(f"  Item Total: ${item_total:.2f}")
    if bulk_discount_amount > 0:
        print(f"  Bulk Discount: -${bulk_discount_amount:.2f}")
    print(f"  Subtotal: ${subtotal:.2f}")
    print(f"  Tax ({tax_rate}%): ${tax_amount:.2f}")
    print(f"  Final Total: ${after_tax:.2f}")
    print(f"  Need ${amount_needed_for_free_shipping:.2f} more for free shipping")
    print(f"----------------------------------------")
    

process_order("Notebooks", 12, 3.50, 8)
process_order("Pens", 6, 1.25, 8)
process_order("Paper", 3, 4.99, 8)
