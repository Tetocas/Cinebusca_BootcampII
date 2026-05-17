import requests

OMDB_BASE_URL = "https://www.omdbapi.com/"
# Chave pública de demonstração (funciona para testes — limite de 1000 req/dia)
API_KEY = "trilogy"


def buscar_filme(titulo: str, api_key: str = API_KEY) -> dict:
    """
    Busca informações de um filme pelo título na OMDb API.
    Retorna um dicionário com os dados do filme ou lança exceção em caso de erro.
    """
    if not titulo or not titulo.strip():
        raise ValueError("O título do filme não pode ser vazio.")

    params = {"t": titulo.strip(), "apikey": api_key}

    response = requests.get(OMDB_BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    dados = response.json()

    if dados.get("Response") == "False":
        raise ValueError(f"Filme não encontrado: {dados.get('Error', 'Erro desconhecido')}")

    return dados


def formatar_filme(dados: dict) -> str:
    """
    Formata os dados de um filme para exibição no terminal.
    """
    linhas = [
        f"\n{'=' * 50}",
        f"🎬  {dados.get('Title', 'N/A')} ({dados.get('Year', 'N/A')})",
        f"{'=' * 50}",
        f"📋  Gênero    : {dados.get('Genre', 'N/A')}",
        f"🎭  Diretor   : {dados.get('Director', 'N/A')}",
        f"🌟  Elenco    : {dados.get('Actors', 'N/A')}",
        f"⏱️   Duração   : {dados.get('Runtime', 'N/A')}",
        f"🌍  País      : {dados.get('Country', 'N/A')}",
        f"🏆  IMDb      : {dados.get('imdbRating', 'N/A')} / 10",
        f"\n📖  Sinopse   :\n    {dados.get('Plot', 'N/A')}",
        f"{'=' * 50}\n",
    ]
    return "\n".join(linhas)
