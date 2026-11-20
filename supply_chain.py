from clean_data import df
import matplotlib.pyplot as plt

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

#=========================================================================================
##e. Order Processing Lead Time

df["Lead Time"] = (df["Ship Date"] - df["Order Date"]).dt.days
valid_df = df[df["Lead Time"].notna() & (df["Lead Time"] >= 0)].copy()

orders = valid_df.drop_duplicates(subset =["Order ID"])

avg_lead_time = orders["Lead Time"].mean()
median_lead_time = orders["Lead Time"].median()
max_lead_time = orders["Lead Time"].max()
min_lead_time = orders["Lead Time"].min()

check = valid_df.groupby("Order ID").agg(
    order_dates=("Order Date", "nunique"),
    ship_dates=("Ship Date", "nunique")
)

print(check[
    (check["order_dates"] > 1) |
    (check["ship_dates"] > 1)
])

print(f"Average Lead Time: {avg_lead_time:.2f} days")
print(f"Median Lead Time: {median_lead_time:.2f} days")
print(f"Max Lead Time: {max_lead_time:.2f} days")
print(f"Min Lead Time: {min_lead_time:.2f} days")
print("Total rows:", len(valid_df))
print("Unique orders:", valid_df["Order ID"].nunique())
print("Rows after deduplication:", len(orders))

plt.figure(figsize=(9,5))

plt.hist(orders["Lead Time"],range(-1,9), align="mid")

plt.title("Order Processing Lead Time Distribution")
plt.xlabel("Lead Time (Days)")
plt.ylabel("Number of Orders")
plt.grid(axis="y", alpha=0.3)
plt.show()

#=========================================================================================
##f. Shipping Mode Performance
ship_mode = orders.groupby("Ship Mode").agg(Orders=("Order ID", "nunique"),
                                            Avg_Lead_Time=("Lead Time", "mean"),
                                            Median_Lead_Time=("Lead Time","median"),
                                            Min_Lead_Time=("Lead Time","min"),
                                            Max_Lead_Time=("Lead Time","max")).sort_values(by="Avg_Lead_Time")
ship_mode["Proportion"] = ship_mode["Orders"]/ship_mode["Orders"].sum()

print(orders.head(20))
print(ship_mode.head(20))