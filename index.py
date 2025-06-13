"""
    Desafio de código para uma aplicação de desconto em loja,


    O uso de 'Decimal' garanti que não haja imprecisão do float,
    é ótimo para aplicação financeira (bancos, lojas, entre outros)
"""

from decimal import Decimal, ROUND_HALF_UP

DEFAULT_DECIMAL_PLACES = 2

def round_decimal(value: Decimal, decimal_places: int) -> Decimal:
    fator = Decimal('1.' + ('0' * decimal_places))
    return value.quantize(fator, rounding=ROUND_HALF_UP)

class Store():
    DISCOUNT_COUPONS: dict = {
        "DESCONTO10": Decimal('0.10'),
        "DESCONTO20": Decimal('0.20'),
        "SEM_DESCONTO": Decimal('0.00')
    }

    @staticmethod
    def apply_discount(coupon: str, value: Decimal) -> Decimal:
        """
        Aplica um cupom de desconto a um valor

        Args:
            coupon (str): A descrição do cupom de desconto
            value (float): O valor a ser descontado

        Returns:
            float: O valor já aplicado o desconto
        """
        discounted_value_decimal: Decimal = value
        # Aplicando o desconto ao valor
        if coupon in Store.DISCOUNT_COUPONS:
            discount = Store.DISCOUNT_COUPONS[coupon]
            discounted_value_decimal *= (Decimal('1.00') - discount)
        # Aplicando a política de arredondamento
        discounted_value_decimal = discounted_value_decimal.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        # return float(discounted_value_decimal)
        return round_decimal(discounted_value_decimal, DEFAULT_DECIMAL_PLACES)

# TODO: Aplique o desconto se o cupom for válido:
# Entrada do usuário
# value = Decimal(input().strip())
# coupon = input().strip()
# print(Store.apply_discount(coupon, value))

EXAMPLES = [
    (Decimal('100'), 'DESCONTO10'),
    (Decimal('200'), 'DESCONTO20'),
    (Decimal('50'), 'SEM_DESCONTO'),
    (Decimal('75'), 'CUPOM_INVALIDO'),
]

for value, coupon in EXAMPLES:
    print(f"valor = {value} e coupon = {coupon} => Valor descontado: {Store.apply_discount(coupon, value)}")