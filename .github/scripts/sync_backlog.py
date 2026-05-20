import os
import re
import subprocess

BACKLOG_FILE = 'docss/docs/backlog.md'

def get_existing_issues():
    """Busca as issues já existentes para evitar duplicação."""
    try:
        # Adicionado limite de 1000 para garantir que pega todo o histórico
        result = subprocess.run(
            ['gh', 'issue', 'list', '--state', 'all', '--limit', '1000', '--json', 'title', '--jq', '.[].title'],
            capture_output=True, text=True, check=True
        )
        return set(result.stdout.strip().split('\n'))
    except subprocess.CalledProcessError:
        return set()

def create_issue(title, body, label):
    """Cria a issue usando o GitHub CLI (gh)."""
    print(f"Criando issue: {title} com label '{label}'")
    try:
        subprocess.run([
            'gh', 'issue', 'create',
            '--title', title,
            '--body', body,
            '--label', label
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao criar a issue '{title}': {e}")

def clean_html(text):
    """Limpa as tags HTML e ajusta as quebras de linha para Markdown."""
    # Troca <br> e <br/> por quebras de linha reais
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    # Remove qualquer outra tag HTML que sobrar
    text = re.sub(r'<[^>]+>', '', text)
    return text.strip()

def main():
    if not os.path.exists(BACKLOG_FILE):
        print(f"Arquivo {BACKLOG_FILE} não encontrado.")
        return

    existing_issues = get_existing_issues()
    
    with open(BACKLOG_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # ==========================================
    # 1. EXTRAIR TEMAS E ÉPICOS
    # ==========================================
    tema_pattern = re.compile(r'(Tema\s+\d+.*)', re.IGNORECASE)
    epico_pattern = re.compile(r'(Épico\s+\d+\.\d+.*)', re.IGNORECASE)
    
    # Lemos o arquivo linha por linha para os temas e épicos
    for line in content.split('\n'):
        line = line.strip()
        if not line:
            continue

        tema_match = tema_pattern.search(line)
        epico_match = epico_pattern.search(line)

        title = None
        label = None

        if tema_match:
            title = tema_match.group(1).strip()
            label = "tema"
        elif epico_match:
            title = epico_match.group(1).strip()
            label = "épico"
        
        if title and title not in existing_issues:
            body = f"Gerado automaticamente a partir do backlog.\n\n**Origem:** {label.capitalize()}"
            create_issue(title, body, label)
        elif title in existing_issues:
            print(f"Issue já existe, ignorando: {title}")

    # ==========================================
    # 2. EXTRAIR USER STORIES DAS TABELAS HTML
    # ==========================================
    # Expressão que pega as 4 colunas de dentro da tag <tr>, ignorando quebras de linha
    tr_pattern = re.compile(
        r'<tr>\s*<td>(.*?)<\/td>\s*<td>(.*?)<\/td>\s*<td>(.*?)<\/td>\s*<td>(.*?)<\/td>\s*<\/tr>', 
        re.DOTALL | re.IGNORECASE
    )

    for match in tr_pattern.finditer(content):
        us_id = clean_html(match.group(1))
        prioridade = clean_html(match.group(2))
        historia = clean_html(match.group(3))
        criterios = clean_html(match.group(4))

        # Ignora linhas que não começam com "US" (como possíveis cabeçalhos de tabela esquecidos)
        if not us_id.upper().startswith("US"):
            continue

        # Monta o título completo. Ex: "US 1.1.1: Como usuário do sistema..."
        title = f"{us_id}: {historia}"
        
        # Limita o tamanho do título para evitar rejeição da API do GitHub
        if len(title) > 200:
            title = title[:197] + "..."

        # Monta o corpo da Issue detalhadinho em Markdown
        body = (
            f"**Prioridade:** {prioridade}\n\n"
            f"**Critérios de Aceitação:**\n{criterios}\n\n"
            f"---\n*Gerado automaticamente a partir do backlog.*"
        )
        label = "user story"

        # Cria ou ignora se já existe
        if title and title not in existing_issues:
            create_issue(title, body, label)
        elif title in existing_issues:
            print(f"Issue já existe, ignorando: {title}")

if __name__ == '__main__':
    main()
