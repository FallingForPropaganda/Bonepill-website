def grapher (injections, title):
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl


    '''
    function (basically the desmos calc but in python)
    takes the input injection list and a numpy linspace
    i barely understand how this works but it works so thats good enough for me
    '''
    def total(injections, t_values):
        result = np.zeros(len(t_values))
        for i in range(len(injections)):
            for t in t_values:
                date = injections[i][0]
                dose = injections[i][1]
                a = injections[i][2][0]
                b = injections[i][2][1]
                c = injections[i][2][2]
                d = injections[i][2][3]
                if date < t < date + 100:
                    term = (dose * d / 5) * a * b * (
                        (np.exp((-t + date) * a) / ((a - b) * (a - c))) +
                        (np.exp((-t + date) * c) / ((a - c) * (b - c))) +
                        (np.exp((-t + date) * b) * (c - a) / ((a - b) * (a - c) * (b - c)))
                    )
                    result[t_values == t] += term
        return result


    #does stuff
    t_values = np.linspace(0, 200, 1000)
    y_values = total(injections, t_values)


    #aesthetics
    plt.rcParams.update({
        'axes.facecolor': '#1e1e1e',
        'figure.facecolor':'#1e1e1e',
        'text.color': '#d4d4d4',
        'axes.titleweight': '500',

        'xtick.color': '#1e1e1e',
        'xtick.labelcolor': '#d4d4d4',
        'ytick.color': '#1e1e1e',
        'ytick.labelcolor': '#d4d4d4',

        'grid.color': '#d4d4d4',
        'grid.linewidth': '0.1',

        'axes.spines.left': 'false',
        'axes.spines.right':'false',
        'axes.spines.top':'false',
        'axes.spines.bottom':'false',

        'font.family': 'monospace'
    })


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
    plt.xlim(-1, injections[(len(injections)-1)][0]+7)
    plt.show()
    return fig
