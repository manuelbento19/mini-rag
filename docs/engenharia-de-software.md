# Engenharia de Software: metodologias, métodos e práticas

Este documento é uma matéria de estudo sobre engenharia de software. Ele serve como fonte de conhecimento para o Mini-RAG: o texto será dividido em chunks, convertido em embeddings e usado nas buscas.

## O que é engenharia de software

Engenharia de software é a aplicação de abordagens sistemáticas, disciplinadas e quantificáveis para desenvolver, operar e manter software. O objetivo é produzir sistemas confiáveis, dentro de prazo e custo previstos, com qualidade suficiente para os usuários.

Não se resume a escrever código. Envolve requisitos, arquitetura, testes, documentação, entrega, manutenção e trabalho em equipe.

### Diferença entre método, metodologia e framework

- **Método:** um conjunto de passos e técnicas para realizar uma atividade. Exemplo: escrever testes antes do código.
- **Metodologia:** uma abordagem geral que organiza o processo de desenvolvimento, definindo fases, papéis e entregas. Exemplo: Scrum.
- **Framework:** uma estrutura concreta que implementa uma metodologia, com regras e práticas mais específicas. Exemplo: SAFe, uma versão escalada do Scrum.

Na prática, esses termos são usados de forma intercambiável, mas a distinção ajuda a evitar confusão: o método é a técnica, a metodologia é o processo e o framework é a implementação do processo.

## Ciclo de vida do desenvolvimento de software

O ciclo de vida descreve as etapas pelas quais um sistema passa desde a ideia até a desativação.

1. **Requisitos:** entender o que o usuário precisa.
2. **Projeto e arquitetura:** decidir como o sistema será estruturado.
3. **Implementação:** escrever o código.
4. **Testes:** verificar se o sistema funciona como esperado.
5. **Entrega:** disponibilizar o software para uso.
6. **Operação e manutenção:** acompanhar, corrigir e evoluir o sistema.

Modelos de ciclo de vida definem como essas etapas se relacionam. Uns são sequenciais, outros são iterativos e incrementais.

## Metodologias de desenvolvimento

### Modelo Cascata

O modelo Cascata, ou *Waterfall*, organiza as fases de forma sequencial: cada etapa só começa quando a anterior termina e é aprovada.

Vantagens:

- fácil de entender e gerenciar;
- documentação abundante;
- adequado para projetos com requisitos estáveis e regulados.

Desvantagens:

- mudanças tardias são caras;
- o cliente só vê o produto ao final;
- risco alto de entregar algo desatualizado.

### Modelo iterativo e incremental

No modelo iterativo, o projeto avança em ciclos curtos. Em cada iteração, a equipe planeja, executa, testa e avalia. A versão incremental significa que o sistema cresce aos poucos, com entregas parciais funcionais.

A combinação reduz risco: erros são descobertos cedo e o cliente pode ajustar prioridades entre iterações.

### Scrum

Scrum é um framework ágil baseado em iterações chamadas *sprints*, normalmente de uma a quatro semanas.

Papéis:

- **Product Owner:** prioriza o backlog e representa o valor de negócio.
- **Scrum Master:** facilita o processo e remove impedimentos.
- **Time de Desenvolvimento:** profissionais que entregam o incremento.

Eventos:

- **Sprint:** o intervalo de trabalho propriamente dito.
- **Planejamento da Sprint:** define o objetivo e quais itens serão feitos.
- **Daily Scrum:** reunião curta de sincronização do time.
- **Revisão da Sprint:** demonstração do incremento para partes interessadas.
- **Retrospectiva:** reflexão sobre o processo e melhorias.

Artefatos:

- **Product Backlog:** lista priorizada de necessidades.
- **Sprint Backlog:** itens selecionados para a sprint.
- **Incremento:** a versão utilizável ao final da sprint.

### Kanban

Kanban foca no fluxo de trabalho contínuo, em vez de sprints. O quadro Kanban normalmente tem colunas como "A fazer", "Em andamento", "Em revisão" e "Concluído".

Princípios principais:

- visualizar o fluxo;
- limitar o trabalho em andamento (*WIP*);
- gerenciar o fluxo;
- tornar políticas explícitas;
- melhorar continuamente.

Métricas comuns incluem *lead time* (tempo total da entrada até a saída) e *cycle time* (tempo entre o início e o fim do trabalho).

### Extreme Programming

Extreme Programming, ou XP, é uma metodologia ágil centrada em práticas de engenharia. Entre elas:

- **Programação em par:** duas pessoas trabalham juntas em um computador.
- **TDD:** desenvolvimento orientado a testes.
- **Integração contínua:** integrar o código várias vezes ao dia.
- **Refatoração:** melhorar a estrutura sem mudar o comportamento.
- **Propriedade coletiva do código:** qualquer pessoa pode alterar qualquer parte.
- **Entregas pequenas e frequentes.**

### Lean

Lean vem da manufatura enxuta e foi adaptado ao software. A ideia central é maximizar valor e minimizar desperdício.

Sete desperdícios típicos no desenvolvimento de software:

1. trabalho parcialmente feito;
2. retrabalho;
3. tarefas desnecessárias;
4. troca frequente de contexto;
5. esperas e bloqueios;
6. defeitos em código entregue;
7. funcionalidades que ninguém usa.

### DevOps

DevOps é uma cultura e um conjunto de práticas que aproximam desenvolvimento e operações. O objetivo é reduzir o tempo entre uma mudança ser escrita e chegar à produção, sem perder estabilidade.

Práticas associadas: integração contínua, entrega contínua, infraestrutura como código, monitoramento e automação de testes.

## Engenharia de requisitos

Requisitos descrevem o que o sistema deve fazer e sob quais condições.

### Requisitos funcionais

Descrevem comportamentos e serviços: "o sistema deve permitir o cadastro de usuários" ou "o sistema deve gerar um relatório mensal".

### Requisitos não funcionais

Descrevem qualidades do sistema: desempenho, segurança, disponibilidade, usabilidade, manutenibilidade e compatibilidade.

Exemplo: "a busca deve responder em menos de 500 ms para 95% das requisições".

### Atividades de requisitos

- **Elicitação:** entrevistas, observação, workshops e análise de documentos.
- **Análise:** organizar, priorizar e detectar conflitos.
- **Especificação:** registrar de forma clara e verificável.
- **Validação:** confirmar com as partes interessadas que os requisitos estão corretos.

Um bom requisito é claro, completo, consistente, verificável e rastreável.

## Projeto e arquitetura de software

Arquitetura trata das decisões estruturais de alto nível: componentes, responsabilidades, comunicação e restrições.

### Padrões de projeto

Padrões de projeto são soluções reutilizáveis para problemas recorrentes. Exemplos clássicos:

- **Singleton:** garante uma única instância de uma classe.
- **Factory:** centraliza a criação de objetos.
- **Observer:** notifica objetos interessados sobre mudanças.
- **Strategy:** troca algoritmos em tempo de execução.
- **Repository:** isola o acesso a dados do restante da aplicação.

### Princípios SOLID

- **S**ingle Responsibility: uma classe tem uma única responsabilidade.
- **O**pen/Closed: aberto para extensão, fechado para modificação.
- **L**iskov Substitution: subtipos devem ser substituíveis por seus tipos-base.
- **I**nterface Segregation: interfaces específicas são melhores que interfaces genéricas.
- **D**ependency Inversion: dependa de abstrações, não de implementações concretas.

### Decisões de arquitetura

Registros de decisões de arquitetura, conhecidos como ADRs, documentam escolhas importantes, o contexto e as consequências. Eles ajudam novos membros a entender por que o sistema é daquele jeito.

## Controle de versão

Controle de versão registra o histórico de alterações do código. Git é o sistema mais usado atualmente.

Boas práticas:

- commits pequenos e com mensagens claras;
- uma responsabilidade por commit;
- branches curtos e focados;
- revisão por pull request;
- nunca commitar segredos, credenciais ou arquivos gerados;
- manter o repositório com histórico legível.

Uma mensagem de commit comum segue o padrão `tipo: descrição curta`, por exemplo `feat: adicionar busca vetorial` ou `fix: corrigir timeout da API`.

## Testes de software

### Pirâmide de testes

A pirâmide de testes recomenda muitas testes unitários, menos testes de integração e poucos testes de interface.

- **Testes unitários:** verificam uma pequena unidade de código, como uma função.
- **Testes de integração:** verificam a comunicação entre componentes.
- **Testes de sistema ou end-to-end:** verificam o fluxo completo, geralmente pela interface.

### TDD

TDD, ou *Test-Driven Development*, segue o ciclo vermelho-verde-refatora:

1. escreva um teste que falha;
2. escreva o código mínimo para o teste passar;
3. refatore o código mantendo os testes verdes.

### Cobertura de testes

Cobertura mede qual parte do código foi executada pelos testes. É um indicador útil, mas não garante qualidade: é possível ter alta cobertura com assertions fracas.

## Integração e entrega contínuas

- **Integração contínua (CI):** cada alteração é integrada ao branch principal e validada automaticamente por build e testes.
- **Entrega contínua (CD):** o código aprovado fica sempre pronto para ser colocado em produção.
- **Deployment contínuo:** a publicação em produção acontece automaticamente após a validação.

O pipeline típico inclui: instalar dependências, executar lint, rodar testes, gerar artefato e publicar.

## Estimativas e planejamento

Estimativas são previsões de esforço, não promessas. Em ágil, é comum usar *story points*, una escala relativa de complexidade, esforço e incerteza.

Técnicas:

- **Planning Poker:** o time revela estimativas ao mesmo tempo e discute diferenças.
- **Velocidade:** média de pontos entregues por sprint, usada para planejar, não para comparar pessoas.
- **Burndown chart:** gráfico do trabalho restante ao longo do tempo.
- **Divisão de histórias:** quebrar histórias grandes em partes menores.

## Documentação

Documentação de qualidade responde perguntas que o código sozinho não responde.

Tipos comuns:

- **README:** visão geral, instalação e execução rápida.
- **Documentação de arquitetura:** decisões e estrutura do sistema.
- **Documentação de API:** endpoints, parâmetros e exemplos.
- **Documentação de usuário:** instruções para quem consome o produto.
- **ADRs:** decisões técnicas relevantes.
- **Comentários no código:** explicam o porquê, não o quê.

Documentação vence quando está perto do código e é atualizada junto com ele.

## Manutenção e dívida técnica

Dívida técnica é o custo implícito de escolhas de código que funcionam agora, mas dificultam mudanças futuras. Pode vir de código duplicado, falta de testes, dependências desatualizadas ou decisões apressadas.

Nem toda dívida é ruim: assumi-la conscientemente pode acelerar uma entrega. O problema é acumulá-la sem plano de pagamento.

Estratégias:

- refatorar junto com mudanças na mesma área;
- registrar dívidas conhecidas em um backlog técnico;
- reservar parte da sprint para melhorias;
- automatizar verificações de qualidade.

## Métricas de desempenho

Métricas ajudam a entender o fluxo, mas não devem ser usadas para punir pessoas.

- **Lead time:** tempo entre a solicitação e a entrega.
- **Cycle time:** tempo entre o início do trabalho e a conclusão.
- **Deployment frequency:** frequência de publicações.
- **MTTR:** tempo médio de recuperação após uma falha.
- **Taxa de defeitos:** quantidade de bugs encontrados após a entrega.
- **Velocidade:** pontos entregues por iteração.

## Comparativo entre abordagens

| Abordagem | Foco | Melhor uso |
| --- | --- | --- |
| Cascata | Fases sequenciais e documentação | Requisitos estáveis e contratos rígidos |
| Scrum | Sprints e entregas regulares | Produtos com requisitos que mudam |
| Kanban | Fluxo contínuo e limite de WIP | Times de suporte e manutenção |
| XP | Práticas de engenharia | Busca por qualidade técnica alta |
| Lean | Eliminação de desperdício | Otimização de valor e fluxo |
| DevOps | Automação e colaboração | Entregas frequentes e confiáveis |

## Como escolher uma metodologia

Considere:

- estabilidade dos requisitos;
- tamanho e experiência do time;
- necessidade de conformidade e auditoria;
- frequência desejada de entrega;
- tipo de produto, se é novo ou legado;
- cultura organizacional.

Times pequenos costumam começar com Scrum ou Kanban e incorporar práticas de XP conforme amadurecem. O importante é inspecionar e adaptar, em vez de seguir regras literalmente.

## Glossário

- **Backlog:** lista priorizada de trabalho pendente.
- **Incremento:** versão funcional resultante de uma iteração.
- **Refatoração:** mudança estrutural que preserve o comportamento.
- **WIP:** trabalho em andamento.
- **ADR:** registro de decisão de arquitetura.
- **CI/CD:** integração e entrega contínuas.
- **Dívida técnica:** custo futuro de atalhos atuais.
- **Story point:** unidade relativa de estimativa de esforço.

## Perguntas frequentes

### Scrum é uma metodologia ou um framework?

Scrum é um framework que implementa princípios ágeis. Ele define papéis, eventos e artefatos, mas não prescreve práticas de programação como TDD.

### Kanban substitui Scrum?

Não obrigatoriamente. Kanban pode ser usado sozinho ou junto com Scrum, por exemplo para visualizar o fluxo dentro da sprint.

### Ágil significa ausência de documentação?

Não. Ágil valoriza documentação útil e suficiente, evitando excesso que não agrega valor.

### Qual a diferença entre erro, defeito e falha?

Erro é uma ação ou decisão humana incorreta. Defeito é o resultado desse erro no código. Falha é o comportamento observado pelo usuário quando o defeito é executado.

### Por que TDD é considerado uma prática e não uma metodologia?

Porque ele é uma técnica local de desenvolvimento. Ele pode ser adotado dentro de Scrum, Kanban ou qualquer outro processo.
