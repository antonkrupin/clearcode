1 (1)
//функция считает определенный тип выражения
// в зависимости от переданных параметров
const calculateExpression = (firstNumber, secondNumber, expressionSign) => {
  switch (expressionSign) {
    case '+': return firstNumber + secondNumber;
    case '-': return firstNumber - secondNumber;
    case '*': return firstNumber * secondNumber;
    default:
      throw new Error('Can`t calculate expression');
  }
};

2 (1)
// нахождение наибольшего общего делителя
const findGCD = (number1, number2) => {
  if (number2 === 0) {
    return Math.abs(number1);
  }
  return findGCD(number2, number1 % number2);
};

3 (1)
// определение является ли число простым
const isPrime = (number) => {
  if (number === 1) {
    return true;
  }
  for (let i = 2; i < number; i += 1) {
    if (number % i === 0) {
      return false;
    }
  }
  return true;
};

4 (1)
// определение четного числа
const isEven = (number) => (number % 2) === 0;

5 (1)
// генерация последовательности
const generateProgression = (progressionStep, progressionSize, firstElement = 5, hiddenIndex) => {
  const progresionArray = [];
  progresionArray.push(firstElement);
  for (let i = 0; i <= progressionSize; i += 1) {
    const progressionEl = progresionArray[i] + progressionStep;
    progresionArray.push(progressionEl);
  }
  progresionArray[hiddenIndex] = '..';
  return progresionArray.join(' ');
};
