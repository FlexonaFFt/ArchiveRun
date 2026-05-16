import matplotlib.pyplot as plt
import pandas as pd
import os

os.makedirs('images', exist_ok=True)

df = pd.read_csv('stats.csv')  # day,points,place,bonus

days = df['day']
points = df['points']
places = df['place']
bonus = df['bonus']

plt.figure(figsize=(10, 5))
plt.plot(days, places, marker='o', color='deepskyblue', alpha=0.6)
for x, y in zip(days, places):
    plt.text(x, y + 0.2, f'{y}', ha='center', fontsize=8)
plt.title('Место по дням')
plt.xlabel('День')
plt.ylabel('Место')
plt.gca().invert_yaxis()
plt.grid(True)
plt.xticks(days)
plt.tight_layout()
plt.savefig('images/places_by_day.png')
plt.close()

total_points = (points + bonus).cumsum()
plt.figure(figsize=(10, 5))
plt.plot(days, total_points, marker='o', color='mediumseagreen', alpha=0.7)
for x, y, p, b in zip(days, total_points, points, bonus):
    plt.text(x, y + 0.3, f'{y}', ha='center', fontsize=8)
    if b > 0:
        plt.text(x, y - 1.2, f'+{b}', ha='center', fontsize=8, color='deepskyblue')
plt.title('Рост баллов по дням (накопительно, с учётом бонусов)')
plt.xlabel('День')
plt.ylabel('Суммарные баллы')
plt.grid(True)
plt.xticks(days)
plt.tight_layout()
plt.savefig('images/total_points_by_day.png')
plt.close()
