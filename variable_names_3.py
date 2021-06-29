7.1
buttonDosentExist - is_button_found
//переменная из кода на JS
//пердназначена для определения 
//найдена ли нужная кнопка на странице
//после переименования имя стало короче 
//и более понятно


flag - is_send_results
//использовал переменную с названием
//flag, так как думал что это будет хорошо
//после изучения вашего занятия, понял
//что это очень неоднозначное название
//теперь название более конкретно передает
//что происходит, если в ней значение true/false


foundedNumber - is_number_found
//булевая переменная по которой 
//определяется найдено ли нужное число
//изначально название не передавало
//однозначное значение true или false
//из названия больше то, что в нем 
//хранится найденное число


formDosentExist - is_form_found
//переменная из кода на JS
//предназначена для определения
//найдена ли на странице форма


endOfProcessingFile - is_file_processing_complete
//переменная для фиксирования
//окончания обработки файла

7.2
def handlingFiles(fileNumber1, fileNumber2):
    sumNumbers = 0
    success = False

    filePath1 = str(fileNumber1) + '.txt'
    filePath2 = str(fileNumber2) + '.txt'
   
    if cf(filePath1) and cf(filePath2):
        f1 = open(filePath1)
        f2 = open(filePath2)

        for s in f1:
            sumNumbers += int(s.rstrip())
        f1.close()
        
        for s in f2:
            sumNumbers += int(s.rstrip())
        f2.close()
        success = True
        
        return sumNumbers, success
    else:
        return success
      
//функция для обработки записи в файл
//по результату возвращается переменная success
//она будет либо True, если все прошло успешно
//либо False

7.3
for x in range(len(lengthString)):
  if(lengthString[x] != '.' and lengthString[x] != '0'):
      formatedString = formatedString + lengthString[x]
      
//вместо x, мне кажется можно использовать string_char
//будет более понятно значение чего сраниваем и проверяем

for string_char in range(len(lengthString)):
  if(lengthString[string_char] != '.' and lengthString[string_char] != '0'):
      formatedString = formatedString + lengthString[string_char]

7.4
hover/unhover
//переменная из JS 
//для отслеживания наведения курсора
//на элемента

while(pointer <= len(string)):
  m = string[pointer:pointer+length]
  n = string[pointer:pointer+length+1]
  if(' ' in m):
      if(n[-1] == ' '):
          splitString.append(m)
          pointer = pointer + length
      if(n[-1] != ' '):
          for i in reversed(range(len(m))):
              if(m[i] == ' '):
                  splitString.append(m[:i])
                  pointer = pointer + i + 1
                  break

  if(not ' ' in m):
      splitString.append(m)
      pointer = pointer + length
      
//заменить переменные m,n на start/finish
//для более четкого понимания что в них находится

while(pointer <= len(string)):
  start = string[pointer:pointer+length]
  finish = string[pointer:pointer+length+1]
  if(' ' in start):
      if(finish[-1] == ' '):
          splitString.append(start)
          pointer = pointer + length
      if(finish[-1] != ' '):
          for i in reversed(range(len(start))):
              if(start[i] == ' '):
                  splitString.append(start[:i])
                  pointer = pointer + i + 1
                  break

  if(not ' ' in start):
      splitString.append(start)
      pointer = pointer + length


7.5

//функция из JS для рендера картинок внутри блока

rectangle_render = function(amount, rectangle, rectangleWidth, rectangleHeight) {
  let coords_from_left = 0;
  let coords_from_top = 0;
  
  //изначально переменные назывались x,y соответственно
  //в коде они терялись, было трудно их найти
  //так как взгляд проскакивал мимо них (из за очень короткого названия)
  //и сразу было не понятно что в них может храниться
}

