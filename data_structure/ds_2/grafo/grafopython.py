rede = {
    "Juan": ["Renan", "Alan", "Pedro"],
    "Renan": ["Juan", "Miguel"],
    "Alan": ["Juan", "Pedro", "Vitor"],
    "Miguel": ["Renan", "Paulo", "Julio"],
    "Paulo": ["Miguel", "Julio"],
    "Vitor": ["Alan", "Gaby", "Laura"],
    "Julio": ["Miguel", "Paulo", "Laura"],
    "Pedro": ["Juan", "Alan", "Gaby"],
    "Gaby": ["Vitor", "Pedro", "Laura"],
    "Laura": ["Vitor", "Julio", "Gaby"]
}

tamanho = len(rede)

for usuario, amigos in rede.items():
    print(usuario, "tem", len(amigos), "conexoes")

soma_graus = sum(len(amigos) for amigos in rede.values())
arestas = soma_graus // 2
densidade = (2 * arestas) / (tamanho * (tamanho - 1))


print("Total de usuarios: ", tamanho)
print("Total de amizades: ", arestas)
print(f"Desnidade: {densidade:.2%}")
