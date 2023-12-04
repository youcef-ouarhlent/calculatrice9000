def calculatrice(num1, operator, num2):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:  # Vérifie si le diviseur n'est pas zéro
            result = num1 / num2
        else:
            return "Division par zéro impossible"
    elif operator == "%":
        result = num1 % num2
    else:
        return "Opérateur non valide"
    
    return f"{num1} {operator} {num2} = {result}"

def afficher_historique(history):
    if not history:
        print("L'historique est vide.")
    else:
        print("Historique des opérations :")
        for index, operation in enumerate(history, start=1):
            print(f"{index}. {operation}")

history = []

while True:
    # Demander à l'utilisateur le type d'opération
    operation = input("Quel type d'opération voulez-vous effectuer (+, -, *, /, %), 'history' pour afficher l'historique ou 'clear' pour supprimer l'historique ? ")

    if operation == 'history':
        afficher_historique(history)
    elif operation == 'clear':
        history = []
        print("L'historique a été effacé.")
    elif operation not in ['+', '-', '*', '/', '%']:
        print("Erreur : Opérateur non valide")
    else:
        try:
            # Demander à l'utilisateur d'entrer le premier nombre
            nombre1 = float(input("Entrez le premier nombre : "))
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide pour le premier nombre")
        else:
            try:
                # Demander à l'utilisateur d'entrer le deuxième nombre
                nombre2 = float(input("Entrez le deuxième nombre : "))
            except ValueError:
                print("Erreur : Veuillez entrer un nombre valide pour le deuxième nombre")
            else:
                # Appeler la fonction calculatrice avec les valeurs entrées par l'utilisateur
                resultat = calculatrice(nombre1, operation, nombre2)

                # Enregistrer l'opération dans l'historique
                operation_str = f"{nombre1} {operation} {nombre2} = {resultat.split('=')[1].strip()}"
                history.append(operation_str)

                # Afficher le résultat
                print(resultat)
            