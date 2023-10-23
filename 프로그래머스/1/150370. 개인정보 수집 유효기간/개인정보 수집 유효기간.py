def solution(today, terms, privacies):
    answer = []
    terms_dic = {}
    t_year, t_month, t_day = map(int, today.split("."))

    for i in terms:
        terms_type, period = map(str, i.split())
        terms_dic[terms_type] = int(period)
        
    for idx, privacy in enumerate(privacies):
        date, menu = map(str, privacy.split())
        year, month, day = map(int, date.split("."))
        month += terms_dic[menu]
        day -= 1
        if month > 12:
            year += month//12
            month = month%12
        if day == 0:
            day = 28
            month -= 1
        if month == 0:
            month = 12
            year -= 1
        if  year < t_year:
            answer.append(idx + 1)
        elif year == t_year:
            if month < t_month:
                answer.append(idx + 1)
            elif month == t_month:
                if day < t_day:
                    answer.append(idx + 1)
                    
    return answer