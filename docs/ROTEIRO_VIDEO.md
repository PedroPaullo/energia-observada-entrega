# Roteiro de pitch — Energia Observada (até 5 minutos)

## Bloco 1 — A dor manual do analista (0:00–1:00)

**[olhar para a câmera]**

“Imagine receber um arquivo da ANEEL com milhões de linhas de interrupções. Sem uma ferramenta, o analista precisa abrir esse arquivo, separar competências, comparar mês a mês e decidir no olho o que merece atenção. Depois, quando alguém pergunta por que determinado conjunto foi escolhido, ele precisa refazer a conta e procurar as linhas originais. O processo consome tempo e não deixa um critério fixo nem uma trilha clara da decisão.

O Energia Observada transforma essa primeira triagem em uma fila explicável. A fila aponta onde olhar primeiro; o Dossiê mostra como chegar àquela decisão e quais são os limites da evidência.”

**Tempo acumulado: 1:00.**

## Bloco 2 — Demonstração da fila com dados reais (1:00–2:30)

**[olhar para a tela e apontar para o título]**

“Esta é a pergunta central do produto: ‘Qual conjunto merece investigação neste mês — e quais registros sustentam esse destaque?’

**[apontar para o aviso amarelo]**

Aqui a própria interface informa: ‘AMOSTRA AUTÊNTICA ANEEL · recorte de demonstração. Não representa cobertura nacional; em comparação nacional bloqueado.’ Portanto, estes números são reais para o recorte demonstrativo, mas não são apresentados como cobertura nacional.

**[apontar para a coluna de variação absoluta]**

A fila está ordenada por aumento absoluto de afetações reportadas. A interface explica: ‘Volume orienta a triagem; não mede qualidade relativa ao adequado.’ O rótulo de situação é uma regra separada. Nesta tela, as quatro linhas têm ‘aumento relevante’, então eu não vou fingir que esse rótulo ordena a tabela.

**[apontar para JUREMA]**

JUREMA é o primeiro conjunto porque tem a maior variação absoluta: 259.038 afetações. No mês atual, são 729 registros e 279.285 afetações; no mês anterior, 635 registros e 20.247 afetações. O destaque vem do volume observado na comparação, não de uma afirmação sobre a causa.

**[apontar para CAUCAIA, BARRA DO CEARÁ e BONSUCESSO]**

Os demais conjuntos também aparecem com suas variações: CAUCAIA, 66.393; BARRA DO CEARÁ, 30.096; BONSUCESSO, 11.406. Assim o analista vê a ordem de prioridade e os valores que sustentam cada posição.”

**Tempo acumulado: 2:30.**

## Bloco 3 — O Dossiê como prova (2:30–3:30)

**[clicar no conjunto JUREMA e abrir o Dossiê; olhar para a tela]**

“O Dossiê organiza a explicação do destaque. Ele reúne a situação, os indicadores atuais e anteriores, a série disponível e as regras usadas para calcular a variação.

**[apontar para a área de evidências/exportação]**

A exportação entrega três arquivos. `dossie.md` é a narrativa legível. `registros.csv` contém os registros utilizados na análise. `manifesto.json` guarda filtros, fórmulas, métricas, versão e hash da fonte. Com esse pacote, outra pessoa consegue reconstruir a conclusão sem depender da minha sessão do Streamlit.

A diferença é prática: o analista não guarda apenas uma lista de conjuntos. Ele consegue defender por que JUREMA entrou na fila e mostrar as linhas que sustentam a decisão.”

**Tempo acumulado: 3:30.**

## Bloco 4 — Limites assumidos pelo produto (3:30–4:15)

**[apontar para os avisos do Dossiê; depois olhar para a câmera]**

“Esses números precisam ser interpretados com cuidado. A interface deixa explícito: ‘O município localiza o equipamento. Não delimita necessariamente os consumidores afetados.’ Portanto, afetações reportadas não são automaticamente consumidores únicos.

O produto também não diz que o aumento de interrupções prova uma causa. Ele apoia a investigação, mas não substitui análise regulatória ou técnica. E ausência de dados não equivale a ausência de interrupções. Essas limitações ficam junto da evidência, para evitar que uma triagem seja apresentada como diagnóstico causal.”

**Tempo acumulado: 4:15.**

## Bloco 5 — Atualização mensal e escala (4:15–5:00)

**[olhar para a tela e mostrar o README/workflow]**

“A ANEEL atualiza essa fonte mensalmente. O pipeline separa ingestão, validação, transformação e publicação. A aquisição registra a origem e o hash; a validação confere schema e integridade; a publicação só promove uma versão depois das verificações. O workflow pode executar essa rotina sem reprocessamento manual na interface.

**[olhar para a câmera]**

O resultado é uma triagem repetível: selecionar um conjunto, entender por que ele foi destacado, abrir o Dossiê, conferir os registros originais e exportar as evidências. O Energia Observada não promete explicar a causa. Ele torna a próxima investigação mais rápida, rastreável e limitada ao que os dados realmente permitem afirmar.”

**Tempo acumulado: 5:00.**
