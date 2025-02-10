#import kagglehub

# Download latest version
#path = kagglehub.dataset_download("hosammhmdali/supermarket-sales")

#print("Path to dataset files:", path)

import pandas as pd

# Ruta al archivo CSV
file_path = './sample_data/supermarket_sales.csv'

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(file_path)

# Mostrar las primeras filas del DataFrame
print(df.head())

import pandas as pd

# Ruta del archivo CSV
file_path = './sample_data/supermarket_sales.csv'
# Cargar los datos
df = pd.read_csv(file_path)

# Revisar si hay valores nulos
print("Valores nulos en cada columna:\n", df.isnull().sum())

# Convertir la columna Date a formato datetime
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

# Extraer nuevas columnas útiles
df["Day"] = df["Date"].dt.day
df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year

# Extraer la hora de la columna Time
df["Hour"] = pd.to_datetime(df["Time"], format="%H:%M").dt.hour

# Renombrar columnas para evitar espacios
df.columns = df.columns.str.replace(" ", "_")

# Mostrar la estructura final de los datos
print("Primeras filas después de la transformación:")
print(df.head())

# Guardar el nuevo CSV limpio (opcional)
df.to_csv("./sample_data/supermarket_sales_cleaned.csv", index=False)


#NO EJECUTAR ESTE CODIGO ESTA CON EL PASS NO SOBRESCRIBIR



# Abrir un túnel en el puerto 8050
public_url = ngrok.connect(8050).public_url
print(f"✅ Dashboard disponible en: {public_url}")


#Si necesitas limpiar los puertos solo permite maximo 3


# Cerrar todos los túneles activos
for tunnel in ngrok.get_tunnels():
    ngrok.disconnect(tunnel.public_url)

    # volviendo a activar todo
    # Abrir un túnel en el puerto 8050
public_url = ngrok.connect(8050).public_url
print(f"✅ Dashboard disponible en: {public_url}")

print("✅ Todos los túneles de ngrok han sido cerrados. Ahora puedes iniciar uno nuevo.")
import pandas as pd
from dash import Dash, html, dcc, Output, Input, dash_table
import plotly.express as px
import dash_bootstrap_components as dbc  # Mover a una línea separada


# Cargar el archivo limpio
file_path = "./sample_data/supermarket_sales_cleaned.csv"
df = pd.read_csv(file_path)

# Inicializar la aplicación Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout mejorado con más análisis detallados
app.layout = html.Div([
    html.H1("Dashboard de Ventas del Supermercado", style={'textAlign': 'center'}),

    # Filtros para categoría de producto y sucursal
    dbc.Row([
        dbc.Col([
            html.Label("Selecciona una Categoría de Producto:"),
            dcc.Dropdown(
                id='product-line-dropdown',
                options=[{'label': line, 'value': line} for line in df["Product_line"].unique()],
                value=df["Product_line"].unique()[0]
            )
        ], width=6),

        dbc.Col([
            html.Label("Selecciona una Sucursal:"),
            dcc.Dropdown(
                id='branch-dropdown',
                options=[{'label': branch, 'value': branch} for branch in df["Branch"].unique()],
                value=df["Branch"].unique()[0]
            )
        ], width=6),
    ]),

    html.Hr(),

    # Métricas clave
    dbc.Row([
        dbc.Col(html.Div(id="total-sales"), width=4),
        dbc.Col(html.Div(id="average-sales"), width=4),
        dbc.Col(html.Div(id="total-transactions"), width=4)
    ], className="text-center"),

    html.Hr(),

    # Gráficos principales
    dcc.Graph(id='sales-time-series'),
    dcc.Graph(id='sales-hour-histogram'),
    dcc.Graph(id='scatter-unitprice-total'),
    dcc.Graph(id='payment-method-pie'),
    dcc.Graph(id='branch-sales-bar'),

    html.Hr(),

    # Nuevo: Análisis por tipo de cliente
    html.H3("Comparación de Ventas por Tipo de Cliente"),
    dcc.Graph(id='customer-type-sales'),

    html.Hr(),

    # Nuevo: Relación entre Rating y Total de Compra
    html.H3("Relación entre Calificación del Cliente y Total de Compra"),
    dcc.Graph(id='rating-vs-total'),

    html.Hr(),

    # Nuevo: Tabla de Datos Interactiva
    html.H3("Detalles de Ventas Filtradas"),
    dash_table.DataTable(
        id='sales-table',
        columns=[{"name": col, "id": col} for col in df.columns],
        page_size=10,
        style_table={'overflowX': 'auto'}
    )
])

# Callback para actualizar métricas clave
@app.callback(
    Output("total-sales", "children"),
    Output("average-sales", "children"),
    Output("total-transactions", "children"),
    [Input("product-line-dropdown", "value"),
     Input("branch-dropdown", "value")]
)
def update_metrics(selected_product, selected_branch):
    filtered_df = df[(df["Product_line"] == selected_product) & (df["Branch"] == selected_branch)]
    total_sales = filtered_df["Total"].sum()
    avg_sales = filtered_df["Total"].mean()
    total_transactions = len(filtered_df)

    return (
        html.H4(f"💰 Ventas Totales: ${total_sales:,.2f}"),
        html.H4(f"📊 Promedio de Venta: ${avg_sales:,.2f}"),
        html.H4(f"🛒 Total de Transacciones: {total_transactions}")
    )

# Callback para actualizar gráficos con los nuevos filtros
@app.callback(
    Output('sales-time-series', 'figure'),
    Output('sales-hour-histogram', 'figure'),
    Output('scatter-unitprice-total', 'figure'),
    Output('payment-method-pie', 'figure'),
    Output('branch-sales-bar', 'figure'),
    Output('customer-type-sales', 'figure'),
    Output('rating-vs-total', 'figure'),
    Output('sales-table', 'data'),
    [Input('product-line-dropdown', 'value'),
     Input('branch-dropdown', 'value')]
)
def update_graphs(selected_product, selected_branch):
    filtered_df = df[(df["Product_line"] == selected_product) & (df["Branch"] == selected_branch)]

    # Gráfico de barras (ventas por fecha)
    grouped_sales = filtered_df.groupby("Date", as_index=False).agg({"Total": "sum"})
    sales_fig = px.bar(grouped_sales, x="Date", y="Total", title=f"Ventas de {selected_product} en {selected_branch}")

    # Histograma de ventas por hora
    hour_hist_fig = px.histogram(filtered_df, x="Hour", nbins=24, title=f"Distribución de Ventas por Hora - {selected_product}")

    # Gráfico de dispersión entre Unit Price y Total
    scatter_fig = px.scatter(filtered_df, x="Unit_price", y="Total", title=f"Relación entre Precio Unitario y Total - {selected_product}")

    # Gráfico de pastel (método de pago)
    grouped_payment = filtered_df.groupby("Payment", as_index=False).agg({"Total": "sum"})
    payment_fig = px.pie(grouped_payment, names="Payment", values="Total", title=f"Métodos de Pago - {selected_product}")

    # Gráfico de ventas por sucursal
    grouped_branch = filtered_df.groupby("Branch", as_index=False).agg({"Total": "sum"})
    branch_fig = px.bar(grouped_branch, x="Branch", y="Total", title=f"Ventas Totales por Sucursal - {selected_product}")

    # Gráfico de ventas por tipo de cliente
    grouped_customer = filtered_df.groupby("Customer_type", as_index=False).agg({"Total": "sum"})
    customer_fig = px.bar(grouped_customer, x="Customer_type", y="Total", title=f"Comparación de Ventas por Tipo de Cliente")

    # Gráfico de dispersión entre Rating y Total de Compra
    rating_fig = px.scatter(filtered_df, x="Rating", y="Total", title="Relación entre Calificación del Cliente y Total de Compra")

    # Datos para la tabla
    table_data = filtered_df.to_dict("records")

    return sales_fig, hour_hist_fig, scatter_fig, payment_fig, branch_fig, customer_fig, rating_fig, table_data

# **Configurar ngrok para exponer el servidor**
public_url = ngrok.connect(8050).public_url
print(f"Dashboard disponible en: {public_url}")

# Ejecutar la aplicación en modo debug
app.run_server(mode="external")

