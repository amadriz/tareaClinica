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

# ***PACIENTE**

pacientes = []
# #Loop Para ingresar los datos a la lista enfermedades[]
while True:
    datos = input(f'Ingrese Cedula, Nombre, Apellido, Telefono y Direccion, digite letra end al finalizar')
    if str.lower(datos) == "end":
        break
    pacientes.append(datos)

    # Loop para escribir en el archivo la enferemedades
    with open('pacientes.txt', 'w') as arch_pacientes:
        for paciente in pacientes:
            arch_pacientes.write(paciente)
            arch_pacientes.write(",")

    listaEnfermedades = list(pacientes)

# ***SECCION ENFERMEDADES**

enfermedades = []

#Loop Para ingresar los datos a la lista enfermedades[]
while True:
    enfermedad = input(f'Ingrese enfermedad tratada, con la letra q finaliza la lista')
    if str.lower(enfermedad) == "end":
        break
    enfermedades.append(enfermedad)
#Loop para escribir en el archivo la enferemedades
with open('enfermedades.txt', 'w') as arch_enfermedades:
    for enfermedad in enfermedades:
        arch_enfermedades.write(enfermedad)
        arch_enfermedades.write("\n")

listaEnfermedades = list(enfermedades)

# with open('enfermedades.txt') as mi_archivo:
# enfermedades = mi_archivo.readlines()

print(f'Lista de enfermedades paciente:{listaEnfermedades}')

# ***SECCION MEDICAMENTOS**

medicamentos = []
#Loop Para ingresar los datos a la lista medicamentos
while True:
    medicamento = input(f'Ingrese medicamento, con la letra q finaliza la lista')
    if str.lower(medicamento) == "end":
        break
    medicamentos.append(medicamento)

#Lopp para escribir en el archivo la medicamentos

with open('medicamentos.txt', 'w') as arch_medicamento:
    for medicamento in medicamentos:
        arch_medicamento.write(medicamento)
        arch_medicamento.write('\n')

listaMedicamentos = list(medicamentos)

print(f'Lista de medicamentos pacientes:{listaMedicamentos}')
#
#
#
#
# cedula = (int(input(f'Ingrese su identificacion sin guiones')))
# nombre = input(f'Ingrese su nombre')
# apellido = input(f'Ingrese su apellido')
# telefono = input(f'Ingrese su numero de telefono')
# direccion = input(f'Ingrese su direccion')

#
#
# print(cedula, nombre, apellido, telefono, direccion, listaEnferm, listaMed)