setup:
	mkdir data
	mkdir data/raw
	mkdir data/processed	
	mkdir scripts
	mkdir notebooks
	mkdir src
	mkdir src/app
	mkdir src/app/data
	mkdir src/app/model
	mkdir src/app/visualization
	
setup_env:
	conda activate ml-framework
	pip install -r requirements.txt
