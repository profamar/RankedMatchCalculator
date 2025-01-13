# src/calculator.py

def calcular_nivel(vitorias):
    if vitorias < 10:
        return "Ferro"
    elif vitorias <= 20:
        return "Bronze"
    elif vitorias <= 50:
        return "Prata"
    elif vitorias <= 80:
        return "Ouro"
    elif vitorias <= 90:
        return "Diamante"
    elif vitorias <= 100:
        return "Lendário"
    else:
        return "Imortal"

def calcular_saldo(vitorias, derrotas):
    return vitorias - derrotas

# src/main.py

from calculator import calcular_nivel, calcular_saldo

def main():
    vitorias = int(input("Digite o número de vitórias: "))
    derrotas = int(input("Digite o número de derrotas: "))

    saldo = calcular_saldo(vitorias, derrotas)
    nivel = calcular_nivel(vitorias)

    print(f"O Herói tem um saldo de {saldo} e está no nível {nivel}")

if __name__ == "__main__":
    main()
