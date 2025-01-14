# Bot de Cadastro de Chamados

Este projeto implementa um bot para automatizar o processo de cadastro de chamados no meu sistema de chamados. O bot lê um arquivo CSV contendo informações sobre os chamados e registra os dados no site de chamados.
As informações registradas incluem o cliente, o serviço e a descrição do serviço.

[Repositório do Meu Sistema De Chamados](https://github.com/CauZy-Goes/Lista-De-Servicos)

## Funcionalidades

- O bot acessa o sistema de chamados e preenche os campos de cadastro com as informações do arquivo CSV.
- Os dados são lidos de um arquivo CSV e enviados para o sistema de chamados automaticamente.
- O cadastro inclui:
  - **Cliente**: Nome do cliente que solicitou o serviço.
  - **Serviço**: Tipo de serviço que será prestado (exemplo: instalação, manutenção, configuração).
  - **Descrição**: Descrição detalhada do problema ou solicitação do cliente.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do bot.
- **Pandas**: Biblioteca utilizada para manipulação e leitura do arquivo CSV.
- **PythonAutoGUI**: Biblioteca utilizada para automação da interface gráfica, permitindo interagir com o sistema de chamados.

## Como Funciona

1. O bot lê os dados do arquivo CSV.
2. Para cada linha, o bot acessa o site de chamados e preenche os campos de cadastro com as informações correspondentes.
3. O bot utiliza a biblioteca **PythonAutoGUI** para simular o preenchimento dos campos de formulário.
4. Os dados do arquivo CSV são registrados no sistema de chamados, ajudando a automatizar o processo de criação de chamados.

## Como Rodar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Para instalar as dependências necessárias, execute o seguinte comando:
   ```bash
   pip install -r requirements.txt

## Possíveis Problemas e Soluções

Durante a execução do bot, alguns problemas podem ocorrer, especialmente relacionados à resolução da tela, velocidade de execução ou internet. Aqui estão alguns dos problemas mais comuns e como resolvê-los:

### 1. **Resolução do Monitor**

Se os cliques não estiverem ocorrendo nos locais corretos ou se a interface gráfica não for exibida corretamente, isso pode ser causado pela resolução do monitor. O **PythonAutoGUI** utiliza coordenadas específicas da tela para clicar nos itens da interface, e essas coordenadas podem variar dependendo da resolução do seu monitor.

#### Solução:
- **Ajustar a posição do clique**: Caso os cliques não ocorram nos lugares corretos, você pode alterar as coordenadas dos cliques diretamente no código. Utilize o comando `pyautogui.click(x, y)` onde `x` e `y` são as coordenadas da tela para o clique. Você pode usar uma ferramenta de captura de coordenadas ou imprimir as coordenadas para descobrir os pontos exatos.

### 2. **Velocidade de Execução e Internet**

O desempenho do bot pode ser afetado pela velocidade de execução do script ou pela qualidade da sua conexão de internet. Se o bot estiver demorando muito para executar ou se os cliques não ocorrerem corretamente devido a uma resposta lenta do sistema, pode ser necessário ajustar o tempo entre as ações.

#### Solução:
- **Ajustar o tempo de cada ação**: Se o bot estiver muito rápido ou se as interações não estiverem sendo executadas de forma sincronizada com a interface, você pode adicionar um tempo de pausa entre as ações. Use o comando `pyautogui.PAUSE` para definir um intervalo de tempo padrão entre todas as ações do bot, ou utilize `time.sleep(seconds)` para inserir uma pausa personalizada entre os cliques. Isso permitirá que o bot execute as ações de forma mais controlada.

  Exemplo:
  ```python
  import pyautogui
  import time

  pyautogui.PAUSE = 1  # Pausa de 1 segundo entre cada ação
  
  # Ou para uma pausa personalizada
  time.sleep(2)  # Pausa de 2 segundos entre duas ações
