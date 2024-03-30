# Giá của từng món ăn
prices = {'Gà rán': 30000, 'Hamburger': 25000, 'Cocacola': 10000}

# Yêu cầu người dùng nhập số lượng từng món ăn
print("Chào mừng các bạn đến với nhà hàng thức ăn nhanh!")
print("Mời bạn nhập số lượng từng món ăn: ")
quantities = {item: int(input(f"{item}: ")) for item in prices}

# In ra hóa đơn và tính tổng trước thuế
print("\nHóa đơn: ")
total_before_tax = sum(quantity * prices[item] for item, quantity in quantities.items())
for item, quantity in quantities.items():
    print(f"{item:<20}{prices[item]:,.0f}đ x {quantity}")
print("\nTổng trước thuế: ")
for item, quantity in quantities.items():
    print(f"{item:<20}{quantity * prices[item]:,.0f}đ")

# Tính và in ra tổng sau thuế
tax_rate = 0.05
tax = total_before_tax * tax_rate
total_after_tax = total_before_tax + tax
print(f"\nTổng sau thuế: {total_after_tax:,.0f}đ")
