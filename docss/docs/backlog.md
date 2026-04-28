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
    <tr>
      <td>US 1.1.3</td>
      <td>SHOULD</td>
      <td>Como usuário, quero ativar a autenticação em dois fatores (2FA) para adicionar uma camada extra de segurança à minha conta.</td>
      <td>- Gerar QR Code para app autenticador. <br/> - Exigir o token de 6 dígitos após o login bem-sucedido com senha. <br/> - Opção de ativar/desativar o 2FA nas configurações do sistema.</td>
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
      <td>- Restringir funcionalidades por nível (RBAC). <br/> - Bloquear exclusões para o nível "Estagiário". <br/> - Interface para gerenciar switches de permissão da equipe.</td>
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

## Tema 2: Gestão Jurídica e Integração de APIs

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

### Épico 2.2: Consulta de Processos Judiciais

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
      <td>- Busca por número e por nome retorna resultados relevantes. <br/> - Resultados exibem status, tribunal e partes. <br/> - Componente de auto-complete visual.</td>
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
      <td>COULD</td>
      <td>Como advogado, quero registrar formalmente a autorização do cliente para busca por CPF/CNPJ para cumprir normas de compliance.</td>
      <td>- Campo para upload de termo de autorização ou checkbox de declaração de posse.<br/>- Registro de data/hora em que a autorização foi confirmada.<br/>- Bloquear busca se a autorização não estiver vinculada.</td>
    </tr>
    <tr>
      <td>US 2.2.6</td>
      <td>MUST</td>
      <td>Como advogado, quero calcular prazos processuais em dias úteis com base na movimentação para não perder datas fatais.</td>
      <td>
        - Selecionar tipo de prazo (Ex: Contestação - 15 dias).<br/>
        - Considerar feriados nacionais e suspensões locais.<br/>
        - Exibir data final com destaque visual no modal da calculadora.
      </td>
    </tr>
    <tr>
      <td>US 2.2.7</td>
      <td>COULD</td>
      <td>Como advogado, quero exportar a listagem dos meus processos em formato CSV para realizar análises em planilhas ou backup.</td>
      <td>- Gerar arquivo CSV através da aba de Ajustes.<br/>- Incluir colunas chave: Número, Cliente, Tribunal e Status atual.</td>
    </tr>
  </tbody>
</table>

### Épico 2.3: Gestão Manual de Processos

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
      <td>US 2.3.1</td>
      <td>MUST</td>
      <td>Como advogado, quero cadastrar um processo manualmente informando os dados básicos para gerenciar casos que não constam na busca automática da API.</td>
      <td>- Campos obrigatórios: Número do Processo, Tribunal, Nome das Partes e Data de Início.<br/>- Validar o formato do Número Único CNPJ (20 dígitos).<br/>- O processo cadastrado manualmente deve aparecer na listagem geral.</td>
    </tr>
    <tr>
      <td>US 2.3.2</td>
      <td>MUST</td>
      <td>Como advogado, quero editar os dados de um processo cadastrado manualmente para corrigir informações ou atualizar o status.</td>
      <td>- Permitir alteração de todos os campos preenchidos no cadastro manual.<br/>- Registrar no log de auditoria quem realizou a alteração e em qual data/hora.</td>
    </tr>
    <tr>
      <td>US 2.3.3</td>
      <td>SHOULD</td>
      <td>Como advogado, quero vincular um processo cadastrado manualmente a uma consulta da API posteriormente para que os dados passem a ser atualizados de forma automática.</td>
      <td>- Opção de "Sincronizar com API" dentro dos detalhes do processo manual.<br/>- Sistema deve buscar o número no Jusbrasil e substituir os dados manuais pelos oficiais.</td>
    </tr>
  </tbody>
</table>

### Épico 2.4: Gestão de Demandas Internas (Casos Extrajudiciais)

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
      <td>US 2.4.1</td>
      <td>MUST</td>
      <td>Como advogado, quero visualizar minhas demandas consultivas e internas em um formato Kanban para gerenciar o fluxo de trabalho geral do escritório.</td>
      <td>- Exibir colunas base (Backlog, Em Execução, Revisão, Finalizado).<br/>- Permitir mudança de status movendo os cards entre colunas.<br/>- Cards devem exibir título da demanda, responsável, prioridade e tag de cor.</td>
    </tr>
    <tr>
      <td>US 2.4.2</td>
      <td>MUST</td>
      <td>Como advogado, quero vincular um ou mais Processos Judiciais a um Caso no Kanban para centralizar a documentação e histórico daquele cliente.</td>
      <td>- Interface no detalhe do Caso para buscar e associar um número de processo existente.<br/>- A tela do Processo Judicial deve exibir uma tag indicativa apontando para o Caso raiz.</td>
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
      <td>- Permitir criar, editar e excluir perfis via modal no CMS. <br/> - Campos: nome, especialidade, OAB e e-mail. <br/> - Exibição automática na página pública.</td>
    </tr>
    <tr>
      <td>US 3.1.4</td>
      <td>MUST</td>
      <td>Como administrador, quero publicar artigos e notícias jurídicas para demonstrar autoridade técnica aos visitantes.</td>
      <td>- Editor de texto rico (Markdown/HTML).<br/>- Upload de imagem de capa.<br/>- Botão de "Preview" antes da publicação.</td>
    </tr>
  </tbody>
</table>

### Épico 3.2: Gestão de Contatos (Leads)

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
      <td>Could</td>
      <td>Como visitante, quero enviar uma mensagem pelo formulário de contato para me comunicar com o escritório.</td>
      <td>- Campos obrigatórios (nome, e-mail, telefone, mensagem). <br/> - Validação de dados de entrada. <br/> - Mensagem armazenada na Caixa de Entrada de Leads.</td>
    </tr>
    <tr>
      <td>US 3.2.2</td>
      <td>Could</td>
      <td>Como administrador, quero gerenciar as mensagens recebidas para responder rapidamente aos potenciais clientes.</td>
      <td>- Listar leads em formato de tabela. <br/> - Permitir responder diretamente ou marcar como arquivado.<br/> - Simulação de opacidade reduzida para leads arquivados.</td>
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
      <td>Como advogado, quero que o sistema gere notificações automáticas de eventos e me permita gerenciá-las para que eu acompanhe atualizações importantes.</td>
      <td>- Disparar notificações baseadas em gatilhos (ex: nova movimentação na API). <br/>- Notificações exibidas em dropdown menu no cabeçalho.<br/> - Permitir redirecionamento rápido para o processo ao clicar na notificação.</td>
    </tr>
    <tr>
      <td>US 4.1.2</td>
      <td>SHOULD</td>
      <td>Como usuário, quero gerenciar minhas preferências de notificação para controlar como sou informado.</td>
      <td>- Permitir ativar/desativar notificações via modal de Ajustes. <br/> - Controle individual para 'Alertas de Prazos' e 'Novas Movimentações'. <br/> - Preferências persistidas no perfil do usuário.</td>
    </tr>
  </tbody>
</table>