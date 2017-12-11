.PHONY: all
all: test build

.PHONY: build
build:
	python3 setup.py sdist build install --user --prefix=

.PHONY: test
test:
	python3 setup.py test
