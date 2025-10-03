# 📘 Notebooks del Proyecto de Deep Learning (Resultados de Fútbol)

Este directorio contiene los notebooks reproducibles para el proyecto.

## 📂 Estructura

- **01-exploracion-datos.ipynb** → Exploración inicial del dataset (EDA).
- **02-preprocesado.ipynb** → Preprocesado del dataset y creación de arrays para deep learning (`X_seq.npy`, `X_static.npy`, `y.npy`).

## ▶️ Ejecución en Google Colab

1. Abre el notebook en Google Colab.  
2. Sube tu archivo `kaggle.json` (desde la pestaña lateral de Archivos en Colab).  
   - Se obtiene desde tu cuenta de Kaggle: *Cuenta → API → Create New API Token*.  
3. Ejecuta todas las celdas en orden.  

El notebook descargará automáticamente el dataset de Kaggle y generará los arrays necesarios para entrenar modelos **CNN, LSTM y Transformers**.

## 📊 Descripción de los `.npy`

- **X_seq.npy** → Secuencias temporales de diferencias de goles (últimos 5 partidos).  
- **X_static.npy** → Features estáticas de los equipos (home, away, país).  
- **y.npy** → Variable objetivo (0 = empate, 1 = gana local, 2 = gana visitante).  

Estos archivos quedan guardados en la carpeta `artifacts/` y se usan en los siguientes notebooks (Cap. 4 y 5).

---
