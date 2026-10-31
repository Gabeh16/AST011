
def criar_carrinho():
    return {
        "total": 0.0,
        "itens": 0
    }


def adicionar_produto(
    carrinho,
    quantidade_desejada,
    estoque_disponivel,
    preco_unitario
):
    if quantidade_desejada > estoque_disponivel:
        raise ValueError("Estoque insuficiente")

    carrinho["itens"] += quantidade_desejada
    carrinho["total"] += quantidade_desejada * preco_unitario
