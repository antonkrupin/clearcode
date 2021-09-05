//код на js
const generateExpression = () => {
  const expressionsSignArray = ['+', '-', '*'];
  const expressionNumber = getRandom(expressionsSignArray.length);
  const expression = {
    firstNumber: getRandom(100),
    secondNumber: getRandom(100),
    sign: expressionsSignArray[expressionNumber],
    expression() {
      return `${expression.firstNumber} ${expression.sign} ${expression.secondNumber}`;
    },
  };
  return expression;
};

//изначально expression была представленна массивом,
//который возвращался функцией
//но при обращении к элементам массива
//легко было ошибиться, с объектом это все более наглядно
