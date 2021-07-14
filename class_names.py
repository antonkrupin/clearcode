//к сожалению в своем коде я не пользовался классами в той мере
//в которой смогу применить занния из данного занятия
//сам код проекта был не очень большим
//и использование классов ограничивалось одним классом


class Rectangle:
  def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def rectangle_area(self):
        return self.width * self.height
      
class Triangle:
  def __init__(self, base_line, height):
        self.base_line = base_line
        self.height = height
        
    def triangle_area(self):
        return 0,5 * self.base_line * self.height
      
//для названия классов использовал существительное
//которое достаточно понятно описывает, что
//содержится в классе
//в обоих классах есть методы, которые похожи друг на друга
//rectangle_area и triangle_area - возвращают площадь фигуры
//чтобы не запутаться и не использовать какие-то синонимы
//для разных методов
//в качестве идентификатора в начале каждого метода
//используется наименование класса, для которого он используется
