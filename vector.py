class Vector3D: 
    def __init__(self, x: float, y: float, z:float):
        self.x = x
        self.y = y
        self.z = z

# Bloco princiapl de execução
if __name__ == "__main__":
    # Instanciando (criando) o nosso primeiro vetor
    v1 = Vector3D(1.0, 2.5, -3.0)

    # Acessando e imprimindo os atributos do vetor
    print(f"Vetor criado com sucesso: X={v1.x}, Y={v1.y}, Z={v1.z}")