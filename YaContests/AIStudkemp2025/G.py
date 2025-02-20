import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import warnings

warnings.filterwarnings('ignore')
train_df = pd.read_csv('H1/train.csv')
test_df = pd.read_csv('H1/test.csv')
train_df = pd.get_dummies(train_df, columns=['B'], prefix='B')
test_df = pd.get_dummies(test_df, columns=['B'], prefix='B')
train_columns = train_df.drop('target', axis=1).columns
test_df = test_df.reindex(columns=train_columns, fill_value=0)

X = train_df.drop('target', axis=1)
y = train_df['target']
X_test = test_df

scaler = StandardScaler()
numeric_cols = ['A', 'C', 'D', 'E', 'F']
X[numeric_cols] = scaler.fit_transform(X[numeric_cols])
X_test[numeric_cols] = scaler.transform(X_test[numeric_cols])
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred_val = model.predict(X_val)
rmse = np.sqrt(mean_squared_error(y_val, y_pred_val))
print(f'RMSE на валидации: {rmse}')
y_test_pred = model.predict(X_test)

submission = pd.DataFrame({'target': y_test_pred})
submission.to_csv('answers.csv', index=False)
print("Файл answers.csv сохранён!")
