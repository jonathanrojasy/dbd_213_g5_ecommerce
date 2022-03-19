class Cliente:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cliente = self.session.get("cliente")
        if not cliente:
            cliente = self.session["cliente"] = {}
        self.cliente = cliente

    def agregar_cliente(self, id_usuario):
        if not self.cliente.keys():
            self.cliente[id_usuario] = {
                "id_usuario": id_usuario,
            }
        self.guardar_cliente()

    def guardar_cliente(self):
        self.session["cliente"] = self.cliente
        self.session.modified = True

    def eliminar_cliente(self):
        self.session["cliente"] = {}
        self.session.modified = True
