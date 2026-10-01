

# JUNIOR CHALLENGE

# use this dataset

data = {
    "study_hours": [2, 3, 4, 5, 6, 7, 8, 9],
    "sleep_hours": [5, 6, 6, 7, 7, 8, 8, 9],
    "attendance": [55, 60, 70, 75, 80, 85, 90, 95],
    "result": [
        "Fail", "Fail", "Pass", "Pass",
        "Pass", "Pass", "Pass", "Pass"
    ]
}



#Tasks:
#1. Create a DataFrame.
#2. Identify the features.
#3. Identify the label.
#4. Create X and y.
#5. Split into 75% training and 25% testing data.
#6. Print X_train, X_test, y_train and y_test.
#7. Print the shapes.

# Do not look at the solution until you have tried it yourself.

import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    "study_hours": [2, 3, 4, 5, 6, 7, 8, 9],
    "sleep_hours": [5, 6, 6, 7, 7, 8, 8, 9],
    "attendance": [55, 60, 70, 75, 80, 85, 90, 95],
    "result": ["Fail", "Fail", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass"]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

features = ["study_hours", "sleep_hours", "attendance"]
label = "result"

print("\nFeatures:")
print(features)

print("\nLabel:")
print(label)

X = df[features]
y = df[label]

print("\nX:")
print(X)

print("\ny:")
print(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

print("\nX_train:")
print(X_train)

print("\nX_test:")
print(X_test)

print("\ny_train:")
print(y_train)

print("\ny_test:")
print(y_test)

print("\nShapes:")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)