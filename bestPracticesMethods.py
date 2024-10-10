#best clase
class Alumno:
    # __init__ crea la función constructor con atributos vacíos
    def __init__(self, nombre, apellido_paterno, apellido_materno, no_control, semestre):
        # Atributos privados
        self.__nombre = nombre
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        self.__no_control = no_control
        self.__semestre = semestre

    # Métodos para establecer los valores (setters)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos para obtener los valores (getters)
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre

    def get_Nombre_Completo(self):
        return self.__nombre + " " + self.__apellido_paterno + " " + self.__apellido_materno

# Diccionario para almacenar a los alumnos
registro_alumnos = {}

# Ciclo para ingresar los datos de los alumnos
for i in range(3):
    # Crear una instancia de Alumno y luego modificar sus atributos
    alumno = Alumno("", "", "", "", 0)

    alumno.set_nombre(input("Ingresa el nombre: "))
    alumno.set_apellido_materno(input("Ingresa el apellido materno: "))
    alumno.set_apellido_paterno(input("Ingresa el apellido paterno: "))
    alumno.set_no_control(input("Ingresa el número de control: "))
    alumno.set_semestre(int(input("Ingresa el semestre: ")))

    
    registro_alumnos[i] = alumno

# Imprimir los datos de los alumnos
for i in range(3):
    print(f"Nombre: {registro_alumnos[i].get_nombre()}")
    print(f"Apellido Paterno: {registro_alumnos[i].get_apellido_paterno()}")
    print(f"Apellido Materno: {registro_alumnos[i].get_apellido_materno()}")
    print(f"No. Control: {registro_alumnos[i].get_no_control()}")
    print(f"Semestre: {registro_alumnos[i].get_semestre()}")
    print(f"Nombre Completo: {registro_alumnos[i].get_Nombre_Completo()}\n")

