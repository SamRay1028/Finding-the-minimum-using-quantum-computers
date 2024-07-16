# Finding-the-minimum-using-quantum-computers

Description:
The ultimate goal of this code is to develop a means of finding the maximum (or minimum) value produced by a function utilizing grover's algorithm. The method "simple_adder" currently being tested on is a simple adder where by the values of two qubits are added together. These two qubits are put into a superposition of states which can be expressed by the state vector, 
(1/2)(|00> + |01> + |10> +|11>). This superposition of states is then fed through a series of gates that add the value of the two qubits together and produce a sum that is displayed via two other qubits. The goal is to take advantage of quantum superposition and entanglement in order to create a means by which a max (or min) value can be found amoung the possible output values. The ultimate goal is to apply such an algorithm to the training of neural networks by setting the learning rate into a superposition of states and then using this hypothetical algorithm to find the lowest cost.

## References
- Qiskit: An open-source quantum computing framework by IBM. For more information, visit [Qiskit Documentation](https://qiskit.org/documentation/).

## Acknowledgments
1. This project uses Qiskit, an open-source quantum computing framework by IBM. For more information on Qiskit, visit [https://qiskit.org](https://qiskit.org).
2. This project uses code from "Hello World | Coding with Qiskit 1.x | Programming on Quantum Computers", a video on the official Qiskit Youtube channel. Link for the video: https://www.youtube.com/watch?v=93-zLTppFZw&t=855s

License: This project is licensed under the MIT license - see the LICENSE file for details.
