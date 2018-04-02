import csv


def write_csv(data):
	with open('names.csv', 'a') as file:
		writer = csv.writer(file)
		writer.writerow((data['name'], data['surname'], data['age']))


def write_csv2(data):
	with open('names.csv', 'a') as file:
		order = ['name', 'surname', 'age']
		writer = csv.DictWriter(file, fieldnames=order)

		writer.writerow(data)


def main():
	d1 = {'name': 'Petr', 'surname': 'Ivanov', 'age': 33}
	d2 = {'name': 'Fedr', 'surname': 'Petrov', 'age': 23}
	d3 = {'name': 'Petro', 'surname': 'Sidorov', 'age': 53}

	l = [d1, d2, d3]

	with open('names.csv') as file:
		fieldnames = ['surname', 'name', 'age']
		reader = csv.DictReader(file, fieldnames=fieldnames)

		for row in reader:
			print(row)


if __name__ == '__main__':
	main()
