NOSETESTS ?= nosetests

.PHONY: nosetests nosetests.coverage test test.coverage flake8

test: nosetests flake8
test.coverage: nosetests.coverage flake8
test.profile: nosetests.profile flake8

nosetests:
	@$(NOSETESTS) --with-doctest

nosetests.coverage:
	@$(NOSETESTS) --with-xcoverage --cover-package=flask_skeleton --cover-tests --cover-erase --with-doctest

nosetests.profile:
	@$(NOSETESTS) --with-doctest --with-profile

flake8:
	@flake8 flask_skeleton tests

clean:
	@rm -rf .coverage
	@rm -rf coverage.xml
