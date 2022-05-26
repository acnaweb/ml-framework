requirements:
	pip install -r requirements.txt

run_etl: clean
	python src/app/data/make_dataset.py

clean: 
	scripts/clean.sh	

setup:
	chmod +x scripts/*
