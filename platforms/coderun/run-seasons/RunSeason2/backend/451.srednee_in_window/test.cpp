#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <limits>

using namespace std;

double max_average_subarray(int n, int k, const vector<int>& array) {
    double max_average = -numeric_limits<double>::infinity();

    for (int length = k; length <= n; ++length) {
        double current_sum = 0;

        // Считаем сумму первых 'length' элементов
        for (int i = 0; i < length; ++i) {
            current_sum += array[i];
        }
        max_average = max(max_average, current_sum / length);

        // Сдвигаем окно
        for (int i = length; i < n; ++i) {
            current_sum += array[i] - array[i - length];
            max_average = max(max_average, current_sum / length);
        }
    }
    return max_average;
}

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> array(n);

    for (int i = 0; i < n; ++i) {
        cin >> array[i];
    }

    double result = max_average_subarray(n, k, array);
    cout << fixed << setprecision(6) << result << endl;

    return 0;
}
