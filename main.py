import pandas as pd
from data_class.OrderSystem import OrderSystem
import matplotlib.pyplot as plt
import seaborn as sns

ordersystem_instance = OrderSystem(orders_path=r'./data/Orders.xlsx', restaurants_path=r"./data/Restaurants.xlsx")

df = ordersystem_instance.load_data()
print(df.columns)

# Peek Hours
# df['Order Date'].value_counts().sort_index().plot.barh()
# plt.show()

# Payment Mode
# df['Payment Mode'].value_counts().sort_index().plot.bar()
# plt.xticks(rotation=0)
# plt.show()


# Avg Order Price
# sns.boxplot(x="RestaurantID", y="Order Amount", data=df)
# plt.ylabel("RestaurantID")
# plt.xlabel("Order Amount")
# plt.show()

# Customer Rating
# df.groupby("RestaurantID")['Customer Rating-Food'].value_counts().unstack().plot(kind='bar')
# plt.xticks(rotation=0)
# plt.ylabel("RestaurantID")
# plt.xlabel("Customer Rating-Food")
# plt.show()


# Order Item System All Restaurant Split
# sns.boxplot(x="RestaurantID", y="Quantity of Items", data=df)
# plt.ylabel("Resturant Id")
# plt.xlabel("Number of Items in Order")
# plt.title("Distribution of Number of Items in Single Order")
# plt.show()


# Order Item System All Restaurant in One
# plt.boxplot(df['Quantity of Items'], vert=False)
# plt.xlabel("Number of Items in Order")
# plt.title("Distribution of Number of Items in Single Order")
# plt.show()


# Order By All Zone
# df.groupby("Zone")['RestaurantName'].value_counts().unstack().plot(kind='bar')
# plt.ylabel("RestaurantID")
# plt.xlabel("Customer Rating-Food")
# plt.show()

# Order by Zone Sperated (Popular Restaurant By Zone)
# zoneA = df.loc[df['Zone'] == 'Zone A'].reset_index()
# zoneA['RestaurantName'].value_counts().plot(kind='bar')
# plt.xticks(rotation=0)
# plt.ylabel("Total Order")
# plt.xlabel("RestaurantName")
# plt.show()
#
# zoneA = df.loc[df['Zone'] == 'Zone D'].reset_index()
# zoneA['RestaurantName'].value_counts().plot(kind='bar')
# plt.xticks(rotation=0)
# plt.ylabel("Total Order")
# plt.xlabel("RestaurantName")
# plt.show()
#
# zoneA = df.loc[df['Zone'] == 'Zone C'].reset_index()
# zoneA['RestaurantName'].value_counts().plot(kind='bar')
# plt.xticks(rotation=0)
# plt.ylabel("Total Order")
# plt.xlabel("RestaurantName")
# plt.show()
#
# zoneA = df.loc[df['Zone'] == 'Zone D'].reset_index()
# zoneA['RestaurantName'].value_counts().plot(kind='bar')
# plt.xticks(rotation=0)
# plt.ylabel("Total Order")
# plt.xlabel("RestaurantName")
# plt.show()

# Most Popular Restaurant by Cuisine
# cuisines = df["Cuisine"].unique()
# for cuisine in cuisines:
#     temp_df = df.loc[df['Cuisine'] == cuisine].reset_index()
#     temp_df['RestaurantName'].value_counts().plot(kind='bar')
#     plt.title(cuisine)
#     plt.xticks(rotation=0)
#     plt.ylabel("Total Count")
#     plt.xlabel("RestaurantName")
#     plt.show()

# Most Popular Cuisine by Zone
# zones = df["Zone"].unique()
# for zone in zones:
#     temp_df = df.loc[df['Zone'] == zone].reset_index()
#     temp_df.groupby("Cuisine")['RestaurantName'].value_counts().unstack().plot(kind='bar')
#     plt.title(zone)
#     plt.xticks(rotation=0)
#     plt.ylabel("Total Count")
#     plt.xlabel("Cuisine")
#     plt.show()


# Most Popular Cuisine Whole
# df["Cuisine"].value_counts().plot(kind='bar')
# plt.ylabel("Total Order")
# plt.xticks(rotation=0)
# plt.xlabel("Cuisine")
# plt.show()

# cuisines = df["Cuisine"].unique()
# for cuisine in cuisines:
#     temp_df = df.loc[df['Cuisine'] == cuisine].reset_index()
#     sns.boxplot(y="RestaurantName", x="Order Amount", data=temp_df, vert=False)
#     plt.ylabel("Restaurant Name")
#     plt.xlabel("Order Amount")
#     plt.title("Distribution of Order Amount for  Cuisine : " + cuisine)
#     plt.show()

# zones = df["Zone"].unique()
# for zone in zones:
#     temp_df = df.loc[df['Zone'] == zone].reset_index()
#     sns.boxplot(y="RestaurantName", x="Order Amount", data=temp_df, vert=False)
#     plt.ylabel("Restaurant Name")
#     plt.xlabel("Order Amount")
#     plt.title("Distribution of Order Amount for Zone : " + zone)
#     plt.show()

# Categories = df["Category"].unique()
# for category in Categories:
#     temp_df = df.loc[df['Category'] == category].reset_index()
#     sns.boxplot(y="RestaurantName", x="Order Amount", data=temp_df, vert=False)
#     plt.ylabel("Restaurant Name")
#     plt.xlabel("Order Amount")
#     plt.title("Avg Order Amount for Category : " + category)
#     plt.show()

# Categories = df["Category"].unique()
# for category in Categories:
#     temp_df = df.loc[df['Category'] == category].reset_index()
#     sns.boxplot(y="RestaurantName", x="Quantity of Items", data=temp_df, vert=False)
#     plt.ylabel("Restaurant Name")
#     plt.xlabel("Quantity of Items")
#     plt.title("Avg Quantity of Items for Category : " + category)
#     plt.show()

# Categories = df["Category"].unique()
# for category in Categories:
#     temp_df = df.loc[df['Category'] == category].reset_index()
#     sns.boxplot(y="RestaurantName", x="Quantity of Items", data=temp_df, vert=False)
#     plt.ylabel("Restaurant Name")
#     plt.xlabel("Quantity of Items")
#     plt.title("Avg Quantity of Items for Category : " + category)
#     plt.show()

# Number of Orders by Category / RestaurantName
# df["Category"].value_counts().plot(kind='bar')
# plt.ylabel("Total Order")
# plt.xticks(rotation=0)
# plt.xlabel("Category")
# plt.title("Distribution of Order Amount for Category")
# plt.show()
