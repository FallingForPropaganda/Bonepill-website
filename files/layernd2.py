def layer(mx, my, x, y, g, u):
      import ttnd2

      fig = ttnd2.grapher(g, u, x, y, mx, my)
      fig.set_figheight(6) 
      fig.set_figwidth(10.5)  
      return fig

      #python -m http.server 8000