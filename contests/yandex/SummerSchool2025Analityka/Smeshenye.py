import pandas as pd

def get_sample(df):
    """
    Функция принимает датафрейм с вердиктами модерации и возвращает 100 banner_id
    с наивысшей долей возможных ошибочных отклонений.

    Параметры:
    df - pandas.DataFrame с колонками: user_id, banner_id, verdict

    Возвращает:
    pandas.DataFrame с одной колонкой banner_id, содержащий 100 баннеров
    """
    # Группируем по banner_id и считаем статистику
    grouped = df.groupby('banner_id')['verdict'].agg(['count', 'sum']).reset_index()

    # Переименовываем колонки для ясности
    grouped.columns = ['banner_id', 'total_verdicts', 'approved_count']

    # Вычисляем отклоненные (No) - общее количество минус принятые (Yes)
    grouped['rejected_count'] = grouped['total_verdicts'] - grouped['approved_count']

    # Вычисляем долю отклонений
    grouped['rejection_rate'] = grouped['rejected_count'] / grouped['total_verdicts']

    # Сортируем по доле отклонений (по убыванию) и берем топ-100
    result = grouped.sort_values(by='rejection_rate', ascending=False).head(100)

    # Возвращаем только колонку banner_id в виде датафрейма
    return result[['banner_id']]
