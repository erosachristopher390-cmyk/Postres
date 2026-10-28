class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


class ListaIngredientes:
    def __init__(self):
        self.cabeza = None

    def insertar(self, nombre):
        nombre = nombre.strip()

        if not nombre:
            return False

        actual = self.cabeza

        while actual:
            if actual.nombre.lower() == nombre.lower():
                return False
            actual = actual.siguiente

        nuevo = NodoIngrediente(nombre)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

        return True

    def mostrar(self):
        ingredientes = []
        actual = self.cabeza

        while actual:
            ingredientes.append(actual.nombre)
            actual = actual.siguiente

        return ingredientes

    def eliminar(self, nombre):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.nombre.lower() == nombre.lower():
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True

            anterior = actual
            actual = actual.siguiente

        return False


class NodoPostre:
    def __init__(self, nombre):
        self.nombre = nombre.strip()
        self.ingredientes = ListaIngredientes()
        self.siguiente = None


class ListaPostres:
    def __init__(self):
        self.cabeza = None

    def buscar(self, nombre):
        actual = self.cabeza

        while actual:
            if actual.nombre.lower() == nombre.lower():
                return actual
            actual = actual.siguiente

        return None

    def insertar_postre(self, nombre):
        nombre = nombre.strip()

        if not nombre:
            print("Error: el nombre del postre no puede estar vacío.")
            return

        if self.buscar(nombre):
            print("Error: el postre ya existe.")
            return

        nuevo = NodoPostre(nombre)

        if self.cabeza is None or nombre.lower() < self.cabeza.nombre.lower():
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            print("Postre agregado correctamente.")
            return

        actual = self.cabeza

        while actual.siguiente and actual.siguiente.nombre.lower() < nombre.lower():
            actual = actual.siguiente

        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

        print("Postre agregado correctamente.")

    def mostrar_postres(self):
        actual = self.cabeza

        if actual is None:
            print("La lista de postres está vacía.")
            return

        while actual:
            print(f"- {actual.nombre}: {actual.ingredientes.mostrar()}")
            actual = actual.siguiente

    # Inciso a: consultar ingredientes
    def consultar_ingredientes(self, nombre):
        postre = self.buscar(nombre)

        if postre is None:
            print("Error: el postre no existe.")
            return

        ingredientes = postre.ingredientes.mostrar()
        print(f"Ingredientes de {postre.nombre}:")
        print(ingredientes if ingredientes else "No tiene ingredientes registrados.")

    # Inciso b: insertar ingrediente
    def insertar_ingrediente(self, nombre, ingrediente):
        postre = self.buscar(nombre)

        if postre is None:
            print("Error: el postre no existe.")
            return

        if postre.ingredientes.insertar(ingrediente):
            print("Ingrediente agregado correctamente.")
        else:
            print("Error: ingrediente vacío o ya existente.")

    # Inciso c: eliminar ingrediente
    def eliminar_ingrediente(self, nombre, ingrediente):
        postre = self.buscar(nombre)

        if postre is None:
            print("Error: el postre no existe.")
            return

        if postre.ingredientes.eliminar(ingrediente):
            print("Ingrediente eliminado correctamente.")
        else:
            print("Error: el ingrediente no existe.")

    # Inciso d: alta de postre
    # Se realiza mediante insertar_postre().

    # Inciso e: baja de postre
    def eliminar_postre(self, nombre):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.nombre.lower() == nombre.lower():
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                print(f"Postre '{actual.nombre}' eliminado.")
                print("Su lista de ingredientes deja de pertenecer a la estructura.")
                return

            anterior = actual
            actual = actual.siguiente

        print("Error: el postre no existe.")

    # Ejercicio 2: eliminar postres repetidos (conserva la primera aparición)
    def eliminar_repetidos(self):
        actual = self.cabeza
        eliminados = 0

        while actual:
            anterior = actual
            duplicado = actual.siguiente

            while duplicado:
                if duplicado.nombre.lower() == actual.nombre.lower():
                    anterior.siguiente = duplicado.siguiente
                    eliminados += 1
                else:
                    anterior = duplicado
                duplicado = anterior.siguiente

            actual = actual.siguiente

        if eliminados:
            print(f"Se eliminaron {eliminados} postre(s) repetido(s).")
            print("Se conservaron las listas de ingredientes de los primeros postres.")
        else:
            print("No se encontraron postres repetidos.")


def menu():
    postres = ListaPostres()

    while True:
        print("\n===== SISTEMA DE POSTRES =====")
        print("1. Dar de alta un postre")
        print("2. Consultar ingredientes")
        print("3. Insertar ingrediente")
        print("4. Eliminar ingrediente")
        print("5. Dar de baja un postre")
        print("6. Mostrar todos los postres")
        print("7. Eliminar postres repetidos")
        print("8. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del postre: ")
            postres.insertar_postre(nombre)

        elif opcion == "2":
            nombre = input("Nombre del postre: ")
            postres.consultar_ingredientes(nombre)

        elif opcion == "3":
            nombre = input("Nombre del postre: ")
            ingrediente = input("Ingrediente a insertar: ")
            postres.insertar_ingrediente(nombre, ingrediente)

        elif opcion == "4":
            nombre = input("Nombre del postre: ")
            ingrediente = input("Ingrediente a eliminar: ")
            postres.eliminar_ingrediente(nombre, ingrediente)

        elif opcion == "5":
            nombre = input("Nombre del postre a eliminar: ")
            postres.eliminar_postre(nombre)

        elif opcion == "6":
            postres.mostrar_postres()

        elif opcion == "7":
            postres.eliminar_repetidos()

        elif opcion == "8":
            print("Programa finalizado.")
            break

        else:
            print("Error: opción no válida.")


if __name__ == "__main__":
    menu()
