import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# 1. Yeh bina internet ke chalega (In-built Flowers Dataset)
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['Target'] = iris.target

# 2. Data ko Machine ke samajhne layak baant rahe hain
X = df.drop(columns=['Target'])
y = df['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Model ko train kar rahe hain
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 4. Result aur Pehli 5 lines screen par dikhegi
print("🚀 SUCCESS! your machine learning model has been trained!")
print(f"🎯 Model Accuracy: {model.score(X_test, y_test) * 100:.2f}%")
print("\n👇 here is your Data which learned by your machine")
df.head()
print(df.head())
