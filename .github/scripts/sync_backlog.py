import os
import re
import subprocess

BACKLOG_FILE = 'backlog.md'

def get_existing_issues():
    """Busca as issues já existentes para evitar duplicação."""
    try:
        result = subprocess.run(
            ['gh', 'issue', 'list', '--state', 'all', '--json', 'title', '--jq', '.[].title'],
            capture_output=True, text=True, check=True
        )
        return set(result.stdout.strip().split('\n'))
    except subprocess.CalledProcessError:
        return set()

def create_issue(title, label):
    """Cria a issue usando o GitHub CLI (gh)."""
    print(f"Criando issue: {title} com label '{label}'")
    try:
        subprocess.run([
            'gh', 'issue', 'create',
            '--title', title,
            '--body', f"Gerado automaticamente a partir do backlog.\n\n**Origem:** {label.capitalize()}",
            '--label', label
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao criar a issue '{title}': {e}")

def main():
    if not os.path.exists(BACKLOG_FILE):
        print(f"Arquivo {BACKLOG_FILE} não encontrado.")
        return

    existing_issues = get_existing_issues()
    
    with open(BACKLOG_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Expressões regulares para identificar as hierarquias
    tema_pattern = re.compile(r'^(Tema\s+\d+.*)')
    epico_pattern = re.compile(r'^(Épico\s+\d+\.\d+.*)')

    for line in lines:
        line = line.strip()
        if not line:
            continue

        title = None
        label = None

        # Identifica e mapeia a palavra-chave inicial para a flag --label correspondente
        if tema_pattern.match(line):
            title = line
            label = "tema"
        elif epico_pattern.match(line):
            title = line
            label = "épico"
        
        # Se encontrou um padrão válido e a issue ainda não existe no repositório
        if title and title not in existing_issues:
            create_issue(title, label)
        elif title in existing_issues:
            print(f"Issue já existe, ignorando: {title}")

if __name__ == '__main__':
    main()
