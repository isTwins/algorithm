import datetime

def solution(fees, records):
    answer = []
    cars = [0 for i in range(10000)]
    records_dict = {}
    for record in records:
        time, number, io = record.split()
        if io == 'IN':
            records_dict[number] = time
        else:
            entrance_time = datetime.datetime.strptime(records_dict[number], '%H:%M')
            exit_time = datetime.datetime.strptime(time, '%H:%M')
            parking_time = exit_time - entrance_time
            parking_time = parking_time.seconds // 60
            cars[int(number)] += parking_time
            records_dict[number] = ''
    for key, value in records_dict.items():
        if value != '':
            entrance_time = datetime.datetime.strptime(value, '%H:%M')
            exit_time = datetime.datetime.strptime('23:59','%H:%M')
            parking_time = exit_time - entrance_time
            parking_time = int(parking_time.total_seconds() // 60)
            cars[int(key)] += parking_time
    basic_time, basic_fee, interval_time, interval_fee = fees
    for key in records_dict.keys():
        print(cars[int(key)])
        if cars[int(key)] <= basic_time:
            fee = basic_fee
        else:
            if (cars[int(key)] - basic_time) % interval_time != 0:
                fee = basic_fee + ((cars[int(key)] - basic_time) // interval_time + 1) * interval_fee
            else:
                fee = basic_fee + ((cars[int(key)] - basic_time) // interval_time) * interval_fee
        cars[int(key)] = fee
    sort_records_dict = sorted(records_dict.keys())
    for key in sort_records_dict:
        answer.append(cars[int(key)])
        
    return answer