data = []
sum = 0

with open ("day-2/input.txt") as f:
    input = f.read().split(',')

for ranges in input:
    if not ranges:
        continue
    start_str, end_str = ranges.split('-')
    start = int(start_str)
    end = int(end_str)

    data.append([start, end])

for i in range(len(data)):
    for j in range(data[i][1] - data[i][0] + 1):
        
        n = data[i][0] + j
        num_string = str(n)
        num_digits = len(num_string)
        h = num_digits // 2
        
        if num_digits % 2 == 1:
            continue
        else:
            first_half = num_string[:h]
            second_half = num_string[h:]
            
            if first_half == second_half:
                sum += n
            
print(f"day 2 part 1: {sum}")