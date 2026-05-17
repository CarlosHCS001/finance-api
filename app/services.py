def categorize(description: str) -> str:
    description = description.lower()  # deixa tudo minúsculo pra facilitar

    if "mercado" in description or "supermercado" in description:
        return "alimentação"

    if "uber" in description or "taxi" in description:
        return "transporte"

    if "netflix" in description or "cinema" in description:
        return "lazer"

    if "consulta" in description or "medico" in description:
        return "saude"

    if "curso" in description or "certificado" in description:
        return "educacao"

    # se não reconheceu nada
    return "outros"

def get_summary(transactions):
    total = 0
    by_category = {}

    for t in transactions:
        total += t.amount
        category = t.category.lower() if t.category else "outros"  # normaliza

        if category not in by_category:
            by_category[category] = 0
        by_category[category] += t.amount

    return {"total": total, "by_category": by_category}