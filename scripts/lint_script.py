import subprocess

# Exécutez flake8 et capturez la sortie
result = subprocess.run(['flake8'], capture_output=True, text=True)
output = result.stdout + result.stderr

# Enregistrez la sortie dans un fichier
with open('flake8_errors.txt', 'w') as file:
    file.write(output)
