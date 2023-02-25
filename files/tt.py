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

    def cords_gen(measurement1, measurement2, dataset):
        cords = []
        with open (dataset) as ansur:
            csvfile = csv.reader(ansur)
            measurements = next(csvfile)
            loc1 = measurements.index(measurement1)
            loc2 = measurements.index(measurement2)
            for row in csvfile:
                temp = []
                temp.append(int(row[loc1]))
                temp.append(int(row[loc2]))
                cords.append(temp)
        return cords

    def list_gen(measurement, dataset):
        list1 = []
        with open (dataset) as ansur:
            csvfile = csv.reader(ansur)
            measurements = next(csvfile)
            loc = measurements.index(measurement)
            for row in csvfile:
                list1.append(int(row[loc]))
        return list1

    def ratio_gen(cords):
        list1 = []
        for item in cords:
            list1.append(item[0]/item[1])
        return list1

    def avg_and_sd_calc(inputlist):
        sd = np.std(inputlist)
        total = 0
        for item in inputlist:
            total += item
        avg = total/len(inputlist)
        return sd, avg

    def print_line():
        return " ------------------------------------------------------------------------------------------------------------------------------------------"

    def fourty_lines():
        return "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

    def blank_line():
        return " |                                                                                                                                        |"

    def better_print(input_string):
        add_spaces = (137-len(input_string))//2
        counter = add_spaces
        output_string = " |"
        for x in range(counter):
            output_string += " "
        output_string += input_string
        counter = add_spaces
        while len(output_string) != 138:
            output_string += " "
        output_string += "| "
        #print(len(output_string))
        return output_string

    def resize():
        print(f"{print_line()}")
        for x in range(10):
            print(better_print(' '))
        print(f"{better_print('Expand/resize your window until this box just fits inside it with no spaces between each vertical line, then press enter.')}")
        for x in range(10):
            print(better_print(' '))
        print(f"{print_line()}")
        
        return

    def line_of_best_fit(coordinates):
        x_total = 0
        y_total = 0
        total = 0
        for item in coordinates:
            x_total += item[0]
            y_total += item[1]
            total += 1
        x_average = x_total/total
        y_average = y_total/total
        
        x_minus_x_average = []
        y_minus_y_average = []
        for item in coordinates:
            x_minus_x_average.append(item[0] - x_average)
            y_minus_y_average.append(item[1] - y_average)

        x_y = 0
        x_x = 0
        counter = 0
        while counter != len(coordinates):
            x_x += (x_minus_x_average[counter] * x_minus_x_average[counter])
            x_y += (x_minus_x_average[counter] * y_minus_y_average[counter])
            counter += 1
        slope = x_y/x_x
        
        b = y_average - slope*x_average

        return slope, b

    def lob_gen(coordinates, m, b):
        xy = [coordinates[0][0]]
        xy.append(m*coordinates[0][0] + b)

        return xy

    def dict_gen(measurement1, measurement2, dataset):
        data = {'gender' : [], measurement1: [],measurement2: []}
        with open (dataset, encoding='cp1252') as ansur:
            csvfile = csv.reader(ansur)
            measurements = next(csvfile)
            loc1 = measurements.index(measurement1)
            loc2 = measurements.index(measurement2)
            for row in csvfile:
                if dataset == 'ansur2_female.csv':
                    data['gender'].append('f')
                elif dataset == 'ansur2_male.csv':
                    data['gender'].append('m')
                else:
                    data['gender'].append('n')
                data[measurement1].append(float(row[loc1]))
                data[measurement2].append(float(row[loc2]))

        return data

    def array_gen(measurement1, measurement2, dataset):
        x = []
        y = []
        with open (dataset) as ansur:
            csvfile = csv.reader(ansur)
            measurements = next(csvfile)
            loc1 = measurements.index(measurement1)
            loc2 = measurements.index(measurement2)
            for row in csvfile:
                x.append(float(row[loc1]))
                y.append(float(row[loc2]))

        xa = np.array(x)
        ya = np.array(y)
        return x, y, xa, ya

    def sd_gen(x, y, xa, ya):
        slope, intercept, r_value, p_value, std_err = linregress(x, y)
        residuals = ya - (slope*xa + intercept)
        std_dev = np.std(residuals)
        return std_dev, slope, intercept

    def top_bottom_line_gen(measurement1, measurement2, x, y, xa, ya):

        #do calculations
        slope, intercept, r_value, p_value, std_err = linregress(x, y)
        residuals = ya - (slope*xa + intercept)
        sd = np.std(residuals)

        #sorry about naming conventions but this just finds the top and bottom line above and belowe 1 SD of the line of best fit
        x_vals = np.arange(0,10000, 1)
        yt_vals = x_vals*slope + intercept + sd
        yb_vals = x_vals*slope + intercept - sd

        #returns things
        return x_vals, yt_vals, yb_vals, sd, slope, intercept

    def linker(measurement):
        links = {
        'Abdominal Extension Depth Sitting': 'abdominalextensiondepthsitting',
        'Acromial Height': 'acromialheight',
        'Acromion Radiale Length': 'acromionradialelength',
        'Ankle Circumference': 'anklecircumference',
        'Axilla Height': 'axillaheight',
        'Ball of Foot Circumference': 'balloffootcircumference',
        'Ball of Foot Length': 'balloffootlength',
        'Biacromial Shoulder Breadth': 'biacromialbreadth',
        'Biceps Circumference, Flexed': 'bicepscircumferenceflexed',
        'Bicristal Hip Breadth':'bicristalbreadth',
        'Bideltoid Shoulder Breadth': 'bideltoidbreadth',
        'Bimalleolar Ankle Breadth': 'bimalleolarbreadth',
        'Bitragion Chin Arc': 'bitragionchinarc',
        'Bitragion Submandibular Arc': 'bitragionsubmandibulararc',
        'Bizygomatic Breadth': 'bizygomaticbreadth',
        'Buttocks Circumference': 'buttockcircumference',
        'Buttocks Depth': 'buttockdepth',
        'Buttocks Height': 'buttockheight',
        'Buttocks Knee Length': 'buttockkneelength',
        'Buttocks Popliteal Length': 'buttockpopliteallength',
        'Calf Circumference': 'calfcircumference',
        'Cervicale Height': 'cervicaleheight',
        'Chest Breadth': 'chestbreadth',
        'Chest Circumference': 'chestcircumference',
        'Chest Depth': 'chestdepth',
        'Chest Height': 'chestheight',
        'Crotch Height': 'crotchheight',
        'Crotch Length Omphalion': 'crotchlengthomphalion',
        'Crotch Length Posterior Omphalion': 'crotchlengthposterioromphalion',
        'Ear Breadth': 'earbreadth',
        'Ear Length': 'earlength',
        'Ear Protrusion': 'earprotrusion',
        'Elbo Wrest Height': 'elbowrestheight',
        'Eye Height Sitting': 'eyeheightsitting',
        'Foot Breadth Horizontal': 'footbreadthhorizontal',
        'Foot Length': 'footlength',
        'Forearm Center of Grip Length': 'forearmcenterofgriplength',
        'Forearm Circumference Flexed': 'forearmcircumferenceflexed',
        'Forearm-Forearm Breadth': 'forearmforearmbreadth',
        'Forearm Hand Length': 'forearmhandlength',
        'Functional Leg Length': 'functionalleglength',
        'Hand Breadth': 'handbreadth',
        'Hand Circumference': 'handcircumference',
        'Hand Length': 'handlength',
        'Head Breadth': 'headbreadth',
        'Head Circumference': 'headcircumference',
        'Head Length': 'headlength',
        'Heel Ankle Circumference': 'heelanklecircumference',
        'Heel Breadth': 'heelbreadth',
        'Hip Breadth': 'hipbreadth',
        'Hip Breadth Sitting': 'hipbreadthsitting',
        'Iliocristale Height': 'iliocristaleheight',
        'Interpupillary Breadth': 'interpupillarybreadth',
        'Interscye 1': 'interscyei',
        'Interscye 2': 'interscyeii',
        'Knee Height Mid Patella': 'kneeheightmidpatella',
        'Knee Height Sitting': 'kneeheightsitting',
        'Lateral Femoral Epicondyle Height': 'lateralfemoralepicondyleheight',
        'Lateral Malleolus Height': 'lateralmalleolusheight',
        'Lower Thigh Circumference': 'lowerthighcircumference',
        'Menton Sellion Length': 'mentonsellionlength',
        'Neck Circumference': 'neckcircumference',
        'Neck Circumference Base': 'neckcircumferencebase',
        'Overhead Fingertip Reach Sitting': 'overheadfingertipreachsitting',
        'Palm Length': 'palmlength',
        'Popliteal Height': 'poplitealheight',
        'Radiale Stylion Length': 'radialestylionlength',
        'Shoulder Circumference': 'shouldercircumference',
        'Shoulder Elbow Length': 'shoulderelbowlength',
        'Shoulder Length': 'shoulderlength',
        'Sitting Height': 'sittingheight',
        'Sleeve Length Spine Wrist': 'sleevelengthspinewrist',
        'Sleeve Outseam': 'sleeveoutseam',
        'Wingspan': 'span',
        'Height': 'stature',
        'Suprasternale Height': 'suprasternaleheight',
        'Tenth Rib Height': 'tenthribheight',
        'Thigh Circumference': 'thighcircumference',
        'Thigh Clearance': 'thighclearance',
        'Thumbtip Reach': 'thumbtipreach',
        'Tibial Height': 'tibialheight',
        'Tragion Top of Head': 'tragiontopofhead',
        'Trochanterion Height': 'trochanterionheight',
        'Vertical Trunk Circumference': 'verticaltrunkcircumferenceusa',
        'Waist Backlength': 'waistbacklength',
        'Waist Breadth': 'waistbreadth',
        'Waist Circumference': 'waistcircumference',
        'Waist Depth': 'waistdepth',
        'Waist Front Length Sitting': 'waistfrontlengthsitting',
        'Waist Height Omphalion': 'waistheightomphalion',
        'Weight (kg)': 'weightkg',
        'Wrist Circumference': 'wristcircumference',
        'Wrist Height': 'wristheight',
        'Weight (lbs)': 'Weightlbs'
        }

        return links[measurement]

    #finds the csv value for each display title
    measurement1 = linker(measurement_x)             
    measurement2 = linker(measurement_y)                    

    #generates a dictionary in the format {gender, measurement 1, measurement 2}, then turns it into a pandas dataframe
    #also has the option to do one or both genders
    dataf = dict_gen(measurement1, measurement2, "ansur2_female.csv")
    datam = dict_gen(measurement1, measurement2, "ansur2_male.csv")

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
    xm, ymt, ymb, sd_m, slope_m, intercept_m = top_bottom_line_gen(
    measurement1,
    measurement2,
    datam[measurement1],
    datam[measurement2],
    np.array(datam[measurement1]),
    np.array(datam[measurement2])
    )

    xf, yft, yfb, sd_f, slope_f, intercept_f = top_bottom_line_gen(
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
    'axes.labelcolor': '#d4d4d4',

    'grid.linewidth': '0.1',
    'axes.spines.left': 'false',
    'axes.spines.right': 'false',
    'axes.spines.top': 'false',
    'axes.spines.bottom': 'false',

    'font.family': 'monospace',

   
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

    fig.set_figheight(6) 
    fig.set_figwidth(10)  
    return fig
