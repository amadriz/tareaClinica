# import csv
#
import csv

pacientes = []
# # # cedula = (int(input(f'Ingrese su identificacion sin guiones')))
# # # nombre = input(f'Ingrese su nombre')
# # # apellido = input(f'Ingrese su apellido')
# # # telefono = input(f'Ingrese su numero de telefono')
# # # direccion = input(f'Ingrese su direccion')
while True:
    cedula = input(f'Ingrese la Cedula')
    nombre = input(f'Ingrese su nombre')
    end = input('')
    pacientes.append([cedula, nombre])

    # Loop para escribir en el archivo la enferemedades
    with open('test.txt', mode='a', newline='') as arch_pacientes:
        writer = csv.writer(arch_pacientes)
        writer.writerows(pacientes)
        # for paciente in pacientes:
        #     arch_pacientes.writelines(paciente,',')

        if end == end:
            break

# Se genera la lista de los pacientes
listaPacientes = list(pacientes)

print(f'Lista de pacientes:{listaPacientes}')



