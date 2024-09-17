def main():
    import sys
    from collections import defaultdict
    sales_data = defaultdict(lambda: defaultdict(int))

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        buyer, product, quantity = line.split()
        quantity = int(quantity)
        sales_data[buyer][product] += quantity

    for buyer in sorted(sales_data.keys()):
        print(f'{buyer}:')
        for product in sorted(sales_data[buyer].keys()):
            print(f'{product} {sales_data[buyer][product]}')

if __name__ == '__main__':
    main()
