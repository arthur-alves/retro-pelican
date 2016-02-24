Title: Automatizando deploy em containers Docker com Fabric
Slug: automatizando-deploy-docker-com-fabric
Date: 2016-02-24 20:30
Tags: tutorial,python,builtin,docker,fabric,deploy
Author: Arthur Alves
Email:  arthur.4lves@gmail.com
Github: arthur-alves
Twitter: Arthur_4lves
Facebook: Arthur4lves
Category: Deploy
Summarize: True


###Sobre o Fabric:
<figure style="float:right;">
<img src="/images/arthur-alves/fabric.png">
</figure>
</br>

Para que não sabe, o (Fabric)[http://www.fabfile.org/] é uma lib Python que permite
automatizar deploy de aplicações (Não somente python), realizar tarefas, entre outros, utilizando o protocolo de rede SSH(**Security Shell**) para realizar suas façanhas. É possível realizar diversas
tarefas, e é um velho conhecido de quem trabalha com Python, e há vários tutoriais dele por aí.
Hoje vou focar em mostrar para vocês uma maneira(dentre muitas) de se realizar o deploy de aplicações
utilizando um container já criado, e que talvez precise de realizar tarefas contínuas e incessantes
durante seu ciclo de vida (Este foi o meu caso).

Obs: Existe já um módulo com o nome de [Docker-Fabric](docker-fabric.readthedocs.org), que
já realiza melhor esta façanha, porém no meu caso eu já tinha um projeto pronto e muito antigo, e utilizava fabric para diversas tarefas eu simplesmente adaptei o fabric para realizar tarefas em containers,
pois se tratava de uma tarefa simples e não justificaria utilizá-lo no momento.


###Mãos ao código:

Primeiramente vamos criar uma tarefa básica para concatenar os comandos simples.
Vamos utilizar list comprehensions aqui, se não conhece sobre, pesquise sobre,
são muito úteis.


```python
from fabric.decorators import hosts

def concat_commands(cmds_list):
    u"""Concatena vários comandos para executar em linha."""
    fmt_cmd = "{} && "
    # Concatenando todos os comandos da lista cmds_list
    joined_cmds = [fmt_cmd.format(i) if i != cmds_list[-1]
                   else i for i in cmds_list]

	# Retornamos aqui uma string com todos os comandos formatados
    return "".join(i for i in joined_cmds)
```

Para ficar mais fácil, leia os comentários acima, e a docstring para entender
seu funcionamento.

Agora vamos criar uma tarefa/comando fabric simples, que vai executar os comandos em
série. Para realizar esta tarefa, você precisa conhecer o *docker exec* que executa
e envia comandos para dentro do container, porém é limitado. Mas quando combinado
com o comando *sh -c* que executa uma série de comandos em uma string, funciona bem
para o proposto. Veja abaixo:


```python
@hosts('user@seuhost')
def docker_deploy_dev(container_id):
    u"""Envia série de comandos para containers."""
    cmds_list = [
        "cd {}".format(DOCKER_CBLANCA_PATH),
        "git pull origin dev",
        "./manage.py collectstatic --noinput",
        "cd {}".format(os.path.join(DOCKER_CBLANCA_PATH, "webservices")),
        "git pull origin dev",
        "cd {}".format(os.path.join(DOCKER_CBLANCA_PATH, "business")),
        "git pull origin dev",
        # restart all apps
        "supervisorctl restart all"
    ]
    # concatenando a lista de comandos
    joined_cmds = concat_commands(cmds_list)
    sudo("docker exec {} sh -c '{}'".format(container_id, joined_cmds),
        user="root"
    )




