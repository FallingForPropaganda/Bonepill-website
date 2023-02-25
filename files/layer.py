import tt
def layer(mx, my, x, y):
      import tt
      genders_to_show = 'mf'                             
      units = 'in'                                     
      
      fig = tt.grapher(genders_to_show, units, x, y, mx, my)
      fig.set_figheight(6) 
      fig.set_figwidth(10.5)  
      return fig