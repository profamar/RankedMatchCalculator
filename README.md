# Projeto: Calculadora de Partidas Rankeadas

Este projeto, desenvolvido como parte do curso "GFT Start #6 - Lógica de Programação" oferecido pela DIO, consiste no desafio de criar uma calculadora de partidas ranqueadas. 

## Objetivo do Projeto
Criar uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador. Depois, retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do cálculo: vitórias - derrotas, aplicando conceitos fundamentais de programação aprendidos ao longo do curso.

## Estrutura do Projeto

- `src/`
  - `calculator.py`: Contém as funções para calcular o nível e o saldo de um jogador.
  - `main.py`: Script principal que solicita a entrada do usuário e exibe o nível e o saldo do jogador.
  - `RankedMatchesDB`: Documento com a classificação dos níveis.

## Classificação do Nível

Utilize estruturas de decisão para classificar o jogador em diferentes níveis com base no número de vitórias:

- **Menos de 10 vitórias:** Ferro
- **Entre 11 e 20 vitórias:** Bronze
- **Entre 21 e 50 vitórias:** Prata
- **Entre 51 e 80 vitórias:** Ouro
- **Entre 81 e 90 vitórias:** Diamante
- **Entre 91 e 100 vitórias:** Lendário
- **Mais de 101 vitórias:** Imortal

 
## Como Executar
1.Clone o repositório:
git clone https://github.com/profamar/RankedMatchCalculator.git

2.Navegue até o diretório do projeto:
cd RankedMatchCalculator/src

3.Execute o script principal:
python main.py

4.Insira o número de vitórias e derrotas quando solicitado.

Contribuição
Sinta-se à vontade para contribuir com o projeto. Para isso, siga os passos abaixo:

Faça um fork do repositório.
Crie uma nova branch.

##  Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Exemplo de Código

Aqui está um exemplo de como essa classificação pode ser implementada em Python:

```python
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
'
'
'
