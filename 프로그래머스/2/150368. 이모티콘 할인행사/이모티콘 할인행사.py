from itertools import product

def solution(users, emoticons):
    answer = []
    discount_li = [10, 20, 30, 40]
    
    users.sort(key=lambda x : x[0])
    for discount in discount_li:
        if discount < users[0][0]:
            discount_li.remove(discount)
        else:
            break
    
    for discounts in product(discount_li, repeat = len(emoticons)):
        discounts = list(discounts)
        users_total = 0
        result = [0, 0]
        for user in users:
            total = 0
            for idx, discount in enumerate(discounts):
                if discount >= user[0]:
                    total += emoticons[idx] * (100 - discount) * 0.01
            
            if total >= user[1]:
                result[0] += 1
            else:
                result[1] += round(total)
        answer.append(result)
    answer.sort(key=lambda x : (x[0], x[1]))
    return answer[-1]