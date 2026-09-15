from os_utils import check_ping, check_disk_space

def mostrar_menu() -> None:
    print("=== Toolkit Sysadmin ===")
    print("1. Comprobar conectividad (ping)")
    print("2. Comprobar espacio en disco")
    print("3. Parsear log SSH")
    print("4. Auditar dispositivo de red")
    print("5. Consultar IP sospechosa")
    print("0. Salir")

def main() -> None:
    while True:
        mostrar_menu()
        opcion: str = input("Elige una opción: ")

        if opcion == "0":
            print("Saliendo del programa...")
            break

        elif opcion == "1":
            ip: str = input("Introduce la dirección IP a comprobar: ")
            if check_ping(ip):
                print(f"Conectividad con {ip} exitosa.")
            else:
                print(f"No se pudo establecer conectividad con {ip}.")

        elif opcion == "2":
            path: str = input("Introduce la ruta del disco a comprobar (por defecto C:\\): ") or "C:\\"
            percentage_free = check_disk_space(path)
            if percentage_free >= 20:
                print(f"Espacio en disco en {path} suficiente.")
            else:
                print(f"Advertencia: Hay menos del 20% de espacio libre en {path}.")
        else:
            print("Opción no implementada aún")

if __name__ == "__main__":
    main()