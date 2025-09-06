def perceptron_input(inputs, weights, bias):
    """
    Calculate the perceptron input.
    :param inputs: List of input values
    :param weights: List of weights corresponding to the inputs
    :param bias: Bias value
    :return: The result of the weighted sum of inputs plus the bias
    """
    if len(inputs) != len(weights):
        raise ValueError("As listas de entradas e pesos devem ter o mesmo tamanho.")
    weighted_sum = sum(i * w for i, w in zip(inputs, weights))
    return weighted_sum + bias

def perceptron_output(inputs, weights, bias):
    """
    Calculate the perceptron output.
    :param inputs: List of input values
    :param weights: List of weights corresponding to the inputs
    :param bias: Bias value
    :return: The output of the perceptron
    """
    return 1 if perceptron_input(inputs, weights, bias) >= 0 else 0

def main():
    print("Hello, World!")
    print("This is the main file.")
    print("O resultado do perceptron com valores fixos é:", perceptron_input([1, 2, 3], [0.1, 0.2, 0.3], 0.4))

    entrada = list(map(float, input("Digite as entradas separadas por espaço: (x) ").split()))
    pesos = list(map(float, input("Digite os pesos separados por espaço: (w) ").split()))
    bias = float(input("Digite o viés (b): "))

    resultado = perceptron_input(entrada, pesos, bias)
    saida = perceptron_output(entrada, pesos, bias)
    print(f"Entradas: {entrada}")
    print(f"Pesos: {pesos}")
    print(f"Viés (b): {bias}")
    print(f"Resultado do Perceptron (soma ponderada + viés): {resultado}")
    print(f"Saída do Perceptron (após função degrau): {saida}")

if __name__ == "__main__":
    main()