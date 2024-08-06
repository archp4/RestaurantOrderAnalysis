import pandas as pd


class OrderSystem:
    def __init__(self, orders_path, restaurants_path):
        self.orders_path = orders_path
        self.restaurants_path = restaurants_path

    def load_data(self):
        xl_file = pd.read_excel(self.orders_path, parse_dates=['Order Date'])
        orders_df = xl_file
        xl_file = pd.ExcelFile(self.restaurants_path)
        restaurants_df = xl_file.parse()
        dataFrame = pd.merge(left=orders_df, right=restaurants_df, how='inner', on=['RestaurantID'])

        return dataFrame

    def replace_missing_mean(self, data, label, column):
        data[column] = data[column].fillna(data.groupby(label)[column].transform('mean'))
        return data
