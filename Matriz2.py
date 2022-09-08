import numpy as np
import matplotlib.pyplot as plt

def calcular_r():
    A = np.array([
    [1,	9.259130536,	2.901421594,	-0.162518929]
    [1,	9.630365631,	2.821378886,	-0.040821995]
    [1,	9.954655839,	3.04927304,	     0.076961041]
    [1,	10.25976242,	2.163323026,	 0.165514438]
    ])

    y_medido=np.array(
    [[4.579339426],
    [4.866764924],
    [5.033309611],
    [5.179815322]
    ])

    Eo = np.array([
    [0.005],
    [0.005],
    [0.005],
    [0.005],
    [0.005],
    [0.005],
    [0.005],
    [0.005],
    [0.01],
    [0.01],
    [0.01],
    [0.01],
    [0.01],
    [0.01],
    [0.01],
    [0.01],
    ])



    Aprima = np.transpose(A)
    A_por_Aprima=np.dot(Aprima, A)
    A_por_Aprima_inversa=np.linalg.inv(A_por_Aprima)
    A_por_Aprima_inversa_por_APrima=np.dot(A_por_Aprima_inversa, Aprima)
    coeficientes=np.dot(A_por_Aprima_inversa_por_APrima, y_medido)
    #print(f'coeficientes:', coeficientes)
    #print("\n")

    ycalculado = np.dot(A, coeficientes)
    print(f'ycalculado:', "\n", ycalculado)
    print("\n")


    rcalculado = np.divide(Eo, ycalculado)
    print(f'r calculado:', '\n', rcalculado)
    k2 = 1/coeficientes[0]
    print("\n", f'k2 = {k2}')
    km = k2*coeficientes[1]
    print(f'km = {km}')

def grafica():
    S2 = [1, 2, 5, 7.5, 10, 15, 20, 30]
    r2 = [0.108, 0.196,0.383, 0.488, 0.56, 0.665, 0.733, 0.815]

    S1=[1, 2, 5, 7.5, 10, 15, 20, 30]
    r1=[0.055, 0.099, 0.193, 0.244, 0.28, 0.333, 0.365, 0.407]
    fig, ax = plt.subplots()
    ax.plot(S1, r1, label= "S1", color="b")
    ax.plot(S2, r2, label= "S2", color="m")

    plt.show()


if __name__=='__main__':
    calcular_r()
    grafica()
