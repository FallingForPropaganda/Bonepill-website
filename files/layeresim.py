def layer(ester, injection_dates, injection_doses):
      import esim
      try:
            dates = list(map(float, [date.strip() for date in injection_dates.split(',') if date.strip() != '']))
            doses = list(map(float, [dose.strip() for dose in injection_doses.split(',') if dose.strip() != '']))
            ester1 = ester.lower()
            fig = esim.grapher(ester1, dates, doses, 'Better Injectable Estradiol Simulator')
            fig.set_figheight(6) 
            fig.set_figwidth(10.5)  
            return fig
      except:
            fig = esim.grapher('een', [0, 7, 15, 21, 28, 35, 42], [4, 5, 3.5, 4, 6, 5, 4], "if you're seeing this you messed up an input field")
            fig.set_figheight(6) 
            fig.set_figwidth(10.5)  
            return fig
      #python -m http.server 8000