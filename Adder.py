from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.quantum_info import Pauli
from qiskit.quantum_info import Statevector, partial_trace
import qiskit.quantum_info as qi
import matplotlib.pyplot as plt
import numpy as np
import math
import cmath
from qiskit.visualization import plot_state_city

class Operations(object):
    def simple_adder(self):
        qc = QuantumCircuit(6, 6)
        qc.h([2, 3])
        #qc.h([2, 3])
        qc.cx(2, 4)
        qc.cx(3, 4)
        qc.ccx(2, 3, 5)
        #qc.h([0, 1])
        custom_gate_1 = np.array(
            [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]])
        custom_gate_2 = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 1, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 1, 0, 0, 0, 0],
                                  [0, 0, 0, 0, -1, 0, 0, 0],
                                  [0, 0, 0, 0, 0, -1, 0, 0],
                                  [0, 0, 0, 0, 0, 0, -1, 0],
                                  [0, 0, 0, 0, 0, 0, 0, -1]])
        #qc.cz(0, 1)
        qc.ch(5, [0, 1])
        qc.unitary(custom_gate_1, [0, 1, 2, 3, 5])
        #qc.unitary(custom_gate_2, [5, 1, 0])
        qc.ch(5, [0, 1])
        qc.cx(5, [0, 1])
        qc.ch(5, 1)
        qc.ccx(5, 0, 1)
        qc.ch(5, 1)
        qc.cx(5, [0, 1])
        qc.ch(5, [0, 1])

        qc.h([0, 1])
        qc.cz(0, 1)
        qc.h([0, 1])
        qc.x([0, 1])
        qc.h(1)
        qc.cx(0, 1)
        qc.h(1)
        qc.x([0, 1])
        qc.h([0, 1])



        statevector = Statevector.from_instruction(qc)
        print("State Vector:")
        print(statevector.to_dict())

        rdm = partial_trace(statevector, [2, 3, 4])
        print("RDM:")
        print(rdm)

        qc.measure(0, 0)
        qc.measure(1, 1)
        #qc.measure(2, 2)
        #qc.measure(3, 3)
        #qc.measure(4, 4)
        #qc.measure(5, 5)
        print(qc)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)
        #!!If none of the possible qubit sequences have 1, 11, 111, etc as there first, first and second, or first, second, and third, or etc, most significant qubits, set qubits 1 and 0 to zero
        # then do quantum amplitude estimation (QAE) for qubits 1 and 0 and if the phase estimation returns with "1" for 00, then return qubits 1 and 0 to their original values.!!

        #When the cycle is complete and a largest value has been found, use quantum phase estimation to extract the phase of the largest value sequence of qubits.
        #Transfer the qubits being added together to a second set of qubits. Last sequence of qubits that has not had set transfered, mark as negative one,
        #and then proceed to transfer qubits back to original set, and reverse the function and then proceed to do grover's algorithm


    def simple_adder_2(self):
        qc = QuantumCircuit(6, 6)
        qc.h([2, 3])
        qc.cx(2, 4)
        qc.cx(3, 4)
        qc.ccx(2, 3, 5)
        custom_gate_1 = np.array(
            [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]])
        custom_gate_2 = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 1, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 1, 0, 0, 0, 0],
                                  [0, 0, 0, 0, -1, 0, 0, 0],
                                  [0, 0, 0, 0, 0, -1, 0, 0],
                                  [0, 0, 0, 0, 0, 0, -1, 0],
                                  [0, 0, 0, 0, 0, 0, 0, -1]])

        qc.h([0, 1])
        qc.cz(0, 1)
        qc.h([0, 1])
        qc.x([0, 1])
        qc.h(1)
        qc.cx(0, 1)
        qc.h(1)
        qc.x([0, 1])
        qc.h([0, 1])

        statevector = Statevector.from_instruction(qc)
        print("State Vector:")
        print(statevector.to_dict())

        rdm = partial_trace(statevector, [2, 3, 4])
        print("RDM:")
        print(rdm)

        qc.measure(0, 0)
        qc.measure(1, 1)
        # qc.measure(2, 2)
        # qc.measure(3, 3)
        # qc.measure(4, 4)
        # qc.measure(5, 5)
        print(qc)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)

    def complex_adder(self):
        num_of_qubits = 2
        qc = QuantumCircuit((num_of_qubits * 3) + 2, (num_of_qubits * 3) + 2)

        qc.h([0, 1, 2, 3])

        qc.cx(0, 4)
        qc.cx(2, 4)
        qc.ccx(0, 2, 7)
        qc.cx(1, 5)
        qc.cx(3, 5)
        qc.cx(7, 5)
        qc.ccx(1, 3, 6)
        qc.ccx(1, 7, 6)
        qc.ccx(3, 7, 6)
        qc.z(6)
        qc.ccx(3, 7, 6)
        qc.ccx(1, 7, 6)
        qc.ccx(1, 3, 6)
        qc.cx(7, 5)
        qc.cx(3, 5)
        qc.cx(1, 5)
        qc.ccx(0, 2, 7)
        qc.cx(2, 4)
        qc.cx(0, 4)

        qc.h([0, 1, 2, 3])
        qc.x([0, 1, 2, 3])
        qc.h(3)
        qc.mcx([0, 1, 2], 3)
        qc.h(3)
        qc.x([0, 1, 2, 3])
        qc.h([0, 1, 2, 3])

        qc.measure(0, 0)
        qc.measure(1, 1)
        qc.measure(2, 2)
        qc.measure(3, 3)
        qc.measure(4, 4)
        qc.measure(5, 5)
        qc.measure(6, 6)
        #qc.measure(7, 7)

        print(qc)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)



    def even_more_complex_adder(self):
        num_of_qubits = 3
        qc = QuantumCircuit((num_of_qubits * 3) + 3, num_of_qubits + 1)
        qc.x(0)
        qc.x(1)
        qc.x(2)
        qc.x(3)
        #qc.x(4)
        qc.x(5)

        qc.cx(0, 6)
        qc.cx(3, 6)
        qc.ccx(0, 3, 10)

        qc.cx(1, 7)
        qc.cx(4, 7)
        qc.cx(10, 7)
        qc.ccx(1, 4, 11)
        qc.ccx(1, 10, 11)
        qc.ccx(4, 10, 11)

        qc.cx(2, 8)
        qc.cx(5, 8)
        qc.cx(11, 8)

        qc.ccx(2, 5, 9)
        qc.ccx(2, 11, 9)
        qc.ccx(5, 11, 9)

        qc.measure(6, 0)
        qc.measure(7, 1)
        qc.measure(8, 2)
        qc.measure(9, 3)

        print(qc)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)


    def simple_multiplyer(self):
        qc = QuantumCircuit(4,2)
        qc.x(0)
        qc.x(1)
        qc.ccx(0, 1, 2)
        qc.measure(2, 0)
        qc.measure(3, 1)
        print(qc)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)

    #This method tests the qiskit unitary method.
    def gate_tester(self):
        qc = QuantumCircuit(2, 2)
        qc.x(0)
        custom_gate = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
        qc.unitary(custom_gate, [1, 0], label="custom")
        qc.measure(0, 0)
        qc.measure(1, 1)
        print(qc)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)

    #This method tests the qiskit t gate which rotates qubits around the z axis.
    def gate_tester_2(self):
        qc = QuantumCircuit(1, 1)
        qc.h(0)
        qc.t(0)
        #qc.t(0)
        #qc.t(0)
        qc.h(0)
        qc.measure(0, 0)
        print(qc)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)

    #This method tests the rz gate which allows users to rotate qubits by any specific amount.
    def gate_tester_3(self):
        qc = QuantumCircuit(2, 2)
        qc.h([0, 1])
        qc.rz(math.pi / 4, 0)
        qc.measure(0, 0)
        print(qc)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)

    #This method tests the qiskit state vector function.
    def gate_tester_4(self):
        qc = QuantumCircuit(3, 3)
        qc.h([0, 1, 2])
        qc.rz(math.pi / 8, [0, 1, 2])
        qc.h([0, 1, 2])
        state = Statevector.from_instruction(qc)
        qc.measure(0, 0)
        qc.measure(1, 1)
        qc.measure(2, 2)
        print(qc)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)
        print(state)

    #This method was used to test how various rotations around the z axis would affect the qubits final state.
    def gate_tester_5(self):
        qc = QuantumCircuit(1, 1)
        #custom_unitary = np.array([[cmath.exp(1j * math.pi / 8), 0], [0, cmath.exp(1j * math.pi / 4)]])
        qc.x(0)
        qc.h(0)
        qc.z(0)
        qc.rz(0.75 * math.pi, 0)
        #qc.unitary(custom_unitary, [0], label="customU")
        qc.h(0)
        #custom_gate = UnitaryGate(custom_unitary, label="Custom")
        qc.measure(0, 0)
        print(qc)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)

    #This method was used to try and create a standardized method of imbuing a collection of qubits with a specific superposition of states.
    #The goal was to avoid the use of gates to achieve such states as the organization of the gates could not be standardized and also be able to produce different specific states.
    def gate_tester_6(self):
        qc = QuantumCircuit(2, 2)
        basis_states = ["00", "11"]
        superposition_state = sum(Statevector.from_label("00") for state in basis_states) / len(basis_states) ** 0.5
        qc.initialize(superposition_state.data, [0, 1])
        print(qc)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        state_vector = job.get_statevector(qc)
        print("Statevector: " + state_vector)

    #This method consists of further testing on the unitary method and rotating qubits on the z axis.
    def gate_tester_7(self):
        qc = QuantumCircuit(1, 1)
        custom_gate = np.array([[1, 0], [0, cmath.exp(1j * math.pi / 4)]])
        custom_gate2 = np.array([[-1, 0], [0, 1]])
        custom_gate3 = np.array([[-1 / math.sqrt(2.0), 1 / math.sqrt(2.0)], [1 / math.sqrt(2.0), 1 / math.sqrt(2.0)]])
        #qc.x(0)
        qc.unitary(custom_gate2, [0], label="custom2")
        qc.unitary(custom_gate3, [0], label="custom3")
        #qc.t(0)
        qc.unitary(custom_gate, [0], label="custom")
        qc.h(0)
        qc.measure(0, 0)
        print(qc)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)

    #This method test's grover's algorithm.
    def gate_tester_8(self):
        qc = QuantumCircuit(4, 4)


        qc.h([0, 1])
        qc.cz(0, 1)

        qc.h([0, 1])
        qc.x([0, 1])
        qc.h(1)
        qc.cx(0, 1)
        qc.h(1)
        qc.x([0, 1])
        qc.h([0, 1])

        qc.measure(0, 0)
        qc.measure(1, 1)

        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)

    #This method tests a unitary method that operates similar to the hadamard gate.
    def gate_tester_9(self):
        qc = QuantumCircuit(2, 2)

        custom_gate1 = np.array([[1, 0], [0, -1]])
        custom_gate2 = np.array([[-1 / math.sqrt(2.0), 1 / math.sqrt(2.0)], [1 / math.sqrt(2.0), 1 / math.sqrt(2.0)]])

        qc.x([0, 1])
        qc.h([0, 1, 2, 3])
        qc.unitary(custom_gate1, [1, 0], label="custom1")
        qc.unitary(custom_gate2, [1, 0], label="custom2")
        #qc.cx(0, 1)
        qc.measure(0, 0)
        qc.measure(1, 1)

        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)
        print("Operation: " + str(-1 / math.sqrt(2.0)))

    #
    def gate_tester_10(self):
        qc = QuantumCircuit(3, 3)
        custom_gate = np.array([[-3.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0],
                  [1.0 / 4.0, -3.0  / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0],
                  [1.0 / 4.0, 1.0 / 4.0, -3.0  / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0],
                  [1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, -3.0  / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0],
                  [1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, -3.0  / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0],
                  [1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, -3.0  / 4.0, 1.0 / 4.0, 1.0 / 4.0],
                  [1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, -3.0  / 4.0, 1.0 / 4.0],
                  [1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0, -3.0  / 4.0]])
        custom_gate2 = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                                 [0, -1, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 1, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 1, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 1, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 1, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 1, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 1],])
        qc.h([0, 1, 2])
        qc.unitary(custom_gate2, [0, 1, 2], label="custom_gate2")
        qc.unitary(custom_gate, [0, 1, 2], label="custom_gate")
        qc.unitary(custom_gate2, [0, 1, 2], label="custom_gate2")
        qc.unitary(custom_gate, [0, 1, 2], label="custom_gate")


        qc.measure(0, 0)
        qc.measure(1, 1)
        qc.measure(2, 2)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)

    def gate_tester_11(self):
        qc = QuantumCircuit(3, 3)
        #qc.rx(math.pi / 0.5, 2)
        #qc.x(0)
        qc.x(1)
        custom_gate1 = np.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, math.cos(1 * math.pi / 2), -1j * cmath.sin(1 * math.pi / 2)],
                                [0, 0, -1j * cmath.sin(1 * math.pi / 2), math.cos(1 * math.pi / 2)]])
        custom_gate2 = np.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, math.cos(1 * math.pi / 8), -1j * cmath.sin(1 * math.pi / 8)],
                                [0, 0, -1j * cmath.sin(1 * math.pi / 8), math.cos(1 * math.pi / 8)]])
        qc.unitary(custom_gate1, [2, 1], label="custom1")
        qc.unitary(custom_gate2, [2, 0], label="custom2")
        qc.measure(0, 0)
        qc.measure(1, 1)
        qc.measure(2, 2)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)

    def gate_tester_12(self):
        qc = QuantumCircuit(1, 1)
        qc.h([0])
        custom_gate1 = np.array([[1, 0,], [0, cmath.exp(-1j * math.pi / 4)]])
        #qc.unitary(custom_gate1, [0], label="custom1")
        custom_gate2 = np.array([[1, 0], [0, cmath.exp(-1j * math.pi / 8)]])
        #qc.unitary(custom_gate2, [0], label="custom2")
        custom_gate3 = np.array([[1, 0], [0, cmath.exp(-1j * math.pi / 8)]])
        qc.unitary(custom_gate3, [0], label="custom3")
        qc.h(0)
        qc.measure(0, 0)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)

    def gate_tester_13(self):
        qc = QuantumCircuit(2, 2)
        #qc.x([0])
        qc.h([0, 1])
        custom_gate1 = np.array([[1, 0, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 0, cmath.exp(1j * math.pi / 2), 0],
                                 [0, 0, 0, cmath.exp(1j * math.pi / 2)]])
        custom_gate2 = np.array([[1, 0, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 0, cmath.exp(1j * math.pi / 4), 0],
                                 [0, 0, 0, cmath.exp(1j * math.pi / 4)]])
        qc.unitary(custom_gate1, [0, 1], label="custom1")
        # qc.unitary(custom_gate2, [0, 2], label="custom2")
        qc.h([0, 1])
        qc.measure(0, 0)
        qc.measure(1, 1)
        #qc.measure(2, 2)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)

    def gate_tester_14(self):
        qc = QuantumCircuit(4, 4)
        qc.h([0, 1])
        qc.ry(math.pi / 3, 2)
        qc.cx(2, 3)
        custom_gate_1 = np.array([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]])
        custom_gate_2 = np.array( [[1.0 / 2.0, 0.0, 0.0, -1.0 * math.sqrt(3.0) / 2.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, -1.0, 0.0], [math.sqrt(3.0) / 2.0, 0.0, 0.0, 1.0 / 2.0]])
        qc.unitary(custom_gate_2, [2, 3], label="custom2")

        qc.measure(0, 0)
        qc.measure(1, 1)
        qc.measure(2, 2)
        qc.measure(3, 3)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)

    def gate_tester_15(self):
        qc = QuantumCircuit(2, 2)
        qc.h(0)
        qc.cx(0, 1)
        backend = Aer.get_backend("statevector_simulator")
        new_circuit = transpile(qc, backend)
        result = backend.run(new_circuit).result()
        statevector = result.get_statevector()
        print("State Vector: ")
        print(statevector)

    def gate_tester_16(self):
        #|ψ> = A|00>
        qc = QuantumCircuit(3, 3)
        qc.h([1, 2])
        qc.x(2)
        qc.ccx(2, 1, 0)
        qc.x(2)

        # Sx
        qc.z(0)

        # A^-1
        qc.x(2)
        qc.ccx(2, 1, 0)
        qc.h(1)
        qc.x(2)
        qc.h(2)

        # So
        qc.x([0, 1, 2])
        qc.h(0)
        qc.ccx(2, 1, 0)
        qc.h(0)
        qc.x([1, 2])
        qc.x(0)

        # A
        qc.h([1, 2])
        qc.x(2)
        qc.ccx(2, 1, 0)
        qc.x(2)

        qc.measure(0, 0)
        qc.measure(1, 1)
        qc.measure(2, 2)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)

    #This method tests how grover's algorithm preforms when

    def gate_tester_17(self):
        qc = QuantumCircuit(5, 5)
        qc.h(4)
        qc.cx(4, 3)
        qc.cx(4, 2)
        qc.h([0, 1])
        custom_gate_1 = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]])
        qc.unitary(custom_gate_1, [0, 1, 2, 3, 4])
        qc.h([0, 1])
        qc.x([0, 1])
        qc.h(1)
        qc.cx(0, 1)
        qc.h(1)
        qc.x([0, 1])
        qc.h([0, 1])
        #!!Use a cH gate, only turn Qubits 1 and 0 into a super position if qubit 4 is 1

        #qc.x(0)
        #qc.cswap(0, 1, 2)
        #qc.x([1])
        custom_gate_2 = np.array([[1, 0, 0, 0],
                                  [0, 1, 0, 0],
                                  [0, 0, -1, 0],
                                  [0, 0, 0, 1]])
        #qc.unitary(custom_gate_2, [0, 1])
        #qc.swap(0, 2)
        #qc.swap(1, 3)

        statevector = Statevector.from_instruction(qc)
        print("State Vector:")
        print(statevector)

        qc.measure(0, 0)
        qc.measure(1, 1)
        #qc.measure(2, 2)
        #qc.measure(3, 3)
        #qc.measure(4, 4)
        #qc.measure(5, 5)
        #qc.measure(3, 3)
        print(qc)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)

    #This method tests the controlled hadamard gate
    def gate_tester_18(self):
        qc = QuantumCircuit(2, 2)
        qc.x(0)
        qc.ch(0, 1)
        qc.measure(0, 0)
        qc.measure(1, 1)
        print(qc)
        backend = Aer.get_backend("qasm_simulator")
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit).result()
        counts = job.get_counts()
        print("Measurement results ", counts)





operator = Operations()
operator.simple_adder()
#operator.simple_multiplyer()
#operator.complex_adder()
#operator.even_more_complex_adder()
#operator.gate_tester_18()
print()
#operator.gate_tester_14()


#num1 = input("input binary: ")
#qc.h(0)
#qc.cx(0, 1)
#num2 = input("Number 2:")
#array = num1.split(" ", len(num1) - 1)
#for i in range(len(array)):
#    if int(array[i]) == 1:
#        qc.x(i)
#qc.measure(0, 0)










#qc.draw(output="mpl")
#plt.show()
#zz = Pauli("ZZ")
#zi = Pauli("ZI")
#iz = Pauli("IZ")
#xx = Pauli("XX")
#xi = Pauli("XI")
#ix = Pauli("IX")
#observables = ["ZZ", "ZI", "IZ", "XX", "XI", "IX"]
#Step 2

#Step 3: Execute on the backend
#from qiskit_aer.primitives import Estimator
#estimator = Estimator()
#job = estimator.run([qc] * len(observables), observables)
#print(job.result())

#Step 4
#data = ["ZZ", "ZI", "IZ", "XX", "XI", "IX"]
#values = job.result().values
#plt.plot(data, values, "-o")
#plt.xlabel("Observables")
#plt.ylabel("Expectation values")
#plt.show()