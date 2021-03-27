VENV ?= "username-checker"

build-lambda:
	rm deployment_package.zip
	zip -r deployment_package \
	lambda_function.py \
	urls \
	usernames
	cd $(VENV)/lib/python3.8/site-packages/ ; \
	zip -ru ../../../../deployment_package.zip *


