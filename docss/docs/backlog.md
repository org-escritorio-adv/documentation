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
  </tbody>
</table>
