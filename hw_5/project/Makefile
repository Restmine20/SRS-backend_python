PIP := venv/Scripts/pip.exe
PYTHON3 := venv/Scripts/python.exe

clear:
	rm -rf venv

venv:
	python -m venv venv

install_requirements:
	${PIP} install -r requirements.txt

run:
	${PYTHON3} manage.py runserver