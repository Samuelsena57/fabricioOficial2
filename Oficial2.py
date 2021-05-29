class Livro:

    def __init__(self, nomelivro, autor, editora, ano_publicacao, ano_aquisicao, ler, datadaleitura ):
        self.nomelivro = nomelivro
        self.autor = autor
        self.editora = editora
        self.ano_publicacao = ano_publicacao
        self.ano_aquisicao = ano_aquisicao
        self.ler = ler
        self.datadaleitura = datadaleitura

    def __repr__(self):
        return repr((self.nomelivro))

    def buscarautorcitado(self, autor):
        for i in livraria:
            if autor == i.autor:
                print(i)

    def buscandootitulo(self, nomelivro):
        for i in livraria:
            if nomelivro == i.nomelivro:
                print(i)



    def leituradolivro(self, datadaleitura):
        self.ler = 'Sim'
        self.datadaleitura = datadaleitura


    def info(self):
        print('*******************************************')
        print()
        print('Registro do Livro : ' + self.nomelivro)
        print('Autor(a) do Livro : ' + self.autor)
        print('Editora do Livro  : ' + self.editora)
        print('Ano de Publicação : ' + str(self.ano_publicacao))
        print('Ano de Aquisição  : ' + str(self.ano_aquisicao))
        print('Livro ler         : ' + self.ler)
        print('Data da leitura   : ' + str(self.datadaleitura))

L1 = Livro('Auto da Compadecida', 'Ariano Suassuna', 'Nova Fronteira', 2019, 2020, 'Não', 00)
L2 = Livro('A Sutil Arte de Ligar o F*da-se', 'Mark Manson', 'Intrinseca', 2017, 2021, 'Não', 00)
L3 = Livro('De Onde Vêm as Boas Ideias', 'Steven Johnson', 'Zahar', 2021, 2021, 'Não', 00)
L4 = Livro('Pai Rico Pai Pobre', 'Robert Kiyosaki', 'Alta Books', 2017, 2019, 'Não', 00)

livraria = [L1, L2, L3, L4]

print()
print(sorted(livraria, key=lambda Livro: Livro.nomelivro))

print('buscadootitulo')
livraria[0].buscandootitulo('De Onde Vêm as Boas Ideias')

print('buscadoautor')
livraria[0].buscarautorcitado('Steven Johnson')

L1.info()
L2.info()
L3.info()
L4.info()

L3.leituradolivro(2021)
L4.leituradolivro(2020)
L3.info()
L4.info()

livraria[0].buscandootitulo('De Onde Vêm as Boas Ideias')
livraria[0].buscarautorcitado('Steven Johnson')