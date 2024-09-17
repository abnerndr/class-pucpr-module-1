# CRUD - Python

## Descrição

Este projeto é uma aplicação CRUD (Create, Read, Update, Delete) que gerencia dados armazenados em arquivos JSON na pasta `db`.

## Pré-requisitos

- [Python](https://www.python.org/) (versão 3.6 ou superior)
- [pip](https://pip.pypa.io/en/stable/installation/) (gerenciador de pacotes do Python)

## Instalação

1. Clone o repositório:

   ```sh
   git clone https://github.com/abnerndr/class-pucpr-module-1.git
   cd class-pucpr-module-1
   ```

2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Uso

1. Inicie a aplicação:

   ```sh
   python main.py
   ```

2. Siga as instruções no menu para realizar operações CRUD.

## Estrutura do Projeto

- [`choice.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fabner%2Fwww%2Fpuc%2Fclass-pucpr-module-1%2Fchoice.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\\Users\abner\www\puc\class-pucpr-module-1\choice.py"): Contém funções para gerenciar as opções de CRUD.
- [`db/`](command:\_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fabner%2Fwww%2Fpuc%2Fclass-pucpr-module-1%2Fdb%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\abner\www\puc\class-pucpr-module-1\db\"): Pasta onde os arquivos JSON são armazenados.
- [`db/load.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fabner%2Fwww%2Fpuc%2Fclass-pucpr-module-1%2Fdb%2Fload.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\\Users\abner\www\puc\class-pucpr-module-1\db\load.py"): Função para carregar dados.
- [`db/save.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fabner%2Fwww%2Fpuc%2Fclass-pucpr-module-1%2Fdb%2Fsave.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\\Users\abner\www\puc\class-pucpr-module-1\db\save.py"): Função para salvar dados.
- [`db/destroy.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fabner%2Fwww%2Fpuc%2Fclass-pucpr-module-1%2Fdb%2Fdestroy.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\\Users\abner\www\puc\class-pucpr-module-1\db\destroy.py"): Função para deletar dados.
- [`db/update.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fabner%2Fwww%2Fpuc%2Fclass-pucpr-module-1%2Fdb%2Fupdate.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\\Users\abner\www\puc\class-pucpr-module-1\db\update.py"): Função para atualizar dados.
- [`main.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fabner%2Fwww%2Fpuc%2Fclass-pucpr-module-1%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\\Users\abner\www\puc\class-pucpr-module-1\main.py"): Arquivo principal que exibe o menu e chama as funções apropriadas.

## Exemplos de Uso

- Para criar um novo registro, escolha a opção 1 no menu.
- Para listar todos os registros, escolha a opção 2 no menu.
- Para atualizar um registro, escolha a opção 3 no menu e forneça o código do registro.
- Para deletar um registro, escolha a opção 4 no menu.

## Contribuição

- Instruções de como contribuir para o projeto.

## Licença

- Informações sobre a licença do projeto.
