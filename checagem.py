from resolucao.codigo import Library


def test_library_management_system():
    library = Library()

    # Teste registrar_usuario
    usuario1 = library.registrar_usuario("Ana Pereira", "987654321")
    assert usuario1.nome == "Ana Pereira"
    assert usuario1.id_usuario == 1
    assert usuario1.telefone == "987654321"
    assert len(library.lista_usuarios) == 1

    # Teste adicionar_livro
    livro1 = library.adicionar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", "1234567890")
    assert livro1.titulo == "O Senhor dos Anéis"
    assert livro1.autor == "J.R.R. Tolkien"
    assert livro1.isbn == "1234567890"
    assert livro1.status == "Disponível"
    assert len(library.lista_livros) == 1

    # Teste emprestar_livro
    assert livro1.disponivel() == True
    resultado_emprestimo = usuario1.emprestar_livro(library, livro1, "2023-07-01", "2023-07-10")
    assert resultado_emprestimo == 'Empréstimo realizado com sucesso!'
    assert livro1.status == "Emprestado"
    assert len(library.lista_emprestimos) == 1

    # Verificar o empréstimo
    emprestimo = library.lista_emprestimos[0]
    assert emprestimo.usuario == usuario1
    assert emprestimo.livro == livro1
    assert emprestimo.data_emprestimo == "2023-07-01"
    assert emprestimo.data_devolucao == "2023-07-10"

    # Teste cancelar_emprestimo
    library.cancelar_emprestimo(emprestimo)
    assert livro1.status == "Disponível"
    assert len(library.lista_emprestimos) == 0

    # Teste exibir_informacoes
    info_usuario1 = usuario1.exibir_informacoes()
    assert info_usuario1 == "Usuário: Ana Pereira, ID: 1, Telefone: 987654321"

    # Teste emprestar_livro com livro indisponível
    livro2 = library.adicionar_livro("1984", "George Orwell", "0987654321")
    livro2.emprestar()  # Forçando o status para 'Emprestado'
    resultado_emprestimo = usuario1.emprestar_livro(library, livro2, "2023-07-01", "2023-07-10")
    assert resultado_emprestimo == 'Falha ao realizar o empréstimo. Livro indisponível.'
    assert len(library.lista_emprestimos) == 0

# Executa os testes
test_library_management_system()
