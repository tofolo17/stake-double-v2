# Stake Double

## Instalação de Dependências

Os passos a seguir foram executados numa máquina virtual zerada. Repetindo-os num sistema operacional como o Windows 10 ou Windows 11 garantem a funcionalidade da aplicação final. Acompanhe:

### Google Chrome

Instale o Google Chrome caso não o tenha instalado. Verifique se está usando a versão mais recente.

### Python

Instale o Python por este [link](https://www.python.org/downloads/) (versão mais recente).

Prossiga com a instalação padrão, mas atente-se em selecionar "Add python.exe to PATH".

Para testar a instalação:
* Aperte `Windows` + `r`;
* Digite `cmd`;
* Execute `python --version`.

Você deve obter algo como:

![alt text](images\image.png)

### Git

O Git será necessário para levar o conteúdo da nuvem até a sua máquina. Também, será utilizado para manter o programa atualizado.

Instale o Git por este [link](https://git-scm.com/download/win) (versão mais recente).

Realize a instalação padrão, clicando em "Next"/"Próximo" a cada nova etapa.

Para testar a instalação:
* Aperte `Windows` + `r`;
* Digite `cmd`;
* Execute `git --version`.

Você deve obter algo como:

![alt text](images\image2.png)

## Instalação do Robô

### Clonagem

Com os requisitos instalados, devemos clonar os arquivos que estão na nuvem no nosso computador. Para tal:
* Aperte `Windows` + `r`;
* Digite `cmd`;
* Vá até a pasta que armazenará o programa através do comando `cd`:
    * Exemplo: `cd Documents`. Para saber mais, clique [aqui](https://www.freecodecamp.org/news/command-line-commands-cli-tutorial/).
* Execute `git clone https://github.com/tofolo17/stake-double-v2.git` (temporário);
* Finalmente, execute `cd stake-double-v2` para entrar no diretório do robô.

![alt text](images\image3.png)

### Ambiente

Estamos quase lá.