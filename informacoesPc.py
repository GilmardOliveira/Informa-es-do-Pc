
import platform
import wmi


def main():
    try:
        c = wmi.WMI()

        computador = c.Win32_ComputerSystem()[0]
        sistema = c.Win32_OperatingSystem()[0]
        processador = c.Win32_Processor()[0]

        memoria_gb = int(computador.TotalPhysicalMemory) / (1024 ** 3)

        print("=" * 45)
        print("       INVENTARIO DE HARDWARE")
        print("=" * 45)

        print("\n[ COMPUTADOR ]")
        print(f"Fabricante: {computador.Manufacturer}")
        print(f"Modelo: {computador.Model}")
        print(f"Nome: {computador.Name}")
        print(f"Familia: {computador.SystemFamily or 'Nao informado'}")

        print("\n[ PROCESSADOR ]")
        print(f"Modelo: {processador.Name.strip()}")
        print(f"Nucleos: {processador.NumberOfCores}")
        print(f"Processadores logicos: {processador.NumberOfLogicalProcessors}")

        print("\n[ MEMORIA RAM ]")
        print(f"Memoria instalada: {memoria_gb:.2f} GB")

        print("\n[ SISTEMA OPERACIONAL ]")
        print(f"Sistema: {sistema.Caption}")
        print(f"Versao: {sistema.Version}")
        print(f"Arquitetura: {platform.machine()}")

        print("\n" + "=" * 45)

    except (wmi.x_wmi, IndexError, AttributeError) as erro:
        print(f"Erro ao consultar informacoes do computador: {erro}")


if __name__ == "__main__":
    main()
