from resolucao.codigo import Restaurant

def test_restaurant_management_system():
    restaurant = Restaurant()

    # Teste adicionar_mesa
    mesa1 = restaurant.adicionar_mesa(1, 4)
    assert mesa1.numero == 1
    assert mesa1.assentos == 4
    assert mesa1.status == "livre"
    assert len(restaurant.lista_mesas) == 1

    # Teste registrar_cliente
    cliente1 = restaurant.registrar_cliente("Carlos Santos")
    assert cliente1.nome == "Carlos Santos"
    assert cliente1.id_cliente == 1
    assert len(restaurant.lista_clientes) == 1

    # Teste fazer_pedido
    item1 = MenuItem("Pizza", "Pizza de queijo", 30.0)
    item2 = MenuItem("Refrigerante", "Refrigerante de cola", 5.0)
    itens = [item1, item2]
    resultado_pedido = cliente1.fazer_pedido(restaurant, mesa1, itens)
    assert resultado_pedido == 'Pedido realizado com sucesso!'
    assert mesa1.status == "ocupada"
    assert len(restaurant.lista_pedidos) == 1

    # Verificar o pedido
    pedido = restaurant.lista_pedidos[0]
    assert pedido.cliente == cliente1
    assert pedido.mesa == mesa1
    assert len(pedido.itens) == 2
    assert pedido.status == "pendente"

    # Teste fechar_pedido
    restaurant.fechar_pedido(pedido)
    assert pedido.status == "servido"
    assert mesa1.status == "livre"

    # Teste exibir_informacoes do item do cardápio
    info_item1 = item1.exibir_informacoes()
    assert info_item1 == "Item: Pizza, Descrição: Pizza de queijo, Preço: 30.00"

    # Teste fazer_pedido com mesa indisponível
    mesa2 = restaurant.adicionar_mesa(2, 2)
    mesa2.reservar()  # Forçando o status para 'ocupada'
    resultado_pedido = cliente1.fazer_pedido(restaurant, mesa2, itens)
    assert resultado_pedido == 'Falha ao realizar o pedido. Mesa indisponível.'
    assert len(restaurant.lista_pedidos) == 1  # Nenhum novo pedido foi adicionado

# Executa os testes
test_restaurant_management_system()