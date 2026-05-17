from app.omdb import buscar_filme, formatar_filme


def main():
    print("\n🎥  CineBusca — Pesquise qualquer filme!")
    print("    (Digite 'sair' para encerrar)\n")

    while True:
        titulo = input("🔍  Nome do filme: ").strip()

        if titulo.lower() == "sair":
            print("\n👋  Até mais!\n")
            break

        if not titulo:
            print("⚠️   Por favor, digite um título.\n")
            continue

        try:
            dados = buscar_filme(titulo)
            print(formatar_filme(dados))
        except ValueError as e:
            print(f"\n❌  {e}\n")
        except Exception as e:
            print(f"\n⚠️   Erro ao buscar o filme: {e}\n")


if __name__ == "__main__":
    main()
