import tt
import matplotlib.pyplot as plt

genders_to_show = 'mf'                             
units = 'in'                                     
input_x = 37.5
input_y = 27.5
measurement_x = 'height'
measurement_y = 'Waist Circumference'

fig = tt.grapher(genders_to_show, units, input_x, input_y, measurement_x, measurement_y)
fig.set_figheight(8)  
plt.show()