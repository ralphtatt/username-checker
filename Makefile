VENV ?= "username-checker"

build-lambda:
	@echo "Removing, if it exists, old deployment_package.zip"
	rm deployment_package.zip
	@echo "Making deployment package zip"
	zip -r deployment_package \
	lambda_function.py \
	urls \
	usernames
	cd $(VENV)/lib/python3.8/site-packages/ ; \
	zip -ru ../../../../deployment_package.zip *

init:
	terraform init terraform/

plan: init build-lambda
	terraform plan terraform/

build: init build-lambda
	terraform apply -auto-approve terraform/

destroy:
	terraform destroy -auto-approve terraform/
