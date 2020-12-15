# http://cs.mipt.ru/python/lessons/lab1.html
# упр 2 построение графиков

import numpy as np
import matplotlib.pyplot as plt
# задаем диапазон точек графика по абсциссе
x = np.arange(-10, 10.01, 0.01)
# задаем размер окна графика
plt.figure('окно с двумя областями графиков' , figsize=(12, 5))
# разбиваем на области для графиков
sp = plt.subplot(1,2,1)
# рисуем виртуально график и добавляем на него элементы
plt.plot(x,np.sin(x),label=r'$f_1(x)=\sin(x)$')
plt.plot(x,np.cos(x),label=r'$f_2(x)=\cos(x)$')
# выводим сетку
plt.grid('Yes')
# надписи осей
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
# заголовок графика
plt.title(r'графики функций')
plt.legend(loc='best', fontsize=12)

# выделяем вторую область
sp = plt.subplot(1,2,2)
plt.plot(x, -x,label=r'$f_3(x)=-x$')
# заголовок графика
plt.title(r'график одной функции')
plt.legend(loc='best', fontsize=10)
# переносим левую и нижнюю границы графика с осями и цифрами в центр, то есть делаем центральные оси
sp.spines['left'].set_position('center')
sp.spines['bottom'].set_position('center')

# показываем получившееся окно с областями и графиками
plt.show()
