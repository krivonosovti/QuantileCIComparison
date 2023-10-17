import numpy as np
import time

def read_sample(file_path):
    sample = np.loadtxt(file_path)
    return sample

def delta_method_confidence_interval(data, percentile):     #бред обычный наивный подход, не дельтам метод
    sorted_data = np.sort(data)
    n = len(sorted_data)
    index = int((n - 1) * percentile)
    lower_bound = sorted_data[index]
    upper_bound = sorted_data[index + 1] if index < n - 1 else sorted_data[index]
    return lower_bound, upper_bound

# Функция для вычисления False Positive Rate (FPR)
def compute_fpr(data, interval):
    false_positive_rate = np.mean((data < interval[0]) | (data > interval[1]))
    return false_positive_rate

#90 квантиль
res_file_path_90 = {f"ResData/ResDataNinety/Delta/ResDataNormal.txt", f"ResData/ResDataNinety/Delta/ResDataExponential.txt",f"ResData/ResDataNinety/Delta/ResDataUniform.txt"}
res_file_path_90 = list (res_file_path_90)

#99 квантиль 
res_file_path_99 = {f"ResData/ResDataNinetyNine/Delta/ResDataNormal.txt",f"ResData/ResDataNinetyNine/Delta/ResDataExponential.txt", f"ResData/ResDataNinetyNine/Delta/ResDataUniform.txt"}
res_file_path_99 = list (res_file_path_99)
sourse_file_path ={f"Data/DataNormal/sampleNormal_", f"Data/DataExponential/sampleExponential_", f"Data/DataUniform/sampleUniform_"}
sourse_file_path = list (sourse_file_path)
for j in range (0,3):
    with open(res_file_path_90[j], "w") as file:
        with open(res_file_path_99[j], "w") as file2:
            for i in range(1,151):
                   
                file_path = sourse_file_path[j] + f"{i}.txt"

                data = read_sample(file_path)
                start_time = time.time()

                percentile_90 = 0.9
                percentile_99 = 0.99

                lower_bound_90, upper_bound_90 = delta_method_confidence_interval(data, percentile_90)
                end90_time = time.time()
                lower_bound_99, upper_bound_99 = delta_method_confidence_interval(data, percentile_99)

                # print(f"Доверительный интервал для {percentile_90*100}% квантиля: ({lower_bound_90}, {upper_bound_90})")
                # print(f"Доверительный интервал для {percentile_99*100}% квантиля: ({lower_bound_99}, {upper_bound_99})")

                end99_time = time.time()
                time_90 = end90_time - start_time
                time_99 = end99_time - end90_time
                
                # Вызов функции для вычисления FPR
                fpr_90 = compute_fpr(data, (lower_bound_90, upper_bound_90))
                fpr_99 = compute_fpr(data, (lower_bound_99, upper_bound_99))

                #Создание  DataSet-а:
                res = (i,' ',lower_bound_90, ' ', upper_bound_90,' ',time_90, ' ',fpr_90, '\n')
                res2 = (i,' ',lower_bound_99,' ', upper_bound_99,' ',time_99,' ',fpr_99, '\n' )

                # Запись в файл 90:
                for value in res:
                    file.write(f"{value}")

                # Запись в файл 99:
                for value2 in res2:
                    file2.write(f"{value2}")
