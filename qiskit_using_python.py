import qiskit as q
matplotlib inline

circuit = q.QuantumCircuit(2,2) # 2 qubits, 2 classical bits

# currently the qubits are: 0, 0

# then you flip the first qubit, using a 'not' gate below
circuit.x(0) 
# leading to this result: 1, 0
#  
circuit.cx()       # this is a cnot (controlled not) and entangles the qubits