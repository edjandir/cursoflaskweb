## Como funcionam as rotas no Flask?

No Flask, uma *rota* é a associação entre uma URL e uma função Python que processa as solicitações feitas para essa URL. As rotas são definidas usando o decorador `@app.route()`, que vincula um caminho específico (como `/`, `/about`) a uma função chamada *view function*. Essa função é executada quando o cliente acessa a URL correspondente[^1][^2].

### Características principais das rotas:

- **Definição de rotas**: O decorador `@app.route()` é usado para especificar o caminho da URL e os métodos HTTP aceitos (por padrão, apenas GET)[^1][^2].
- **Rotas dinâmicas**: É possível definir rotas que aceitam parâmetros dinâmicos usando `<variavel>` na URL. Esses parâmetros podem ser convertidos para tipos específicos, como `int` ou `float`[^1].
- **Renderização de templates**: As funções vinculadas às rotas podem retornar HTML diretamente ou usar o método `render_template()` para renderizar arquivos HTML localizados na pasta `templates`[^1][^6].

---

## Explicação do exemplo fornecido

O código fornecido define várias rotas no Flask com diferentes funcionalidades. Vamos analisar cada uma delas:

### 1. **Rota raiz (`/`)**

```python
@app.route('/', methods=['GET'])
def hello():
    return '''<h1>Hello from Flask!</h1>
            <p> Este é um exemplo do roteamento no Flask</p>
            <p> bla bla bla bla </p>
        '''
```

- **Descrição**: Essa rota responde ao caminho `/` e aceita apenas requisições GET (definido pelo parâmetro `methods=['GET']`).
- **Retorno**: Retorna uma string contendo HTML diretamente. Esse conteúdo será exibido no navegador quando o usuário acessar a URL raiz do aplicativo[^2].

---

### 2. **Rota `/goodbye`**

```python
@app.route('/goodbye')
def goodbye():
    return '<h1>Goodbye from PHP!</h1>'
```

- **Descrição**: Essa rota responde ao caminho `/goodbye`.
- **Retorno**: Retorna uma string HTML simples que será exibida no navegador[^2].

---

### 3. **Rota dinâmica `/aluno/<nome_aluno>`**

```python
@app.route('/aluno/<nome_aluno>')
def saudacao(nome_aluno):
    return render_template('saudacao.html', nome=nome_aluno)
```

- **Descrição**: Essa rota aceita um parâmetro dinâmico chamado `nome_aluno`. Por exemplo, acessar `/aluno/Maria` passará o valor `"Maria"` para a função.
- **Uso de templates**: A função utiliza `render_template()` para renderizar o arquivo `saudacao.html`, passando o valor de `nome_aluno` como variável para o template[^6].
- **Exemplo de uso**: O arquivo HTML pode exibir algo como "Olá, Maria!", dependendo da lógica implementada no template.

---

### 4. **Rota dinâmica com múltiplos parâmetros `/soma/<int:num1>/<int:num2>`**

```python
@app.route('/soma/<int:num1>/<int:num2>')
def soma(num1, num2):
    return render_template('soma.html', num1=num1, num2=num2)
```

- **Descrição**: Essa rota aceita dois parâmetros inteiros (`num1` e `num2`). Por exemplo, acessar `/soma/3/5` passará os valores `3` e `5` para a função.
- **Uso de templates**: A função renderiza o arquivo `soma.html`, passando os números como variáveis para o template. O template pode realizar operações ou exibir os números diretamente.
- **Exemplo de uso**: O arquivo HTML pode exibir "A soma de 3 e 5 é 8", dependendo da lógica implementada no template.

---

## Funcionamento geral do código

1. O decorador `@app.route()` registra as funções em um mapeamento interno do Flask que associa URLs às funções correspondentes.
2. Quando o servidor é iniciado com `app.run(debug=True)`, ele começa a escutar requisições HTTP.
3. Ao receber uma solicitação, o Flask verifica qual função está associada à URL requisitada e executa essa função, retornando seu resultado ao cliente[^3][^5].

Esse exemplo demonstra tanto rotas estáticas quanto dinâmicas, além da utilização de templates para criar páginas web mais complexas e interativas.

<div style="text-align: center">⁂</div>

[^1]: https://hackersandslackers.com/flask-routes/

[^2]: https://dev.to/emma_donery/python-flask-app-routing-3l57

[^3]: https://stackoverflow.com/questions/46123448/how-do-decorated-functions-work-in-flask-python-app-route

[^4]: https://stackoverflow.com/questions/49915758/what-is-flask-route

[^5]: https://stackoverflow.com/questions/59789001/how-does-the-route-decorator-used-in-flask-work

[^6]: https://flask.palletsprojects.com/en/stable/patterns/viewdecorators/

[^7]: https://www.tutorialspoint.com/flask/flask_routing.htm

[^8]: https://www.youtube.com/watch?v=FkVQFkaSzlM

[^9]: https://flask.palletsprojects.com/en/stable/quickstart/

[^10]: https://www.turing.com/kb/build-flask-routes-in-python

[^11]: http://explore-flask.readthedocs.org/en/latest/views.html

[^12]: https://circleci.com/blog/authentication-decorators-flask/

[^13]: https://www.reddit.com/r/flask/comments/z4lv55/how_exactly_does_approute_tell_flask_about/

[^14]: https://www.youtube.com/watch?v=XTLg6TLfy7M

