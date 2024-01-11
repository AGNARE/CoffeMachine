class CoffeeMachine:
    data = {
        'cappuccino': {
            'price': 130,
            'quantity': 20
        },
        'latte': {
            'price': 120,
            'quantity': 25
        }
    }

    def __init__(self, place, total_revenue=0):
        self.place = place
        self.data = dict(self.data)  # Создание копии данных чтобы не изменять оригинал(защищенность)
        self.total_revenue = total_revenue

    def buy_coffee(self, name, amount):
        if name not in self.data:
            return f"У нас нет {name} в меню."

        available_quantity = self.data[name]['quantity']
        amount_to_buy = min(amount, available_quantity)  # Купить не более, чем доступное количество.

        if amount_to_buy > 0:
            # Получение цены выбранного типа кофе.
            price = self.data[name]['price']
            # Расчет общей стоимости купленного кофе.
            cost = price * amount_to_buy
            # Уменьшение количества выбранного типа кофе в инвентаре.
            self.data[name]['quantity'] -= amount_to_buy
            # Увеличение общей выручки на сумму стоимости купленного кофе.
            self.total_revenue += cost
            return f"Вы купили {amount_to_buy} {name} за {cost} сомов."
        else:
            return f"Извините, {name} закончился."

    def refill_coffee(self, name, amount):
        if name in self.data:
            self.data[name]['quantity'] += amount
            return f"Добавлено {amount} {name} в машину."
        else:
            return f"У нас нет {name} в меню."

    def get_total_revenue(self):
        return f'Общая выручка {self.total_revenue}'

    def add_coffee(self, name, price, initial_quantity):
        if name not in self.data:
            self.data[name] = {'price': price, 'quantity': initial_quantity}
            return f"Добавлено {initial_quantity} {name} по цене {price}."
        else:
            return f"{name} уже есть в меню."


coffee_machine = CoffeeMachine(place="Office")

# print(coffee_machine.buy_coffee('latte', 1))

# Пополнение кофе
# print(coffee_machine.refill_coffee('latte', 20))

print(coffee_machine.buy_coffee('latte', 26))

# print(coffee_machine.get_total_revenue())

# print(coffee_machine.add_coffee('espresso', 110, 30))
