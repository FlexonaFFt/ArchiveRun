#include <iostream>
#include <cmath>

void findSquares(int n, int* a, int* b) {
    for (*a = 0; (*a) * (*a) <= n; (*a)++) {
        int b_squared = n - (*a) * (*a);
        *b = sqrt(b_squared);
        if ((*b) * (*b) == b_squared && *a <= *b) {
            return;
        }
    }
    *a = -1; // Если решение не найдено
    *b = -1;
}

int main() {
    int n;
    std::cin >> n;

    int a, b;
    findSquares(n, &a, &b);

    if (a != -1) {
        std::cout << a << " " << b << std::endl;
    } else {
        std::cout << "NO" << std::endl;
    }

    return 0;
}
