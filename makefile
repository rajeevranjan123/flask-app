venv:
	python -m venv venv

install: venv
	. venv/bin/activate && pip install -r requirements.txt

run: 
	. venv/bin/activate && python app.py 

clean:
	rm -rf venv
	find . -type d -name "__pycache__" -exec rm -r {} +
