# Se propone crear una aplicación escrita en Python que permita la gestión de pacientes de una
# clínica. La aplicación debe solicitar al usuario la información clásica de paciente como:

# 1. identificación
# 2. Nombre
# 3. Apellido
# 4. teléfono
# 5. dirección
# 6. lista de enfermedades tratadas
# 7. lista de medicamentos que toma

# pacientes = ['Allan', 'Roberto', 'Luis', 'Jose','Juan']
#
# with open('pacientes.txt', 'w') as arch_pacientes:
#     for paciente in pacientes:
#         arch_pacientes.write(paciente)
#         arch_pacientes.write("\n")
import csv
# ***PACIENTE**
# #Loop Para ingresar los datos a la lista enfermedades[]
pacientes = []
# # cedula = (int(input(f'Ingrese su identificacion sin guiones')))
# # nombre = input(f'Ingrese su nombre')
# # apellido = input(f'Ingrese su apellido')
# # telefono = input(f'Ingrese su numero de telefono')
# # direccion = input(f'Ingrese su direccion')
while True:
    cedula = input(f'Ingrese la Cedula')
    nombre = input(f'Ingrese su nombre')
    apellido = input(f'Ingrese su apellido')
    telefono = input(f'Ingrese su numero telefonico')
    direccion = input(f'Ingrese la direccion')
    enfermedad = input(f'Ingrese enfermedad tratada')
    medicamento = input(f'Ingrese medicamento')
    end = input(f'Ecriba end para terminar')
    pacientes.append([cedula, nombre, apellido, telefono, direccion, enfermedad, medicamento])
    with open('pacientes.txt', mode='a', newline='') as arch_pacientes:
        writer = csv.writer(arch_pacientes)
        writer.writerows(pacientes)
        if end == end:
            break

# Se genera la lista de los pacientes
listaPacientes = list(pacientes)

print(f'Lista de pacientes:{listaPacientes}')

##Leer archivo
def leer_datos():
    with open('pacientes.txt', mode='r') as f:
        reader = csv.reader(f)
        for i in reader:
            print(i)


##MéTODO PARA ELIMINAR PACIENTE
lines = []

def delete():
    borrar = input(f'Escriba el paciente que desea eliminar')
    with open('pacientes.txt', mode='r') as r:
        reader = csv.reader(r)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == borrar:
                    lines.remove(row)
    with open('pacientes.txt', mode='w', newline='') as w:
        writer = csv.writer(w)
        writer.writerows(lines)

delete()

