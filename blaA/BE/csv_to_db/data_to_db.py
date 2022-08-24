import csv
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apiserver.settings")
django.setup() 

from categorys.models import JobCategory,Sido,Gugun,Dong

job_main = './csv_to_db/job_category.csv'

with open(job_main, newline='') as f_csv:
		row_dics = csv.DictReader(f_csv)
		for row in row_dics: 
			print(row)
			JobCategory.objects.create(
				job_main_code = row['job_main_code'],
				job_main_category = row['job_main_category'],
			)

# job_sub = 'C:/Users/multicampus/Desktop/blaA/BE/csv_to_db/job_sub_category.csv'

# with open(job_sub, newline='') as f_csv:
# 		row_dics = csv.DictReader(f_csv)
# 		for row in row_dics: 
# 			print(row)
# 			JobSubCategory.objects.create(
# 				job_sub_code = row['job_sub_code'],
# 				job_sub_category = row['job_sub_category'],
# 			)


sido = './csv_to_db/sido.csv'

with open(sido, newline='') as f_csv:
		row_dics = csv.DictReader(f_csv)
		for row in row_dics: 
			print(row)
			Sido.objects.create(
				sido_code = row['sido_code'],
				sido_name = row['sido_name'],
			)
gugun = './csv_to_db/gugun.csv'

with open(gugun, newline='') as f_csv:
		row_dics = csv.DictReader(f_csv)
		for row in row_dics: 
			print(row)
			Gugun.objects.create(
				gugun_code = row['gugun_code'],
				gugun_name = row['gugun_name'],
			)
dong = './csv_to_db/dong.csv'

with open(dong, newline='') as f_csv:
		row_dics = csv.DictReader(f_csv)
		for row in row_dics: 
			print(row)
			Dong.objects.create(
				dong_code = row['dong_code'],
				sido_name = row['sido_name'],
				gugun_name = row['gugun_name'],
				dong_name = row['dong_name'],
			)