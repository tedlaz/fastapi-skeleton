from pathlib import Path

current_dict = Path(__file__).parent.resolve()


def acc_sql(filename='chart.txt', table='acc'):
    slines = []
    with open(current_dict / filename, encoding='utf8') as fil:
        for line in fil.readlines():
            code, *namewords = line.split()
            name = ' '.join(namewords)
            slines.append(f" ('{code}', '{name}')")
    sql = f"INSERT INTO {table} (code, name) VALUES"
    sql += ','.join(slines)
    return sql
