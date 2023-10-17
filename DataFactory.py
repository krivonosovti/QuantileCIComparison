import numpy as np
import os

# Создание директории для сохранения файлов
save_path = "Data/DataUniform2"

# Создание директории для сохранения файлов
if not os.path.exists(save_path):
    os.makedirs(save_path)

num_samples = 150
lambd = 1
# Генерация и сохранение выборок
for i in range(num_samples):

    # Генерация случайной выборки
    #sample = np.random.normal(loc=0, scale=1, size=1000)  # Пример: нормальное распределение
    #sample = np.random.uniform(size=1000)  # Пример: равномерное распределение
    sample = np.random.exponential(scale=1/lambd, size=1000)  # Пример: экспоненциальное распределение
    lambd = lambd / 1.4
    # Создание пути и имени файла
    file_name = f"sampleExponential_{i+1}.txt"
    file_path = os.path.join(save_path, file_name)

    # Сохранение выборки в файл
    with open(file_path, "w") as file:
        for value in sample:
            file.write(f"{value}\n")