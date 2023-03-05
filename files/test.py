import tt
import matplotlib.pyplot as plt

genders_to_show = 'f'                             
units = 'in'                                     
input_x = 75
input_y = 27.5
measurement_x = 'height'
measurement_y = 'waist circumference'

fig = tt.grapher(genders_to_show, units, input_x, input_y, measurement_x, measurement_y)
fig.set_figheight(8)  
plt.show()