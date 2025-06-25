def solution(n, m):
    left, right = 0, int((n + m) ** 0.5) + 1
    while left < right:
        mid = (left + right + 1) // 2
        total_cells = mid * mid
        
        if mid % 2 == 0:
            needed_white = total_cells // 2
            needed_black = total_cells // 2
        else:
            needed_min = total_cells // 2
            needed_max = total_cells // 2 + 1
            
            variant1 = (n >= needed_max and m >= needed_min)
            variant2 = (n >= needed_min and m >= needed_max)
            
            if variant1 or variant2:
                left = mid
            else:
                right = mid - 1
            continue
        
        if n >= needed_white and m >= needed_black:
            left = mid
        else:
            right = mid - 1
    
    return left


n, m = map(int, input().split())
result = solution(n, m)
print(result)
