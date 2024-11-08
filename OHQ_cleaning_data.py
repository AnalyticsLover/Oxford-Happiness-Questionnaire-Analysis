#importando librerias
import pandas as pd
# leyendo el archivo csv
ohq_csv = pd.read_csv("2024_11_ConsejoEducacion_OHQ_CSV.csv")

# lidiando con valores faltantes
ohq_cleaned = ohq_csv.dropna(axis=0)

# cambiando el tipo de dato de todas las columnas a int
ohq_cleaned = ohq_cleaned.astype({'A01': "int", 'A02': "int", 'A03': "int", 'A04': "int", 'A05': "int", 'A06': "int", 'A07': "int", 'A08': "int", 'A09': "int", 'A10': "int", 'A11': "int", 'A12': "int", 'A13': "int", 'A14': "int", 'A15': "int", 'A16': "int", 'A17': "int", 'A18': "int", 'A19': "int",
       'A20': "int", 'A21': "int", 'A22': "int", 'A23': "int", 'A24': "int", 'A25': "int", 'A26': "int", 'A27': "int", 'A28': "int", 'A29': "int"})

# invirtiendo los numeros de las 12 columnas seleccionadas para luego calcular puntaje
ohq_cleaned[["A01", "A05", "A06", "A10", "A13", "A14", "A19", "A23", "A24", "A27", "A28", "A29"]] = ohq_cleaned[["A01", "A05", "A06", "A10", "A13", "A14", "A19", "A23", "A24", "A27", "A28", "A29"]].replace({1:6, 2:5, 3:4, 4:3, 5:2, 6:1})

# crando una nueva columna 'Puntaje' con el puntaje promedio de felicidad
ohq_cleaned['Puntaje'] = ohq_cleaned[["A01", "A02", "A03", "A04", "A05", "A06", "A07", "A08", "A09",
                                      "A10", "A11", "A12", "A13", "A14", "A15", "A16", "A17", "A18",
                                      "A19", "A20", "A21", "A22", "A23", "A24", "A25", "A26", "A27",
                                      "A28", "A29"]].sum(axis=1) / 29

def definir_categoria(puntaje):
    '''
    Toma el valor de la columna "Puntaje" y asigna una categoria segun su valor.
    Parametros:
    puntaje: numero del puntaje final
    '''
    if puntaje <= 1.99:
        return "Infeliz"
    elif puntaje <= 2.99:
        return "Un poco infeliz"
    elif puntaje <= 3.99:
        return "Neutral"
    elif puntaje <= 4.49:
        return "Poco feliz o satisfecho"
    elif puntaje <= 4.99:
        return "Relativamente feliz"
    elif puntaje <= 5.99:
        return "Muy feliz"
    else:
        return "Demasiado feliz"
    
# creando columna "Nivel_Felicidad" usando la funcion definir categoria para cada fila en el dataframe

ohq_cleaned["Nivel_Felicidad"] = ohq_cleaned["Puntaje"].apply(definir_categoria)

# importar el dataframe limpio a un archivo csv

ohq_cleaned.to_csv("2024_11_OHQ_DatosLimpios.csv", index=False)
