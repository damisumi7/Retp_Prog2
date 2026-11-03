import os
from procesamiento_txt import menu_procesamiento_txt
from analisis_csv import menu_analisis_csv

def main():
    while True:
        print("\n" + "="*40)
        print("     MENÚ PRINCIPAL - ANÁLISIS DE DATOS")
        print("="*40)
        print("1. Explorar directorio (.txt y .csv)")
        print("2. Procesar Bitácoras / Textos Reales (.txt)")
        print("3. Analizar Dataset de Datos Abiertos (.csv)")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            ruta = input("Ingrese la ruta del directorio a explorar (deje en blanco para el directorio actual): ").strip()
            if not ruta:
                ruta = "."
            try:
                archivos = [f for f in os.listdir(ruta) if f.endswith(('.txt', '.csv'))]
                print(f"\n--- Archivos encontrados en '{ruta}' ---")
                if not archivos:
                    print("No se encontraron archivos .txt o .csv.")
                for archivo in archivos:
                    print(f" - {archivo}")
            except Exception as e:
                print(f"[Error] No se pudo leer el directorio: {e}")
                
        elif opcion == "2":
            menu_procesamiento_txt()
            
        elif opcion == "3":
            menu_analisis_csv()
            
        elif opcion == "4":
            print("\n¡Saliendo del programa. Hasta pronto!")
            break
        else:
            print("[Opción inválida] Por favor, ingrese un número del 1 al 4.")

if __name__ == "__main__":
    main()