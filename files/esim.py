def grapher (ester, dates, doses, title):
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl



    #function (gun to my head i could not tell you what this does)
    def total(p, q, a, b, c, d, t_values):
        result = np.zeros(len(t_values))
        for i in range(len(p)):
            for t in t_values:
                if p[i] < t < p[i] + 300:
                    term = (q[i] * d / 5) * a * b * (
                        (np.exp((-t + p[i]) * a) / ((a - b) * (a - c))) +
                        (np.exp((-t + p[i]) * c) / ((a - c) * (b - c))) +
                        (np.exp((-t + p[i]) * b) * (c - a) / ((a - b) * (a - c) * (b - c)))
                    )
                    result[t_values == t] += term
        return result

    #returns k and d values for the ester
    match ester:
        case "een":
            values_list = [333.874181, 0.42412968, 0.43452980, 0.15291485]
        case "ev":
            values_list = [2596.05956, 2.38229125, 0.23345814, 1.37642769]
        case "ec": 
            values_list = [1920.89671, 0.10321089, 0.89854779, 0.89359759]
        case "eu":
            values_list = [65.9493374, 0.29634323, 4799337.57, 0.03141554]


    #ignore this its just for formatting
    k1 = values_list[1]
    k2 = values_list[2]  
    k3 = values_list[3]  
    d_value = values_list[0]  

    t_values = np.linspace(0, 200, 1000)
    y_values = total(dates, doses, k1, k2, k3, d_value, t_values)

    #aesthetics
    mpl.rcParams['axes.facecolor'] = '#1e1e1e'
    mpl.rcParams['figure.facecolor'] ='#1e1e1e'
    mpl.rcParams['text.color'] = '#d4d4d4'

    mpl.rcParams['xtick.color'] = '#1e1e1e'
    mpl.rcParams['xtick.labelcolor'] = '#d4d4d4'

    mpl.rcParams['ytick.color'] = '#1e1e1e'
    mpl.rcParams['ytick.labelcolor'] = '#d4d4d4'

    mpl.rcParams['grid.color'] = '#d4d4d4'

    mpl.rcParams['grid.linewidth'] = '0.1'

    mpl.rcParams['axes.spines.left'] = 'false'
    mpl.rcParams['axes.spines.right']= 'false'
    mpl.rcParams['axes.spines.top']= 'false'
    mpl.rcParams['axes.spines.bottom']= 'false'

    mpl.rcParams['font.family']= 'monospace'
    mpl.rcParams['font.weight']= '150'


    #plot stuff
    fig, ax = plt.subplots()
    ax.xaxis.label.set_color('#d4d4d4')
    ax.yaxis.label.set_color('#d4d4d4')

    plt.plot(t_values, y_values, color= '#FADADD')

    plt.fill_between(t_values, y_values, alpha = 0.1, color= "#FADADD", linewidth= 0)

    plt.title(title)
    plt.xlabel('Days')
    plt.ylabel('Estradiol level (pg/mL)')
    plt.grid(True)
    plt.xlim(-1, dates[(len(dates)-1)]+14)
    plt.show()
    return fig
