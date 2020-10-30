# http://cs.mipt.ru/python/lessons/lab1.html
# упр 2 построение графиков

import numpy as np
import matplotlib.pyplot as plt
# задаем диапазон точек графика по абсциссе
x = np.arange(-10, 10.01, 0.01)
# рисуем виртуально график и добавляем на него элементы
plt.plot(x, np.log(abs(x))/10)
plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))
# выводим сетку
plt.grid('Yes')
# надписи осей
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
# заголовок графика
plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=\log(abs(x))/10$')

# показываем получившийся график
plt.show()
