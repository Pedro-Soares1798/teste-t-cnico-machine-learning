import subprocess
import sys
import os # Importar 'os'

def run_docker_compose():
    
    # ... (O código de limpeza 'down' e 'up --build' que já te passei) ...
    # O código que funciona deve estar aqui
    
    # 1. Limpeza
    print("--- 1. Tentando derrubar containers antigos ('docker compose down')... ---")
    subprocess.run(["docker", "compose", "down"], timeout=60, stdout=sys.stdout, stderr=sys.stderr)
    
    # 2. Subida
    command = ["docker", "compose", "up", "-d", "--build"]
    print(f"\n--- 2. Iniciando a aplicação: {' '.join(command)} ---")
    
    try:
        subprocess.run(command, check=True, stdout=sys.stdout, stderr=sys.stderr)
        
        print("\n\n✅ SUCESSO! Aplicação Docker Compose iniciada.")
        
    except Exception as e:
        print(f"\n\n❌ ERRO: Falha na execução do Docker Compose. {e}")


if __name__ == "__main__":
    # ESSENCIAL: Garante que o Python está rodando no diretório do script, 
    # para que o docker compose encontre o docker-compose.yml
    os.chdir(os.path.dirname(os.path.abspath(__file__))) 
    run_docker_compose()