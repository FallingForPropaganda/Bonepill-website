#I made this to generate charts showing compairisons between 2 measurements
#There are 5 input varilables
#genders_to_show, which can be a string of 'f', 'm', or 'mf', it toggles which genders to display
#units, which is either 'cm' or 'in', it is used for unit conversions
#input_x and input_y, which are inputs for the x and y coordinates that will be graphed 
#measurement_x and measurement_y, which are the measurements being graphed
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ansur_functions as funcs
import scipy.stats as st

#input variables
genders_to_show = 'f'                             
units = 'in'                                     
input_x = 71
input_y = 17
measurement_x = 'Height'
measurement_y = 'Bideltoid Shoulder Breadth'

#finds the csv value for each display title
measurement1 = funcs.linker(measurement_x)             
measurement2 = funcs.linker(measurement_y)                    

#generates a dictionary in the format {gender, measurement 1, measurement 2}, then turns it into a pandas dataframe
#also has the option to do one or both genders
dataf = funcs.dict_gen(measurement1, measurement2, "ansur2_female.csv")
datam = funcs.dict_gen(measurement1, measurement2, "ansur2_male.csv")

#unit conversions, this is some weird ass mf code
data_list = dataf, datam
for data in data_list:
    measurementlist = [measurement1, measurement2]
    for measurement in measurementlist:

        #converts from mm to either cm to in
        new_measurement = []
        for value in data[measurement]:
            if units == 'cm':
                new_measurement.append(value / 10)
            elif units == 'in':
                new_measurement.append(value / (10*2.54))

        #replaces the old data with the unit converted data
        data[measurement] = new_measurement


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
