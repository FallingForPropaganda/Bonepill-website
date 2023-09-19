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
    with open (dataset, encoding='cp1252') as ansur:
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
            if 'female' in dataset:
                data['gender'].append('f')
            elif 'male' in dataset:
                data['gender'].append('m')
            else:
                data['gender'].append('n')
            data[measurement1].append(float(row[loc1]))
            data[measurement2].append(float(row[loc2]))

    return data

def ratio_gen2(measurement1, measurement2, dataset):
    data = {'gender' : [], measurement1: []}
    with open (dataset, encoding='cp1252') as ansur:
        csvfile = csv.reader(ansur)
        measurements = next(csvfile)
        loc1 = measurements.index(measurement1)
        loc2 = measurements.index(measurement2)
        for row in csvfile:
            if 'female' in dataset:
                data['gender'].append('f')
            elif 'male' in dataset:
                data['gender'].append('m')
            else:
                data['gender'].append('n')
            data[measurement1].append(float(row[loc1])/float(row[loc2]))

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

def linker2(measurement):
    links = {
    'abdominal extension depth sitting': 'abdominalextensiondepthsitting',
    'acromial height': 'acromialheight',
    'acromion radiale length': 'acromionradialelength',
    'ankle circumference': 'anklecircumference',
    'axilla height': 'axillaheight',
    'ball of foot circumference': 'balloffootcircumference',
    'ball of foot length': 'balloffootlength',
    'biacromial shoulder breadth': 'biacromialbreadth',
    'biceps circumference, flexed': 'bicepscircumferenceflexed',
    'bicristal hip breadth':'bicristalbreadth',
    'bideltoid shoulder breadth': 'bideltoidbreadth',
    'bimalleolar ankle breadth': 'bimalleolarbreadth',
    'bitragion chin arc': 'bitragionchinarc',
    'bitragion submandibular arc': 'bitragionsubmandibulararc',
    'bizygomatic breadth': 'bizygomaticbreadth',
    'buttocks circumference': 'buttockcircumference',
    'buttocks depth': 'buttockdepth',
    'buttocks height': 'buttockheight',
    'buttocks knee length': 'buttockkneelength',
    'buttocks popliteal length': 'buttockpopliteallength',
    'calf circumference': 'calfcircumference',
    'cervicale height': 'cervicaleheight',
    'chest breadth': 'chestbreadth',
    'chest circumference': 'chestcircumference',
    'chest depth': 'chestdepth',
    'chest height': 'chestheight',
    'crotch height': 'crotchheight',
    'crotch length omphalion': 'crotchlengthomphalion',
    'crotch length posterior omphalion': 'crotchlengthposterioromphalion',
    'ear breadth': 'earbreadth',
    'ear length': 'earlength',
    'ear protrusion': 'earprotrusion',
    'elbo wrest height': 'elbowrestheight',
    'eye height sitting': 'eyeheightsitting',
    'foot breadth horizontal': 'footbreadthhorizontal',
    'foot length': 'footlength',
    'forearm center of grip length': 'forearmcenterofgriplength',
    'forearm circumference flexed': 'forearmcircumferenceflexed',
    'forearm-forearm breadth': 'forearmforearmbreadth',
    'forearm hand length': 'forearmhandlength',
    'functional leg length': 'functionalleglength',
    'hand breadth': 'handbreadth',
    'hand circumference': 'handcircumference',
    'hand length': 'handlength',
    'head breadth': 'headbreadth',
    'head circumference': 'headcircumference',
    'head length': 'headlength',
    'heel ankle circumference': 'heelanklecircumference',
    'heel breadth': 'heelbreadth',
    'hip breadth': 'hipbreadth',
    'hip breadth sitting': 'hipbreadthsitting',
    'iliocristale height': 'iliocristaleheight',
    'interpupillary breadth': 'interpupillarybreadth',
    'interscye 1': 'interscyei',
    'interscye 2': 'interscyeii',
    'knee height mid patella': 'kneeheightmidpatella',
    'knee height sitting': 'kneeheightsitting',
    'lateral femoral epicondyle height': 'lateralfemoralepicondyleheight',
    'lateral malleolus height': 'lateralmalleolusheight',
    'lower thigh circumference': 'lowerthighcircumference',
    'menton sellion length': 'mentonsellionlength',
    'neck circumference': 'neckcircumference',
    'neck circumference base': 'neckcircumferencebase',
    'overhead fingertip reach sitting': 'overheadfingertipreachsitting',
    'palm length': 'palmlength',
    'popliteal height': 'poplitealheight',
    'radiale stylion length': 'radialestylionlength',
    'shoulder circumference': 'shouldercircumference',
    'shoulder elbow length': 'shoulderelbowlength',
    'shoulder length': 'shoulderlength',
    'sitting height': 'sittingheight',
    'sleeve length spine wrist': 'sleevelengthspinewrist',
    'sleeve outseam': 'sleeveoutseam',
    'wingspan': 'span',
    'height': 'stature',
    'suprasternale height': 'suprasternaleheight',
    'tenth rib height': 'tenthribheight',
    'thigh circumference': 'thighcircumference',
    'thigh clearance': 'thighclearance',
    'thumbtip reach': 'thumbtipreach',
    'tibial height': 'tibialheight',
    'tragion top of head': 'tragiontopofhead',
    'trochanterion height': 'trochanterionheight',
    'vertical trunk circumference': 'verticaltrunkcircumferenceusa',
    'waist backlength': 'waistbacklength',
    'waist breadth': 'waistbreadth',
    'waist circumference': 'waistcircumference',
    'waist depth': 'waistdepth',
    'waist front length sitting': 'waistfrontlengthsitting',
    'waist height omphalion': 'waistheightomphalion',
    'weight (kg)': 'weightkg',
    'wrist circumference': 'wristcircumference',
    'wrist height': 'wristheight',
    'weight (lbs)': 'weightlbs'
}

    return links[measurement]




def linker1(measurement):
    links = {
    'abdominal extension depth, sitting': 'AB-EXT-DEPTH-SIT',
    'acromial height': 'ACROMION_HT',
    'acromial height, sitting': 'ACR_HT-SIT',
    'acromion-radiale length': 'ACR-RADL_LNTH',
    'ankle circumference': 'ANKLE_CIRC',
    'axilla height': 'AXILLA_HT',
    'axillary arm circumference': 'ARM_CIRC-AXILLARY',
    'foot circumference': 'FOOT_CIRC',
    'ball of foot length': 'INSTEP_LNTH',
    'biacromial breadth': 'BIACROMIAL_BRTH',
    'biceps circumference, flexed': 'ARMCIRCBCPS_FLEX',
    'bideltoid breadth': 'BIDELTOID_BRTH',
    'bimalleolar breadth': 'BIMALLEOLAR_BRTH',
    'bispinous breadth': 'BISPINOUS_BRTH',
    'bitragion chin arc': 'BITR_MENTON_ARC',
    'bitragion coronal arc': 'BITR-CORONAL_ARC',
    'bitragion crinion arc': 'BITR-CRINION_ARC',
    'bitragion frontal arc': 'BITR-MINIMUM_FRNTAL_ARC',
    'bitragion submandibular arc': 'BITR_SUBMANDIBULAR_ARC',
    'bitragion subnasale arc': 'BITR_SUBNASALE_ARC',
    'bizygomatic breadth': 'BIZYGOMATIC_BRTH',
    'bustpoint to bustpoint breadth (thelion breadth)': 'BUSTPOINT_TO_BUSTPOINT_BRTH',
    'buttock cirucmference (hip circumference)': 'BUTTOCK_CIRC',
    'buttock depth': 'BUTT_DEPTH',
    'buttock height': 'BUTT_HT',
    'buttock-knee length': 'BUTT_KNEE_LNTH',
    'buttock-popliteal length': 'BUTT_POPLITEAL_LNTH',
    'calf circumference': 'CALF_CIRC',
    'calf height': 'CALF_HT',
    'cervicale height': 'CERVIC_HT',
    'cervicale height, sitting': 'CERVIC_HT_SITTING',
    'chest breadth': 'CHEST_BRTH',
    'chest circumference': 'CHEST_CIRC',
    'chest circumference at scye': 'CHEST_CIRC_AT_SCYE',
    'chest circumference below breast (underbust)': 'CHEST_CIRC-BELOW_BUST_',
    'chest depth': 'CHEST_DEPTH',
    'chest height': 'CHEST_HT',
    'crotch height': 'CROTCH_HT',
    'crotch length (natural indentation)': 'CROTCH_UMBILICUS',
    'crotch length (omphalion)': 'CROTCH_NAT_WAIST',
    'crotch length, posterior (natural indentation)': 'CRTCH_PST_NATURAL',
    'crotch length, posterior (omphalion)': 'CRTCH_PST_OMPHALION',
    'ear breadth': 'EAR_BRTH',
    'ear length': 'EAR_LNTH',
    'ear length above tragion': 'EAR_LNTH-ABOVE_TRAGION',
    'ear protrusion': 'EAR_PROTRUSION',
    'elbow circumference': 'ELBOW_CIRC-EXTENDED',
    'elbow rest height': 'ELBOW_REST_HT',
    'eye height, sitting': 'EYE_HT-SITTING',
    'foot breadth (horizontal)': 'FOOT_BRTH',
    'foot length': 'FOOT_LNTH',
    'forearm cirucmferencce, flexed': 'FOREARM_CIRC-FLEXED',
    'forearm-forearm breadth': 'FOREARM_TO_FOREARM_BRTH',
    'forearm-hand length': 'FOREARM-HAND_LENTH',
    'functional leg breadth': 'FUNCTIONAL_LEG_LNTH',
    'gluteal furrow height': 'GLUTEAL_FURROW_HT',
    'hand breadth': 'HAND_BRTH_AT_METACARPALE',
    'hand circumference': 'HAND_CIRC_AT_METACARPALE',
    'hand length': 'HAND_LNTH',
    'head breadth': 'HEAD_BRTH',
    'head cirumference': 'HEAD_CIRC',
    'head length': 'HEAD_LNTH',
    'heel ankle circumference': 'HEEL_ANKLE_CIRC',
    'heel breadth': 'HEEL_BRTH',
    'hip breadth': 'HIP_BRTH',
    'hip breadth, sitting': 'HIP_BRTH_SITTING',
    'iliocristale height': 'ILIOCRISTALE_HT',
    'interpupillary breadth': 'INTERPUPILLARY_DIST',
    'interscye 1': 'INTRSCY_DIST',
    'interscye 2': 'INTRSCY_MID_DIST',
    'knee circumference': 'KNEE_CIRC',
    'knee height, midpatella': 'PATELLA-MID_HT',
    'knee height, sitting': 'KNEE_HT_-_SITTING',
    'lateral femoral epicondyle height': 'LATERAL_FEMORAL_EPICONDYLE_HT',
    'lateral malleolus height': 'LATERAL-MALLEOUS_HT',
    'lower thight circumference': 'THIGH_CIRC-DISTAL',
    'menton-sellion length': 'MENTON_TO_NASAL_ROOT_DEP_LNTH',
    'midshoulder height, sitting': 'MIDSHOULDER_HT-SITTING',
    'neck-bustpoint/thelion length': 'NECK_TO_BUSTPOINT_LNTH',
    'neck circumference': 'NECK_CIRC-OVER_LARYNX',
    'neck circumference, base': 'NECK_CIRC-BASE',
    'neck height, lateral': 'NECK_HT-LATERAL',
    'overhead fingertip reach': 'OVRHD_REACH',
    'overhead fingertip reach, extended': 'OVRHD_EXT_REACH',
    'overhead fingertip reach, sitting': 'OVRHD_SIT_REACH',
    'popliteal height': 'POPLITEAL_HT-SITTING',
    'radiale-stylion length': 'RADIALE-STYLION_LNTH',
    'scye circumference': 'SCYE_CIRC_OVER_ACROMION',
    'scye depth': 'SCYE_DEPTH',
    'shoulder circumference': 'SHOULDER_CIRC',
    'shoulder-elbow length': 'SHOULDER_ELBOW_LNTH',
    'shoulder length': 'SHOULDER_LNTH',
    'sitting height': 'SITTING_HT',
    'sleeve length: spine-elbow': 'SPINE_TO_ELBOW_LNTH_(SL)',
    'sleeve length: spine-scye': 'SPINE_TO_SCYE_LNTH_(SL)',
    'sleeve length: sline-wrist': 'SPINE_TO_WRIST_LNTH_(SL)',
    'sleeve outseam': 'SLEEVE-OUTSEAM_LNTH',
    'span (wingspan)': 'SPAN',
    'stature (standing height)': 'STATURE',
    'strap length': 'STRAP_LNTH',
    'suprasternale height': 'SUPRASTERNALE_HT',
    'tenth rib height': 'TENTH_RIB',
    'thigh circumference (upper thigh)': 'THIGH_CIRC-PROXIMAL',
    'thigh clearance': 'THIGH_CLEARANCE',
    'thumb breadth': 'THUMB_BRTH',
    'thumbtip reach': 'THUMB-TIP_REACH',
    'trochanterion height': 'TROCHANTERION_HT',
    'vertical trunk circumference': 'VERTICAL_TRUNK_CIRC',
    'waist back length (natural indentation)': 'WAIST_NAT_LNTH',
    'waist back length (omphalion)': 'WAIST_OMPH_LNTH',
    'waist breadth': 'WAIST_BRTH_OMPHALION',
    'waist circumference (natural indentation)': 'WAIST_CIRC_NATURAL',
    'waist circumference (omphalion)': 'WAIST_CIRC-OMPHALION',
    'waist depth': 'WAIST_DEPTH-OMPHALION',
    'waist front length (natural indentation)': 'WST_NAT_FRONT',
    'waist front length (omphalion)': 'WST_OMP_FRONT',
    'waist height (natural indentation)': 'WAIST_HT_NATURAL',
    'waist height (omphalion)': 'WAIST_HT-OMPHALION',
    'waist height, sitting (natural indentation)': 'WAIST_HT_SIT_NATURAL',
    'waist height, sitting (omphalion)': 'WAIST_HT-UMBILICUS-SITTING',
    'waist-hip length': 'WAIST_HIP_LNTH',
    'waist (natural indenation) - waist (omphalion) length': 'WAIST_NATURAL_TO_WAIST_UMBILICUS',
    'weight': 'WEIGHT',
    'wrist-center of grip length': 'WRIST_TO_CENTER_OF_GRIP_LNTH',
    'wrist circumference': 'WRIST_CIRC-STYLION',
    'wrist height': 'WRIST_HT',
    'wrist height, sitting': 'WRIST_HT-SITTING',
    'wrist-index finger length': 'WRIST_TO_INDEX_FINGER_LNTH',
    'wrist-thumbtip length': 'WRIST_TO_THUMBTIP_LNTH',
    'wrist-wall length': 'WRST_LNTH_TO_WALL',
    'wrist-wall length, extended': 'WRST_EXT_TO_WALL'
        }
    return links[measurement]