import os
import csv
import matplotlib.pyplot as plt

def leer_csv(ruta):
    filas = []
    with open(ruta, mode='r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            filas.append(fila)
    return filas

def menu_analisis_csv():
    while True:
        print("\n--- Submenú 2: Análisis de Datasets (.csv) ---")
        print("1. Vista Previa de Datos (primeras 10 y últimas 5 filas)")
        print("2. Cálculo de Estadísticas Descriptivas (Columna numérica)")
        print("3. Gráfico 3 - Evolución Temporal / Tendencia (Líneas)")
        print("4. Gráfico 4 - Comparación Categórica (Pastel)")
        print("5. Gráfico 5 - Correlación de Variables (Dispersión)")
        print("6. Volver al Menú Principal")
        
        opcion = input("\nSeleccione una opción (1-6): ").strip()
        
        if opcion == "6":
            break
            
        if opcion in ["1", "2", "3", "4", "5"]:
            ruta = input("Ingrese la ruta del archivo .csv: ").strip()
            if not os.path.exists(ruta):
                print("[Error] El archivo CSV no existe.")
                continue
                
            try:
                datos = leer_csv(ruta)
            except Exception as e:
                print(f"[Error] No se pudo leer el archivo CSV: {e}")
                continue
                
            if len(datos) < 2:
                print("[Error] El archivo CSV está vacío o no tiene cabecera.")
                continue
                
            cabecera = datos[0]
            filas = datos[1:]
            
            if opcion == "1":
                print("\n=== VISTA PREVIA DE DATOS ===")
                print(f"Cabecera: {cabecera}")
                print("\nPrimeras 10 filas:")
                for f in filas[:10]:
                    print(f)
                print("\nÚltimas 5 filas:")
                for f in filas[-5:]:
                    print(f)
                    
            elif opcion == "2":
                print(f"\nColumnas disponibles: {list(enumerate(cabecera))}")
                try:
                    col_idx = int(input("Ingrese el número de la columna numérica a analizar: "))
                    # Limpiar y convertir datos válidos
                    valores = []
                    for f in filas:
                        if len(f) > col_idx and f[col_idx].strip() != "":
                            try:
                                valores.append(float(f[col_idx]))
                            except ValueError:
                                pass # Ignorar valores no numéricos
                                
                    if not valores:
                        print("[Error] No se encontraron valores numéricos válidos en esta columna.")
                        continue
                        
                    valores.sort()
                    total_validos = len(valores)
                    promedio = sum(valores) / total_validos
                    minimo = valores[0]
                    maximo = valores[-1]
                    
                    if total_validos % 2 == 1:
                        mediana = valores[total_validos // 2]
                    else:
                        mediana = (valores[(total_validos // 2) - 1] + valores[total_validos // 2]) / 2
                        
                    print(f"\n=== ESTADÍSTICAS DESCRIPTIVAS ({cabecera[col_idx]}) ===")
                    print(f"Registros válidos: {total_validos}")
                    print(f"Promedio: {promedio:.2f}")
                    print(f"Mediana: {mediana:.2f}")
                    print(f"Valor Mínimo: {minimo}")
                    print(f"Valor Máximo: {maximo}")
                except Exception as e:
                    print(f"[Error] Entrada inválida: {e}")
                    
            elif opcion == "3":
                print(f"\nColumnas disponibles: {list(enumerate(cabecera))}")
                try:
                    idx_x = int(input("Ingrese el índice de la columna de Fechas / Eje X: "))
                    idx_y = int(input("Ingrese el índice de la columna numérica / Eje Y: "))
                    
                    eje_x, eje_y = [], []
                    for f in filas:
                        if len(f) > max(idx_x, idx_y) and f[idx_x].strip() and f[idx_y].strip():
                            eje_x.append(f[idx_x])
                            try:
                                eje_y.append(float(f[idx_y]))
                            except ValueError:
                                eje_x.pop() # mantener alineación
                                
                    plt.figure(figsize=(12, 6))
                    plt.plot(eje_x, eje_y, marker='o', color='purple', linestyle='-')
                    plt.xlabel(cabecera[idx_x])
                    plt.ylabel(cabecera[idx_y])
                    plt.title(f"Evolución Temporal: {cabecera[idx_y]} vs {cabecera[idx_x]}")
                    plt.xticks(rotation=45, ha='right')
                    plt.tight_layout()
                    
                    os.makedirs("outputs", exist_ok=True)
                    ruta_salida = "outputs/gráfico_evolucion_temporal.png"
                    plt.savefig(ruta_salida)
                    plt.show()
                    plt.close()
                    print(f"\n[Éxito] Gráfico guardado en '{ruta_salida}'")
                except Exception as e:
                    print(f"[Error] Ocurrió un error generando el gráfico: {e}")
                    
            elif opcion == "4":
                print(f"\nColumnas disponibles: {list(enumerate(cabecera))}")
                try:
                    col_idx = int(input("Ingrese el índice de la columna categórica (ej. Ciudad o Categoría): "))
                    conteo_cat = {}
                    for f in filas:
                        if len(f) > col_idx and f[col_idx].strip():
                            cat = f[col_idx].strip()
                            conteo_cat[cat] = conteo_cat.get(cat, 0) + 1
                            
                    categorias = list(conteo_cat.keys())
                    cantidades = list(conteo_cat.values())
                    
                    plt.figure(figsize=(8, 8))
                    plt.pie(cantidades, labels=categorias, autopct='%1.1f%%', startangle=140)
                    plt.title(f"Comparación Categórica: {cabecera[col_idx]}")
                    plt.tight_layout()
                    
                    os.makedirs("outputs", exist_ok=True)
                    ruta_salida = "outputs/gráfico_comparacion_categorica.png"
                    plt.savefig(ruta_salida)
                    plt.show()
                    plt.close()
                    print(f"\n[Éxito] Gráfico guardado en '{ruta_salida}'")
                except Exception as e:
                    print(f"[Error] Ocurrió un error generando el gráfico: {e}")
                    
            elif opcion == "5":
                print(f"\nColumnas disponibles: {list(enumerate(cabecera))}")
                try:
                    idx_x = int(input("Ingrese el índice de la primera columna numérica (Eje X): "))
                    idx_y = int(input("Ingrese el índice de la segunda columna numérica (Eje Y): "))
                    
                    x_vals, y_vals = [], []
                    for f in filas:
                        if len(f) > max(idx_x, idx_y):
                            try:
                                x_vals.append(float(f[idx_x]))
                                y_vals.append(float(f[idx_y]))
                            except ValueError:
                                pass
                                
                    plt.figure(figsize=(10, 6))
                    plt.scatter(x_vals, y_vals, color='teal', alpha=0.7)
                    plt.xlabel(cabecera[idx_x])
                    plt.ylabel(cabecera[idx_y])
                    plt.title(f"Correlación: {cabecera[idx_y]} vs {cabecera[idx_x]}")
                    plt.tight_layout()
                    
                    os.makedirs("outputs", exist_ok=True)
                    ruta_salida = "outputs/gráfico_correlacion.png"
                    plt.savefig(ruta_salida)
                    plt.show()
                    plt.close()
                    print(f"\n[Éxito] Gráfico guardado en '{ruta_salida}'")
                except Exception as e:
                    print(f"[Error] Ocurrió un error generando el gráfico: {e}")
        else:
            print("[Opción inválida] Intente de nuevo.")