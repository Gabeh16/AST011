
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from carrinho import criar_carrinho, adicionar_produto


# Carrega os cenários do arquivo Gherkin
scenarios("carrinho.feature")


@given("que o carrinho está vazio", target_fixture="carrinho")
def dado_carrinho_vazio():
    return criar_carrinho()


@when(
    parsers.parse(
        "adiciono {quantidade:d} unidades com estoque de "
        "{estoque:d} e preço unitário de {preco:f}"
    )
)
def adicionar_com_estoque_suficiente(
    carrinho, quantidade, estoque, preco
):
    adicionar_produto(carrinho, quantidade, estoque, preco)


@when(
    parsers.parse(
        "tento adicionar {quantidade:d} unidades com estoque de "
        "{estoque:d} e preço unitário de {preco:f}"
    )
)
def tentar_adicionar_sem_estoque(
    carrinho, quantidade, estoque, preco
):
    try:
        adicionar_produto(carrinho, quantidade, estoque, preco)
    except ValueError as erro:
        carrinho["erro"] = str(erro)


@then(parsers.parse("o total do carrinho deve ser {total_esperado:f}"))
def verificar_total(carrinho, total_esperado):
    assert carrinho["total"] == pytest.approx(total_esperado)


@then(parsers.parse("a quantidade de itens deve ser {itens_esperados:d}"))
def verificar_quantidade(carrinho, itens_esperados):
    assert carrinho["itens"] == itens_esperados


@then(parsers.parse('deve ocorrer o erro "{mensagem_esperada}"'))
def verificar_erro(carrinho, mensagem_esperada):
    assert carrinho.get("erro") == mensagem_esperada
