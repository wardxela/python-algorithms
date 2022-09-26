bull_cost = 10
cow_cost = 5
calf_cost = 0.5
wallet = 100

bull_count = 0
cow_count = 0
calf_count = 0

num = 1

while wallet - bull_count * bull_cost - cow_count * cow_cost - calf_count * calf_cost > 0:
    bull_count += 1
    while wallet - bull_count * bull_cost - cow_count * cow_cost - calf_count * calf_cost > 0:
        cow_count += 1
        while wallet - bull_count * bull_cost - cow_count * cow_cost - calf_count * calf_cost > 0:
            calf_count += 1
        if calf_count == 0:
            continue
        print(f'{num}. Быки: {bull_count}, коровы: {cow_count}, телята: {calf_count}')
        calf_count = 0
        num += 1
    cow_count = 0
