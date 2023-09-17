#I made this to generate charts showing compairisons between 2 measurements
#There are 5 input varilables
#genders_to_show, which can be a string of 'f', 'm', or 'mf', it toggles which genders to display
#units, which is either 'cm' or 'in', it is used for unit conversions
#input_x and input_y, which are inputs for the x and y coordinates that will be graphed 
#measurement_x and measurement_y, which are the measurements being graphed
def grapher(genders_to_show, units, input_x, input_y, measurement_x, measurement_y):
    import csv
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import scipy.stats as st
    from scipy.stats import linregress
    import ansur_functions as funcs

    #finds the csv value for each display title
    measurement_x1 = measurement_x
    measurement_y1 = measurement_y
    measurement1 = funcs.linker1(measurement_x.lower())             
    measurement2 = funcs.linker1(measurement_y.lower())                    


    #generates a dictionary in the format {gender, measurement 1, measurement 2}, then turns it into a pandas dataframe
    #also has the option to do one or both genders
    dataf = funcs.ratio_gen2(measurement1, measurement2, "ansur1_female.csv")
    datam = funcs.ratio_gen2(measurement1, measurement2, "ansur1_male.csv")

    #unit conversions, this is some weird ass mf code


    #adds female data to the list if 'f' is in the gender list 
    data = {'gender' : [], measurement1: []}
    if 'f' in genders_to_show:
        data['gender'] += dataf['gender']
        data[measurement1] += dataf[measurement1]

    #adds male data to the list if 'm' is in the gender list 
    if 'm' in genders_to_show:
        data['gender'] += datam['gender']
        data[measurement1] += datam[measurement1]

        
    #turns data dict into a datafram to be used in the graphing
    df = pd.DataFrame(data=data)

    sns.set(rc={
    'axes.facecolor':'#1e1e1e',
    'figure.facecolor':'#1e1e1e',

    'text.color': '#d4d4d4',
    'xtick.color': '#d4d4d4',
    'ytick.color': '#d4d4d4',
    'ytick.labelleft': 'false',
    'grid.color': '#d4d4d4',

    'grid.linewidth': '0.1',

    'font.family': 'monospace',
    'font.family' : ['courier new'],

    },)
    colormap = {"f": "#FADADD80", "m": "#ADD8E680", }

    fig, ax = plt.subplots()

    sns.histplot(
    df,
    x= measurement1,
    hue = 'gender',
    palette={"f": "#FADADD80", "m": "#ADD8E680", },
    element="step",

    #kde = True,
    #rug= True
    )


    sns.despine(top=True, right=True, left=True, bottom=False)
    a = list(plt.ylim())
    print(a)

    try:
        x1, y1 = [(input_x/input_y), (input_x/input_y)], [0, 1000]
        plt.plot(x1, y1, color = '#cc0000')
    except:
        x1, y1 = [1, 1], [0, 1000]
    plt.ylim(0, a[1])
    plt.xlabel(str(measurement_x1 + '/' + measurement_y1),
    fontfamily= 'monospace',
    color= '#d4d4d4',
    fontweight= 100)
    plt.show()

    fig.set_figheight(6) 
    fig.set_figwidth(10) 

    return fig

