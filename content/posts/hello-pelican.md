Title: Hello Pelican!  
Date: 2014-12-28 17:00  
Category: Tutoriais  
Tags: blog, pelican, python, ipython-notebook
Slug: hello-pelican  
Author: Rudolf Hellmuth

<!-- PELICAN_BEGIN_SUMMARY -->
{% img align-center {filename}/figures/592px-PelecanusGronvold.jpg 450  "PelecanusGronvold by Henrik Groenvold - Ibis 1914. Licensed under Public Domain via Wikimedia Commons" "pelicanos"  %}
<p align="center" style="width: 350px; max-width: 100%; text-align: left; margin-left: auto; margin-right: auto;">
  PelecanusGronvold by Henrik Groenvold - Ibis 1914.
  </br>
  <font color="#C8C8C8">
    Licensed under Public Domain via Wikimedia Commons.
  </font>
</p>


#Criando meu primeiro post no Pelican

Estava pensando em criar este blog há algum tempo. Queria que fosse um blog onde pudesse postar tutoriais de [computação científica](http://pt.wikipedia.org/wiki/Computação_científica) e fórmulas matemáticas em [LaTeX](http://pt.wikipedia.org/wiki/LaTeX). Mais importante do que isso, queria ter total controle sobre layout e conteúdo (inclusive aquelas informações automáticas de rodapé). Então li o post "[Migrating from Octopress to Pelican](http://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/)" do [Pythonic Perambulations](https://jakevdp.github.io/) e acabei conhecendo o pacote [Pelican](http://blog.getpelican.com/). Pelican é um gerador de páginas estáticas criado em *python* para facilitar nossa vida, na criação de blogs ou site estáticos. Sites estáticos podem ser servidos no servidor [github](https://github.com/) usando a ferramenta [git](http://git-scm.com/) de gerenciamento de versão de código fonte. Já havia tentado começar este blog usando [Octopress](octopress.org) há uns meses atrás, mas acabei perdendo a motivação em parte porque Octopress funciona em *Ruby*, que é uma linguagem que não domino. Como eu adoro Python, Pelican acabou sendo uma ótima opção. A [documentação oficial](http://docs.getpelican.com/) está em inglês, mas no blog [Mind Bending](http://mindbending.org/pt/series/migrando-para-o-pelican) existem ótimos tutoriais em português.
<!-- PELICAN_END_SUMMARY -->

A minha primeira experiência com o Pelican foi estranha. Achei que seria mais simples. Achei muito simples configurar o Pelican, porque tudo é feito em dois scripts de configuração em Python. Se eu tivesse usado qualquer tema pronto teria colocado esse blog no ar no mesmo dia. O tema que mais tinha gostado para este blog foi mesmo o *default* chamado *notmyidea*, mas não tinha gostado de algumas características dele. Daí resolvi fazer algumas pequenas modificações neste tema, e isso me deu uma dor de cabeça porque não estou acostumado a editar [CSS](http://pt.wikipedia.org/wiki/Cascading_Style_Sheets). Acredito que seja super fácil para quem tem experiência em webdesign. 


## Escrever em Markdown ou reStructuredText?

Havia também uma coisa que precisava decidir, Python permite que escrevamos artigos usando tanto no formato [Markdown](http://pt.wikipedia.org/wiki/Markdown) quanto no [reStructuredText](http://pt.wikipedia.org/wiki/ReStructuredText). reStructuredText é o formato mais usado para documentação em de bibliotecas Python, e permite que passêmos mais opções para diferentes diagramações de coisas como figuras, tabelas, links e parágrafos. Basicamente podemos especificar tags diferentes no template HTML do tema e os chamar usando flags dos comandos do reStructuredText. Isso parece ser mais flexível porque Markdown não pode fazer isso. Entretanto, é necessário configurar várias opções no template que basicamente esqueceria depois de um tempo. Então acabei escolhendo escrever tudo em Markdown porque Markdown tem a vantagem de interpretar livremente pedaços de HTML sempre que quiser alguma diagramação especial para qualquer coisa. Foi assim que coloquei a legenda na figura dos pelicanos no topo desse artigo:

```liquid
{% img align-center {filename}/figures/592px-PelecanusGronvold.jpg 450  "PelecanusGronvold by Henrik Groenvold - Ibis 1914. Licensed under Public Domain via Wikimedia Commons" "pelicanos"  %}
```
```html
<p align="center" style="width: 350px; max-width: 100%; text-align: left; margin-left: auto; margin-right: auto;">
  PelecanusGronvold by Henrik Groenvold - Ibis 1914.
  </br>
  <font color="#C8C8C8">
    Licensed under Public Domain via Wikimedia Commons.
  </font>
</p>
```

## Plugins que estou usando

A primeira linha do exemplo acima é um [liquid](https://github.com/Shopify/liquid/wiki) tag que permite configurar o tamanho da figura. Existem liquid tags preconfigurados em plugins do Pelican. Curti principalmente o liquid tag que inserere [IPython Notebooks](http://ipython.org/notebook.html), algo que vou usar bastante. Aqui vai a lista dos plugins que estou usando no momento:

```python
PLUGINS = ['liquid_tags.img',
           'liquid_tags.video',
           'liquid_tags.youtube',
           'liquid_tags.vimeo',
           'liquid_tags.include_code',
           'liquid_tags.notebook',
           'summary',
           'sitemap',
           'latex',
          ]
```

Funciona super bem para por filmes nos posts configurando o tamanho da janela. Olhe o exemplo:

```liquid
{% youtube 9F1iWp4Gl3k [240] [180] %}
```
{% youtube 9F1iWp4Gl3k [240] [180] %}


## Usando $\LaTeX$

O plugin de $\LaTeX$ funciona super bem. Para colocar fórmulas no texto, basta escrever entre símbolos de dolar `$...$`. Por exemplo, `$x^2_a$` vira $x^2_a$! Quando usamos dólares duplos `$$...$$`, a equação é escrita numa linha sozinha e centralizada. Por exemplo:

```latex
$$
	F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} \, dx
$$
```

$$
    F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} \, dx
$$

Também é possível colocar numerações com labels nas equações de duplo dólar usando o "environment" `equation` do $\LaTeX$:

```latex
$$
	\begin{equation}
		F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} \, dx 
		\label{eq}
	\end{equation}
$$
```
$$
	\begin{equation}
		F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} \, dx 
		\label{eq}
	\end{equation}
$$

Então chamamos a referência no meio do texto usando o comando `$\ref{eq}$`: "Veja a Eq. $\ref{eq}$!". Faz até link para a linha da equação no texto!

## Incluindo código fonte

```liquid
  {% include_code hello-pelican-teste.py lang:python Hello Pelican Codigo Teste%}
```

{% include_code hello-pelican-teste.py lang:python Hello Pelican Codigo Teste%}

## Incluindo Ipython Notebooks


No base.html
```liquid
    {% if 'liquid_tags.notebook' in PLUGINS %}
        {% include 'liquid_tags_nb_header.html' %}
    {% endif %}
```
--------------------------------------------------

{% notebook hello-pelican-teste.ipynb %}


