build: dist/cython_oracle-*.whl

install: .venv dist/cython_oracle-*.whl
	.venv/bin/pip install --force-reinstall dist/cython_oracle-*.whl

test: .venv install
	.venv/bin/pip install pytest
	.venv/bin/pytest tests

list: dist/cython_oracle-*.whl
	.venv/bin/python -m zipfile --list dist/cython_oracle-*.whl

clean:
	rm -rf build
	rm -rf dist
	rm -rf .venv

.venv:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip

dist/cython_oracle-*.whl: .venv cython_oracle/oracle.pyx liboracle/src/oracle.*
	.venv/bin/pip install build
	.venv/bin/python -m build
