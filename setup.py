# setup.py

import subprocess

def install_requirements():
    print("📦 Instalando requerimientos desde requirements.txt …")
    subprocess.run(["pip", "install", "-q", "-r", "requirements.txt"], check=True)
    print("✅ Dependencias instaladas correctamente.")

if __name__ == "__main__":
    install_requirements()
