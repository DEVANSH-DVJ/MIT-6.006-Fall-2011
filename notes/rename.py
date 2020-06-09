from pathlib import Path

for i in range(1, 134):
	try:
		if i in range(1,10):
			data_file = Path('CamScanner 06-10-2020 01.50.19_' + str(i) + '.jpg')
			data_file.rename('MIT-6006-00' + str(i) + '.jpg')
		if i in range(10,100):
			data_file = Path('CamScanner 06-10-2020 01.50.19_' + str(i) + '.jpg')
			data_file.rename('MIT-6006-0' + str(i) + '.jpg')
		if i in range(100,1000):
			data_file = Path('CamScanner 06-10-2020 01.50.19_' + str(i) + '.jpg')
			data_file.rename('MIT-6006-' + str(i) + '.jpg')
	except:
		continue
