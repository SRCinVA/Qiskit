import qiskit as q
matplotlib inline

# we'll use Python to program the quantum computer

circuit = q.QuantumCircuit(2,2) # 2 qubits, 2 classical bits

# currently the qubits are: 0, 0

# then you flip the first qubit, using the 'not' gate below:
circuit.x(0) 
# leading to result: 1, 0

circuit.cx(0, 1)        # this is a cnot (controlled not) and it entangles the qubits. 
                        # it flips the second qubit value IF the first qubit is a 1. 
                        # as a result of this operation, we should have a (1,1). 

circuit.measure([0,1], [0, 1])      # remember that measuring causes collapse into a state. 
                                    # the parameters specify how the qubit register will map to the calssical register. 
                                    # Question: not a good explanation.  

circuit.draw()                      # Amazingy, this will return an ASCII representation of the circuit. 