# SimpleBible 📖
### Api simples que retorna trechos da Biblia em formatos diversos

---
### Objetivo 📋
Desenvolver uma **ferramenta para consultas em banco de dados**, que permita acessar os resultados tanto via **API web** quanto pelo **terminal**.  
A ferramenta retorna os resultados em texto no terminal ou, na versão web, em formatos como **JSON, TXT ou HTML**.

---
### Recursos 🛠️
- ✅ Retorna trechos da biblia em Html, Json ou txt
- ✅ Permite buscar trechos especificos
- ✅ Dados salvos no db
- ✅ Versões web e cli

<span>
  <h3> Tecnologias 🔋 </h3>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white" />
</span>

---
### Como usar:
```
# Api
  - Executa a api flask para consultas pelo navegador

  . http://127.0.0.1:5000/?book=tiago&capt=1&vers=1 
  . retorna o versiculo 1 do capitulo 1 do livro de Tiago em html
  
  . http://127.0.0.1:5000/json 
  . retorna a Biblia em json
  
  . http://127.0.0.1:5000/txt
  . retorna a Biblia em txt
```

``` 
# Python
  - Permite executar as consultas via terminal 
  $ python run_terminal.py bible Tiago
  $ retorna o livro de Tiago 
```

```
# Bash
  - Adiciona a função bible() ao arquivo ~.bashrc para executar a função diretamente do terminal. 
  $ bible 1_pedro 1:5 
  $ retorna o versiculo 5 do caipulo 1 de 1 Pedro 
```
