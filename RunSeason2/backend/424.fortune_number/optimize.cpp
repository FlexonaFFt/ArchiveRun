#include <iostream>
#include <string>
#include <cctype>

std::string sum_of_half_digits(const std::string& number) {
    int half = number.length() / 2;
    int first_half = 0, second_half = 0;
    for (int i = 0; i < half; i++) {
        first_half += number[i] - '0';
    }
    for (int i = half; i < number.length(); i++) {
        second_half += number[i] - '0';
    }
    return std::to_string(first_half) + " " + std::to_string(second_half);
}

bool is_sum_equal(const std::string& number) {
    std::string halves = sum_of_half_digits(number);
    int space = halves.find(" ");
    int first_half = std::stoi(halves.substr(0, space));
    int second_half = std::stoi(halves.substr(space + 1));
    return first_half == second_half;
}

std::string find_closest_number(const std::string& input_number) {
    std::string number = std::to_string(std::stoi(input_number) + 1);
    number = std::string(input_number.length() - number.length(), '0') + number;
    while (true) {
        if (number != std::string(input_number.length(), '0') && is_sum_equal(number)) {
            return number;
        }
        number = std::to_string(std::stoi(number) + 1);
        if (number.length() > input_number.length()) {
            number = std::string(input_number.length(), '0');
        }
    }
}

int main() {
    std::string number;
    std::getline(std::cin, number);
    std::cout << find_closest_number(number) << std::endl;
    return 0;
}
