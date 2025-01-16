# Calculadora de Partidas Rankeadas [Python]

Este projeto, desenvolvido como parte do curso **"GFT Start #6 - Lógica de Programação"** oferecido pela DIO, consiste no desafio de criar uma calculadora de partidas ranqueadas.

## 🎯 Objetivo do Projeto

Criar uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador. Depois, retorna o resultado para uma variável, onde o saldo de partidas ranqueadas é calculado utilizando a fórmula:

\[ \text{Saldo} = \text{Vitórias} - \text{Derrotas} \]

Este projeto aplica conceitos fundamentais de programação aprendidos ao longo do curso.

---

## 🗂️ Estrutura do Projeto

- **`src/`**
  - **`calculator.py`**: Contém as funções para calcular o nível e o saldo de um jogador.
  - **`main.py`**: Script principal que solicita a entrada do usuário e exibe o nível e o saldo do jogador.
  - **`RankedMatchesDB`**: Documento contendo a classificação dos níveis.

---

## 🏆 Classificação do Nível

O jogador é classificado em diferentes níveis com base no número de vitórias, utilizando estruturas de decisão:

- **Menos de 10 vitórias**: Ferro
- **Entre 11 e 20 vitórias**: Bronze
- **Entre 21 e 50 vitórias**: Prata
- **Entre 51 e 80 vitórias**: Ouro
- **Entre 81 e 90 vitórias**: Diamante
- **Entre 91 e 100 vitórias**: Lendário
- **Mais de 101 vitórias**: Imortal

---

## 🚀 Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/profamar/RankedMatchCalculator.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd RankedMatchCalculator/src
   ```

3. Execute o script principal:

   ```bash
   python main.py
   ```

4. Insira o número de vitórias e derrotas quando solicitado.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para colaborar com o projeto:

1. Faça um fork do repositório.
2. Crie uma nova branch:

   ```bash
   git checkout -b minha-branch
   ```

3. Envie suas alterações e crie um pull request.

---

## 💻 Exemplo de Código

Aqui está um exemplo de como a classificação pode ser implementada em Python:

```python
# Função para classificar o jogador com base no número de vitórias
def classificar_jogador(vitorias):
    if vitorias < 10:
        return "Ferro"
    elif 10 <= vitorias <= 20:
        return "Bronze"
    elif 21 <= vitorias <= 50:
        return "Prata"
    elif 51 <= vitorias <= 80:
        return "Ouro"
    elif 81 <= vitorias <= 90:
        return "Diamante"
    elif 91 <= vitorias <= 100:
        return "Lendário"
    else:
        return "Imortal"

# Exemplo de uso
def main():
    vitorias = int(input("Digite o número de vitórias: "))
    derrotas = int(input("Digite o número de derrotas: "))
    saldo = vitorias - derrotas
    nivel = classificar_jogador(vitorias)

    print(f"Saldo: {saldo}")
    print(f"Nível: {nivel}")

if __name__ == "__main__":
    main()
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.9+**: Linguagem principal para a implementação.
- **Git & GitHub**: Para versionamento e colaboração.
- **Editor de Código**: Visual Studio Code, PyCharm ou outro de sua preferência.

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais informações.

---

Para dúvidas ou sugestões, entre em contato pelo LinkedIn: [Márcia Soares](https://www.linkedin.com/in/márcia-soares-236974256)

⭐ Se este projeto foi útil para você, considere dar uma estrela!
