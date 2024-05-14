class Cliente():

    def __init__(self, nombre, correo, edad, tipo="Standard",compras=0):
        self.id = nombre
        self.correo = correo
        self.edad = edad
        self.tipo = tipo
        self.preferencias = []

    def __str__(self):
        return f'Usuario {self.id}\n> Perfil de usuario: {self.tipo}\n> Edad:{self.edad}\n> Correo:{self.correo}'

    def modificar_perfil(self,valor):
        if valor>0:
            self.tipo = "Premium"
            return f'Su perfil de usuario se modfico a{self.tipo}'

    def indicar_preferencias(self, rubros):
        self.preferencias.append(rubros)
    
    def mostrar_preferencias(self):
        if len(self.preferencias) >0: 
            mensaje = 'Sus preferencias son:\n'
            for rubro in self.preferencias:
                mensaje += f'- {rubro}\n'
            return mensaje
        else: 
            return 'No tiene preferencias'
    