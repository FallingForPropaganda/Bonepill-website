def layer(userinput):
      import esim
      #ester a, b, c, d values (used in calculations)
      een = [0.42412968, 0.43452980, 0.15291485, 333.874181]
      ev = [2.38229125, 0.23345814, 1.37642769, 2596.05956]
      eu = [0.29634323, 4799337.57, 0.03141554, 65.9493374]
      ec = [0.29634323, 4799337.57, 0.03141554, 65.9493374] #apparently ur supposed to use EEn instead of EC when ur graphing bause EC data is flawed
      try:
            injections = []
            for term in [term.strip(" ()[]").lower() for term in userinput.split(',')]:
                  a = term.split('/')
                  a[0] = float(a[0])
                  a[1] = float(a[1])
                  match a[2]:
                        case 'een': a[2] = een
                        case 'ev': a[2] = ev
                        case 'ec': a[2] = ec
                        case 'eu': a[2] = eu
                  injections.append(a)
            fig = esim.grapher(injections, 'Better Injectable Estradiol Simulator')
            fig.set_figheight(6) 
            fig.set_figwidth(10.5)  
            return fig
      except:
            fig = esim.grapher([[0, 4, ev],[7, 4, een],[14, 2.5, een],[21, 1.5, een],[28, 4, ev],[35, 4, een],[42, 2.5, een],[49, 1.5, een]], "IF YOU'RE SEEING THIS YOU MESSED UP AN INPUT FIELD")
            fig.set_figheight(6) 
            fig.set_figwidth(10.5)  
            return fig
      #python -m http.server 8000