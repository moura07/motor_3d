class Vector3D: 
    def __init__(self, x: float, y: float, z:float):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self) -> str:
        # Retorna uma string formatada representando o vetor
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def __add__(self, other: 'Vector3D') -> 'Vector3D':
        # Cria e retorna um NOVO vetor com a soma dos eixos
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        novo_z = self.z + other.z
        return Vector3D(novo_x, novo_y, novo_z)

# Bloco princiapl de execução
if __name__ == "__main__":
    # Instanciando (criando) o nosso primeiro vetor
    v1 = Vector3D(1.0, 2.5, -3.0)
    v2 = Vector3D(4.0, 5.0, -1.0)

    # A mágica do __add__ acontece aqui
    v3 = v1 + v2

    # A mágica do __repr__ acontece aqui
    print(f"Vetor 1: {v1}")
    print(f"Vetor 2: {v2}")
    print(f"Resultado da Soma: {v3}")

    # Acessando e imprimindo os atributos do vetor
    # print(f"Vetor criado com sucesso: X={v1.x}, Y={v1.y}, Z={v1.z}")