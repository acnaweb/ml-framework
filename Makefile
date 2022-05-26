requirements:
	pip install -r requirements.txt

run_etl: clean
	python src/app/data/make_dataset.py

clean: 
	scripts/clean.sh	

setup: clean
	chmod +x scripts/*
	scripts/create_folder.sh


run_train: 
	python src/app/models/train_model.py
