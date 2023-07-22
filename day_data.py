import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

#data
df = pd.read_csv('./src/restaurant-1-orders.csv', delimiter=',')

myDict1 = {}
id = []

for row in df['Item Name']:
    myDict1[row] = 0

items = list(myDict1.keys())


for i in range(len(items)):
  df['Item Name'] = df['Item Name'].replace(items[i], items[i%20])

myDict1 = {}

for row in df['Item Name']:
    myDict1[row] = 0

items = list(myDict1.keys())


names_dict = {}

for i, name in enumerate(items):
  names_dict[name] = i


for row in df['Item Name']:
    id.append(names_dict[row])
df['Item Id'] = id

df['Order Date'] = pd.to_datetime(df['Order Date'],dayfirst = True)
df['Hour'] = df['Order Date'].dt.hour
df['Minute'] = df['Order Date'].dt.minute
df['Day'] = df['Order Date'].dt.day
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year
df['Weekday'] = df['Order Date'].dt.weekday

df['Order Number'] = df['Order Number'].astype(int)


#df.sort_values(by = ['Year', 'Month','Day','Hour','Minute'], ascending = [True, True, True,True, True])
df = df.sort_values(by=['Order Number'],ascending = True)

"""##Train the model based on each day"""

# train the data based on weekday
df3 = df.groupby(['Year','Month','Day','Weekday','Item Id'])['Quantity'].sum()
df3 = df3.reset_index()
df3

# Preprocess the data and extract features and labels
X1 = df3[['Item Id', 'Weekday', 'Day', 'Month','Year']]
y1 = df3['Quantity']

# Split the dataset into training and testing sets
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)

# Initialize the Random Forest Regressor
random_forest1 = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the Random Forest model
random_forest1.fit(X1_train, y1_train)

# Make predictions on the test set
y1_pred = random_forest1.predict(X1_test)

row2 = df3.iloc[100][:5]


input_2 = [[3,2,23,12,2023],[2,1,23,12,2018],[5,0,23,12,2017],[0,5,23,12,2019],[3,4,23,12,2017]] #[Item Id,Weekday,Day,Month,Year]
output2 = random_forest1.predict(input_2)
ItemNames = [items[input_2[0][0]],items[input_2[1][0]],items[input_2[2][0]],items[input_2[3][0]],items[input_2[4][0]]]
data = [{"ItemName": Predicted_ItemNames, "Quantity": int(Predicted_Quantity)} for Predicted_ItemNames, Predicted_Quantity in zip(ItemNames, output2)]
print(data)
