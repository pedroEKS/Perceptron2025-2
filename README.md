# Perceptron

Este repositório contém a resolução da atividade prática da disciplina de Inteligência Artificial da UniBH, focada na implementação e análise do modelo **Perceptron**.


## Questionamento

### 1. Conceito: O que é um Perceptron?

O **Perceptron** é um dos modelos mais antigos e fundamentais de redes neurais, criado por Frank Rosenblatt em 1957. Ele funciona como um classificador binário, aprendendo a dividir dados em duas categorias. Sua importância histórica reside em ter sido o primeiro algoritmo a demonstrar a capacidade de uma máquina aprender com exemplos, abrindo caminho para todo o campo de redes neurais.

### 2. Funcionamento: O que significa ser um classificador linear?

Ser um **classificador linear** significa que o Perceptron só consegue separar dados que podem ser divididos por uma única linha reta. Sua principal limitação é a incapacidade de resolver problemas mais complexos onde os dados não são linearmente separáveis, como a função **XOR**.

### 3. Código: Quais foram as etapas de treinamento?

O processo de treinamento do Perceptron no código envolve quatro etapas principais. Primeiro, os pesos e o viés são iniciados com valores pequenos. Em seguida, o modelo passa por todos os dados de treinamento várias vezes, em ciclos chamados épocas. Para cada dado, a saída é calculada e comparada com o valor esperado. Por fim, se houver erro, os pesos e o viés são ajustados para corrigir a previsão.

### 4. Aplicação Prática: Um exemplo real de uso.

O Perceptron poderia ser usado para uma versão simplificada da **classificação de e-mails como spam ou não-spam**. Ele poderia aprender a classificar e-mails com base em características simples, como o número de palavras-chave ("oferta") ou a contagem de links. Sua simplicidade e eficiência o tornam ideal para problemas onde os dados são bem definidos e linearmente separáveis.
