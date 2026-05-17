"""
Testes de Integração — CineBusca
Valida a comunicação com a OMDb API e o fluxo de dados da aplicação.
"""

import pytest
from unittest.mock import patch, MagicMock
from app.omdb import buscar_filme, formatar_filme


# ─── Dados de resposta simulada (mock) ────────────────────────────────────────

FILME_MOCK = {
    "Title": "Inception",
    "Year": "2010",
    "Genre": "Action, Adventure, Sci-Fi",
    "Director": "Christopher Nolan",
    "Actors": "Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page",
    "Runtime": "148 min",
    "Country": "United States, United Kingdom",
    "imdbRating": "8.8",
    "Plot": "A thief who steals corporate secrets through the use of dream-sharing technology.",
    "Response": "True",
}

RESPOSTA_NAO_ENCONTRADO = {
    "Response": "False",
    "Error": "Movie not found!",
}


# ─── Testes de Integração (com mock da chamada HTTP) ──────────────────────────

class TestBuscarFilme:

    @patch("app.omdb.requests.get")
    def test_busca_filme_com_sucesso(self, mock_get):
        """Verifica se a função retorna os dados corretamente quando a API responde com sucesso."""
        mock_response = MagicMock()
        mock_response.json.return_value = FILME_MOCK
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        resultado = buscar_filme("Inception")

        assert resultado["Title"] == "Inception"
        assert resultado["Director"] == "Christopher Nolan"
        assert resultado["imdbRating"] == "8.8"
        assert resultado["Response"] == "True"

    @patch("app.omdb.requests.get")
    def test_filme_nao_encontrado_lanca_excecao(self, mock_get):
        """Verifica se ValueError é lançado quando a API retorna filme não encontrado."""
        mock_response = MagicMock()
        mock_response.json.return_value = RESPOSTA_NAO_ENCONTRADO
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        with pytest.raises(ValueError, match="Filme não encontrado"):
            buscar_filme("xyzxyzxyz_titulo_invalido")

    @patch("app.omdb.requests.get")
    def test_parametros_enviados_corretamente(self, mock_get):
        """Verifica se a chamada à API usa os parâmetros corretos."""
        mock_response = MagicMock()
        mock_response.json.return_value = FILME_MOCK
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        buscar_filme("Inception", api_key="minha_chave")

        args, kwargs = mock_get.call_args
        assert kwargs["params"]["t"] == "Inception"
        assert kwargs["params"]["apikey"] == "minha_chave"

    def test_titulo_vazio_lanca_excecao(self):
        """Verifica se ValueError é lançado para títulos vazios sem chamar a API."""
        with pytest.raises(ValueError, match="título do filme não pode ser vazio"):
            buscar_filme("")

    def test_titulo_apenas_espacos_lanca_excecao(self):
        """Verifica se espaços em branco são rejeitados sem chamar a API."""
        with pytest.raises(ValueError, match="título do filme não pode ser vazio"):
            buscar_filme("   ")


# ─── Testes de Formatação ─────────────────────────────────────────────────────

class TestFormatarFilme:

    def test_formatar_exibe_titulo_e_ano(self):
        """Verifica se o título e o ano aparecem na saída formatada."""
        saida = formatar_filme(FILME_MOCK)
        assert "Inception" in saida
        assert "2010" in saida

    def test_formatar_exibe_diretor(self):
        """Verifica se o diretor aparece na saída formatada."""
        saida = formatar_filme(FILME_MOCK)
        assert "Christopher Nolan" in saida

    def test_formatar_exibe_nota_imdb(self):
        """Verifica se a nota do IMDb aparece na saída formatada."""
        saida = formatar_filme(FILME_MOCK)
        assert "8.8" in saida

    def test_formatar_lida_com_campos_ausentes(self):
        """Verifica se campos ausentes são exibidos como N/A sem quebrar a aplicação."""
        saida = formatar_filme({})
        assert "N/A" in saida
