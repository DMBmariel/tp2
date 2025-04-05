

puntuacion = {'kill': 3, 'asistencia': 1, 'muerte': -1}

def calculo_kills(kill):
    """Recibo el dato kill y lo multiplico por los puntos"""
    nuevo_kill = kill *puntuacion['kill']
    return nuevo_kill


def calculo_assists(assist):
    """Recibo el dato assists y lo multiplico por los puntos"""
    nuevo_assists = assist * puntuacion['asistencia']
    return nuevo_assists 


def calculo_deaths(death):
    """Recibo el dato death y segun su valor lo multiplico por los puntos"""
    if death == True:
                nuevo_death = -1
                return nuevo_death
    else:
                nuevo_death = 0
                return nuevo_death


def calculo_puntos(kill, assists, death):
     """Recibo los puntajes y los sumo """
     puntos = kill + assists + death
     return puntos


def calculo_mejor_jugador(resultados):
     """Recibo los puntos de los jugadores y obtengo cual es el mejor"""
     mejor_jugador = ""
     mejor_puntaje = -1
     for jugador, datos in resultados.items():
          if datos["Puntos"] > mejor_puntaje:
               mejor_puntaje = datos["Puntos"]
               mejor_jugador = jugador
     return mejor_jugador  


def imprimo_resultados(resultados):
     """Imprimo los resultados en forma de tabla"""
     print('Ranking rondalina: ')
     print(f"{'Jugador':<10}{'Kills':<7}{'Asistencias':<7}{'Muertes':<7}{'MVPs':<7}{'Puntos':<7}")
     print("-" * 22)

     for resultado, datos in resultados.items():
          print(f"{resultado:<10}{datos['kills']:<10}{datos['assists']:<10}{datos['deaths']:<10}{datos['MVPs']:<10}{datos['Puntos']:<10}")         
           
          
     


def calculo_partidas(rounds):
    """ Calculo los puntos obtenidos """

    for round in rounds:
        resultados = {}
        for jugador, datos in round.items():
            # hago una copia de los datos para modificar con los puntos obtenidos
            nuevo_dato = datos.copy()
            nuevo_dato["kills"] = calculo_kills(datos["kills"])
            nuevo_dato["assists"] = calculo_assists(datos["assists"])
            nuevo_dato["deaths"] = calculo_deaths(datos["deaths"])
            nuevo_dato["Puntos"] = calculo_puntos(nuevo_dato["kills"],nuevo_dato["assists"], nuevo_dato["deaths"])
            nuevo_dato["MVPs"] = 0   
            resultados[jugador] = nuevo_dato
        mejor = calculo_mejor_jugador(resultados)
        if mejor in resultados:
             resultados[mejor]["MVPs"] += 1 

        result_final = {}
        for jugador, datos in resultados.items():
            nuevo_dato = datos.copy()
            nuevo_dato["kills"] += datos["kills"]
            nuevo_dato["assists"] += datos["assists"]
            nuevo_dato["deaths"] += datos["deaths"]
            nuevo_dato["Puntos"] += datos["Puntos"] 
            nuevo_dato["MVPs"] += datos["MVPs"]
            result_final[jugador] = nuevo_dato
            
        imprimo_resultados(resultados)
    
    print('Ranking final:')
    imprimo_resultados(result_final)
    
          
       

        
         


