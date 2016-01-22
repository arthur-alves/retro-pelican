Title: Os segredos sombrios do type
Slug: os-segredos-sombrios-de-type
Date: 2016-01-22 06:30
Tags: tutorial,python,builtin
Author: Arthur Alves
Email:  arthur.4lves@gmail.com
Github: arthur-alves
Twitter: Arthur_4lves
Facebook: Arthur4lves
Category: Builtin
Summarize: True


###Sobre o type:

O *type* do Python tem um uso comum, assim como seus respectivos em cada linguagem, que é de verificar os tipos dos objetos,
como em *Javascript*, por exemplo, com o *typeof* você verifica os tipos de variáveis e objetos como String, Number, Array e etc.
Porém, no Python type é muito mais importante e poderoso, pois ele é o ator principal e base de todos os objetos
Python. Vamos ver com nossos próprios olhos. Abra um terminal *python* e digite:

```python
In [1]: print str.__class__
Out[1]: type


In [2]: print int.__class__
Out[2]: type
```

Ou simplesmente:

```python
In [3]: print type(float)
Out[3]: type

In [3]: print type(type)
Out[3]: type
```

Podemos dizer que *type* é a base de todos os tipos de objetos em python. Tudo em python é e vem dele.


"Mas como assim type é a base de tudo em Python", você deve se perguntar. Vamos ver seu poder mais
obscuro e talvez menos conhecido.

###Os poderes sombrios de type:

O tipo *type* quando chamado com 1 argumento apenas lhe devolve o tipo do objeto em questão, porém
ele aceita mais 2 argumentos, que quando usados, produzem um resultado que talvez poucos conheçam, repare bem no exemplo abaixo:

```python
# Criando uma classe da maneira tradicional em python
class Foo(object):
    foo = 'Foo class'

# Imprimindo o atributo foo de Foo
In [1]: Foo.foo
Out[1]: 'Foo class'


# Agora criando uma class utilizando os poderes de type
Bar = type('Bar', (), {'bar': 'Bar class'})

# Imprimindo o atributo bar de Bar criado pelo type
In [2]: Bar.bar
Out[2]: 'Bar class'

```
Legal não? Agora vamos ver quais argumentos precisamos para criar uma classe utilizando *type*.

```python

# Imprimindo parte da doc
Type:        type
String form: <type 'type'>
Namespace:   Python builtin
Docstring:
type(object) -> the object's type
type(name, bases, dict) -> a new type

```
**Args**:


1º argumento é uma string que vai ser o nome base da sua classe

2º argumento é uma tupla com os objetos(classes) que você deseja herdar atributos por exemplo.

3º argumento é um dicionário com as propriedades que sua classe deve possuir.


Outro exemplo para melhor clarificação:

```python
class Foo(object):
    def __init__(self):
        print "Hello {}".format(self.__class__.__name__)

foo = Foo()

print Foo.__base__

# Imprime:
# Hello Foo
# <type 'object'>


# Herdando de Foo
Bar = type('Bar', (Foo,), {'bar':'Atributo bar'})

bar = Bar()
print bar.bar

print Bar.__base__

# Imprime:
# Hello Bar
# Atributo bar
# <class '__main__.Foo'>

```
**Explicando:**
Criamos a classe **Foo** da maneira tradicional em python, e depois criamos **Bar** utilizando
*type* e herdando características de **Foo** e adicionando um atributo com o nome de *"bar"*. Veja que o funcionamento
é identico para criar uma classe da maneira tradicional ou com type.

###Utilidade

A utilidade de criar classes com type podem ou não ser vantajosas, isto depende do uso, mas um exemplo comum, é quando utilizado para criar classes dinâmicas que precisam de heranças, atributos e comportamentos diferentes de acordo com a necessidade, simplesmente passando objetos dinamicos seguindo a ordem:

```python

type([str], [tuple], [dict])
# str(nome), tuple(classe) e dict(atributos)
```

Para não digitar mais nenhum exemplo chato, vou passar um uso simples de *type* que está em uso em uma lib famosa sandman(que é utilizada para criar APIs REST dinamicas com base em um banco de dados sem
muito esforço). Clique no link abaixo:


[**Github sandman**](https://github.com/jeffknupp/sandman/blob/develop/sandman/model/utils.py#L147)


Espero que tenham gostado, e espero que possa ser útil para vocês, como acabou sendo para mim.
