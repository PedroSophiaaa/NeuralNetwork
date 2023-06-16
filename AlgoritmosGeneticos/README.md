# 🧬 Experimentos de otimização e algoritmos genéticos

Essa pasta contém os experimentos que utilizam *algorítmos genéticos* como estratégia de resolução. Os arquivos estão descritos abaixo:

### Organização dos arquivos

Os experimentos são arquivos `.ipynb`, cujo nome segue o padrão definido pelo professor que minitra o curso.

<details><summary>Experimentos desenvolvidos em aula</summary><br>

<a href="https://github.com/PedroSophiaaa/NeuralNetwork/blob/main/AlgoritmosGeneticos/experimento%20A.01%20-%20busca%20aleatoria.ipynb">Experimento A.01</a> - O **experimento A.01** é introdutório à estratégia de algoritmos genéticos, tratando a questão da busca aleatória no problema das caixas binárias. O algoritmo não resolve o problema;

<a href="https://github.com/PedroSophiaaa/NeuralNetwork/blob/main/AlgoritmosGeneticos/experimento%20A.02%20-%20busca%20em%20grade.ipynb"> Experimento A.02</a> - O **experimento A.02** mostra outra maneira de resolução do problema das caixas binárias - a busca em grade por produto cartesiano. Esse experimento também ocorre de maneira introdutória;

<a href="https://github.com/PedroSophiaaa/NeuralNetwork/blob/main/AlgoritmosGeneticos/experimento%20A.03%20-%20algoritmo%20genetico.ipynb"> Experimento A.03</a> - O **experimento A.03** resolve o problema das caixas binárias, com utilização de um algoritmo genético, utilizando conceitos de `gene`, `indivíduo`, `população`, `seleção`, `mutação` e `cruzamento`;

<a href="https://github.com/PedroSophiaaa/NeuralNetwork/blob/main/AlgoritmosGeneticos/experimento%20A.04%20-%20caixas%20nao-binarias.ipynb"> Experimento A.04</a> - O **experimento A.04** resolve o problema das caixas não binárias, utilizando uma estratégia extremamente semelhante com o **experimento A.03**;

<a href="https://github.com/PedroSophiaaa/NeuralNetwork/blob/main/AlgoritmosGeneticos/experimento%20A.05%20-%20descobrindo%20a%20senha.ipynb">Experimento A.05</a> - O **experimento A.05** resolve o problema de minimização de descoberta de senha, onde o algoritmo deve encontrar uma senha (de tamanho definido e conhecida);

<a href="https://github.com/PedroSophiaaa/NeuralNetwork/blob/main/AlgoritmosGeneticos/experimento%20A.06%20-%20o%20caixeiro%20viajante.ipynb">Experimento A.06</a> - O **experimento A.06** é um experimento do tipo NP difícil conhecido como **Caixeiro Viajante**. É um problema de minimização, onde se busca encontrar o menor caminho que passe por todos os pontos de um grafo conhecido;

<a href="https://github.com/PedroSophiaaa/NeuralNetwork/blob/main/AlgoritmosGeneticos/experimento%20A.07%20-%20aplicando%20restricoes.ipynb">Experimento A.07</a> - O **experimento A.07** é um experimento de maximização com restrição, também do tipo NP difícil, conhecido como **Problema da mochila**. O código deve encontrar o conjunto de itens mais valioso com restrição de peso.

</details>


<details><summary>Experimentos da lista de exercícios</summary><br>

<a href="https://github.com/PedroSophiaaa/NeuralNetwork/blob/main/AlgoritmosGeneticos/experimento%20GA.01%20-%20senha%20de%20tamanho%20variavel.ipynb">Experimento GA.01 - Senha de tamanho variável</a> - Esse experimento é semelhante ao **experimento A.05**, porém o tamanho da senha não é fornecido ao algoritmo, sendo assim, a *fitness function* deve considerar o tamanho da *string*, e a função de *crossover* e de mutação também.

</details>

Cada arquivo apresenta uma conclusão sobre o experimento apresentado.

Em `funcoes.py` temos as funções utilizadas nos experimentos. 📚

### O que são algoritmos genéticos?
Utilizando conceitos da evolução **Darwiniana** e da **genealogia**, como herança, mutações e cromossomos, o algoritmo é pensado de maneira a solucionar problemas, complexos ou não, gerando uma *população* de *indivíduos* válidos e evoluindo-os com o passar das *gerações*, sendo assim, o algoritmo deve ser capaz de selecionar os melhores *indivíduos* de uma *população*, de acordo com uma **função de objetivo** definida.  
Os algoritmos genéticos podem resolver problemas complexos (como problemas **NP difíceis**) evitando o uso de estratégias custosas computacionalmente, como busca em grade por produto cartesiano ou outra estratégia de força bruta.

Fique à vontade para explorar e experimentar com os códigos! 💻