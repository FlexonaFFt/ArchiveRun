import pandas as pd
import numpy as np
from scipy.interpolate import RBFInterpolator
from sklearn.metrics import r2_score

train_df = pd.read_csv('H2/field_train.csv')
longitudes = np.arange(55.0, 60.1, 0.1)
latitudes = np.arange(34.0, 37.1, 0.1)
grid_lon, grid_lat = np.meshgrid(longitudes, latitudes)
grid_points = np.vstack((grid_lon.ravel(), grid_lat.ravel())).T

train_points = train_df[['longitude', 'latitude']].values
train_intensity = train_df['intensity'].values

interpolator = RBFInterpolator(train_points, train_intensity, kernel='thin_plate_spline')
pred_intensity = interpolator(grid_points)

answers_df = pd.DataFrame({
    'longitude': grid_points[:, 0],
    'latitude': grid_points[:, 1],
    'intensity': pred_intensity
})

answers_df['intensity'] = np.round(answers_df['intensity'], 2)
answers_df.to_csv('answers.csv', index=False)
print("Файл answers.csv сохранён!")

train_pred = interpolator(train_points)
r2 = r2_score(train_intensity, train_pred)
print(f'R^2 на обучающих данных: {r2}')
