from clean_data import df
import matplotlib.pyplot as plt
import pandas as pd

# a. Show sales by category 
sales_by_category = df.groupby("Category")["Sales"].sum()

plt.bar(sales_by_category.index, sales_by_category.values)

plt.title("Sales by category")
plt.xlabel("Category")
plt.ylabel("Sales ($)")

plt.show()
#=========================================================================================
#b. Total profit by region

profit_by_region = df.groupby("Region")["Profit"].sum()

plt.bar(profit_by_region.index, profit_by_region.values)

plt.title("Profit by region")
plt.xlabel("Region")
plt.ylabel("Profit ($)")

plt.show()
#=========================================================================================

##c. Monthly sales trends 


df["Month"] = df["Order Date"].dt.month
df["Year"] = df["Order Date"].dt.year


monthly_sales = df.groupby(["Year","Month"])["Sales"].sum().unstack(level=0)
monthly_orders = df.groupby(["Year","Month"])["Order ID"].nunique().sort_index().unstack(level=0)

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

for year in monthly_sales.columns:

    axes[0].plot(monthly_sales.index,
             monthly_sales[year], 
             marker = "o",
             label = year)

axes[0].set_title("Monthly sales trend")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Sales ($)")
axes[0].set_xticks(range(1, 13))
axes[0].legend(title="Year")
axes[0].grid(True, alpha=0.3)


#=========================================================================================

##d. Monthly Order Volume Trend

for year in monthly_orders.columns:

    axes[1].plot(monthly_orders.index,
             monthly_orders[year], 
             marker = "o",
             label = year)

axes[1].set_title("Monthly orders trend")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Orders")
axes[1].set_xticks(range(1, 13))
axes[1].legend(title="Year")
axes[1].grid(True, alpha=0.3)

plt.show()