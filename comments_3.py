1(13)
const isEven = (number) => (number % 2) === 0;

//ранее был комментарий:
//функция для определения чётности числа

2(13)
const startGame = () => {
  invokeGameFunction(generateRound, gameRules);
};

//ранее был комментарий:
//функция старта игры

3(13)
const findGCD = (number1, number2) => {
  if (number2 === 0) {
    return Math.abs(number1);
  }
  return findGCD(number2, number1 % number2);
};

//ранее был комментарий:
//функция для наохждения наибольшего общего делителя

4(13)
const isPrime = (number) => {
  if (number < 2) {
    return false;
  }
  for (let i = 2; i < number; i += 1) {
    if (number % i === 0) {
      return false;
    }
  }
  return true;
};

//ранее был комментарий
// функция для определения является ли число простым
