import numpy as np
#from scipy import stats
import time

def read_sample(file_path):
    sample = np.loadtxt(file_path)
    return sample

# Вычисление доверительного интервала с помощью метода бутстрепа
def bootstrap_confidence_interval(data, alpha, n_bootstrap=10000):
    n = len(data)
    bootstrap_samples = np.random.choice(data, size=(n_bootstrap, n), replace=True)
    sample_statistics = np.percentile(bootstrap_samples, [100 * alpha / 2, 100 * (1 - alpha / 2)], axis=1)
    lower_bound = np.percentile(sample_statistics[0], 100 * alpha / 2)
    upper_bound = np.percentile(sample_statistics[1], 100 * (1 - alpha / 2))
    return lower_bound, upper_bound

# Функция для вычисления False Positive Rate (FPR)
def compute_fpr(data, interval):
    false_positive_rate = np.mean((data < interval[0]) | (data > interval[1]))
    return false_positive_rate

#90 квантиль
res_file_path_90 = {f"ResData/ResDataNinety/Bootstrap/ResDataNormal.txt", f"ResData/ResDataNinety/Bootstrap/ResDataExponential.txt",f"ResData/ResDataNinety/Bootstrap/ResDataUniform.txt"}
res_file_path_90 = list (res_file_path_90)

#99 квантиль 
res_file_path_99 = {f"ResData/ResDataNinetyNine/Bootstrap/ResDataNormal.txt",f"ResData/ResDataNinetyNine/Bootstrap/ResDataExponential.txt", f"ResData/ResDataNinetyNine/Bootstrap/ResDataUniform.txt"}
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
                # Вычисление доверительного интервала для 90-го квантиля
                alpha_90 = 0.1
                lower_bound_90, upper_bound_90 = bootstrap_confidence_interval(data, alpha_90)

                end90_time = time.time()

                # Вычисление доверительного интервала для 99-го квантиля
                alpha_99 = 0.01
                lower_bound_99, upper_bound_99 = bootstrap_confidence_interval(data, alpha_99)

                end99_time = time.time()
                time_90 = end90_time - start_time
                time_99 = end99_time - end90_time
                
                # Вызов функции для вычисления FPR
                fpr_90 = compute_fpr(data, (lower_bound_90, upper_bound_90))
                fpr_99 = compute_fpr(data, (lower_bound_99, upper_bound_99))
                
                # print("Доверительный интервал для 90-го квантиля:", (lower_bound_90, upper_bound_90))
                #print("Доверительный интервал для 99-го квантиля:", (lower_bound_99, upper_bound_99))
                    
                #Создание  DataSet-а:
                res = (i,' ',lower_bound_90, ' ', upper_bound_90,' ',time_90, ' ', fpr_90,'\n')
                res2 = (i,' ',lower_bound_99,' ', upper_bound_99,' ',time_99,' ',fpr_99,'\n' )

                # Запись в файл 90:
                for value in res:
                    file.write(f"{value}")

                # Запись в файл 99:
                for value2 in res2:
                    file2.write(f"{value2}")