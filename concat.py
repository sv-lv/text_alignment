'''Напишите алгоритм выравнивания текста.  Задана последовательность
слов и целое число k длина строки, верните список строк,
которые представляют каждую строку, полностью выровненную.
В частности, в каждой строке должно быть как можно больше слов.
Между каждым словом должен быть хотя бы один пробел.
При необходимости добавьте лишние пробелы, чтобы каждая строка имела длину равную k.
Пространства следует распределять как можно более равномерно, а дополнительные места,
если таковые имеются, распределять, начиная с левой стороны.

Если вы можете уместить только одно слово в строке, вы должны заполнить правую часть пробелами.
Гарантируется, что каждое слово не длиннее k. Например, учитывая список слов
the quick brown fox jumps over the lazy dog и k = 16,
вы должны вернуть следующее: [“the  quick brown”, “fox  jumps  over”, “the   lazy   dog”]'''
'''the quick brown fox jumps over the lazy dog'''
from text_alignment.input_k import input_k
from text_alignment.input_str import input_str
from text_alignment.first import first

def concat():
    k = input_k()
    string = input_str()
    new_string = []
    new_list = []
    len_result = 0
    x = 0
    result = [] #итоговый список с выровненными строками
    for i in range(1, 1 + len(string)):
        '''условие для первой итерации (строчки)'''
        if i == k:
            new_list_changed = first()
            result.append(new_list_changed)
            len_result = len(new_list_changed)

        lr = len_result + x
        '''условие для следующих после первой итераций (строчек)'''
        if i == lr + k:
            len_result += x
            new_list = string[len_result:len_result + k]
            if string[len_result + k] != ' ' and string[len_result + k + 1] != ' ':
                new_list_changed = new_list[:new_list.rfind(' ')]
                result.append(new_list_changed)
                x = len(new_list_changed)

            if string[len_result + k + 1] == ' ' or string[len_result + k] == ' ':
                new_list_changed = new_list[:len_result + k]
                result.append(new_list_changed)
                x = len(new_list_changed)

        if i == len(string):
            new_list = string[lr:len(string)]
            result.append(new_list)

    return result




