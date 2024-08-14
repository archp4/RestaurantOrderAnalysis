import pandas as pd
from datetime import datetime
from data_class.OrderSystem import OrderSystem
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ordersystem_instance = OrderSystem(orders_path=r'./data/Orders.xlsx', restaurants_path=r"./data/Restaurants.xlsx")

df = ordersystem_instance.load_data()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/peak_hours")
async def peak_hours():
    # Peek Hours
    temp_df = df['Order Date'].dt.strftime('%H:%M')
    peek_hours = temp_df.value_counts().sort_index().to_dict()
    keys = []
    values = []
    for k in peek_hours.keys():
        keys.append(k)
    for v in peek_hours.values():
        values.append(v)
    return {
        "labels": keys,
        "values": values
    }


@app.get("/payment_mode")
def payment_mode():
    # Payment Mode
    dict_data = df['Payment Mode'].value_counts().sort_index().to_dict()
    keys = []
    values = []
    for k in dict_data.keys():
        keys.append(k)
    for v in dict_data.values():
        values.append(v)
    return {
        "labels": keys,
        "values": values
    }


@app.get("/avg_order_price")
def avg_order_price():
    # Avg Order Price
    stats = df.groupby("RestaurantID")["Order Amount"].describe(percentiles=[.25, .5, .75])

    print(stats)
    # Extract the values needed for Chart.js
    chart_data = []
    labels = []
    for restaurant_id, group in stats.iterrows():
        labels.append(restaurant_id)
        chart_data.append({
                'x': restaurant_id,
                'min': group['min'],
                'q1': group['25%'],
                'median': group['50%'],
                'q3': group['75%'],
                'high': group['max']
        })
    return {
        "labels": labels,
        "datasets": chart_data
    }


@app.get("/customer_rating")
def customer_rating():
    # Customer Rating
    return df.groupby("RestaurantID")['Customer Rating-Food'].value_counts().unstack(fill_value=0).to_dict(orient='index')


@app.get("/order_item_system_all_restaurant")
def order_item_system_all_restaurant():
    # Order Item System All Restaurant Split
    stats = df.groupby("RestaurantID")["Quantity of Items"].describe(percentiles=[.25, .5, .75])
    # Extract the values needed for Chart.js
    chart_data = []
    labels = []
    for restaurant_id, group in stats.iterrows():
        labels.append(restaurant_id)
        chart_data.append({
                'x': restaurant_id,
                'min': group['min'],
                'q1': group['25%'],
                'median': group['50%'],
                'q3': group['75%'],
                'high': group['max']
        })
    return {
        "labels": labels,
        "datasets": chart_data
    }


@app.get("/order_item_system_single")
def order_item_system_single():
    # Order Item System All Restaurant in Single Box
    stats = df['Quantity of Items'].describe(percentiles=[.25, .5, .75])
    min_val = stats['min']
    q1 = stats['25%']
    median = stats['50%']
    q3 = stats['75%']
    max_val = stats['max']

    return {
        'x': "Quantity of Items",
        'min': min_val,
        'q1': q1,
        'median': median,
        'q3': q3,
        'high': max_val
    }


@app.get("/most_popular_r_cuisine")
def most_popular_r_cuisine():
    # Most Popular Restaurant by Cuisine
    cuisines = df["Cuisine"].unique()
    result = {}
    for cuisine in cuisines:
        temp_df = df.loc[df['Cuisine'] == cuisine].reset_index()
        result[cuisine] = temp_df['RestaurantName'].value_counts().to_dict()

    return result


@app.get("/most_popular_r_zone")
def most_popular_r_zone():
    # Most Popular Cuisine by Zone
    zones = df["Zone"].unique()
    result = {}
    for zone in zones:
        temp_df = df.loc[df['Zone'] == zone].reset_index()
        result[zone] = temp_df.groupby("Cuisine")['RestaurantName'].value_counts().unstack(fill_value=0).to_dict(orient='index')

    return result


@app.get("/most_popular_cuisine")
def most_popular_cuisine():
    # Cuisine Count
    cuisines = df["Cuisine"].value_counts().to_dict()
    keys = []
    values = []
    for k in cuisines.keys():
        keys.append(k)
    for v in cuisines.values():
        values.append(v)
    return {
        "labels": keys,
        "values": values
    }


@app.get("/most_popular_cat")
def most_popular_cat():
    # Most Popular Cuisine by Zone
    categories = df["Category"].value_counts().to_dict()
    keys = []
    values = []
    for k in categories.keys():
        keys.append(k)
    for v in categories.values():
        values.append(v)
    return {
        "labels": keys,
        "values": values
    }


@app.get("/most_order_r_cuisine")
def most_order_r_cuisine():
    # Most Popular Restaurant by Cuisine
    cuisines = df["Cuisine"].unique()
    labels = []
    datasets = []
    for cuisine in cuisines:
        temp_df = df.loc[df['Cuisine'] == cuisine].reset_index()
        stats = temp_df['Order Amount'].describe(percentiles=[.25, .5, .75])
        min_val = stats['min']
        q1 = stats['25%']
        median = stats['50%']
        q3 = stats['75%']
        max_val = stats['max']
        labels.append(cuisine)
        datasets.append({
            'x': cuisine,
            'min': min_val,
            'q1': q1,
            'median': median,
            'q3': q3,
            'high': max_val
        })

    return {
        "labels": labels,
        "datasets": datasets
    }


@app.get("/most_order_r_zone")
def most_order_r_zone():
    # Most Popular Cuisine by Zone
    zones = df["Zone"].unique()
    labels = []
    datasets = []

    for zone in zones:
        temp_df = df.loc[df['Zone'] == zone].reset_index()
        stats = temp_df['Order Amount'].describe(percentiles=[.25, .5, .75])
        min_val = stats['min']
        q1 = stats['25%']
        median = stats['50%']
        q3 = stats['75%']
        max_val = stats['max']
        labels.append(zone)
        datasets.append({
            'x': zone,
            'min': min_val,
            'q1': q1,
            'median': median,
            'q3': q3,
            'high': max_val
        })

    return {
        "labels": labels,
        "datasets": datasets
    }


@app.get("/most_order_r_cat")
def most_order_r_cat():
    # Most Popular Cuisine by Category
    Categories = df["Category"].unique()
    labels = []
    datasets = []

    for category in Categories:
        temp_df = df.loc[df['Category'] == category].reset_index()
        stats = temp_df['Order Amount'].describe(percentiles=[.25, .5, .75])
        min_val = stats['min']
        q1 = stats['25%']
        median = stats['50%']
        q3 = stats['75%']
        max_val = stats['max']
        labels.append(category)
        datasets.append({
            'x': category,
            'min': min_val,
            'q1': q1,
            'median': median,
            'q3': q3,
            'high': max_val
        })

    return {
        "labels": labels,
        "datasets": datasets
    }

