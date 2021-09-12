1. Код на JS, определение 
является ли число простым
const isPrime = (number) => {
  if (number === 1) {
    return 'yes';
  }
  for (let i = 2; i < number; i += 1) {
    if (number % i === 0) {
      // если число не простое возвращает 'no'
      return 'no';
    }
  }
  // если число просто возвращает 'yes'
  return 'yes';
};

// заменил 'yes', 'no' на true, false
// комментарии стали не нужны
const isPrime = (number) => {
  if (number === 1) {
    return true;
  }
  for (let i = 2; i < number; i += 1) {
    if (number % i === 0) {
      return false;
    }
  }
  return false;
};
