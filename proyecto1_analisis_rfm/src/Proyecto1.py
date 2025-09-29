import pandas as pd

# Cargar el conjunto de datos
df = pd.read_csv('data.csv', encoding='ISO-8859-1')

# Eliminar filas con valores nulos en 'CustomerID'
df.dropna(subset=['CustomerID'], inplace=True)

# Convertir 'CustomerID' a tipo de dato entero
df['CustomerID'] = df['CustomerID'].astype(int)

# Convertir 'InvoiceDate' a formato de fecha y hora
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Calcular el 'TotalPrice' para cada transacción
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Filtrar las transacciones con 'TotalPrice' mayor a 0
df = df[df['TotalPrice'] > 0]

# Obtener la fecha más reciente en el conjunto de datos para calcular la recencia
most_recent_date = df['InvoiceDate'].max()

# Agrupar los datos por 'CustomerID' para calcular las métricas RFM
rfm_df = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda date: (most_recent_date - date.max()).days,
    'InvoiceNo': lambda num: num.nunique(),
    'TotalPrice': lambda price: price.sum()
})

# Renombrar las columnas para mayor claridad
rfm_df.columns = ['Recency', 'Frequency', 'Monetary']

# Asignar un puntaje del 1 al 5 para cada métrica RFM
# Para Recencia: a menor valor, mayor puntuación
rfm_df['R_Score'] = pd.qcut(rfm_df['Recency'], 5, labels=[5, 4, 3, 2, 1])

# Para Frecuencia y Monetario: a mayor valor, mayor puntuación
rfm_df['F_Score'] = pd.qcut(rfm_df['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
rfm_df['M_Score'] = pd.qcut(rfm_df['Monetary'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])

# Calcular el puntaje RFM total para cada cliente
rfm_df['RFM_Score'] = rfm_df['R_Score'].astype(str) + rfm_df['F_Score'].astype(str) + rfm_df['M_Score'].astype(str)

# Asignar los segmentos a los clientes
def asignar_segmento(row):
    r, f, m = row['R_Score'], row['F_Score'], row['M_Score']

    # Lógica de segmentación basada en la puntuación RFM
    if r in [4, 5] and f in [4, 5] and m in [4, 5]:
        return 'Campeones' # Clientes de alto valor y leales
    elif r in [4, 5] and f in [2, 3] and m in [2, 3]:
        return 'Leales' # Clientes recientes y frecuentes, pero con un valor medio
    elif r in [3, 4] and f in [3, 4] and m in [3, 4]:
        return 'Potenciales Leales' # Clientes que podrían convertirse en leales
    elif r in [4, 5] and f in [1, 2] and m in [1, 2]:
        return 'Nuevos Clientes' # Recientes pero con pocas compras
    elif r in [1, 2] and f in [1, 2] and m in [1, 2]:
        return 'En Riesgo' # Clientes que podrían abandonar la marca
    elif r in [1, 2] and f in [3, 4] and m in [3, 4]:
        return 'Necesitan Atención' # Clientes que solían ser valiosos pero han dejado de comprar
    elif r in [1, 2] and f in [4, 5] and m in [4, 5]:
        return 'No se los puede perder' # Clientes que compraban mucho pero no han vuelto
    else:
        return 'Segmento General' # Resto de los clientes

# Aplicar la función para crear la columna de segmento
rfm_df['Segmento_RFM'] = rfm_df.apply(asignar_segmento, axis=1)

# Asegurar que la columna 'Monetary' es un tipo de dato numérico (flotante) y redondear
rfm_df['Monetary'] = pd.to_numeric(rfm_df['Monetary'], errors='coerce')
rfm_df['Monetary'] = rfm_df['Monetary'].round(2)

# Guardar los resultados finales en un archivo CSV usando un punto y coma como separador
rfm_df.to_csv('analisis_rfm_final.csv', sep=';', index=True)

print("\nAnálisis RFM completado y guardado en 'analisis_rfm_final.csv' usando un punto y coma como separador.")