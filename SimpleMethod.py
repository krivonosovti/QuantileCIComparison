import numpy as np
import time;

def read_sample(file_path):
    sample = np.loadtxt(file_path)
    return sample

def calculate_confidence_interval(data, confidence_level):
    # Сортировка выборки
    sorted_data = np.sort(data)

    # Вычисление индексов для квантилей
    lower_index = int((1 - confidence_level) / 2 * len(sorted_data))
    upper_index = int((1 + confidence_level) / 2 * len(sorted_data))

    # Получение соответствующих квантилей
    lower_quantile = sorted_data[lower_index]
    upper_quantile = sorted_data[upper_index]

    return lower_quantile, upper_quantile

# Функция для вычисления False Positive Rate (FPR)
def compute_fpr(data, interval):
    false_positive_rate = np.mean((data < interval[0]) | (data > interval[1]))
    return false_positive_rate


#90 квантиль
res_file_path_90 = {f"ResData/ResDataNinety/Simple/ResDataNormal.txt", f"ResData/ResDataNinety/Simple/ResDataExponential.txt",f"ResData/ResDataNinety/Simple/ResDataUniform.txt"}
res_file_path_90 = list (res_file_path_90)

#99 квантиль 
res_file_path_99 = {f"ResData/ResDataNinetyNine/Simple/ResDataNormal.txt",f"ResData/ResDataNinetyNine/Simple/ResDataExponential.txt", f"ResData/ResDataNinetyNine/Simple/ResDataUniform.txt"}
res_file_path_99 = list (res_file_path_99)
sourse_file_path ={f"Data/DataNormal/sampleNormal_", f"Data/DataExponential/sampleExponential_", f"Data/DataUniform/sampleUniform_"}
sourse_file_path = list (sourse_file_path)
for j in range (0,3):
    with open(res_file_path_90[j], "w") as file:
        with open(res_file_path_99[j], "w") as file2:
            
            for i in range(1,151):
                
                file_path = sourse_file_path[j] + f"{i}.txt"

                sample = read_sample(file_path)
                start_time = time.time()
                # Расчет доверительного интервала для 90% квантилей
                lower_quantile_90, upper_quantile_90 = calculate_confidence_interval(sample, 0.9)
                end90_time = time.time()
                # Расчет доверительного интервала для 99% квантилей
                lower_quantile_99, upper_quantile_99 = calculate_confidence_interval(sample, 0.99)
                end99_time = time.time()
                time_90 = end90_time - start_time
                time_99 = end99_time - end90_time

                # # Вывод результатов
                # print("sample_",i)
                #print("Доверительный интервал для 90% квантилей:", (lower_quantile_90, upper_quantile_90))
                # print("Доверительный интервал для 99% квантилей:", (lower_quantile_99, upper_quantile_99))
                # results = np.insert(results,[i, lower_quantile_90, upper_quantile_90, round(time_90,4), lower_quantile_99, upper_quantile_99,round(time_99,4)])
                # print(results)

                # Созджание примера строки
                #res = ("sample_",i, " 90-доверительный интервал [",lower_quantile_90," ; " , upper_quantile_90, "] Время поиска 90 интервала: ", format(time_90, ',')," 99-доверительный интервал [", lower_quantile_99," ; ", upper_quantile_99, "] Время поиска 99 доверительного интервала: ", format(time_99,','),'\n')
                
            # Вызов функции для вычисления FPR
                fpr_90 = compute_fpr(sample, (lower_quantile_90, upper_quantile_90))
                fpr_99 = compute_fpr(sample, (lower_quantile_99, upper_quantile_99))

                #Создание  DataSet-а:
                res = (i,' ',lower_quantile_90, ' ', upper_quantile_90,' ',time_90, ' ', fpr_90, '\n')
                res2 = (i,' ',lower_quantile_99, ' ', upper_quantile_99,' ',time_99, ' ', fpr_99, '\n')

                # Запись в файл 90:
                for value in res:
                    file.write(f"{value}")

                # Запись в файл 99:
                for value2 in res2:
                    file2.write(f"{value2}")