def lucky_ticket(n):
    sum_dict = {}
    half = n // 2
    for i in range(10 ** half):
        digits_sum = sum(map(int, list(str(i))))
        if digits_sum in sum_dict:
            sum_dict[digits_sum] += 1
        else:
            sum_dict[digits_sum] = 1
    print(sum(map(lambda v: v ** 2, sum_dict.values())))


lucky_ticket(2)
lucky_ticket(4)
lucky_ticket(12)
