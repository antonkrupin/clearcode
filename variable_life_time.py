1. Выделяем в отдельный метод  
 for (let i = index; i < count - 1; i++) {
    array[i] = array[i + 1];
};
2. Выделяем в отдельный метод
for (let i = count; i > index; i--) {
    array[i] = array[i - 1]
};
3. в первом курсе по Алгоритмам,
можно сделать свойства классов и методы приватными,
хотя в python это идет (если не использовать доп. библиотеки)
на уровне соглашения
def __print_all_nodes(self),
def __find(self)
4. Выделить в отдельный метод
if (array.length != 0) {
    let elem = array.pop();
}
5. Выделить в отдельный метод
while (b % a != 0) {
    a = b - a * (b / a);
}

