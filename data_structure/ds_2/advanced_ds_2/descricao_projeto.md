Projeto de Game Design Educativo — Estruturas de Dados II

## 1. Identificação do projeto

**Disciplina:** Estruturas de Dados 2
**Tema:** Design de Jogos Educativos sobre Árvores Avançadas por meio da Engenharia Reversa e Reuso de Modelos  

### Integrantes

- Gabriella Rocha Gonçalves Cardoso
- Miguel Henrico de Araujo França
- Juan Carlos Siqueira de Lima
- Arthur Ferreira

---

## 2. Visão geral

O **AVL Balance Challenge** é uma proposta de upgrade pedagógico baseada no módulo **Binary Search Tree / AVL Tree do VisuAlgo**.

O VisuAlgo permite visualizar operações realizadas em Árvores Binárias de Busca (BST) e Árvores AVL, acompanhando inserções, remoções, buscas, fatores de balanceamento e rotações.

Nossa proposta parte desse modelo de visualização e o transforma em uma experiência de **aprendizagem ativa**.

Em vez de apenas observar o algoritmo identificar um desequilíbrio e realizar automaticamente a rotação necessária, o jogador passa a ser responsável por:

1. acompanhar a inserção dos nós;
2. analisar a estrutura formada;
3. identificar quando existe desequilíbrio;
4. localizar o primeiro nó desbalanceado;
5. analisar seu Fator de Balanceamento;
6. reconhecer o caso de desequilíbrio;
7. escolher e executar a rotação correta.

Assim, o conhecimento de Árvores AVL deixa de ser apenas conteúdo apresentado pela ferramenta e passa a constituir a **mecânica central do jogo**.

---

## 3. Modelo reutilizado

### Ferramenta base

**VisuAlgo — Binary Search Tree / AVL Tree**

Referência oficial:

- https://visualgo.net/en/avl

O VisuAlgo foi desenvolvido como uma plataforma interativa para auxiliar o aprendizado de estruturas de dados e algoritmos por meio de visualizações e animações.

### Reuso proposto

Este projeto realiza **reuso conceitual e pedagógico do modelo**, e não reutilização do código-fonte do VisuAlgo.

A proposta utiliza como referência:

- a representação visual dos nós;
- a organização de uma BST;
- as operações de inserção;
- o cálculo de altura;
- o Fator de Balanceamento;
- as rotações de uma AVL;
- a visualização passo a passo.

Esses elementos são reorganizados em uma mecânica de jogo baseada na tomada de decisões pelo estudante.

---

### Upgrade proposto

Transformar o processo de rebalanceamento em um **desafio interativo**.

Quando uma inserção gerar um desequilíbrio, a execução automática será interrompida e o jogador deverá diagnosticar a situação e escolher a operação correta.
