def conditioner_settings(troom, tcond, mode):
    if mode == 'freeze':
        result = min(troom, tcond)
        return result
    elif mode == 'heat':
        result = max(troom, tcond)
        return result
    elif mode == 'auto':
        result = tcond
        return result
    elif mode == 'fan':
        result = troom
        return result

def main():
    troom, tcond = map(int, input().split())
    mode = input().strip()
    print(conditioner_settings(troom, tcond, mode))

if __name__ == '__main__':
    main()
