def bmi(weight, height):
    imc = weight / (height * height)

    if imc <= 18.5: 
        return "Underweight"
    if imc <= 25.0: 
        return "Normal"
    if imc <= 30.0: 
        return "Overweight"
    else: 
        return "Obese"
