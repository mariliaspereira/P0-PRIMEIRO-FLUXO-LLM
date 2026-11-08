def criar_prompt(resumo):
    prompt = f"""
    Você é um assistente especializado em leitura científica.

    Analise o resumo de artigo científico fornecido abaixo.

    Extraia as seguintes informações:

    1. Objetivo do estudo:
    2. Desenho metodológico:
    3. População estudada:
    4. Principais resultados:
    5. Conclusão dos autores:

    Regras importantes:
    - Utilize somente informações presentes no resumo.
    - Não invente informações.
    - Se uma informação não estiver disponível, escreva:
      "Não identificado no resumo".
    - Seja claro e objetivo.

    RESUMO DO ARTIGO:
    {resumo}
    """

    return prompt
