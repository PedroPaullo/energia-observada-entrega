# Guia vivo de entrevista técnica — Energia Observada

Este documento será ampliado camada por camada durante a preparação para a entrevista. A regra é entender primeiro, depois explicar com precisão técnica.

## Como usar este guia

Para cada camada, estudaremos quatro coisas:

1. o problema que a camada resolve;
2. como ela foi implementada;
3. quais decisões e alternativas existem;
4. como explicar isso oralmente em uma entrevista.

As respostas devem ser sustentadas pelo código, pelos testes e pelo comportamento observado da aplicação.

## Camada 1 — Problema e decisão de produto

### O problema

A base pública da ANEEL contém registros mensais de interrupções de energia. Um analista precisa identificar quais conjuntos elétricos merecem investigação primeiro. Fazer isso manualmente exige filtrar a distribuidora, a competência e a região, comparar períodos e decidir quais variações justificam atenção.

O problema central não é apenas volume de dados. É a falta de uma decisão inicial que seja rápida, repetível e justificável depois.

### A decisão de produto

O Energia Observada foi construído como uma **fila explicável de investigação**.

A fila prioriza conjuntos pela variação absoluta de afetações reportadas. Ao selecionar um conjunto, o usuário abre um **Dossiê de Investigação**, que reúne:

- indicadores atuais e anteriores;
- variações mensais;
- histórico disponível;
- contexto comparativo;
- classificação baseada em regras transparentes;
- confiança documental;
- registros-fonte;
- exportação reproduzível.

A solução não tenta provar a causa de uma interrupção. Ela organiza a próxima investigação e mostra quais evidências sustentam a prioridade.

### O que o produto resolve

Antes:

- o analista procura manualmente em arquivos extensos;
- a seleção pode depender de julgamento informal;
- a justificativa fica separada dos registros originais;
- a comparação pode não ser reproduzível.

Depois:

- a fila apresenta uma ordem de leitura baseada em uma regra explícita;
- o Dossiê explica por que o conjunto foi destacado;
- os indicadores têm denominadores, fórmulas e períodos identificados;
- os registros utilizados podem ser exportados;
- o manifesto registra filtros, versões e hashes;
- outra pessoa consegue verificar o pacote fora da sessão do Streamlit.

### Como explicar em 30 segundos

> “Eu não construí apenas um ranking. Construí uma fila de investigação explicável. A fila ajuda o analista a decidir onde olhar primeiro usando variações observadas entre competências. Depois, o Dossiê mostra os indicadores, as regras, o histórico, os registros que sustentam a leitura e os limites do que pode ser concluído. O produto apoia a investigação, mas não afirma causalidade.”

### Termos técnicos que você deve dominar

- **triagem:** priorização inicial dos casos que merecem leitura;
- **conjunto elétrico:** unidade de análise da interrupção na base;
- **competência:** mês de referência dos registros;
- **indicador:** medida calculada a partir dos registros, como quantidade de registros ou afetações reportadas;
- **rastreabilidade:** capacidade de ligar uma conclusão aos dados, filtros, regras e versão da fonte que a produziram;
- **reprodutibilidade:** capacidade de obter a mesma conclusão executando novamente o processo com os mesmos insumos.

### Perguntas prováveis

**Por que isso é útil para um analista?**

> “Porque reduz o trabalho repetitivo da primeira triagem e torna a escolha defensável. O analista não recebe apenas um conjunto destacado; ele recebe a variação observada, a regra aplicada e os registros usados para sustentar a leitura.”

**O produto identifica a causa da interrupção?**

> “Não. Ele apresenta sinais reportados pela fonte como hipóteses de investigação. Causa raiz, responsabilidade e nexo causal exigem outras evidências e análise técnica.”

**Por que você não chamou isso de ranking de qualidade?**

> “Porque volume e variação orientam a prioridade de leitura, mas não são uma medida completa de qualidade relativa entre distribuidoras ou conjuntos. O produto faz triagem, não avaliação regulatória.”

**Por que a demonstração mostra apenas um recorte?**

> “O recorte foi deliberado para demonstrar o fluxo completo com dados autênticos. O produto preserva a arquitetura para trabalhar com outras distribuidoras e competências quando os dados correspondentes estiverem carregados e validados.”

### Exercício oral

Explique, sem olhar o texto, em até um minuto:

1. qual é o trabalho manual do analista;
2. qual decisão o produto apoia;
3. por que a fila não é uma prova de causa;
4. o que o Dossiê acrescenta à fila.

### Critério para avançar

Você deve conseguir responder às quatro perguntas usando suas próprias palavras, sem listar tecnologias antes de explicar o problema.

## Camadas seguintes

- Camada 2 — estrutura e semântica dos dados da ANEEL;
- Camada 3 — aquisição, validação e transformação;
- Camada 4 — indicadores e regras de classificação;
- Camada 5 — confiança e comparação contextual;
- Camada 6 — Dossiê, exportação e verificação;
- Camada 7 — arquitetura da aplicação e interface;
- Camada 8 — testes, operação mensal e evolução do produto.
