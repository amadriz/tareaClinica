def leer_archivo(nombre_archivo):

    with open(nombre_archivo) as file:
        datos = file.readlines()

        #procesar, limpiar los datos
        datos = [reglon.replace('\n', '') for reglon in datos]

        # pro convencion datos como lista de listas cambiar separador por comas
        datos = [reglon.split(',') for reglon in datos]

        #convertir lista de listas a lista de diccionarios
        # elemento 0 = nombre
        # elemento 1 = apellido
        # elemento 2 = edad
        # elemento 3 = saldo

        datos = [{'nombre': reglon[0],
            'apellido': reglon[1],
            'edad': reglon[2],
            'enfermedades': reglon[3],
            'medicamentos': reglon[4]
            } for reglon in datos]

        [paciente.update({'enfermedades': paciente['enfermedades'].split('|') }) for paciente in datos]
        [paciente.update({'medicamentos': paciente['medicamentos'].split('|')}) for paciente in datos]
        return datos

if __name__ == '__main__':
    mis_datos = leer_archivo('mi_familia.txt')

#Quiero leer el archivo mi_familia.txt

print(mis_datos)


def escribir_archivo(nombre_archivo, mis_datos):
    # param 1 nombre archivo
    # param 2 los datos a incluir

    #Escribir en archivo
    # nombre, apellido, edad, enfermedades, medicamentos
    # medicamento -> pastilla | crema | agua
    # enfermedades -> diabetes|cancer|hambre

    #Convertir la lista de medicamentos hacia string de medicamentos separados por |
    [paciente.update({'medicamentos': '|'.join(paciente['medicamentos'])}) for paciente in mis_datos]

    #Convertir la lista de medicamentos hacia string de medicamentos separados por |
    [paciente.update({'enfermedades': '|'.join(paciente['enfermedades'])}) for paciente in mis_datos]

    #Convertir de lista de diccionarios a lista de listas
    mis_datos = [list(paciente.values()) for paciente in mis_datos]
    #convertir de lista de listas a lista de strings
    mis_datos = [','.join(paciente) for paciente in mis_datos]

    #agregarle el separador de reglon \n para que incluya las lineas

    mis_datos = [f'{paciente}\n' for paciente in mis_datos]

    with open('nombre_archivo', mode='w') as file:
        file.writelines(mis_datos)

# def borrar_paciente(id, mis_datos):
#     #verificar que el nombre existe
#
# def agregar_paciente():
#     #usar append

#



pass