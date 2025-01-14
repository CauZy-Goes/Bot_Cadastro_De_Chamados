import acoes_robo

acoes_robo.configurarRobo()

acoes_robo.entrarNavegador()

acoes_robo.acessarSite("https://lista-de-servicos-cauzy.netlify.app/")

acoes_robo.fazerAutenticacao("teste@teste.com","123123")

acoes_robo.acessarCadastro()

acoes_robo.cadastrarChamadosDoCsv("chamados_para_cadastrar.csv")
