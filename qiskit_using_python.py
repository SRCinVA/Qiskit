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

circuit.draw()                      # Amazingly, this will return an ASCII representation of the circuit.  

circuit.draw(output='mpl')          # This will render a MatplotLib version of the circuit. 

# to run this code on a quantum machine:

from qiskit import IBMQ

IBM.save_account("whatever your token is")  #it will save your token
IBM.load_account()
provider = IBM.get_provider("ibm q")
for backend in provider.backends():
    try:
        qubit_count = len(backend.properties().qubits)
    except:
        qubit_count = 'simulated'
    print(f"{backend.name()} has {backend.status().pending_jobs} queued and {qubit_count} qubits")

from qiskit.tools.monitor import job_monitor

backend = provider.get_backend("ibmq_xyz")
job = q.execute(circuit, backend=backend, shots = 500)  # 'shots' specifies how many times you will run it to get a useful representation.) 
job_monitor(job)