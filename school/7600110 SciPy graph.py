import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import curve_fit


def sheets():
    xflista = []
    yflista = []
    while True:
        print("")
        print("No Google sheets, selecione toda a coluna com valores e copie")
        print("No programa, apenas cole, notação cientifica funciona")
        ylista = input("y = ")
        print("")
        xlista = input("x = ")
        y = ylista.split()
        x = xlista.split()
        #criando a lista com floats
        try:
            for p in y:
                yflista.append(float(p.replace(',','.').rstrip()))
            for o in x:
                xflista.append(float(o.replace(',','.').rstrip()))
            break
        except:
            x = []
            y = []
            print(yflista,xflista)
            print("Os valores foram corretamente digitados?")
            continue
    return xflista, yflista

def grafico():
    xflista, yflista = sheets()
    plt.figure(figsize = (8,6))
    plt.errorbar(xflista,yflista,c = "b",fmt='o')
    plt.plot(xflista,yflista,'-r')
    plt.show()

def graficodet():   
    xflista, yflista = sheets()
    titulo = input("Digite o titulo do grafico: ")
    eixoy = input("Legenda do Eixo y: ")
    eixox = input("Legenda do Eixo x: ")
    plt.figure(figsize = (10,8))
    plt.errorbar(xflista,yflista,c = "b",fmt='o')
    plt.plot(xflista,yflista,'-r')
    plt.title(titulo)
    plt.xlabel(eixox)
    plt.ylabel(eixoy)
    plt.grid()
    plt.show()

def graficodaora():
    xflista, yflista = sheets()
    for i in range(0, len(yflista)):
        funci[float(yflista[i])*100] = xflista[i]
        i += 1

    yflista2 = yflista
    xflista = np.array(xflista, dtype = float)
    yflista = np.array(yflista, dtype = float)
    def func(x, a, b, c):
        return a / ((b**2 -(x*2*np.pi)**2)**2 + 4*(c*x*2*np.pi)**2)**0.5
    popt, pcov = curve_fit(func, xflista, yflista)

    yflista = yflista * 100
    yflista2 = list(yflista)
    plt.figure(figsize = (10,8))
    
    plt.plot(xflista,yflista,'ob', label = "dados")
    plt.plot(xflista,yflista,'-r', label = "liga ponto")
    maxi = np.amax(yflista)
    mini = np.amin(yflista)
    med = (maxi)/2
    
    plt.vlines(x = funci[maxi], ymax = maxi, ymin = 0, label = "max amp", linestyles = "--", color = "purple")
    plt.title("Gráfico da Amplitude para diferentes valores de Frequência")
    plt.ylabel("Amplitude (cm)")
    plt.xlabel("Frequência ω/2π (Hz)")

    omega = popt[1] / (2*np.pi)
    mse = np.average(func(xflista, *popt)*100 - yflista)**2
    plt.plot(xflista, func(xflista, *popt)*100, 'g--',
         label='curve_fit: F/m=%5.3f, ω_0=%5.3f, γ=%5.3f' % tuple(popt))
    
    

    perto = min(yflista, key=lambda x:abs(x-med))
    yflista2.remove(perto)
    perto2 = min(yflista2, key=lambda x:abs(x-med))
    plt.annotate(s = "", xy = (funci[perto],perto), xytext = (funci[perto2],perto), arrowprops = dict(linewidth = 0.1, color = "gold"))
    plt.annotate(s = "", xytext = (funci[perto],perto), xy = (funci[perto2],perto), arrowprops = dict(linewidth = 0.1, color = "gold"))
    print(funci[perto2] - funci[perto])
    plt.plot(xflista[0],yflista[0],'white', label = 'mse = %5.5f, ω_0/2π = %5.5f' % tuple((mse,omega)))
    plt.legend()
    plt.grid()
    plt.show()
    
def graficosuper():
    xflista, yflista = sheets()
    funci = {}
    i = 0
    for i in range(0, len(yflista)):
        funci[float(yflista[i])*100] = xflista[i]
        i += 1

    yflista2 = yflista
    xflista = np.array(xflista, dtype = float)
    yflista = np.array(yflista, dtype = float)

    yflista = yflista * 100
    yflista2 = list(yflista)
    plt.figure(figsize = (10,8))

    plt.plot(xflista,yflista,'-b', label = "no ar")
    maxi = np.amax(yflista)
    mini = np.amin(yflista)
    med = (maxi - mini)/2
    
    plt.vlines(x = funci[maxi], ymax = maxi, ymin = 0, label = "max amp no ar", linestyles = "--", color = "green")    

    perto = min(yflista, key=lambda x:abs(x-med))
    yflista2.remove(perto)
    perto2 = min(yflista2, key=lambda x:abs(x-med))
    plt.annotate(s = "", xy = (funci[perto],perto), xytext = (funci[perto2],perto), arrowprops = dict(linewidth = 0.1, color = "green"))
    plt.annotate(s = "", xytext = (funci[perto],perto), xy = (funci[perto2],perto), arrowprops = dict(linewidth = 0.1, color = "green"))

 
    xflista, yflista = sheets()
    funci = {}
    i = 0
    for i in range(0, len(yflista)):
        funci[float(yflista[i])*100] = xflista[i]
        i += 1

    yflista2 = yflista
    xflista = np.array(xflista, dtype = float)
    yflista = np.array(yflista, dtype = float)

    yflista = yflista * 100
    yflista2 = list(yflista)

    plt.plot(xflista,yflista,"-r",label = "na água")
    maxi = np.amax(yflista)
    mini = np.amin(yflista)
    med = (maxi - mini)/2
    
    plt.vlines(x = funci[maxi], ymax = maxi, ymin = 0, label = "max amp na água", linestyles = "--", color = "orange")
    plt.title("Gráfico comparativo amplitude por frequência no ar/água")
    plt.ylabel("Amplitude (cm)")
    plt.xlabel("Frequência ω/2π (Hz)")

    perto = min(yflista, key=lambda x:abs(x-med))
    yflista2.remove(perto)
    perto2 = min(yflista2, key=lambda x:abs(x-med))
    plt.annotate(s = "", xy = (funci[perto],perto), xytext = (funci[perto2],perto), arrowprops = dict(linewidth = 0.1, color = "orange"))
    plt.annotate(s = "", xytext = (funci[perto],perto), xy = (funci[perto2],perto), arrowprops = dict(linewidth = 0.1, color = "orange"))

    plt.legend()
    plt.grid()
    plt.show()

