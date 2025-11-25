# Script para automatizar commit y push

# Asegúrate de que el primer argumento ($args[0]) contenga un mensaje
if ($args[0] -eq $null) {
    Write-Host "Error: Debes proporcionar un mensaje para el commit. Ejemplo: .\commit.ps1 'Mi mensaje'"
    exit 1
}

git add .
git commit -m "$args[0]"
git push
