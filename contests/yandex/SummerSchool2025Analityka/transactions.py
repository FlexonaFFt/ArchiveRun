import pandas as pd

def process(customers, transactions):
    # Шаг 1: Фильтрация данных
    # Оставляем только успешные транзакции и те, где сумма <= 1 000 000
    filtered_transactions = transactions[
        (transactions['success_flg'] == 1) &
        (transactions['amount_rur'] <= 1_000_000)
    ]

    # Сортируем транзакции по клиенту и времени транзакции
    filtered_transactions = filtered_transactions.sort_values(by=['customer_id', 'transaction_dttm'])

    # Шаг 2: Добавляем индекс транзакций для каждого клиента
    filtered_transactions['transaction_rank'] = filtered_transactions.groupby('customer_id').cumcount() + 1

    # Шаг 3: Добавляем колонки с максимальной суммой до текущей транзакции
    filtered_transactions['max_amount_before'] = filtered_transactions.groupby('customer_id')['amount_rur'].cummax()

    # Шаг 4: Определяем интересные транзакции
    # Транзакция считается интересной, если:
    # 1. Она больше всех предыдущих
    # 2. Или она последняя для клиента
    interesting_transactions = filtered_transactions[
        (filtered_transactions['amount_rur'] > filtered_transactions['max_amount_before']) |
        (filtered_transactions['transaction_rank'] == filtered_transactions.groupby('customer_id')['transaction_rank'].transform('max'))
    ]

    # Шаг 5: Объединяем с таблицей customers для получения имени клиента
    result = pd.merge(
        interesting_transactions[['customer_id', 'id']],
        customers[['id', 'name']],
        left_on='customer_id',
        right_on='id',
        how='left'
    )

    result = result.rename(columns={
        'name': 'customer_name',
        'id_x': 'transaction_id'
    })[['customer_name', 'transaction_id']]

    return result
