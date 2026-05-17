# 🎬 CineBusca

> Aplicação CLI em Python para busca de filmes utilizando a [OMDb API](https://www.omdbapi.com/).  
> Projeto desenvolvido como parte do BootCamp — Etapa 2 (Entrega Intermediária).

---

## 🚀 Acesso à Aplicação

▶️ **[Executar no Replit](https://replit.com)** ← _substitua pelo seu link após o deploy_

---

## 📋 Sobre o Projeto

O **CineBusca** é uma aplicação de linha de comando (CLI) que permite ao usuário pesquisar informações detalhadas sobre qualquer filme diretamente no terminal. Os dados são obtidos em tempo real pela **OMDb API** (Open Movie Database), uma API pública e gratuita.

**Informações exibidas por filme:**
- Título e ano de lançamento
- Gênero, diretor e elenco principal
- Duração e país de origem
- Nota no IMDb
- Sinopse

---

## 🗂️ Estrutura do Projeto

```
cinebusca/
├── app/
│   ├── __init__.py
│   └── omdb.py          # Integração com a OMDb API
├── tests/
│   ├── __init__.py
│   └── test_omdb.py     # Testes de integração
├── .github/
│   └── workflows/
│       └── ci.yml       # Pipeline de CI (GitHub Actions)
├── main.py              # Ponto de entrada da aplicação CLI
├── requirements.txt
└── README.md
```

---

## ⚙️ Como Executar Localmente

### Pré-requisitos
- Python 3.9+
- pip

### Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/cinebusca.git
cd cinebusca

# 2. (Opcional) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# 3. Instale as dependências
pip install -r requirements.txt
```

### Execução

```bash
python main.py
```

---

## 🧪 Executar os Testes

```bash
pytest tests/ -v
```

Os testes de integração utilizam **mock** da chamada HTTP para validar o fluxo de dados sem depender da disponibilidade da API externa.

---

## 🔌 API Utilizada

| API | Endpoint | Método |
|-----|----------|--------|
| [OMDb API](https://www.omdbapi.com/) | `https://www.omdbapi.com/?t={titulo}&apikey={chave}` | GET |

A OMDb é uma API pública gratuita (até 1.000 requisições/dia) que não requer cadastro para uso com a chave de demonstração.

---

## 🌿 Branches e Issues

| Branch | Descrição |
|--------|-----------|
| `main` | Código estável e revisado |
| `entrega-intermediaria` | Feature de integração com a OMDb API (Issue #1) |

---

## ✅ CI/CD

O projeto utiliza **GitHub Actions** para rodar automaticamente a cada push:
1. **Lint** com `flake8`
2. **Testes** com `pytest`

---

## 👤 Autor

Desenvolvido por **Mateus Carreiro Claudino** — BootCamp Etapa 2.
