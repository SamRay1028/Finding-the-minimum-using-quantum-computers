#Step 1
from qiskit import QuantumCircuit
from qiskit.quantum_info import Pauli
import matplotlib.pyplot as plt
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.draw(output="mpl")
plt.show()
zz = Pauli("ZZ")
zi = Pauli("ZI")
iz = Pauli("IZ")
xx = Pauli("XX")
xi = Pauli("XI")
ix = Pauli("IX")
observables = ["ZZ", "ZI", "IZ", "XX", "XI", "IX"]
#Step 2

#Step 3: Execute on the backend
from qiskit_aer.primitives import Estimator
estimator = Estimator()
job = estimator.run([qc] * len(observables), observables)
print(job.result())

#Step 4
data = ["ZZ", "ZI", "IZ", "XX", "XI", "IX"]
values = job.result().values
plt.plot(data, values, "-o")
plt.xlabel("Observables")
plt.ylabel("Expectation values")
plt.show()




