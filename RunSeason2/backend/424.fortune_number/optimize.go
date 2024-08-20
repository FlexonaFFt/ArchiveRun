package main

import (
	"fmt"
	"strconv"
	"strings"
)

// Функция для суммирования цифр в первой и второй половинах числа
func sumOfHalfDigits(number string) (int, int) {
	half := len(number) / 2
	firstHalf := 0
	secondHalf := 0

	for i := 0; i < half; i++ {
		digit, _ := strconv.Atoi(string(number[i]))
		firstHalf += digit
	}

	for i := half; i < len(number); i++ {
		digit, _ := strconv.Atoi(string(number[i]))
		secondHalf += digit
	}

	return firstHalf, secondHalf
}

// Функция для проверки, равны ли суммы первой и второй половин
func isSumEqual(number string) bool {
	firstHalf, secondHalf := sumOfHalfDigits(number)
	return firstHalf == secondHalf
}

// Основная функция для нахождения ближайшего числа
func findClosestNumber(inputNumber string) string {
	number := strconv.Itoa(toInt(inputNumber) + 1)
	number = padLeft(number, len(inputNumber))

	for {
		if number != strings.Repeat("0", len(inputNumber)) && isSumEqual(number) {
			return number
		}
		number = strconv.Itoa(toInt(number) + 1)
		number = padLeft(number, len(inputNumber))

		if len(number) > len(inputNumber) {
			number = strings.Repeat("0", len(inputNumber))
		}
	}
}

// Функция для преобразования строки в целое число
func toInt(s string) int {
	result, _ := strconv.Atoi(s)
	return result
}

// Функция для дополнения строки нулями слева
func padLeft(s string, length int) string {
	return fmt.Sprintf("%0*s", length, s)
}

// Главная функция
func main() {
	var inputNumber string
	fmt.Scan(&inputNumber)
	fmt.Println(findClosestNumber(inputNumber))
}
