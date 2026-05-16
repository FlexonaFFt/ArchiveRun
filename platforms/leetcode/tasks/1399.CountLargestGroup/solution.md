# Solution Explanation

## Intuition

The task is to group numbers from 1 to n by the sum of their digits, then find how many groups have the largest size. The natural approach is to compute the digit sum for each number, count how many numbers fall into each group (based on digit sum), and finally identify the largest group(s).

## Approach

1. **Calculate Digit Sum:**  
   For each number from 1 to n, calculate the sum of its digits. For example, the digit sum of 123 is 1 + 2 + 3 = 6.

2. **Group Numbers by Digit Sum:**  
   Use a dictionary (hash map) to keep track of how many numbers belong to each digit sum group.

3. **Find the Largest Group(s):**  
   After grouping, find the maximum group size, then count how many groups have this size.

## Complexity

- **Time Complexity:**  
  O(n * D), where D is the number of digits in n. Each digit sum computation takes O(D) time.

- **Space Complexity:**  
  O(n) in the worst case, but usually much less, since the number of possible digit sums is limited.

## Code

---

## Python

```python
class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sum(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10 
                n //= 10
            return s 
        
        g = {}
        for k in range(1, n + 1):
            a = digit_sum(k)
            if a not in g:
                g[a] = 1
            else:
                g[a] += 1
        
        m = max(g.values())
        return sum(1 for v in g.values() if v == m)
```

---

## JavaScript

```javascript
function countLargestGroup(n) {
    function digitSum(num) {
        let sum = 0;
        while (num > 0) {
            sum += num % 10;
            num = Math.floor(num / 10);
        }
        return sum;
    }

    const groups = {};
    for (let k = 1; k <= n; k++) {
        const sum = digitSum(k);
        groups[sum] = (groups[sum] || 0) + 1;
    }

    const maxSize = Math.max(...Object.values(groups));
    return Object.values(groups).filter(v => v === maxSize).length;
}
```

---

## Java

```java
import java.util.HashMap;

class Solution {
    public int countLargestGroup(int n) {
        HashMap<Integer, Integer> groups = new HashMap<>();
        for (int k = 1; k <= n; k++) {
            int sum = digitSum(k);
            groups.put(sum, groups.getOrDefault(sum, 0) + 1);
        }
        int maxSize = 0;
        for (int size : groups.values()) {
            if (size > maxSize) maxSize = size;
        }
        int count = 0;
        for (int size : groups.values()) {
            if (size == maxSize) count++;
        }
        return count;
    }

    private int digitSum(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}
```
