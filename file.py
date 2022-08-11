print('Hello world')

numbers = [8,22,3,2,6,16,36,33,90,2,87,96,88]
size = len(numbers)               # len - задает длину списка
index = 0
max_number_index = 0
max = 0
#first_max = 0
while(index < size):              # запускаем цикл до тех пор пока не переберем весь список
    if (numbers[index] > max):
        max = numbers[index]      
        max_number_index = index  
    index = index + 1
index = 0
second_max = numbers[0]
if (max_number_index == 0):
    second_max = numbers[1]
while (index < size):
    if (index != max_number_index):
        if (numbers[index] > second_max):
            second_max = numbers[index]
    index = index + 1
print ('количество элементов в массиве', size)
print ('наибольшее второе число в массиве ', second_max)
print ('наибольшее число в массиве ', max)