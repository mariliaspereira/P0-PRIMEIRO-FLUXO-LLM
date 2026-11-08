def main():
    print("====================================")
    print("EXTRATOR DE INFORMAÇÕES CIENTÍFICAS")
    print("====================================")

    texto_artigo = input("\nCole o resumo do artigo científico: ").strip()

    if not texto_artigo:
        print("\nErro: você precisa informar um resumo.")
        return

    print("\nTexto recebido com sucesso!")
    print(f"Quantidade de caracteres: {len(texto_artigo)}")


if __name__ == "__main__":
    main()
