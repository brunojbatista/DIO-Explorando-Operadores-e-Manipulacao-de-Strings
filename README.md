# 🛍️ Sistema de Aplicação de Desconto em Loja

Este projeto implementa um sistema simples de aplicação de cupons de desconto em valores monetários, utilizando a biblioteca `decimal` do Python para garantir precisão em contextos financeiros.

---

## ⚙️ Funcionalidades

- Aplicação de cupons de desconto como `DESCONTO10`, `DESCONTO20` e `SEM_DESCONTO`.
- Arredondamento correto para duas casas decimais (evita erros comuns com `float`).
- Pode ser facilmente integrado a sistemas de vendas ou lojas virtuais.

---

## 🧠 Como Funciona

### 🎯 Classe `Store`

A classe `Store` contém:

- Um dicionário `DISCOUNT_COUPONS` com os cupons disponíveis e os respectivos percentuais de desconto.
- Um método `apply_discount(coupon, value)` que aplica o desconto ao valor e retorna o resultado corretamente arredondado.

### 📐 Precisão Financeira

A biblioteca `decimal` é usada para garantir que não haja erros de arredondamento (como ocorre com `float`). O arredondamento segue a regra `ROUND_HALF_UP`, comum em contextos monetários.

---

## ▶️ Como Usar

1. Certifique-se de estar usando **Python 3.6 ou superior**.
2. Copie o código para um arquivo `.py`, por exemplo: `descontos.py`.
3. Execute o script:

```bash
python descontos.py
```

4. O script contém alguns exemplos:

```python
EXAMPLES = [
    (Decimal('100'), 'DESCONTO10'),
    (Decimal('200'), 'DESCONTO20'),
    (Decimal('50'), 'SEM_DESCONTO'),
    (Decimal('75'), 'CUPOM_INVALIDO'),
]
```

Saída esperada:
```
valor = 100 e coupon = DESCONTO10 => Valor descontado: 90.00
valor = 200 e coupon = DESCONTO20 => Valor descontado: 160.00
valor = 50 e coupon = SEM_DESCONTO => Valor descontado: 50.00
valor = 75 e coupon = CUPOM_INVALIDO => Valor descontado: 75.00
```

---

## ⚠️ Possíveis Erros e Comportamentos

| Situação | Resultado / Comportamento |
|---------|---------------------------|
| Cupom válido (e.g. `DESCONTO10`) | Aplica o desconto correspondente |
| Cupom inválido (e.g. `CUPOM_INVALIDO`) | Nenhum desconto é aplicado |
| Valor não numérico (em entrada interativa) | Lançará exceção se não tratado |
| Precisão inconsistente (com `float`) | Evitada pelo uso de `Decimal` |

---

## ✏️ Sugestões de Melhorias

- Validar entrada do usuário via `try/except`.
- Adicionar novos cupons com datas de validade.
- Gerar relatórios de vendas com desconto aplicado.
- Criar interface para uso via terminal ou web.

---

## 📄 Licença

Este projeto é livre para uso e modificação com fins educacionais ou comerciais.