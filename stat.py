import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt


if __name__=='__main__':
    
    SMALL_SIZE = 10
    MEDIUM_SIZE = 14
    BIGGER_SIZE = 18
    
    plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    
    
    x = np.linspace(0,1,100)
    betas = [(1,1),(3,1),(10,10), (1,2)]
    fig, ax = plt.subplots(1,len(betas),sharey=True)
    
    for i,(a,b) in enumerate(betas):
        ax[i].plot(x, stats.beta(a,b).pdf(x))
        
    fig.text(0.5,0.05,'X')
    fig.text(0.05,0.5,'p(X)',rotation=90)
    # stat = stats.beta