{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OYSkmn_W9UT4"
      },
      "source": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Pu8zw_7a9Yzk"
      },
      "source": [
        "Estimados  Alumnos,\n",
        "El trabajo final del curso consiste en generar:\n",
        "- DashBoard Interactivo con Biblioteca DASH de python.\n",
        "\n",
        "\n",
        "Caracteristicas del Dashboard.\n",
        "Cargar datos de un archivo CSV\n",
        "\n",
        "Selección de columnas numéricas para visualización.\n",
        "\n",
        "Gráfico de dispersión interactivo usando Plotly\n",
        "\n",
        "Actualización dinámica según la selección del usuario\n",
        "\n",
        "\n",
        "CÓDIGO:\n",
        "\n",
        "Importar librerías\n",
        "\n",
        "Inicializar la aplicacion\n",
        "\n",
        "Layout del dashboard\n",
        "\n",
        "html\n",
        "\n",
        "dcc\n",
        "\n",
        "Callback\n",
        "\n",
        "Output\n",
        "\n",
        "Input\n",
        "\n",
        "Metodo update_graph\n",
        "\n",
        "Ejecución del servidor\n",
        "\n",
        "\n",
        "\n",
        "import plotly.express as px\n",
        "\n",
        "data_g =  px.data.gapminder()\n",
        "\n",
        "gapminder_2018 = data_g.query(“year==2018”)\n",
        "\n",
        "\n",
        "# Este trabajo va a ser u script en python\n",
        "\n",
        "\n",
        "dash_app.py\n",
        "\n",
        "\n",
        "Fecha de Entrega: Lunes 10 de Febrero 22:00pm"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "k5zHMsVskHh6",
        "outputId": "52ef0da2-f7a2-4eb9-c4e0-65361122c773"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Warning: Looks like you're using an outdated `kagglehub` version (installed: 0.3.6), please consider upgrading to the latest version (0.3.7).\n",
            "Path to dataset files: /root/.cache/kagglehub/datasets/hosammhmdali/supermarket-sales/versions/1\n"
          ]
        }
      ],
      "source": [
        "#import kagglehub\n",
        "\n",
        "# Download latest version\n",
        "#path = kagglehub.dataset_download(\"hosammhmdali/supermarket-sales\")\n",
        "\n",
        "#print(\"Path to dataset files:\", path)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W38z7ku29Tbv",
        "outputId": "cd5d2d73-094e-4f85-8542-b60cd228c169"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "    Invoice ID Branch       City Customer type  Gender  \\\n",
            "0  750-67-8428      A     Yangon        Member  Female   \n",
            "1  226-31-3081      C  Naypyitaw        Normal  Female   \n",
            "2  631-41-3108      A     Yangon        Normal    Male   \n",
            "3  123-19-1176      A     Yangon        Member    Male   \n",
            "4  373-73-7910      A     Yangon        Normal    Male   \n",
            "\n",
            "             Product line  Unit price  Quantity   Tax 5%     Total       Date  \\\n",
            "0       Health and beauty       74.69         7  26.1415  548.9715   1/5/2019   \n",
            "1  Electronic accessories       15.28         5   3.8200   80.2200   3/8/2019   \n",
            "2      Home and lifestyle       46.33         7  16.2155  340.5255   3/3/2019   \n",
            "3       Health and beauty       58.22         8  23.2880  489.0480  1/27/2019   \n",
            "4       Sports and travel       86.31         7  30.2085  634.3785   2/8/2019   \n",
            "\n",
            "    Time      Payment    cogs  gross margin percentage  gross income  Rating  \n",
            "0  13:08      Ewallet  522.83                 4.761905       26.1415     9.1  \n",
            "1  10:29         Cash   76.40                 4.761905        3.8200     9.6  \n",
            "2  13:23  Credit card  324.31                 4.761905       16.2155     7.4  \n",
            "3  20:33      Ewallet  465.76                 4.761905       23.2880     8.4  \n",
            "4  10:37      Ewallet  604.17                 4.761905       30.2085     5.3  \n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "\n",
        "# Ruta al archivo CSV\n",
        "file_path = './sample_data/supermarket_sales.csv'\n",
        "\n",
        "# Cargar el archivo CSV en un DataFrame\n",
        "df = pd.read_csv(file_path)\n",
        "\n",
        "# Mostrar las primeras filas del DataFrame\n",
        "print(df.head())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4uRM3qzvE-7X",
        "outputId": "25d6c50a-d3ae-437c-9d3c-0597860e5b12"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Valores nulos en cada columna:\n",
            " Invoice ID                 0\n",
            "Branch                     0\n",
            "City                       0\n",
            "Customer type              0\n",
            "Gender                     0\n",
            "Product line               0\n",
            "Unit price                 0\n",
            "Quantity                   0\n",
            "Tax 5%                     0\n",
            "Total                      0\n",
            "Date                       0\n",
            "Time                       0\n",
            "Payment                    0\n",
            "cogs                       0\n",
            "gross margin percentage    0\n",
            "gross income               0\n",
            "Rating                     0\n",
            "dtype: int64\n",
            "Primeras filas después de la transformación:\n",
            "    Invoice_ID Branch       City Customer_type  Gender  \\\n",
            "0  750-67-8428      A     Yangon        Member  Female   \n",
            "1  226-31-3081      C  Naypyitaw        Normal  Female   \n",
            "2  631-41-3108      A     Yangon        Normal    Male   \n",
            "3  123-19-1176      A     Yangon        Member    Male   \n",
            "4  373-73-7910      A     Yangon        Normal    Male   \n",
            "\n",
            "             Product_line  Unit_price  Quantity   Tax_5%     Total  ...  \\\n",
            "0       Health and beauty       74.69         7  26.1415  548.9715  ...   \n",
            "1  Electronic accessories       15.28         5   3.8200   80.2200  ...   \n",
            "2      Home and lifestyle       46.33         7  16.2155  340.5255  ...   \n",
            "3       Health and beauty       58.22         8  23.2880  489.0480  ...   \n",
            "4       Sports and travel       86.31         7  30.2085  634.3785  ...   \n",
            "\n",
            "    Time      Payment    cogs  gross_margin_percentage  gross_income  Rating  \\\n",
            "0  13:08      Ewallet  522.83                 4.761905       26.1415     9.1   \n",
            "1  10:29         Cash   76.40                 4.761905        3.8200     9.6   \n",
            "2  13:23  Credit card  324.31                 4.761905       16.2155     7.4   \n",
            "3  20:33      Ewallet  465.76                 4.761905       23.2880     8.4   \n",
            "4  10:37      Ewallet  604.17                 4.761905       30.2085     5.3   \n",
            "\n",
            "   Day  Month  Year  Hour  \n",
            "0    5      1  2019    13  \n",
            "1    8      3  2019    10  \n",
            "2    3      3  2019    13  \n",
            "3   27      1  2019    20  \n",
            "4    8      2  2019    10  \n",
            "\n",
            "[5 rows x 21 columns]\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "\n",
        "# Ruta del archivo CSV\n",
        "file_path = './sample_data/supermarket_sales.csv'\n",
        "# Cargar los datos\n",
        "df = pd.read_csv(file_path)\n",
        "\n",
        "# Revisar si hay valores nulos\n",
        "print(\"Valores nulos en cada columna:\\n\", df.isnull().sum())\n",
        "\n",
        "# Convertir la columna Date a formato datetime\n",
        "df[\"Date\"] = pd.to_datetime(df[\"Date\"], format=\"%m/%d/%Y\")\n",
        "\n",
        "# Extraer nuevas columnas útiles\n",
        "df[\"Day\"] = df[\"Date\"].dt.day\n",
        "df[\"Month\"] = df[\"Date\"].dt.month\n",
        "df[\"Year\"] = df[\"Date\"].dt.year\n",
        "\n",
        "# Extraer la hora de la columna Time\n",
        "df[\"Hour\"] = pd.to_datetime(df[\"Time\"], format=\"%H:%M\").dt.hour\n",
        "\n",
        "# Renombrar columnas para evitar espacios\n",
        "df.columns = df.columns.str.replace(\" \", \"_\")\n",
        "\n",
        "# Mostrar la estructura final de los datos\n",
        "print(\"Primeras filas después de la transformación:\")\n",
        "print(df.head())\n",
        "\n",
        "# Guardar el nuevo CSV limpio (opcional)\n",
        "df.to_csv(\"./sample_data/supermarket_sales_cleaned.csv\", index=False)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Gl6d44WaA5tD"
      },
      "source": [
        "# COLOCANDO NGROK PARA MSOTRAR DATOS"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "jnRDW_g75gT0"
      },
      "outputs": [],
      "source": [
        "!pip install dash plotly pandas dash-bootstrap-components pyngrok"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZTuU7QPe3o21",
        "outputId": "6e0e8bdf-f3a1-4c52-b802-541631abc635"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: pyngrok in /usr/local/lib/python3.11/dist-packages (7.2.3)\n",
            "Requirement already satisfied: PyYAML>=5.1 in /usr/local/lib/python3.11/dist-packages (from pyngrok) (6.0.2)\n",
            "Authtoken saved to configuration file: /root/.config/ngrok/ngrok.yml\n"
          ]
        }
      ],
      "source": [
        "!pip install pyngrok\n",
        "!ngrok authtoken 2sp7CTFcCQf1h78MSM8vuEV7BlY_7nZPaN5G3PMg3PZpAKHbP\n",
        "#NO EJECUTAR ESTE CODIGO ESTA CON EL PASS NO SOBRESCRIBIR"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 27,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MOvTxhsn3r63",
        "outputId": "66f3a708-7e48-4f9f-adc9-debbbb06610b"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "✅ Dashboard disponible en: https://a83d-34-106-0-71.ngrok-free.app\n"
          ]
        }
      ],
      "source": [
        "from pyngrok import ngrok\n",
        "\n",
        "# Abrir un túnel en el puerto 8050\n",
        "public_url = ngrok.connect(8050).public_url\n",
        "print(f\"✅ Dashboard disponible en: {public_url}\")\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 32,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uTDUE26a_VGA",
        "outputId": "76fcae9c-405a-4ff1-c3f2-5aebd4377662"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "WARNING:pyngrok.process.ngrok:t=2025-02-09T23:13:44+0000 lvl=warn msg=\"Stopping forwarder\" name=http-8050-205e35d5-7427-4c5a-8915-cd36dc505994 acceptErr=\"failed to accept connection: Listener closed\"\n",
            "WARNING:pyngrok.process.ngrok:t=2025-02-09T23:13:44+0000 lvl=warn msg=\"Stopping forwarder\" name=http-8050-68ff372e-da95-4e5d-b4ed-1c63f834ab91 acceptErr=\"failed to accept connection: Listener closed\"\n",
            "WARNING:pyngrok.process.ngrok:t=2025-02-09T23:13:44+0000 lvl=warn msg=\"Stopping forwarder\" name=http-8050-5bd56c72-356e-4afc-af49-e15b5c37093c acceptErr=\"failed to accept connection: Listener closed\"\n"
          ]
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "✅ Dashboard disponible en: https://aa54-34-106-0-71.ngrok-free.app\n",
            "✅ Todos los túneles de ngrok han sido cerrados. Ahora puedes iniciar uno nuevo.\n"
          ]
        }
      ],
      "source": [
        "#Si necesitas limpiar los puertos solo permite maximo 3\n",
        "\n",
        "from pyngrok import ngrok\n",
        "\n",
        "# Cerrar todos los túneles activos\n",
        "for tunnel in ngrok.get_tunnels():\n",
        "    ngrok.disconnect(tunnel.public_url)\n",
        "\n",
        "    # volviendo a activar todo\n",
        "    # Abrir un túnel en el puerto 8050\n",
        "public_url = ngrok.connect(8050).public_url\n",
        "print(f\"✅ Dashboard disponible en: {public_url}\")\n",
        "\n",
        "print(\"✅ Todos los túneles de ngrok han sido cerrados. Ahora puedes iniciar uno nuevo.\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 33,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 688
        },
        "id": "mMlWv42DBmRO",
        "outputId": "fe2e7606-2265-42c0-a355-35fde9f46f15"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Dashboard disponible en: https://6b07-34-106-0-71.ngrok-free.app\n"
          ]
        },
        {
          "data": {
            "application/javascript": "(async (port, path, width, height, cache, element) => {\n    if (!google.colab.kernel.accessAllowed && !cache) {\n      return;\n    }\n    element.appendChild(document.createTextNode(''));\n    const url = await google.colab.kernel.proxyPort(port, {cache});\n    const iframe = document.createElement('iframe');\n    iframe.src = new URL(path, url).toString();\n    iframe.height = height;\n    iframe.width = width;\n    iframe.style.border = 0;\n    iframe.allow = [\n        'accelerometer',\n        'autoplay',\n        'camera',\n        'clipboard-read',\n        'clipboard-write',\n        'gyroscope',\n        'magnetometer',\n        'microphone',\n        'serial',\n        'usb',\n        'xr-spatial-tracking',\n    ].join('; ');\n    element.appendChild(iframe);\n  })(8050, \"/\", \"100%\", 650, false, window.element)",
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "import pandas as pd\n",
        "from dash import Dash, html, dcc, Output, Input, dash_table\n",
        "import plotly.express as px\n",
        "from pyngrok import ngrok\n",
        "import dash_bootstrap_components as dbc\n",
        "\n",
        "# Cargar el archivo limpio\n",
        "file_path = \"./sample_data/supermarket_sales_cleaned.csv\"\n",
        "df = pd.read_csv(file_path)\n",
        "\n",
        "# Inicializar la aplicación Dash\n",
        "app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])\n",
        "\n",
        "# Layout mejorado con más análisis detallados\n",
        "app.layout = html.Div([\n",
        "    html.H1(\"Dashboard de Ventas del Supermercado\", style={'textAlign': 'center'}),\n",
        "\n",
        "    # Filtros para categoría de producto y sucursal\n",
        "    dbc.Row([\n",
        "        dbc.Col([\n",
        "            html.Label(\"Selecciona una Categoría de Producto:\"),\n",
        "            dcc.Dropdown(\n",
        "                id='product-line-dropdown',\n",
        "                options=[{'label': line, 'value': line} for line in df[\"Product_line\"].unique()],\n",
        "                value=df[\"Product_line\"].unique()[0]\n",
        "            )\n",
        "        ], width=6),\n",
        "\n",
        "        dbc.Col([\n",
        "            html.Label(\"Selecciona una Sucursal:\"),\n",
        "            dcc.Dropdown(\n",
        "                id='branch-dropdown',\n",
        "                options=[{'label': branch, 'value': branch} for branch in df[\"Branch\"].unique()],\n",
        "                value=df[\"Branch\"].unique()[0]\n",
        "            )\n",
        "        ], width=6),\n",
        "    ]),\n",
        "\n",
        "    html.Hr(),\n",
        "\n",
        "    # Métricas clave\n",
        "    dbc.Row([\n",
        "        dbc.Col(html.Div(id=\"total-sales\"), width=4),\n",
        "        dbc.Col(html.Div(id=\"average-sales\"), width=4),\n",
        "        dbc.Col(html.Div(id=\"total-transactions\"), width=4)\n",
        "    ], className=\"text-center\"),\n",
        "\n",
        "    html.Hr(),\n",
        "\n",
        "    # Gráficos principales\n",
        "    dcc.Graph(id='sales-time-series'),\n",
        "    dcc.Graph(id='sales-hour-histogram'),\n",
        "    dcc.Graph(id='scatter-unitprice-total'),\n",
        "    dcc.Graph(id='payment-method-pie'),\n",
        "    dcc.Graph(id='branch-sales-bar'),\n",
        "\n",
        "    html.Hr(),\n",
        "\n",
        "    # Nuevo: Análisis por tipo de cliente\n",
        "    html.H3(\"Comparación de Ventas por Tipo de Cliente\"),\n",
        "    dcc.Graph(id='customer-type-sales'),\n",
        "\n",
        "    html.Hr(),\n",
        "\n",
        "    # Nuevo: Relación entre Rating y Total de Compra\n",
        "    html.H3(\"Relación entre Calificación del Cliente y Total de Compra\"),\n",
        "    dcc.Graph(id='rating-vs-total'),\n",
        "\n",
        "    html.Hr(),\n",
        "\n",
        "    # Nuevo: Tabla de Datos Interactiva\n",
        "    html.H3(\"Detalles de Ventas Filtradas\"),\n",
        "    dash_table.DataTable(\n",
        "        id='sales-table',\n",
        "        columns=[{\"name\": col, \"id\": col} for col in df.columns],\n",
        "        page_size=10,\n",
        "        style_table={'overflowX': 'auto'}\n",
        "    )\n",
        "])\n",
        "\n",
        "# Callback para actualizar métricas clave\n",
        "@app.callback(\n",
        "    Output(\"total-sales\", \"children\"),\n",
        "    Output(\"average-sales\", \"children\"),\n",
        "    Output(\"total-transactions\", \"children\"),\n",
        "    [Input(\"product-line-dropdown\", \"value\"),\n",
        "     Input(\"branch-dropdown\", \"value\")]\n",
        ")\n",
        "def update_metrics(selected_product, selected_branch):\n",
        "    filtered_df = df[(df[\"Product_line\"] == selected_product) & (df[\"Branch\"] == selected_branch)]\n",
        "    total_sales = filtered_df[\"Total\"].sum()\n",
        "    avg_sales = filtered_df[\"Total\"].mean()\n",
        "    total_transactions = len(filtered_df)\n",
        "\n",
        "    return (\n",
        "        html.H4(f\"💰 Ventas Totales: ${total_sales:,.2f}\"),\n",
        "        html.H4(f\"📊 Promedio de Venta: ${avg_sales:,.2f}\"),\n",
        "        html.H4(f\"🛒 Total de Transacciones: {total_transactions}\")\n",
        "    )\n",
        "\n",
        "# Callback para actualizar gráficos con los nuevos filtros\n",
        "@app.callback(\n",
        "    Output('sales-time-series', 'figure'),\n",
        "    Output('sales-hour-histogram', 'figure'),\n",
        "    Output('scatter-unitprice-total', 'figure'),\n",
        "    Output('payment-method-pie', 'figure'),\n",
        "    Output('branch-sales-bar', 'figure'),\n",
        "    Output('customer-type-sales', 'figure'),\n",
        "    Output('rating-vs-total', 'figure'),\n",
        "    Output('sales-table', 'data'),\n",
        "    [Input('product-line-dropdown', 'value'),\n",
        "     Input('branch-dropdown', 'value')]\n",
        ")\n",
        "def update_graphs(selected_product, selected_branch):\n",
        "    filtered_df = df[(df[\"Product_line\"] == selected_product) & (df[\"Branch\"] == selected_branch)]\n",
        "\n",
        "    # Gráfico de barras (ventas por fecha)\n",
        "    grouped_sales = filtered_df.groupby(\"Date\", as_index=False).agg({\"Total\": \"sum\"})\n",
        "    sales_fig = px.bar(grouped_sales, x=\"Date\", y=\"Total\", title=f\"Ventas de {selected_product} en {selected_branch}\")\n",
        "\n",
        "    # Histograma de ventas por hora\n",
        "    hour_hist_fig = px.histogram(filtered_df, x=\"Hour\", nbins=24, title=f\"Distribución de Ventas por Hora - {selected_product}\")\n",
        "\n",
        "    # Gráfico de dispersión entre Unit Price y Total\n",
        "    scatter_fig = px.scatter(filtered_df, x=\"Unit_price\", y=\"Total\", title=f\"Relación entre Precio Unitario y Total - {selected_product}\")\n",
        "\n",
        "    # Gráfico de pastel (método de pago)\n",
        "    grouped_payment = filtered_df.groupby(\"Payment\", as_index=False).agg({\"Total\": \"sum\"})\n",
        "    payment_fig = px.pie(grouped_payment, names=\"Payment\", values=\"Total\", title=f\"Métodos de Pago - {selected_product}\")\n",
        "\n",
        "    # Gráfico de ventas por sucursal\n",
        "    grouped_branch = filtered_df.groupby(\"Branch\", as_index=False).agg({\"Total\": \"sum\"})\n",
        "    branch_fig = px.bar(grouped_branch, x=\"Branch\", y=\"Total\", title=f\"Ventas Totales por Sucursal - {selected_product}\")\n",
        "\n",
        "    # Gráfico de ventas por tipo de cliente\n",
        "    grouped_customer = filtered_df.groupby(\"Customer_type\", as_index=False).agg({\"Total\": \"sum\"})\n",
        "    customer_fig = px.bar(grouped_customer, x=\"Customer_type\", y=\"Total\", title=f\"Comparación de Ventas por Tipo de Cliente\")\n",
        "\n",
        "    # Gráfico de dispersión entre Rating y Total de Compra\n",
        "    rating_fig = px.scatter(filtered_df, x=\"Rating\", y=\"Total\", title=\"Relación entre Calificación del Cliente y Total de Compra\")\n",
        "\n",
        "    # Datos para la tabla\n",
        "    table_data = filtered_df.to_dict(\"records\")\n",
        "\n",
        "    return sales_fig, hour_hist_fig, scatter_fig, payment_fig, branch_fig, customer_fig, rating_fig, table_data\n",
        "\n",
        "# **Configurar ngrok para exponer el servidor**\n",
        "public_url = ngrok.connect(8050).public_url\n",
        "print(f\"Dashboard disponible en: {public_url}\")\n",
        "\n",
        "# Ejecutar la aplicación en modo debug\n",
        "app.run_server(mode=\"external\")\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
