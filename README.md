# Predicción de Resultados en Fútbol Internacional con Deep Learning

Este proyecto aplica técnicas de **aprendizaje profundo (CNN, RNN, Transformers)** para predecir el resultado de partidos internacionales de fútbol (1872–2017), usando el dataset de Kaggle: [International football results](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017).

## 📌 Estructura del repositorio

- **notebooks/**  
  - `01-exploracion-datos.ipynb`: Análisis exploratorio inicial (EDA).  
  - `02-preprocesado.ipynb`: Limpieza, encoding, creación de features secuenciales y estáticos.  
  - `03_arquitectura_de_linea_de_base.ipynb`: Modelo baseline (logística o red simple).  
  - `04-CNN.ipynb`: Modelos convolucionales sobre secuencias.  
  - `05-RNN-LSTM.ipynb`: Redes recurrentes (LSTM/GRU, bidireccionales).  
  - `06-Transformers.ipynb`: Modelos avanzados basados en atención.  
  - `07-resultados-finales.ipynb`: Comparativa de modelos y resultados.

- **reports/**  
  - `ENTREGA1.pdf`: Informe inicial (máx. 3 páginas, IEEE).  
  - `INFORME_PROYECTO.pdf`: Informe final (5-10 páginas).  

- **src/**  
  Código auxiliar para funciones de preprocesamiento y métricas personalizadas.  

- **models/**  
  Modelos entrenados (ej. `trained_model.h5`).  

## 🚀 Ejecución en Google Colab
Todos los notebooks están preparados para ejecutarse en Google Colab. Solo se requiere montar Google Drive o descargar el dataset desde Kaggle.

Instalación de dependencias:
```bash
pip install -r requirements.txt


📊 Métricas

Accuracy

F1-score macro

Matriz de confusión

🎥 Video de Presentación

YouTube - Explicación del proyecto