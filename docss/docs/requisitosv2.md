---
sidebar_position: 3
---
# Documento de Especificação de Requisitos - Sistema Jurídico

## **Lista de Requisitos**

<p style={{textAlign: 'justify'}}>A seguir, apresenta-se a lista detalhada dos requisitos do projeto, dividida entre requisitos funcionais e não funcionais. Esta organização visa garantir a rastreabilidade das funcionalidades centrais do escritório e assegurar que os padrões técnicos de segurança e performance sejam atingidos.</p>

## **Tabela de Requisitos Funcionais**

<table border="1">
  <thead style={{backgroundColor: '#24f072', color: 'white'}}>
    <tr>
      <th><strong>Objetivo Específico</strong></th>
      <th><strong>Código</strong></th>
      <th><strong>Requisito</strong></th>
      <th><strong>Descrição</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowSpan="5">Autenticação e Acesso (Base)</td>
      <td>RF1.1</td>
      <td>Autenticação de usuários</td>
      <td>O sistema deve permitir a autenticação segura de usuários mediante fornecimento de login e senha.</td>
    </tr>
    <tr>
      <td>RF1.2</td>
      <td>Recuperação de senha</td>
      <td>O sistema deve permitir que o usuário solicite a recuperação de sua credencial de acesso via e-mail.</td>
    </tr>
    <tr>
      <td>RF1.3</td>
      <td>Controle de perfis (RBAC)</td>
      <td>O sistema deve implementar controle de acesso baseado em níveis (Admin, Advogado, Estagiário).</td>
    </tr>
    <tr>
      <td>RF1.4</td>
      <td>Dashboard inicial</td>
      <td>O sistema deve disponibilizar um painel de controle com resumo de dados logo após a autenticação.</td>
    </tr>
    <tr>
      <td>RF1.5</td>
      <td>Logout seguro</td>
      <td>O sistema deve garantir o encerramento seguro da sessão (logout), invalidando os tokens ativos.</td>
    </tr>
    <tr>
      <td rowSpan="9">Cadastro e Gestão de Clientes e Processos</td>
      <td>RF2.1</td>
      <td>Cadastro manual de processos</td>
      <td>Permitir que o usuário insira manualmente novos processos no banco de dados local.</td>
    </tr>
    <tr>
      <td>RF2.2</td>
      <td>Vínculo Cliente-Processo</td>
      <td>O sistema deve permitir associar um processo a um ou mais clientes cadastrados na base.</td>
    </tr>
    <tr>
      <td>RF2.3</td>
      <td>Anotações internas</td>
      <td>Permitir o registro de notas e observações estratégicas dentro da ficha de cada processo.</td>
    </tr>
    <tr>
      <td>RF2.4</td>
      <td>Histórico de alterações</td>
      <td>O sistema deve manter um log detalhado de todas as modificações realizadas nos dados dos processos.</td>
    </tr>
    <tr>
      <td>RF2.5</td>
      <td>Categorização e Tags</td>
      <td>Permitir a organização de processos através de etiquetas personalizadas (ex: Urgente, Inicial).</td>
    </tr>
    <tr>
      <td>RF2.6</td>
      <td>Cadastro de PF e PJ</td>
      <td>O sistema deve permitir o cadastro detalhado de clientes pessoa física e jurídica.</td>
    </tr>
    <tr>
      <td>RF2.7</td>
      <td>Armazenamento de dados</td>
      <td>Garantir a persistência de informações de contato, endereço e documentos básicos dos clientes.</td>
    </tr>
    <tr>
      <td>RF2.8</td>
      <td>Busca e filtragem</td>
      <td>Permitir a localização rápida de clientes através de filtros de nome, documento ou status.</td>
    </tr>
    <tr>
      <td>RF2.9</td>
      <td>Favoritos</td>
      <td>Permitir que o usuário marque processos específicos como favoritos para acesso rápido.</td>
    </tr>
    <tr>
      <td rowSpan="12">Acompanhamento do Status Processual (API)</td>
      <td>RF3.1</td>
      <td>Integração Jusbrasil</td>
      <td>O sistema deve integrar-se tecnicamente à API do Jusbrasil para consumo de dados públicos.</td>
    </tr>
    <tr>
      <td>RF3.2</td>
      <td>Consulta por número/partes</td>
      <td>Permitir a busca de processos externos informando o número da ação ou nome dos envolvidos.</td>
    </tr>
    <tr>
      <td>RF3.3</td>
      <td>Consulta por CPF/CNPJ</td>
      <td>Permitir o rastreamento de processos vinculados a um documento específico, quando autorizado.</td>
    </tr>
    <tr>
      <td>RF3.4</td>
      <td>Atualização manual</td>
      <td>Disponibilizar botão para que o usuário force a sincronização de um processo com o tribunal.</td>
    </tr>
    <tr>
      <td>RF3.5</td>
      <td>Atualização automática</td>
      <td>O sistema deve possuir rotina automatizada para atualizar dados processuais sem intervenção.</td>
    </tr>
    <tr>
      <td>RF3.6</td>
      <td>Tratamento de falhas</td>
      <td>O sistema deve gerenciar erros de API (timeout, indisponibilidade) sem interromper a operação.</td>
    </tr>
    <tr>
      <td>RF3.7</td>
      <td>Varredura periódica</td>
      <td>Implementar rotina (Cron Job) para consulta recorrente de novos andamentos nos tribunais.</td>
    </tr>
    <tr>
      <td>RF3.8</td>
      <td>Formato de dados (JSON)</td>
      <td>A integração deve processar dados em formato JSON com codificação de caracteres UTF-8.</td>
    </tr>
    <tr>
      <td>RF3.9</td>
      <td>Busca integrada</td>
      <td>Permitir busca que cruze dados do banco local com informações em tempo real da API externa.</td>
    </tr>
    <tr>
      <td>RF3.10</td>
      <td>Filtros de busca</td>
      <td>Permitir filtrar resultados por tribunal, status, cliente ou intervalo de datas.</td>
    </tr>
    <tr>
      <td>RF3.11</td>
      <td>Ordenação de resultados</td>
      <td>Permitir que o usuário ordene as buscas por relevância ou data de movimentação.</td>
    </tr>
    <tr>
      <td>RF3.12</td>
      <td>Informações detalhadas</td>
      <td>Exibir status, movimentações completas, vara, tribunal e partes de cada processo.</td>
    </tr>
    <tr>
      <td rowSpan="4">Agenda Jurídica e Alertas</td>
      <td>RF4.1</td>
      <td>Notificação de atualização</td>
      <td>Notificar o usuário imediatamente sobre qualquer nova movimentação detectada em seus processos.</td>
    </tr>
    <tr>
      <td>RF4.2</td>
      <td>Alertas internos</td>
      <td>Disponibilizar uma central de notificações dentro da interface do sistema.</td>
    </tr>
    <tr>
      <td>RF4.3</td>
      <td>Notificação por E-mail</td>
      <td>Permitir o envio opcional de avisos de prazos e movimentações para o e-mail do advogado.</td>
    </tr>
    <tr>
      <td>RF4.4</td>
      <td>Atividades recentes</td>
      <td>Exibir um log visual das últimas interações e andamentos no dashboard do usuário.</td>
    </tr>
    <tr>
      <td rowSpan="5">Controle de Honorários e Indicadores</td>
      <td>RF5.1</td>
      <td>Contagem de ativos</td>
      <td>Exibir de forma gráfica ou numérica a quantidade total de processos ativos no escritório.</td>
    </tr>
    <tr>
      <td>RF5.2</td>
      <td>Agrupamento por status</td>
      <td>Apresentar a distribuição dos processos de acordo com sua fase atual (Execução, Inicial, etc).</td>
    </tr>
    <tr>
      <td>RF5.3</td>
      <td>Indicadores de produtividade</td>
      <td>Apresentar métricas de desempenho baseadas em processos encerrados e novos prazos cumpridos.</td>
    </tr>
    <tr>
      <td>RF5.4</td>
      <td>Atualização de BI</td>
      <td>O sistema deve possuir rotina diária para processar e atualizar os dados do dashboard.</td>
    </tr>
    <tr>
      <td>RF5.5</td>
      <td>Gestão de Custas</td>
      <td>Funcionalidade para acompanhamento básico de honorários e despesas processuais vinculadas.</td>
    </tr>
    <tr>
      <td rowSpan="7">Portal de Acesso ao Cliente e Institucional</td>
      <td>RF6.1</td>
      <td>Area Institucional</td>
      <td>Apresentar história, missão e valores do escritório em uma página pública (Landing Page).</td>
    </tr>
    <tr>
      <td>RF6.2</td>
      <td>Areas de atuação</td>
      <td>Exibir as especialidades jurídicas atendidas pelo escritório de forma detalhada.</td>
    </tr>
    <tr>
      <td>RF6.3</td>
      <td>Perfil da Equipe</td>
      <td>Disponibilizar os perfis profissionais e áreas de foco de cada advogado da equipe.</td>
    </tr>
    <tr>
      <td>RF6.4</td>
      <td>Formulário de contato</td>
      <td>Permitir que visitantes enviem mensagens de interesse diretamente pelo site.</td>
    </tr>
    <tr>
      <td>RF6.5</td>
      <td>Integração WhatsApp</td>
      <td>Disponibilizar botão flutuante para contato direto via WhatsApp institucional.</td>
    </tr>
    <tr>
      <td>RF6.6</td>
      <td>Blog Juridico</td>
      <td>Permitir a publicação de artigos e notícias jurídicas para engajamento de clientes.</td>
    </tr>
    <tr>
      <td>RF6.7</td>
      <td>Otimização SEO</td>
      <td>A área institucional deve seguir práticas de indexação para mecanismos de busca.</td>
    </tr>
  </tbody>
</table>

## **Tabela de Requisitos Não Funcionais**

<table border="1">
  <thead style={{backgroundColor: '#24f072', color: 'white'}}>
    <tr>
      <th><strong>Código</strong></th>
      <th><strong>Requisito Não Funcional</strong></th>
      <th><strong>Descrição</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RNF01</td>
      <td>Segurança (Hashing)</td>
      <td>O sistema deve armazenar senhas de forma criptografada utilizando algoritmos de hashing robustos (ex: Argon2 ou BCrypt) para prevenir vazamentos.</td>
    </tr>
    <tr>
      <td>RNF02</td>
      <td>Gestão de Sessão</td>
      <td>O sistema deve controlar as sessões de usuários via tokens seguros, garantindo a expiração por inatividade e prevenção de ataques de sequestro de sessão.</td>
    </tr>
    <tr>
      <td>RNF03</td>
      <td>Sigilo de Dados</td>
      <td>O sistema deve garantir a proteção e o controle de acesso estrito a dados restritos e documentos em segredo de justiça.</td>
    </tr>
    <tr>
      <td>RNF04</td>
      <td>Conformidade LGPD</td>
      <td>O tratamento de dados pessoais de clientes e usuários deve seguir estritamente as diretrizes da Lei Geral de Proteção de Dados (LGPD).</td>
    </tr>
    <tr>
      <td>RNF05</td>
      <td>Rastreabilidade (Logs)</td>
      <td>O sistema deve registrar logs detalhados de acesso e de todas as ações críticas realizadas pelos usuários para fins de auditoria.</td>
    </tr>
    <tr>
      <td>RNF06</td>
      <td>Resiliência (Backup)</td>
      <td>O sistema deve possuir um mecanismo de backup automatizado para garantir a recuperação de dados em caso de falha crítica do servidor.</td>
    </tr>
    <tr>
      <td>RNF07</td>
      <td>Containerização</td>
      <td>O sistema deve ser desenvolvido e implantado utilizando Docker para garantir a consistência entre ambientes de dev e produção.</td>
    </tr>
    <tr>
      <td>RNF08</td>
      <td>Arquitetura</td>
      <td>O sistema deve possuir uma arquitetura definida e documentada (monolítica modular ou microsserviços), visando manutenibilidade.</td>
    </tr>
    <tr>
      <td>RNF09</td>
      <td>Desacoplamento</td>
      <td>O serviço de autenticação deve ser desacoplado das regras de negócio principais para facilitar integrações e segurança.</td>
    </tr>
    <tr>
      <td>RNF10</td>
      <td>Banco de Dados</td>
      <td>Utilização de SGBD Relacional (SQL) para garantir a integridade dos dados via chaves estrangeiras e suporte a transações ACID complexas.</td>
    </tr>
    <tr>
      <td>RNF11</td>
      <td>Paridade de Ambientes</td>
      <td>O sistema deve operar em ambientes distintos (Desenvolvimento, Homologação e Produção) com configurações isoladas.</td>
    </tr>
    <tr>
      <td>RNF12</td>
      <td>Responsividade (UX)</td>
      <td>A interface do usuário deve ser responsiva, adaptando-se a diferentes tamanhos de tela (desktop, tablets e smartphones).</td>
    </tr>
    <tr>
      <td>RNF13</td>
      <td>Usabilidade</td>
      <td>O sistema deve seguir boas práticas de IHC (Interação Humano-Computador) para minimizar a curva de aprendizado dos advogados.</td>
    </tr>
  </tbody>
</table>