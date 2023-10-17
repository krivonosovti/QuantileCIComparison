import matplotlib.pyplot as plt
import numpy as np

def average_arrays(arr1, arr2, arr3):
    result = (arr1 + arr2 + arr3) / 3
    return result

def CreateData(file_path):
    samples = []
    execution_times = []
    fprs = []
    with open(file_path, "r") as file:
        for line in file:
            data = line.split()
            sample_name = data[0]
            execution_time = float(data[3])
            fpr = data[4]
            samples.append(sample_name)
            execution_times.append(execution_time)
            fprs.append(fpr)
    return samples, execution_times, fprs

filetype ={"Bootstrap","Delta","Simple"}
filetype = list(filetype)
quantil ={"ResDataNinety/","ResDataNinetyNine/"}
quantil = list(quantil)
k = 1
l = int(input("quanti "))

if (l == 90):
    l = 0
else:
    l = 1

for j in range(0,3):
    # Чтение данных из файлов
    file_pathExp = "ResData/"+quantil[l]+filetype[j]+"/ResDataExponential.txt"
    file_pathN = "ResData/"+quantil[l]+filetype[j]+"/ResDataNormal.txt"
    file_pathUni = "ResData/"+quantil[l]+filetype[j]+"/ResDataUniform.txt"

    samples_exp, execution_times_exp, fpr_exp = CreateData(file_pathExp)
    samples_n, execution_times_n, fpr_n = CreateData(file_pathN)
    samples_uni, execution_times_uni, fpr_uni = CreateData(file_pathUni)

    # Создание графика времени выполнения задания
    x = np.arange(len(samples_exp))  # Номера сэмплов
    y1 = np.array(execution_times_exp)
    y2 = np.array(execution_times_n)
    y3 = np.array(execution_times_uni)

    mean_execution_times_exp = np.mean(execution_times_exp)
    mean_execution_times_n = np.mean(execution_times_n)
    mean_execution_times_uni = np.mean(execution_times_uni)

    mean_execution_time= average_arrays(mean_execution_times_n,mean_execution_times_exp,mean_execution_times_uni)
    if(j == 0):
        mean_execution_time_bootstrap = mean_execution_time 
    elif (j == 1): 
        mean_execution_time_Delta  = mean_execution_time
    elif (j == 2): 
        mean_execution_time_Simple  = mean_execution_time

    plt.figure(k)
    plt.plot(x, y1, color='r', label='Время выполнения exp')
    plt.plot(x, y2, color='g', label='Время выполнения normal')
    plt.plot(x, y3, color='b', label='Время выполнения uni')

    plt.axhline(y=mean_execution_times_exp, color='r', linestyle='--', label='Среднее время exp')
    plt.axhline(y=mean_execution_times_n, color='g', linestyle='--', label='Среднее время n')
    plt.axhline(y=mean_execution_times_uni, color='b', linestyle='--', label='Среднее время uni')
    plt.axhline(y=mean_execution_time, color='k', linestyle='--', label='Среднее время '+filetype[j])

    plt.xlabel("Номер сэмпла")
    plt.ylabel("Время выполнения (сек)")
    plt.title("Отношение номера выборки к скорости выполнения метода " + filetype[j])
    plt.legend()

    # Создание графика FPR
    fpr_exp = np.array(fpr_exp, dtype=float)
    fpr_n = np.array(fpr_n, dtype=float)
    fpr_uni = np.array(fpr_uni, dtype=float)

    mean_fpr= average_arrays(fpr_uni,fpr_exp,fpr_n)

    if(j == 0):
        mean_fpr_bootstrap = mean_fpr
    elif (j == 1): 
        mean_fpr_delta =  mean_fpr
    elif (j == 2): 
        mean_fpr_simple = mean_fpr

    k+=1
    plt.figure(k)
    plt.plot(x, fpr_exp, color='r', label='FPR exp')
    plt.plot(x, fpr_n, color='g', label='FPR normal')
    plt.plot(x, fpr_uni, color='b', label='FPR uni')
    plt.plot(x, mean_fpr, color='k', linestyle = '--', label='mean FPR ' + filetype[j])
    if (filetype[j] == "Bootstrep"):
        plt.ylim(0.075,0.085)


    plt.xlabel("Номер сэмпла")
    plt.ylabel("FPR")
    plt.title("Отношение номера выборки к FPR "+ filetype[j])
    plt.legend()
    k+=1


plt.figure(k)
plt.plot(x, mean_fpr_bootstrap, color='r', label='FPR Bootstrep')
plt.plot(x, mean_fpr_delta, color='g', label='FPR Delta')
plt.plot(x, mean_fpr_simple, color='b', label='FPR Simple')


plt.xlabel("Номер сэмпла")
plt.ylabel("FPR")
plt.title("Отношение FPR разных методов")
plt.legend()

# Отображение графиков
plt.show()