# Simulação de Qubit

Projeto de estudo sobre computação quântica, combinando o uso do **Qiskit** para circuitos reais e uma implementação própria em Python para entender a matemática por trás de um qubit.

> 🚧 **Em desenvolvimento.** Este projeto está em fase inicial e vai crescer aos poucos conforme o aprendizado avança.

## Conteúdo atual

### 1. Circuito com Qiskit (par de Bell)

Cria um circuito de 2 qubits que gera um **estado de Bell** (par entrelaçado):

- Aplica uma porta Hadamard (`h`) no qubit 0, colocando-o em superposição
- Aplica uma porta CNOT (`cx`) entre os qubits 0 e 1, entrelaçando-os
- Mede os dois qubits e armazena o resultado nos bits clássicos
- Imprime a representação visual do circuito

### 2. Classe `Qubit` (implementação própria — em desenvolvimento)

Representação manual de um qubit como vetor de estado `[alpha, beta]`, usando `numpy`, com:

- `is_normalized()`: verifica se o vetor de estado está normalizado (norma ≈ 1), tolerando erro de arredondamento de máquina
- `normalize()`: normaliza o vetor de estado, com tratamento de erro para vetor nulo

## Tecnologias

- Python
- [Qiskit](https://www.ibm.com/quantum/qiskit) (`qiskit`, `qiskit.primitives`, `qiskit.visualization`)
- NumPy

## Como rodar

```bash
pip install qiskit numpy
python qubit_simulation.py
```

## Próximos passos

- Expandir a classe `Qubit` (operações com portas quânticas, medição, etc.)
- Integrar a implementação própria com os circuitos do Qiskit para comparação
- Adicionar visualizações (histograma de resultados, esfera de Bloch)

## Sobre

Projeto pessoal de portfólio, ligado aos estudos de Engenharia de Computação (UFGD) e ao interesse em computação/pesquisa quântica.

**Autor:** Heitor Pardinho Romero
