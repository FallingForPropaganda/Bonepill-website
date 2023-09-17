import tt
import matplotlib.pyplot as plt

genders_to_show = 'fm'                             
units = 'in'                                     
input_x = 75
input_y = 27.5
measurement_x = 'Height'
measurement_y = 'Waist Circumference'

fig = tt.grapher(genders_to_show, units, input_x, input_y, measurement_x, measurement_y)
fig.set_figheight(8)  
plt.show()

''' 
{
    'AB-EXT-DEPTH-SIT': 'Abdominal Extension Depth, Sitting',
    'ACROMION_HT': 'Acromial Height',
    'ACR_HT-SIT': 'Acromial Height, Sitting',
    'ACR-RADL_LNTH': 'Acromion-Radiale Length',
    'ANKLE_CIRC': 'Ankle Circumference',
    'AXILLA_HT': 'Axilla Height',
    'ARM_CIRC-AXILLARY' : 'Axillary Arm Circumference',
    'FOOT_CIRC': 'Foot Circumference',
    'INSTEP_LNTH': 'Ball of Foot Length',
    'BIACROMIAL_BRTH': 'Biacromial Breadth',
    'ARMCIRCBCPS_FLEX': 'Biceps Circumference, Flexed',
    'BIDELTOID_BRTH': 'Bideltoid Breadth',
    'BIMALLEOLAR_BRTH': 'Bimalleolar Breadth',
    'BISPINOUS_BRTH': 'Bispinous Breadth',
    'BITR_MENTON_ARC': 'Bitragion CHin Arc',
    'BITR-CORONAL_ARC': 'Bitragion Coronal Arc',
    'BITR-CRINION_ARC': 'Bitragion Crinion Arc',
    'BITR-MINIMUM_FRNTAL_ARC': 'Bitragion Frontal Arc',
    'BITR_SUBMANDIBULAR_ARC': 'Bitragion Submandibular Arc',
    'BITR_SUBNASALE_ARC': 'Bitragion Subnasale Arc',
    'BIZYGOMATIC_BRTH': 'Bizygomatic Breadth',
    'BUSTPOINT_TO_BUSTPOINT_BRTH': 'Bustpoint to Bustpoint Breadth (THELION BREADTH)',
    'BUTTOCK_CIRC': 'Buttock Cirucmference (Hip Circumference)',
    'BUTT_DEPTH': 'Buttock Depth',
    'BUTT_HT': 'Buttock Height',
    'BUTT_KNEE_LNTH':'Buttock-Knee Length' ,
    'BUTT_POPLITEAL_LNTH': 'Buttock-Popliteal Length',
    'CALF_CIRC': 'Calf Circumference',
    'CALF_HT': 'Calf Height',
    'CERVIC_HT': 'Cervicale Height',
    'CERVIC_HT_SITTING': 'Cervicale Height, Sitting',
    'CHEST_BRTH': 'Chest Breadth',
    'CHEST_CIRC': 'Chest Circumference',
    'CHEST_CIRC_AT_SCYE': 'Chest Circumference at Scye',
    'CHEST_CIRC-BELOW_BUST_': 'Chest Circumference Below Breast (Underbust)', 
    'CHEST_DEPTH': 'Chest Depth',
    'CHEST_HT': 'Chest Height',
    'CROTCH_HT': 'Crotch Height',
    'CROTCH_UMBILICUS': 'Crotch Length (Natural Indentation)',
    'CROTCH_NAT_WAIST': 'Crotch Length (Omphalion)',
    'CRTCH_PST_NATURAL': 'Crotch Length, Posterior (Natural Indentation)',
    'CRTCH_PST_OMPHALION': 'Crotch Length, Posterior (Omphalion)',
    'EAR_BRTH': 'Ear Breadth',
    'EAR_LNTH': 'Ear Length',
    'EAR_LNTH-ABOVE_TRAGION': 'Ear Length Above Tragion',
    'EAR_PROTRUSION': 'Ear Protrusion',
    'ELBOW_CIRC-EXTENDED': 'Elbow Circumference',
    'ELBOW_REST_HT': 'Elbow Rest Height',
    'EYE_HT-SITTING': 'Eye Height, Sitting',
    'FOOT_BRTH': 'Foot Breadth (Horizontal)',
    'FOOT_LNTH': 'Foot Length',
    'FOREARM_CIRC-FLEXED': 'Forearm Cirucmferencce, Flexed',
    'FOREARM_TO_FOREARM_BRTH': 'Forearm-Forearm Breadth',
    'FOREARM-HAND_LENTH': 'Forearm-Hand Length',
    'FUNCTIONAL_LEG_LNTH': 'Functional Leg Breadth',
    'GLUTEAL_FURROW_HT': 'Gluteal Furrow Height',
    'HAND_BRTH_AT_METACARPALE': 'Hand Breadth',
    'HAND_CIRC_AT_METACARPALE': 'Hand Circumference',
    'HAND_LNTH': 'Hand Length',
    'HEAD_BRTH': 'Head Breadth',
    'HEAD_CIRC': 'Head Cirumference',
    'HEAD_LNTH': 'Head Length',
    'HEEL_ANKLE_CIRC': 'Heel Ankle Circumference',
    'HEEL_BRTH': 'Heel Breadth',
    'HIP_BRTH': 'Hip breadth',
    'HIP_BRTH_SITTING': 'Hip breadth, Sitting',
    'ILIOCRISTALE_HT': 'Iliocristale Height',
    'INTERPUPILLARY_DIST': 'Interpupillary breadth',
    'INTRSCY_DIST': 'Interscye 1',
    'INTRSCY_MID_DIST': 'Interscye 2',
    'KNEE_CIRC': 'Knee Circumference',
    'PATELLA-MID_HT': 'Knee Height, Midpatella',
    'KNEE_HT_-_SITTING': 'Knee Height, Sitting',
    'LATERAL_FEMORAL_EPICONDYLE_HT': 'Lateral Femoral Epicondyle Height',
    'LATERAL-MALLEOUS_HT': 'Lateral Malleolus Height',
    'THIGH_CIRC-DISTAL': 'Lower Thight Circumference',
    'MENTON_TO_NASAL_ROOT_DEP_LNTH': 'Menton-Sellion Length',
    'MIDSHOULDER_HT-SITTING': 'Midshoulder Height, Sitting',
    'NECK_TO_BUSTPOINT_LNTH': 'Neck-Bustpoint/Thelion Length',
    'NECK_CIRC-OVER_LARYNX': 'Neck Circumference',
    'NECK_CIRC-BASE': 'Neck Circumference, Base',
    'NECK_HT-LATERAL': 'Neck Height, Lateral',
    'OVRHD_REACH': 'Overhead Fingertip Reach',
    'OVRHD_EXT_REACH': 'Overhead Fingertip Reach, Extended',
    'OVRHD_SIT_REACH': 'Overhead Fingertip Reach, Sitting',
    'POPLITEAL_HT-SITTING': 'Popliteal Height',
    'RADIALE-STYLION_LNTH': 'Radiale-Stylion Length',
    'SCYE_CIRC_OVER_ACROMION': 'Scye Circumference',
    'SCYE_DEPTH': 'Scye Depth',
    'SHOULDER_CIRC': 'Shoulder Circumference',
    'SHOULDER_ELBOW_LNTH': 'Shoulder-Elbow Length',
    'SHOULDER_LNTH': 'Shoulder Length',
    'SITTING_HT': 'Sitting Height',
    'SPINE_TO_ELBOW_LNTH_(SL)': 'Sleeve Length: Spine-Elbow',
    'SPINE_TO_SCYE_LNTH_(SL)': 'Sleeve Length: Spine-Scye',
    'SPINE_TO_WRIST_LNTH_(SL)': 'Sleeve Length: Sline-Wrist',
    'SLEEVE-OUTSEAM_LNTH': 'Sleeve Outseam',
    'SPAN': 'Span (Wingspan)',
    'STATURE': 'Stature (Standing Height)',
    'STRAP_LNTH': 'Strap Length',
    'SUPRASTERNALE_HT': 'Suprasternale Height',
    'TENTH_RIB': 'Tenth Rib Height',
    'THIGH_CIRC-PROXIMAL': 'Thigh Circumference (Upper thigh)',
    'THIGH_CLEARANCE': 'Thigh Clearance',
    'THUMB_BRTH': 'Thumb Breadth',
    'THUMB-TIP_REACH': 'Thumbtip Reach',
    'TROCHANTERION_HT': 'Trochanterion Height',
    'VERTICAL_TRUNK_CIRC': 'Vertical Trunk Circumference',
    'WAIST_NAT_LNTH': 'Waisst Back Length (Natural Indentation)',
    'WAIST_OMPH_LNTH': 'Waist Back Length (Omphalion)',
    'WAIST_BRTH_OMPHALION': 'Waist Breadth',
    'WAIST_CIRC_NATURAL': 'Waist Circumference (Natural Indentation)',
    'WAIST_CIRC-OMPHALION': 'Waist Circumference (Omphalion)',
    'WAIST_DEPTH-OMPHALION': 'Waist Depth',
    'WST_NAT_FRONT': 'Waist Front Length (Natural Indentation)',
    'WST_OMP_FRONT': 'Waist Front Length (Omphalion)',
    'WAIST_HT_NATURAL': 'Waist Height (Natural Indentation)',
    'WAIST_HT-OMPHALION': 'Waist Height (Omphalion)',
    'WAIST_HT_SIT_NATURAL': 'Waist Height, Sitting (Natural Indentation)',
    'WAIST_HT-UMBILICUS-SITTING': 'Waist Height, Sitting (Omphalion)',
    'WAIST_HIP_LNTH': 'Waist-Hip Length',
    'WAIST_NATURAL_TO_WAIST_UMBILICUS': 'Waist (Natural Indenation) - Waist (Omphalion) Length',
    'WEIGHT': 'Weight',
    'WRIST_TO_CENTER_OF_GRIP_LNTH': 'Wrist-Center of Grip Length',
    'WRIST_CIRC-STYLION': 'Wrist Circumference',
    'WRIST_HT': 'Wrist Height',
    'WRIST_HT-SITTING': 'Wrist Height, Sitting',
    'WRIST_TO_INDEX_FINGER_LNTH': 'Wrist-Index Finger Length',
    'WRIST_TO_THUMBTIP_LNTH': 'Wrist-Thumbtip Length',
    'WRST_LNTH_TO_WALL': 'Wrist-Wall Length',
    'WRST_EXT_TO_WALL': 'Wrist-Wall Length, Extended'
    }
'''