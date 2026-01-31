PIP := venv/Scripts/pip.exe
PYTHON3 := venv/Scripts/python.exe
TESTS := venv/Scripts/pytest.exe -v test_controllers.py

clear:
	rm -rf venv

venv:
	python -m venv venv

install_requirements:
	${PIP} install -r requirements.txt

run:
	${PYTHON3} server.py

test:
    ${TESTS}