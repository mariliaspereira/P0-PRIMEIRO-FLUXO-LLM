from src.prompt import criar_prompt


def test_criar_prompt():
    resumo = "O estudo avaliou a eficácia de uma vacina em adultos."

    resultado = criar_prompt(resumo)

    assert "Objetivo do estudo" in resultado
    assert "Desenho metodológico" in resultado
    assert "População estudada" in resultado
    assert resumo in resultado
