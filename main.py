def bank_credit(price, year_percent, months):
    month_percent = year_percent / 1200
    return int(price * (month_percent + month_percent / ((1 + month_percent)**months - 1)))


def main(max_can_pay_month, house_price):
    bank_will_pay = 400_000_000

    if house_price * 0.74 < bank_will_pay:
        bank_will_pay = house_price * 0.74

    print(f'bank will pay you: {bank_will_pay}')

    first_deposit = house_price - bank_will_pay
    print(f'your first deposit: {first_deposit}')

    for_ipoteka_bank_every_month = bank_credit(bank_will_pay, 18, 240)
    for_tbc_bank_every_month = bank_credit(first_deposit - 50_000_000, 28, 36)

    every_month_pay = for_ipoteka_bank_every_month + for_tbc_bank_every_month

    print(f'ipoteka({for_ipoteka_bank_every_month}) + tbc({for_tbc_bank_every_month}) = {every_month_pay}')


if __name__ == '__main__':
    max_can_pay_month = 4_000_000
    house_price = int(input('The house price: '))
    main(max_can_pay_month, house_price)
