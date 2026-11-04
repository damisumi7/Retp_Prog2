# CLI en Python: Análisis de Textos y Datos 📊

Este repositorio reúne una solución práctica en Python para organizar, procesar y analizar tanto textos como conjuntos de datos desde la terminal. La idea principal fue construir una aplicación de consola (CLI) modular y limpia, capaz de lidiar con problemas del día a día —como archivos que no aparecen o carpetas faltantes— sin que el programa se caiga de repente. 

Todo está estructurado en un menú interactivo fácil de usar que se encarga de procesar desde contenido literario hasta registros de servidores y datasets industriales, generando gráficos profesionales con `matplotlib` de manera automática.

---

## 📂 ¿Cómo está organizado el código?

Para evitar tener un archivo gigante e imposible de leer, el proyecto se divide en tres componentes clave y un par de carpetas de soporte:

* **`main.py`**: Es el punto de partida. Muestra el menú interactivo en la consola, recibe tus comandos y conecta lo que pides con la parte del código que se encarga de resolverlo.
* **`procesamiento_txt.py`**: Aquí vive toda la lógica para leer archivos de texto plano, contar palabras y líneas, filtrar conectores comunes, armar un Top 5 de frecuencias y buscar patrones o errores específicos en bitácoras.
* **`analisis_csv.py`**: Se encarga de leer los archivos tabulares, calcular estadísticas descriptivas (como promedios, medianas, mínimos y máximos) y levantar los gráficos de líneas, dispersión y pastel.

### Directorios del sistema:
* **`/data`**: Es el espacio donde debes colocar los archivos que quieras analizar.
* **`/outputs`**: No tienes que preocuparte por crearla; el código la genera automáticamente en cuanto exportas tu primer gráfico.

---

## 🚀 ¿Cómo ponerlo a funcionar en tu computadora?

Poner en marcha el proyecto es bastante sencillo si sigues estos pasos:

1. Asegúrate de tener instalado **Python 3.x**.
2. Guarda los archivos de prueba que quieras analizar dentro de la carpeta `/data`.
3. Abre tu terminal en la carpeta principal del proyecto y corre el programa:

   ```bash
   python main.py

## 📚 ¿De dónde sacamos los datos para las pruebas?

Para que el sistema analizara información real y con sentido, utilizamos archivos de dominio público:

1. **El texto literario (`Impostor.txt`):**
   * *Qué es:* Una copia en texto plano de la revista de poesía *Impostor: A Poetry Journal (Volume 4, Issue 1)*. Lo usamos para probar el conteo de palabras y las estadísticas de texto.
   * *Fuente:* [Internet Archive - Impostor Issue 4.1](https://archive.org/details/impostor-4-1/page/18/mode/2up)

2. **El dataset de mantenimiento (`errors.csv`):**
   * *Qué es:* Un archivo con miles de registros sobre fallas y mantenimientos en equipos industriales. Es perfecto para probar las estadísticas y los gráficos de tendencias.
   * *Fuente:* GitHub - DeeptiChevvuri / Predictive-Maintenance-Modelling-Datasets

3. **El archivo de bitácora (`sample-log.txt`):**
   * *Qué es:* Un registro de servidor real (`log`) lleno de trazas de actividad, advertencias y errores (`INFO`, `WARNING`, `ERROR`, `404`). Lo usamos para probar la búsqueda rápida de patrones.
   * *Fuente:* GitHub - ryuneeee / logbackCustomAppender