import os
import matplotlib.pyplot as plt
import string

STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "is", "it", "this", "that", "my",
    "el", "la", "los", "las", "un", "una", "de", "del", "a", "en", "y", "o", "que", "por", "con", "para", "es", "se"
}

def limpiar_palabra(palabra):
    # Limpiar puntuación básica y convertir a minúsculas
    return palabra.lower().strip(".,;:()[]{}\"'¡!¿?")

def menu_procesamiento_txt():
    while True:
        print("\n--- Submenú 1: Procesamiento de Textos (.txt) ---")
        print("1. Resumen Estadístico del Texto")
        print("2. Extracción de Patrones (Logs: ERROR, 404, etc.)")
        print("3. Gráfico 1 - Frecuencia de Palabras Clave (Barras horizontales)")
        print("4. Gráfico 2 - Distribución de Longitud de Líneas (Histograma)")
        print("5. Volver al Menú Principal")
        
        opcion = input("\nSeleccione una opción (1-5): ").strip()
        
        if opcion == "5":
            break
            
        if opcion in ["1", "2", "3", "4"]:
            ruta = input("Ingrese la ruta del archivo .txt: ").strip()
            if not os.path.exists(ruta):
                print("[Error] El archivo no existe. Verifique la ruta.")
                continue
                
            try:
                with open(ruta, 'r', encoding='utf-8') as f:
                    lineas = f.readlines()
            except Exception as e:
                print(f"[Error] No se pudo abrir el archivo: {e}")
                continue
                
            if opcion == "1":
                total_lineas = len(lineas)
                total_caracteres_con = sum(len(l) for l in lineas)
                total_caracteres_sin = sum(len(l.replace(" ", "").replace("\n", "")) for l in lineas)
                
                palabras_totales = []
                for linea in lineas:
                    palabras_totales.extend([limpiar_palabra(p) for p in linea.split() if limpiar_palabra(p)])
                
                # Filtrar stopwords
                palabras_filtradas = [p for p in palabras_totales if p not in STOPWORDS and len(p) > 1]
                
                # Top 5
                frecuencias = {}
                for p in palabras_filtradas:
                    frecuencias[p] = frecuencias.get(p, 0) + 1
                top_5 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:5]
                
                print("\n=== RESUMEN ESTADÍSTICO DEL TEXTO ===")
                print(f"Total de líneas: {total_lineas}")
                print(f"Total de palabras: {len(palabras_totales)}")
                print(f"Total de caracteres (con espacios): {total_caracteres_con}")
                print(f"Total de caracteres (sin espacios): {total_caracteres_sin}")
                print("Top 5 de palabras más repetidas:")
                for palabra, freq in top_5:
                    print(f" - {palabra}: {freq} veces")
                    
            elif opcion == "2":
                patrones = ["ERROR", "404", "WARNING", "FAIL", "Exception"]
                conteo_patrones = {p: 0 for p in patrones}
                
                for linea in lineas:
                    for p in patrones:
                        if p in linea:
                            conteo_patrones[p] += 1
                            
                print("\n=== EXTRACCIÓN DE PATRONES ===")
                for p, count in conteo_patrones.items():
                    print(f"Coincidencias de '{p}': {count}")
                    
            elif opcion == "3":
                palabras_totales = []
                for linea in lineas:
                    palabras_totales.extend([limpiar_palabra(p) for p in linea.split() if limpiar_palabra(p)])
                palabras_filtradas = [p for p in palabras_totales if p not in STOPWORDS and len(p) > 2]
                
                frecuencias = {}
                for p in palabras_filtradas:
                    frecuencias[p] = frecuencias.get(p, 0) + 1
                top_10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:10]
                
                if not top_10:
                    print("No hay suficientes palabras para generar el gráfico.")
                    continue
                    
                palabras = [x[0] for x in top_10][::-1]
                valores = [x[1] for x in top_10][::-1]
                
                plt.figure(figsize=(10, 6))
                plt.barh(palabras, valores, color='skyblue')
                plt.xlabel("Frecuencia")
                plt.ylabel("Palabras Clave")
                plt.title("Frecuencia de Palabras Clave")
                plt.tight_layout()
                
                os.makedirs("outputs", exist_ok=True)
                ruta_salida = "outputs/gráfico_frecuencia_palabras.png"
                plt.savefig(ruta_salida)
                plt.show()
                plt.close()
                print(f"\n[Éxito] Gráfico guardado en '{ruta_salida}'")
                
            elif opcion == "4":
                longitudes = [len(l.strip()) for l in lineas if l.strip()]
                
                plt.figure(figsize=(10, 6))
                plt.hist(longitudes, bins=[0, 50, 100, 150, 200, 300, 500], color='salmon', edgecolor='black')
                plt.xlabel("Longitud de Línea (Caracteres)")
                plt.ylabel("Frecuencia")
                plt.title("Distribución de Longitud de Líneas")
                plt.tight_layout()
                
                os.makedirs("outputs", exist_ok=True)
                ruta_salida = "outputs/gráfico_longitud_lineas.png"
                plt.savefig(ruta_salida)
                plt.show()
                plt.close()
                print(f"\n[Éxito] Gráfico guardado en '{ruta_salida}'")
        else:
            print("[Opción inválida] Intente de nuevo.")