.PHONY: test

test:
	pytest --log-cli-level=DEBUG -s -x --cov --cov-report=html tests/
