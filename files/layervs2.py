def layer(mx, my, x, y, g, u):
      import ttvs2

      fig = ttvs2.grapher(g, u, x, y, mx, my)
      fig.set_figheight(6) 
      fig.set_figwidth(10.5)  
      return fig

      #python -m http.server 8000