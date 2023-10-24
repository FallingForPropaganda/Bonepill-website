def layer(ester, injection_dates, injection_doses):
      import esim

      fig = esim.grapher(ester, injection_dates, injection_doses)
      fig.set_figheight(6) 
      fig.set_figwidth(10.5)  
      return fig

      #python -m http.server 8000