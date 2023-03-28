from itertools import product
discount_rates = [10, 20, 30, 40]


def solution(users, emoticons):
    result = [0, 0]
    for rates in product(discount_rates, repeat=len(emoticons)):
        emo_plus = 0
        emo_sales = 0
        for user in users:
            rate, standard = user
            price = 0

            for j in range(len(rates)):
                if rates[j] >= rate:
                    price += (100 - rates[j]) * emoticons[j] / 100

            if price >= standard:
                emo_plus += 1
            else:
                emo_sales += price

        if emo_plus > result[0]:
            result[0] = emo_plus
            result[1] = emo_sales
        elif emo_plus == result[0] and emo_sales > result[1]:
            result[1] = emo_sales

    return result
