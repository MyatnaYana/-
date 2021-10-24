from operator import itemgetter

class File:
    def __init__(self, name, id, memory, gr_id):
        self.id = id
		self.name = name
        self.memory = memory  
        self.log_id = log_id  
                            
class Catalog:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Fillog:
    def __init__(self, fileId, logId):
        self.file_id = fileId
        self.log_id = logId


catalogs = [
    Catalog ('Путешествия', 1)
	Catalog ('Сериалы', 2)
	Catalog ('АСОИУ', 3)
	Catalog ('Алиса', 4)
	
	Catalog ('other Путешествия', 11)
	Catalog ('other Сериалы', 22)
	Catalog ('other АСОИУ', 33)
	Catalog ('other Алиса', 44) ]

files = [
    File(1, 'Новая Зеландия', 1.3, 1)
	File(2, 'Аннотация 1-10', 0.2, 4)
	File(3, 'Акация', 5, 2)
	File(4,'Концерт в Самаре 11.09', 2, 5)
	File(5,'Контрольный вопрос 310', 0.4, 4) ]

file_catalogs = [
    Fillog (1, 1)
	Fillog (2, 3)
	Fillog (3, 2)
	Fillog (4, 4)
	Fillog (5, 3)

	 Fillog (1, 11)
	Fillog (2, 33)
	Fillog (3, 22)
	Fillog (4, 44)
	Fillog (5, 33) ]


def main():
    one_to_many = [(f.name, f.rate, c.name)
                   for c in catalogs
                   for f in files if c.id == f.log_id]

    many_to_many_temp = [(c.name, fc.stud_id, fc.grp_id)
                         for c in catalogs
                         for fc in log_id if c.id == fc.grp_id]

    many_to_many = [(f.name, f.memory, c_name)
                    for c_name, st_id, c_id in many_to_many_temp
                    for f in files if f.id == st_id]

    print("Задание В1:")
    res1 = []
    for name, _, group in one_to_many:
        if name[0] == "А":
            res1.append((name, group))
    print(res1)

    print("\nЗадание B2:")
    res2 = []
    for g in groups:
        g_students = list(filter(lambda x: x[2] == g.name, one_to_many))

        if len(g_students) > 0:
            g_rate = [rate for _, rate, _ in g_students]
            g_rate_min = min(g_rate)
            res2.append((g.name, g_rate_min))
    res2_sorted = sorted(res2, key=itemgetter(1))
    print(res2_sorted)

    print("\nЗадание В3:")
    res3 =[]
    for name, _, group in many_to_many:
        res3.append((name, group))
    res3_sorted = sorted(res3, key=itemgetter(0))
    print(res3_sorted)

if __name__ == "__main__":
    main()
