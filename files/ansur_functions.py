import csv
import pandas as pd
import numpy as np
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