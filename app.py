# app.py
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

if __name__ == "__main__":
    print("=== Calculadora de IMC ===")
    try:
        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))
        imc = calcular_imc(peso, altura)
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificar_imc(imc)}")
    except ValueError:
        print("Entrada inválida. Digite números válidos.")
