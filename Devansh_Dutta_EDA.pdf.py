import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
customers = pd.read_csv("Customers.csv")
products = pd.read_csv("Products.csv")
transactions = pd.read_csv("Transactions.csv")

# Display basic information
print("Customers Dataset:\n", customers.head(), "\n")
print("Products Dataset:\n", products.head(), "\n")
print("Transactions Dataset:\n", transactions.head(), "\n")

# Summary Statistics
print("Customers Summary:\n", customers.describe(include='all'), "\n")
print("Products Summary:\n", products.describe(include='all'), "\n")
print("Transactions Summary:\n", transactions.describe(include='all'), "\n")

# Data Cleaning (Example: Check for missing values)
def check_missing(df, name):
    missing = df.isnull().sum()
    print(f"Missing values in {name}:\n", missing[missing > 0], "\n")

check_missing(customers, "Customers")
check_missing(products, "Products")
check_missing(transactions, "Transactions")

# Merging datasets for analysis
merged_data = transactions.merge(customers, on="CustomerID").merge(products, on="ProductID")

# EDA Visualization Examples
plt.figure(figsize=(10, 6))
sns.countplot(data=customers, x="Region", order=customers["Region"].value_counts().index)
plt.title("Customer Distribution by Region")
plt.show()

plt.figure(figsize=(10, 6))
most_popular_products = merged_data["ProductName"].value_counts().head(10)
sns.barplot(x=most_popular_products.values, y=most_popular_products.index)
plt.title("Top 10 Most Popular Products")
plt.xlabel("Number of Transactions")
plt.ylabel("Product Name")
plt.show()

# Business Insights (Placeholder for PDF report generation)
insights = [
    "Insight 1: Placeholder for the most purchased product information.",
    "Insight 2: Placeholder for regional customer distribution trends.",
    "Insight 3: Placeholder for sales trends over time.",
    "Insight 4: Placeholder for customer signup trends.",
    "Insight 5: Placeholder for high-value transaction identification."
]

# Print insights for review
for i, insight in enumerate(insights, 1):
    print(f"Insight {i}: {insight}\n")
