
# language: pt

Funcionalidade: Carrinho de compras
  Como cliente de um e-commerce
  Quero adicionar produtos ao carrinho
  Para acompanhar o valor das minhas compras

  Cenário: Adicionar um produto com estoque suficiente
    Dado que o carrinho está vazio
    Quando adiciono 2 unidades com estoque de 10 e preço unitário de 5.00
    Então o total do carrinho deve ser 10.00
    E a quantidade de itens deve ser 2

  Cenário: Tentar adicionar um produto sem estoque suficiente
    Dado que o carrinho está vazio
    Quando tento adicionar 5 unidades com estoque de 3 e preço unitário de 5.00
    Então deve ocorrer o erro "Estoque insuficiente"
    E o total do carrinho deve ser 0.00
