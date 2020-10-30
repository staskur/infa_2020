# http://cs.mipt.ru/python/lessons/lab1.html
# упр 2 построение графиков

import numpy as np
import matplotlib.pyplot as plt
# задаем диапазон точек графика по абсциссе
x = np.arange(-10, 10.01, 0.01)
# задаем размер окна графика
plt.figure('окно с графиками' , figsize=(10, 5))
# рисуем виртуально график и добавляем на него элементы
plt.plot(x, -x,label=r'$f_3(x)=-x$')
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

# показываем получившийся график
plt.show()
