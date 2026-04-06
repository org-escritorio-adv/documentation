---
sidebar_position: 2
---

# Backlog do Produto

## Backlog Geral

Nosso backlog é mantido no *Github Projects*, onde especificamos critérios de aceitação e regras de negócio em cada US, além de utilizarmos tags para:

- Identificar a priorização das User Stories (US).
- Identificar a qual funcionalidade ou agrupamento cada US pertence.
- Classificar o nível de granularidade: Tema, Épico ou User Story.

## Tema 1: Autenticação e Segurança

### Épico 1.1: Autenticação e Sessão

<table>
  <thead>
    <tr>
      <th><strong>ID</strong></th>
      <th><strong>Prioridade</strong></th>
      <th><strong>User Story</strong></th>
      <th><strong>Critérios de Aceitação</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>US 1.1.1</td>
      <td>MUST</td>
      <td>Como usuário do sistema, quero realizar login com e-mail e senha para acessar meus dados com segurança.</td>
      <td>- Validar credenciais no banco de dados. <br/> - Impedir acesso com senhas incorretas. <br/> - Redirecionar para o Dashboard após o login.</td>
    </tr>
    <tr>
      <td>US 1.1.2</td>
      <td>MUST</td>
      <td>Como usuário, quero recuperar minha senha via e-mail.</td>
      <td>- Enviar link único para o e-mail cadastrado. <br/> - O link deve expirar após 24h.</td>
    </tr>
  </tbody>
</table>

### Épico 1.2: Permissões e Auditoria

<table>
  <thead>
    <tr>
      <th><strong>ID</strong></th>
      <th><strong>Prioridade</strong></th>
      <th><strong>User Story</strong></th>
      <th><strong>Critérios de Aceitação</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>US 1.2.1</td>
      <td>MUST</td>
      <td>Como administrador, quero definir perfis de acesso (Admin, Advogado, Estagiário).</td>
      <td>- Restringir funcionalidades por nível (RBAC). <br/> - Bloquear exclusões para o nível "Estagiário".</td>
    </tr>
    <tr>
      <td>US 1.2.2</td>
      <td>MUST</td>
      <td>Como advogado, quero um dashboard com resumo e favoritos logo após o login.</td>
      <td>- Exibir processos marcados como favoritos. <br/> - Mostrar resumo de movimentações recentes no painel inicial.</td>
    </tr>
    <tr>
      <td>US 1.2.3</td>
      <td>MUST</td>
      <td>Como gestor, quero visualizar o histórico de alterações dos processos.</td>
      <td>- Registrar Log com: usuário, data, hora e dado alterado. <br/> - O log deve ser imutável.</td>
    </tr>
  </tbody>
</table>

## Tema 2: Integração API Jurídica

### Épico 2.1 Atualização de Dados

<table>
  <thead>
    <tr>
      <th><strong>ID</strong></th>
      <th><strong>Prioridade</strong></th>
      <th><strong>User Story</strong></th>
      <th><strong>Critérios de Aceitação</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>US 2.1.1</td>
      <td>MUST</td>
      <td>Como advogado, quero ser informado quando a API do Jusbrasil estiver indisponível para saber que os dados podem estar desatualizados.</td>
      <td>- Mensagem de erro clara quando API está indisponível. <br/> - Dados anteriores permanecem visíveis com aviso de data. <br/> - Sistema não trava em caso de timeout.</td>
    </tr>
    <tr>
      <td>US 2.1.2</td>
      <td>MUST</td>
      <td>Como advogado, quero que o sistema atualize os processos automaticamente para não precisar fazer isso manualmente todos os dias.</td>
      <td>- Rotina automática executa diariamente. <br/> - Log de execução registrado. <br/> - Notificação gerada em caso de falha.</td>
    </tr>
  </tbody>
</table>

### Épico 2.2: Consulta de Processos

<table >
  <thead>
    <tr>
      <th><strong>ID</strong></th>
      <th><strong>Prioridade</strong></th>
      <th><strong>User Story</strong></th>
      <th><strong>Critérios de Aceitação</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>US 2.2.1</td>
      <td>MUST</td>
      <td>Como advogado, quero buscar processos pelo número ou nome das partes na API do Jusbrasil para encontrar informações rapidamente.</td>
      <td>- Busca por número e por nome retorna resultados relevantes. <br/> - Resultados exibem status, tribunal e partes. <br/> - Busca sem resultados exibe mensagem adequada.</td>
    </tr>
    <tr>
      <td>US 2.2.2</td>
      <td>MUST</td>
      <td>Como advogado, quero consultar processos por CPF/CNPJ para localizar todos os processos de um cliente.</td>
      <td>- Consulta requer autorização prévia registrada no sistema. <br/> - Resultado lista todos os processos vinculados ao documento. <br/> - Dados exibidos em formato legível.</td>
    </tr>
    <tr>
      <td>US 2.2.3</td>
      <td>MUST</td>
      <td>Como advogado, quero visualizar os detalhes completos de um processo para acompanhar seu andamento sem acessar outros sistemas.</td>
      <td>- Detalhes incluem status, movimentações, tribunal e partes. <br/> - Movimentações ordenadas por data, mais recente primeiro. <br/> - Interface responsiva.</td>
    </tr>
    <tr>
    <td>US 2.2.4</td>
    <td>SHOULD</td>
    <td>Como advogado, quero exportar um relatório resumido do processo em PDF para enviar atualizações rápidas aos meus clientes.</td>
    <td>- Gerar PDF com: Número, Status, Últimas 3 movimentações e Tribunal.<br/>- Layout limpo com a logomarca do escritório (se disponível).<br/> - Opção de "Baixar PDF" na tela de detalhes.</td>
    </tr>
    <tr>
      <td>US 2.2.5</td>
      <td>Could</td>
      <td>Como advogado, quero registrar formalmente a autorização do cliente para busca por CPF/CNPJ para cumprir normas de compliance.</td>
      <td>- Campo para upload de termo de autorização ou checkbox de declaração de posse.<br/>- Registro de data/hora em que a autorização foi confirmada.<br/>- Bloquear busca se a autorização não estiver vinculada.</td>
    </tr>
    
  </tbody>
</table>

## Tema 3: Sistema Web — Área Institucional

### Épico 3.1: Gestão de Conteúdo Institucional

<table>
  <thead>
    <tr>
      <th><strong>ID</strong></th>
      <th><strong>Prioridade</strong></th>
      <th><strong>User Story</strong></th>
      <th><strong>Critérios de Aceitação</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>US 3.1.1</td>
      <td>MUST</td>
      <td>Como administrador, quero cadastrar e editar informações institucionais para manter o site atualizado.</td>
      <td>- Permitir criar, editar e excluir conteúdos institucionais. <br/> - Campos: história, missão e valores. <br/> - Alterações refletidas na página pública.</td>
    </tr>
    <tr>
      <td>US 3.1.2</td>
      <td>MUST</td>
      <td>Como administrador, quero gerenciar as áreas de atuação para atualizar os serviços oferecidos.</td>
      <td>- Permitir criar, editar e excluir áreas. <br/> - Cada área possui título e descrição. <br/> - Listagem atualizada automaticamente no site.</td>
    </tr>
    <tr>
      <td>US 3.1.3</td>
      <td>MUST</td>
      <td>Como administrador, quero gerenciar os perfis da equipe de advogados para manter os dados atualizados.</td>
      <td>- Permitir criar, editar e excluir perfis. <br/> - Campos: nome, foto, descrição. <br/> - Exibição automática na página pública.</td>
    </tr>
  </tbody>
</table>

### Épico 3.2: Gestão de Contatos

<table>
  <thead>
    <tr>
      <th><strong>ID</strong></th>
      <th><strong>Prioridade</strong></th>
      <th><strong>User Story</strong></th>
      <th><strong>Critérios de Aceitação</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>US 3.2.1</td>
      <td>MUST</td>
      <td>Como visitante, quero enviar uma mensagem pelo formulário de contato para me comunicar com o escritório.</td>
      <td>- Campos obrigatórios (nome, e-mail, mensagem). <br/> - Validação de dados. <br/> - Mensagem armazenada no sistema.</td>
    </tr>
    <tr>
      <td>US 3.2.2</td>
      <td>MUST</td>
      <td>Como administrador, quero gerenciar as mensagens recebidas para responder aos contatos.</td>
      <td>- Listar mensagens recebidas. <br/> - Visualizar detalhes. <br/> - Permitir marcar como respondida ou excluir.</td>
    </tr>
  </tbody>
</table>

## Tema 4: Notificações

### Épico 4.1: Gestão de Notificações

<table>
  <thead>
    <tr>
      <th><strong>ID</strong></th>
      <th><strong>Prioridade</strong></th>
      <th><strong>User Story</strong></th>
      <th><strong>Critérios de Aceitação</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>US 4.1.1</td>
      <td>MUST</td>
      <td>Como advogado, quero que o sistema gere notificações automáticas de eventos e me permita gerenciá-las para que eu acompanhe atualizações importantes e  mantenha meu histórico organizado.</td>
      <td>- Sistema deve disparar notificações baseadas em gatilhos (ex: nova movimentação na API ou nota interna). <br/>- Notificações devem ser vinculadas ao usuário dono do processo.<br/> - Exibir listagem por ordem cronológica (mais recentes primeiro). <br/>- Permitir que o usuário marque como lida/não lida ou exclua a notificação.</td>
    </tr>
    <tr>
      <td>US 4.1.3</td>
      <td>SHOULD</td>
      <td>Como usuário, quero gerenciar minhas preferências de notificação para controlar como sou informado.</td>
      <td>- Permitir ativar/desativar notificações por tipo de evento. <br/> - Preferências persistidas no perfil do usuário. <br/> - Sistema respeita as configurações definidas.</td>
    </tr>
  </tbody>
</table>
