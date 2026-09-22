from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler as Sampler
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(2, 2) #Cria um circuito com 2 qubits e 2 estados
qc.h(0) #coloca o qubit 0 em superposicao
qc.cx(0, 1) #entrelaca o qubit 0 e qubit 1
qc.measure([0, 1], [0, 1]) #faz a medicao dos qubits e guarda o resultado nos bits classicos
print(qc.draw()) #printa o circuito






"""import numpy as np

class Qubit:
    def __init__(self, alpha=1.0, beta=0.0): #prob de estados do qubit (alfa e beta)
        self.state = np.array([alpha, beta], dtype=complex)

    #verifica se está normalizado, retorna true caso esteja, false não estando
    def is_normalized(self):
        norma = np.linalg.norm(self.state) #linalg é o submodulo do np para algebra linear
        return np.isclose(norma, 1.0) #desconsidera uma pequena diferença causada pelo arredondamento de máquina

    #normaliza o qubit
    def normalize(self):
        norma = np.linalg.norm(self.state)
        if norma == 0:
            raise ValueError("O vetor de estado não pode ser normalizado porque é o vetor nulo.")
        self.state /= norma


q1 = Qubit(1.0, 0.0)
print("q1 está normalizado?", q1.is_normalized())

q2 = Qubit(1.0, 1.0)
print("q2 está normalizado?", q2.is_normalized())
q2.normalize()
print("q2 após normalização:", q2.state)"""