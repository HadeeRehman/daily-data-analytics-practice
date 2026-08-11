# Compare sales against targets and calculate regional tax using broadcasting
import numpy as np

sales = np.array([
    [1000, 2000, 3000],
    [1500, 2500, 3500],
    [1200, 2200, 3200]
])
# 3 regions, 3 products

targets = np.array([1200, 2000, 3000])  # target per product
tax_rates = np.array([0.1, 0.15, 0.2])  # tax per region

farnes = sales - targets # Subtract targets from sales — how far is each region from target per product?

cell_target = sales >= targets

reshaping = tax_rates.reshape(3, 1) # 3 rows, 1 columns. 

tax_rates_per_region = sales * reshaping

total_tax_paid = np.sum(tax_rates_per_region, axis=1)

print(total_tax_paid)