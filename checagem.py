from resolucao.codigo import Hotel

def test_hotel_management_system():
    hotel = Hotel()

    # Teste registrar_hospede
    hospede1 = hotel.registrar_hospede("João Silva", "123456789")
    assert hospede1.nome == "João Silva"
    assert hospede1.id_hospede == 1
    assert hospede1.telefone == "123456789"
    assert len(hotel.lista_hospedes) == 1

    # Teste adicionar_quarto
    quarto1 = hotel.adicionar_quarto(101, "Simples")
    assert quarto1.numero == 101
    assert quarto1.tipo == "Simples"
    assert quarto1.status == "Disponível"
    assert len(hotel.lista_quartos) == 1

    # Teste fazer_reserva
    assert quarto1.disponivel() == True
    resultado_reserva = hospede1.fazer_reserva(hotel, quarto1, "2023-07-01", "2023-07-05")
    assert resultado_reserva == 'Reserva realizada com sucesso!'
    assert quarto1.status == "Ocupado"
    assert len(hotel.lista_reservas) == 1

    # Verificar a reserva
    reserva = hotel.lista_reservas[0]
    assert reserva.hospede == hospede1
    assert reserva.quarto == quarto1
    assert reserva.check_in == "2023-07-01"
    assert reserva.check_out == "2023-07-05"

    # Teste cancelar_reserva
    hotel.cancelar_reserva(reserva)
    assert quarto1.status == "Disponível"
    assert len(hotel.lista_reservas) == 0

    # Teste exibir_informacoes
    info_hospede1 = hospede1.exibir_informacoes()
    assert info_hospede1 == "Hóspede: João Silva, ID: 1, Telefone: 123456789"

    # Teste fazer_reserva com quarto indisponível
    quarto2 = hotel.adicionar_quarto(102, "Duplo")
    quarto2.reservar()  # Forçando o status para 'Ocupado'
    resultado_reserva = hospede1.fazer_reserva(hotel, quarto2, "2023-07-01", "2023-07-05")
    assert resultado_reserva == 'Falha ao realizar a reserva. Quarto indisponível.'
    assert len(hotel.lista_reservas) == 0

# Executa os testes
test_hotel_management_system()