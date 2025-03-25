function findLargestNumber(numbers) {
  if (numbers.length === 0) return undefined; // или можно вернуть null

  let largest = numbers[0]; // инициализируем первым элементом

  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > largest) {
      largest = numbers[i];
    }
  }

  return largest;
}

function main() {
  const fs = require("fs");
  const input = fs.readFileSync(0, "utf8").trim();

  if (input === "") {
    // обработка пустого ввода
    console.log(""); // или можно вернуть undefined/null
    return;
  }

  const numbers = input.split(" ").map(Number);

  console.log(findLargestNumber(numbers));
}

main();
