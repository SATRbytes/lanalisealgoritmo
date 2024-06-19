
# Análise de relação das famílias envolvidas na dança dos dragões da série House of the dragon

O projeto foi desenvolvido para a avaliação final da disciplina de Análise de Algoritmos. São utilizadas as bibliotecas networkx, numpy e matplotlib para criar e visualizar grafos que representam as relações entre diferentes núcleos familiares envolvidos na Dança dos Dragões (uma guerra que ocorreu no universo fictício de game of thrones). O projeto permite analisar alianças, neutralidade e inimizades que existiam entre as famílias utilizando um grafo simétrico onde as arestas tem cores diferentes para representar qual o tipo de relação entre os nós (famílias). Além disso, é possível percorrer os reinos das principais casas envolvidas naquela guerra.

# Algoritmo que percorre o grafo e encontra o caminho mínimo entre dois nós.
Utilizando um algoritmo de busca em largura (BFS) no grafo para encontrar um caminho mínimo entre duas regiões. Esse algoritmo foi escolhido porque ele funciona explorando o grafo em níveis a partir de um nó inicial, usando uma fila do tipo primeiro a entrar e primeiro a sair.

## Funcionalidades
Interface gráfica com PyQt 
Adicionar conexões entre as famílias, visualizar as relações em um grafo, seleção de dados (famílias e relações).
Algoritmo que percorre o grafo e encontra o caminho mínimo entre dois nós.

## Pré-requisitos
Bibliotecas matplotlib, pyqt, networkx e numpy instaladas.

## Visualização do grafo
Após adicionar as conexões o grafo será exibido usando matplotlib (pyplot). As cores dos nós são determinadas pela família colocada, se a familia for targaryen os nós serão pretos, se for hightower os nós serão verdes, se a família não for nenhuma das duas os nós serão azuis.
Da segunda parte os nós são reinos/casas e a estradas são os caminhos que os conectam.
As cores representam os times. Os nós em cor vermelha representam o time black, os nós verdes representam o time verde, o nó cinza representa neutralidade e o nó amarelo é o local que já foi governado por ambos os times.

## Autores
- Shelda Azevedo
- Isabella Monte
- Antonio Palmeira




- [@SATRbytes](https://github.com/SATRbytes)
- [@Stormvcz](https://github.com/Stormvcz)
- [@Zabella0751](https://github.com/Zabella0751)




## Referência

 - [Analise de redes sociais com python](https://www.youtube.com/watch?v=tNeL4kNcJ94)
 - [Documentação networkx](https://networkx.org/documentation/stable/index.html)
 - [Grafos em Python](https://www.kaggle.com/code/flaviagg/grafos-em-python)
 - [Criando algoritmo de pesquisa em largura BFS](https://dev.to/antiduhring/criando-um-algoritmo-de-pesquisa-em-largura-em-grafos-3af3)
