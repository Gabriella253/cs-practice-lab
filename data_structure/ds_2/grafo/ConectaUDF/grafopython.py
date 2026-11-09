rede = {
    
    "Juan": ["Renan", "Alan", "Pedro"],
    "Renan": ["Juan", "Alan", "Miguel"],
    "Alan": ["Juan", "Renan", "Pedro", "Gaby"],
    "Miguel": ["Renan", "Paulo", "Julio"],
    "Paulo": ["Miguel", "Julio"],
    "Vitor": ["Pedro", "Gaby", "Laura"],
    "Julio": ["Miguel", "Paulo", "Laura"],
    "Pedro": ["Juan", "Alan", "Vitor"],
    "Gaby": ["Alan", "Vitor", "Laura"],
    "Laura": ["Vitor", "Gaby", "Julio"]
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
