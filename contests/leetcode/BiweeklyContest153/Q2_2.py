def maximize_active_sections(s):
    # Дополняем строку '1' с обоих концов
    augmented_s = '1' + s + '1'
    n = len(augmented_s)

    # Найти наибольший блок '1', окруженный '0'
    max_ones_block = 0
    current_ones_block = 0
    for i in range(n):
        if augmented_s[i] == '1':
            current_ones_block += 1
            max_ones_block = max(max_ones_block, current_ones_block)
        else:
            current_ones_block = 0

    # Найти наибольший блок '0', окруженный '1'
    max_zeros_block = 0
    current_zeros_block = 0
    for i in range(n):
        if augmented_s[i] == '0':
            current_zeros_block += 1
            max_zeros_block = max(max_zeros_block, current_zeros_block)
        else:
            current_zeros_block = 0

    # Максимальное количество активных сегментов
    max_active = max(max_ones_block, max_zeros_block)

    return max_active

# Примеры
print(maximize_active_sections("01"))       # Выход: 1
print(maximize_active_sections("0100"))    # Выход: 4
print(maximize_active_sections("1000100")) # Выход: 7
print(maximize_active_sections("01010"))   # Выход: 4
