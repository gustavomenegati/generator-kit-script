# generator-kit-script

## Descrição
Automatização do processo de identificação de kits de geradores.

## Pré-requisitos
Observação: Para realizar o desenvolvimento, utilizei o **WSL**(_Windows Subsystem for Linux_) **Ubuntu 24.04.1 LTS** , instalando o **_Docker_** nele para executar a aplicação dentro de um _container_.

- WSL (opcional)
- Docker

## Instalação

Para instalar o **WSL**, execute `wsl --install -d <Distribution Name>`, sendo possível encontrar as distribuições executando `wsl --list --online`, caso deseje outra que não seja **Ubuntu-24.04**. Tendo algum problema após isso, consulte a documentação oficial em https://learn.microsoft.com/pt-br/windows/wsl/install

Feito isso, para instalar o Docker, acesse o seu **WSL**, executando `Ubuntu` no terminal. Em seguida execute `apt install docker` (isso para **Ubuntu**). Se houver algum problema, verifique a documentação oficial em https://docs.docker.com/desktop/features/wsl/

Com o _Docker_ já instalado no seu computador (dentro do _WSL_ caso esteja utilizando) execute `git clone https://github.com/gustavomenegati/generator-kit-script.git` para clonar o repositório via _HTTPS_ ou baixe a aplicação compactada clicando no botão _*Code*_ e *_Download ZIP_* no link https://github.com/gustavomenegati/generator-kit-script, descompactando-a em um diretório dentro do seu **WSL**.

## Uso

### Configuração

Acesse a pasta da aplicação acesse o diretório raiz da aplicação(caso baixe o arquivo direto, ele pode estar com o nome **generator-kit-script-main**)

Esse projeto lê uma base de dados em json, fornecida no diretório **data-resources** no seguinte formato (exemplo com dados _Mock_):

```
[
  {
    "Categoria": "Painel Solar",
    "Id": 1001,
    "Potencia em W": 500,
    "Produto": "Painel Solar 500 W Marca A"
  },
  {
    "Categoria": "Painel Solar",
    "Id": 1002,
    "Potencia em W": 500,
    "Produto": "Painel Solar 500 W Marca B"
  },
  {
    "Categoria": "Painel Solar",
    "Id": 1003,
    "Potencia em W": 500,
    "Produto": "Painel Solar 500 W Marca C"
  },
  {
    "Categoria": "Controlador de carga",
    "Id": 2001,
    "Potencia em W": 500,
    "Produto": "Controlador de Carga 30A Marca E"
  },
  {
    "Categoria": "Controlador de carga",
    "Id": 2002,
    "Potencia em W": 750,
    "Produto": "Controlador de Carga 50A Marca E"
  },
  {
    "Categoria": "Controlador de carga",
    "Id": 2003,
    "Potencia em W": 1000,
    "Produto": "Controlador de Carga 40A Marca D"
  },
  {
    "Categoria": "Inversor",
    "Id": 3001,
    "Potencia em W": 500,
    "Produto": "Inversor 500W Marca D"
  },
  {
    "Categoria": "Inversor",
    "Id": 3002,
    "Potencia em W": 1000,
    "Produto": "Inversor 1000W Marca D"
  }
]
```

É nesse diretório que deve ser atualizada a base de dados a serem consumidos pelo _script_.

### Execução

Com a aplicação já configurada, acesse o diretório raiz da aplicação "_generator-kit-script_" e execute o comando `docker-compose up` 

A partir disso, os dados serão transformados para serem exportados no seguinte formato, no mesmo diretório, com o nome de

_generator_kits.csv_

| ID Gerador | Potência do Gerador (em W) | ID Produto | Nome do Produto   | Quantidade Item |
|------------|---------------------------|------------|-------------------|-----------------|
| 11111      | 500                       | 9001       | Painel Alpha      | 1               |
| 11111      | 500                       | 8001       | Inversor Gama     | 1               |
| 11111      | 500                       | 7001       | Controlador Zeta  | 1               |
| 22222      | 1000                      | 9001       | Painel Alpha      | 2               |
| 22222      | 1000                      | 8002       | Inversor Delta    | 1               |
| 22222      | 1000                      | 7002       | Controlador Beta  | 1               |

Na aplicação, a rotina é realizada no momento em que o _container_ é iniciado e, depois disso, só a cada 7 dias.

### Observação

Entendo que a lógica de execução semanal pode ser tratada de outras formas que deixam mais precisa essa periodicidade e, além disso, otimizam os recursos computacionais necessários, como a execução do script sem nenhuma gestão de tempo embutida diretamente, utilizando recursos como agendador de tarefas / _cronjob_ / AWS Lambda e outros que fazem com que não seja necessário a execução 24/7 de um servidor.

Otimizações coo essa também podem ser aplicadas para a fonte de consumo dos dados fornecidos, podendo ser diretamente de uma base de dados modular em outros servidores, acessando via HTTP e até mesmo alteração de onde armazenamos a planilha final que essa aplicação resulta, guardando em algum serviço de armazenamento como o Amazon S3, removendo a necessidade de qualquer interação com o servidor que executa essa aplicação para extrair o valor que ele agrega.