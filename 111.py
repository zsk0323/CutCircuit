import numpy as np
import qiskit as qk
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

shot = 1000
qr = qk.QuantumRegister(1)
cr = qk.ClassicalRegister(1)
qc = qk.QuantumCircuit(qr, cr)

qc.h(0)
qc.x(0)
qc.measure(0,0)

qc.draw('mpl')
plt.show()

device = qk.Aer.get_backend('qasm_simulator')
job = qk.execute(qc, device, shots=shot)
result = job.result()
ddict = result.get_counts(0)

qubit0 = ddict['0']/shot
qubit1 = ddict['1']/shot
print(qubit0)
print(qubit1)

##############################################

shot1 = 1000
qr1 = qk.QuantumRegister(1)
cr1 = qk.ClassicalRegister(1)
qc1 = qk.QuantumCircuit(qr, cr)

qc1.h(0)
qc1.measure(0,0)

qc1.draw('mpl')
plt.show()

device1 = qk.Aer.get_backend('qasm_simulator')
job1 = qk.execute(qc1, device1, shots=shot1)
result1 = job1.result()
ddict1 = result1.get_counts(0)

qubit01 = ddict1['0']/shot
qubit11 = ddict1['1']/shot
print(qubit01)
print(qubit11)
