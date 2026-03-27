---
sidebar_position: 3
---

# Requisitos

Listagem dos nossos requisitos

## Requisitos Funcionais

### Sistema Web — Área Institucional (Landing Page)
- **RF01** — O sistema deve apresentar informações institucionais do escritório (história, missão e valores).
- **RF02** — O sistema deve disponibilizar página com as áreas de atuação do escritório.
- **RF03** — O sistema deve exibir a equipe de advogados com seus respectivos perfis.
- **RF04** — O sistema deve disponibilizar formulário de contato para visitantes.
- **RF05** — O sistema deve permitir integração com WhatsApp para contato direto.
- **RF06** — O sistema deve permitir publicação de artigos jurídicos (blog).
- **RF07** — O sistema deve atender às práticas básicas de SEO para indexação em mecanismos de busca.

### Autenticação e Acesso
- **RF08** — O sistema deve permitir autenticação de usuários por login e senha.
- **RF09** — O sistema deve permitir recuperação de senha.
- **RF10** — O sistema deve implementar controle de acesso baseado em perfis de usuário.
- **RF11** — O sistema deve disponibilizar dashboard inicial após login.
- **RF12** — O sistema deve permitir encerramento seguro de sessão (logout).

### Integração com API Jurídica
- **RF13** — O sistema deve integrar-se à API do Jusbrasil.
- **RF14** — O sistema deve permitir consulta de processos pelo número do processo e nome das partes.
- **RF15** — O sistema deve permitir consulta por CPF/CNPJ, quando autorizado.
- **RF16** — O sistema deve exibir informações detalhadas do processo (status, movimentações, tribunal e partes).
- **RF17** — O sistema deve permitir atualização manual dos dados de processos.
- **RF18** — O sistema deve permitir atualização automática dos dados de processos.
- **RF19** — O sistema deve tratar falhas na comunicação com a API (timeout, indisponibilidade, limites de uso).
- **RF20** — O sistema deve possuir uma rotina de consulta periódica aos processos.
- **RF21** — A API deve retornar a integração em formato JSON com codificação UTF-8.

### Gestão de Processos
- **RF22** — O sistema deve permitir cadastro manual de processos.
- **RF23** — O sistema deve permitir vincular processos a clientes.
- **RF24** — O sistema deve permitir registrar anotações internas em processos.
- **RF25** — O sistema deve manter histórico de alterações dos processos.
- **RF26** — O sistema deve permitir marcar processos como favoritos.
- **RF27** — O sistema deve permitir categorização de processos por tags ou categorias.

### Gestão de Clientes
- **RF28** — O sistema deve permitir cadastro de clientes pessoa física e jurídica.
- **RF29** — O sistema deve armazenar dados básicos dos clientes.
- **RF30** — O sistema deve permitir associação entre clientes e processos.
- **RF31** — O sistema deve permitir busca e filtragem de clientes.

### Sistema de Busca
- **RF32** — O sistema deve permitir busca de processos internos.
- **RF33** — O sistema deve permitir busca integrada com dados da API externa.
- **RF34** — O sistema deve permitir aplicação de filtros (status, tribunal, cliente, data).
- **RF35** — O sistema deve permitir ordenação dos resultados de busca.

### Notificações
- **RF36** — O sistema deve notificar usuários sobre atualizações em processos.
- **RF37** — O sistema deve disponibilizar notificações internas no sistema.
- **RF38** — O sistema deve permitir envio de notificações por e-mail (opcional).

### Dashboard e Indicadores
- **RF39** — O sistema deve exibir quantidade de processos ativos.
- **RF40** — O sistema deve exibir processos agrupados por status.
- **RF41** — O sistema deve exibir atividades recentes.
- **RF42** — O sistema deve apresentar indicadores básicos de produtividade.
- **RF43** — O sistema deve possuir uma rotina diária de atualização do dashboard.

---

## Requisitos Não-Funcionais

### Segurança e Conformidade
- **RNF01** — O sistema deve armazenar senhas de forma criptografada.
- **RNF02** — O sistema deve controlar sessões de usuários.
- **RNF03** — O sistema deve proteger o acesso a dados restritos.
- **RNF04** — O sistema deve estar em conformidade com a LGPD.
- **RNF05** — O sistema deve registrar logs de acesso e ações dos usuários.
- **RNF06** — O sistema deve possuir mecanismo de backup de dados.

### Infraestrutura e Arquitetura
- **RNF07** — O sistema deve utilizar containerização com Docker.
- **RNF08** — O sistema deve possuir arquitetura definida (monolítica ou baseada em microsserviços).
- **RNF09** — O sistema deve possuir serviço de autenticação desacoplado.
- **RNF10** — O sistema deve utilizar banco de dados relacional.
- **RNF11** — O sistema deve possuir ambientes distintos (desenvolvimento, homologação e produção).

### UX/UI
- **RNF16** — O sistema deve ser responsivo para diferentes dispositivos.
- **RNF17** — O sistema deve seguir boas práticas de usabilidade.
