import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ansur_functions as funcs
import scipy.stats as st

measurement_x = 'bmi'
measurement_y = 'whr'
units = 'cm'
genders_to_show = 'f'    
input_x = 19.5
input_y = 26.75/38.75
measurement1 = measurement_x             
measurement2 = measurement_y      


def bmi_gen(dataset):
    data = {'gender' : [], 'bmi': [],'whr': []}
    with open (dataset, encoding='cp1252') as ansur:
        csvfile = csv.reader(ansur)
        measurements = next(csvfile)
        loc1 = measurements.index('WEIGHT')
        loc2 = measurements.index('STATURE')
        loc3 = measurements.index('WAIST_CIRC_NATURAL')
        loc4 = measurements.index('BUTTOCK_CIRC')

        for row in csvfile:
            if dataset == 'ansur1_female.csv':
                data['gender'].append('f')
            elif dataset == 'ansur1_male.csv':
                data['gender'].append('m')
            else:
                data['gender'].append('n')
            data['bmi'].append(((float(row[loc1]))/10)/((float(row[loc2])/1000)*(float(row[loc2])/1000)))
            if (((float(row[loc1]))/10)/((float(row[loc2])/1000)*(float(row[loc2])/1000))) < 15:
                print(((float(row[loc1]))/10))
                print(((float(row[loc2])/1000)))
                print(((float(row[loc1]))/10)/((float(row[loc2])/1000)*(float(row[loc2])/1000)))
                print()
            data['whr'].append((float(row[loc3]))/(float(row[loc4])))

    return data


dataf = bmi_gen("ansur1_female.csv")
datam = bmi_gen("ansur1_male.csv")



#unit conversions, this is some weird ass mf code



#adds female data to the list if 'f' is in the gender list 
data = {'gender' : [], measurement1: [],measurement2: []}
if 'f' in genders_to_show:
    data['gender'] += dataf['gender']
    data[measurement1] += dataf[measurement1]
    data[measurement2] += dataf[measurement2]

#adds male data to the list if 'm' is in the gender list 
if 'm' in genders_to_show:
    data['gender'] += datam['gender']
    data[measurement1] += datam[measurement1]
    data[measurement2] += datam[measurement2]
    
#turns data dict into a datafram to be used in the graphing
df = pd.DataFrame(data=data)
print(df)


#questionable coding but it works and took me like 2 minutes to write, it find the max and min x and y values
#then it adds 2.5%  of the difference to the top and bottom, it's used to lock the x and y limits for the axes
max_y = max(data[measurement2])
min_y = min(data[measurement2])
y_dif = max_y - min_y

max_y = max_y + y_dif/40
min_y = min_y - y_dif/40

max_x = max(data[measurement1])
min_x = min(data[measurement1])
x_dif = max_x - min_x

max_x = max_x + x_dif/40
min_x = min_x - x_dif/40




#gnerates info for line of best fit and band of 1 SD +- the line of best fit
#shit variable names lmao but whatever
xm, ymt, ymb, sd_m, slope_m, intercept_m = funcs.top_bottom_line_gen(
measurement1,
measurement2,
datam[measurement1],
datam[measurement2],
np.array(datam[measurement1]),
np.array(datam[measurement2])
)

xf, yft, yfb, sd_f, slope_f, intercept_f = funcs.top_bottom_line_gen(
measurement1,
measurement2,
dataf[measurement1],
dataf[measurement2],
np.array(dataf[measurement1]),
np.array(dataf[measurement2])
)

#finds how far from the female and male line of best fit you are in SDs
sd_from_m = round((input_y - (input_x * slope_m + intercept_m) )/sd_m, 2)
sd_from_f = round((input_y - (input_x * slope_f + intercept_f) )/sd_f, 2)

colormap = {"f": "#FADADD80", "m": "#ADD8E680", }
#colormap2 = {"f": "#fce9ea", "m": "#d8ecf3", }, for if you want non-transparent centers

#chart setings
sns.set(rc={
'axes.facecolor':'#1e1e1e',
'figure.facecolor':'#1e1e1e',

'text.color': '#d4d4d4',
'xtick.color': '#d4d4d4',
'ytick.color': '#d4d4d4',
'grid.color': '#d4d4d4',

'grid.linewidth': '0.1',
'axes.spines.left': 'false',
'axes.spines.right': 'false',
'axes.spines.top': 'false',
'axes.spines.bottom': 'false',

'font.family': 'monospace',
'font.family' : ['courier new'],

},)

#idk what this does
fig, ax = plt.subplots()

#plots the points for male and female measurements
sns.scatterplot(
x=measurement1,
y=measurement2,
data=df,
marker = 'o',
ec=df["gender"].map(colormap),
fc= "none",
#fc=df["gender"].map(colormap2), for if you want non-transparent centers
linewidth=1.5,
s=20)

#plots the user input measurement
plt.plot(
input_x, input_y,
'o',
ms=5,
markerfacecolor="#cc0000",
markeredgecolor='#cc0000',
markeredgewidth=1.2)
plt.annotate('Maya', (input_x, input_y), color='#cc0000')

'''
plt.plot(
23.4, .9,
'o',
ms=5,
markerfacecolor="#002BFF",
markeredgecolor='#002BFF',
markeredgewidth=1.2)
plt.annotate('Maria', (23.4, .9), color='#002BFF')

plt.plot(
18.0, .68,
'o',
ms=5,
markerfacecolor="#00FF78",
markeredgecolor='#00FF78',
markeredgewidth=1.2)
plt.annotate('Helene', (18.0, .68), color='#00FF78')

plt.plot(
18.7, .79,
'o',
ms=5,
markerfacecolor="#9E00FF",
markeredgecolor='#9E00FF',
markeredgewidth=1.2)
plt.annotate('iwnbaw', (18.7, .79), color='#9E00FF')

plt.plot(
17.9, .83,
'o',
ms=5,
markerfacecolor="#FF00D8",
markeredgecolor='#FF00D8',
markeredgewidth=1.2)
plt.annotate('pvnkice', (17.9, .83), color='#FF00D8')

plt.plot(
25.3, .86,
'o',
ms=5,
markerfacecolor="#FBFF00",
markeredgecolor='#FBFF00',
markeredgewidth=1.2)
plt.annotate('Ryles', (25.3, .86), color='#FBFF00')

plt.plot(
22.4, .74,
'o',
ms=5,
markerfacecolor="#FFAE00",
markeredgecolor='#FFAE00',
markeredgewidth=1.2)
plt.annotate('Bee', (22.4, .74), color='#FFAE00')

plt.plot(
22.5, .75,
'o',
ms=5,
markerfacecolor="#00CDFF",
markeredgecolor='#00CDFF',
markeredgewidth=1.2)
plt.annotate('Miya', (22.5, .75), color='#00CDFF')

plt.plot(
18.6, .72,
'o',
ms=5,
markerfacecolor="#00FFB9",
markeredgecolor='#00FFB9',
markeredgewidth=1.2)
plt.annotate('Elise', (18.6, .72), color='#00FFB9')

plt.plot(
16.3, .73,
'o',
ms=5,
markerfacecolor="#000000",
markeredgecolor='#000000',
markeredgewidth=1.2)
plt.annotate('Bella', (16.3, .73), color='#000000')

plt.plot(
25.8, .84,
'o',
ms=5,
markerfacecolor="#FFFFFF",
markeredgecolor='#FFFFFF',
markeredgewidth=1.2)
plt.annotate('Ava', (25.8, .84), color='#FFFFFF')

plt.plot(
28, .87,
'o',
ms=5,
markerfacecolor="#873e23",
markeredgecolor='#873e23',
markeredgewidth=1.2)
plt.annotate('Riley', (28, .87), color='#873e23')'''

#plots the 1sd distrubution for male and female
if 'm' in genders_to_show:
    plt.fill_between(xm, ymt, ymb, alpha = 0.25, color= "#ADD8E6", linewidth= 0)
if 'f' in genders_to_show:
    plt.fill_between(xf, yft, yfb, alpha = 0.25, color= "#FADADD", linewidth= 0)

#locks the limits of the graph
plt.xlim(min_x, max_x)
plt.ylim(min_y, max_y)

#chart title
title = f''
if 'f' in genders_to_show:
    title += f'SDs From Female Average: {sd_from_f}, {round(st.norm.cdf(sd_from_f)*100, 2)} percentile'
if len(genders_to_show) == 2:
    title += f'\n'
if 'm' in genders_to_show:
    title += f'SDs From Male Average: {sd_from_m}, {round(st.norm.cdf(sd_from_m)*100, 2)} percentile'
plt.title(title)

#axis titles
plt.xlabel(measurement_x)
plt.ylabel(measurement_y)

plt.show()
