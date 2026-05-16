def main():
    k = int(input())
    weights = list(map(int, input().split()))
    print(solve_function(k, weights))
   
def solve_function(n, weights):
    set_weights = set()

    def generate_diffs(i, current_diff):
        if i == len(weights):
            set_weights.add(abs(current_diff))
            return 
        generate_diffs(i + 1, weights[i])
        generate_diffs(i + 1, current_diff + weights[i])
        generate_diffs(i + 1, current_diff - weights[i])
    generate_diffs(0, 0)
    
    for i in range(1, n + 1):
        if i not in set_weights:
            return "Yes" 
        return "No"

if __name__ == '__main__':
    main()
