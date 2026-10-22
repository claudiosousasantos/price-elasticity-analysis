import numpy as np

# Simulating a product's price and quantity sold across different time periods
prices = np.array([20.00, 22.00, 25.00, 18.00, 24.00, 20.00])
quantity_sold = np.array([500, 420, 300, 600, 350, 490])

pct_change_price = np.diff(prices) / prices[:-1]
pct_change_quantity = np.diff(quantity_sold) / quantity_sold[:-1]

elasticity = pct_change_quantity / pct_change_price

average_elasticity = np.mean(elasticity)
print(f"Average elasticity: {average_elasticity:.2f}")

if average_elasticity < -1:
    print("📉 Demand is elastic — customers are highly sensitive to price changes")
elif -1 <= average_elasticity < 0:
    print("📊 Demand is inelastic — customers are relatively insensitive to price changes")
else:
    print("📈 Unusual pattern — demand increases with price (possible luxury good behavior)")

current_price = 20.00
current_quantity = 490

proposed_price_change_pct = 0.10  # testing a 10% price increase

estimated_quantity_change_pct = average_elasticity * proposed_price_change_pct
estimated_new_quantity = current_quantity * (1 + estimated_quantity_change_pct)

new_price = current_price * (1 + proposed_price_change_pct)
estimated_new_revenue = new_price * estimated_new_quantity
current_revenue = current_price * current_quantity

print(f"Current: ${current_price} x {current_quantity} units = ${current_revenue:.2f} revenue")
print(f"Proposed: ${new_price:.2f} x {estimated_new_quantity:.0f} units = ${estimated_new_revenue:.2f} revenue")