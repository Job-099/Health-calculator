IMAGE_NAME=health-calculator-service
PORT=5000

init:
	@echo "initialization";
	@echo "Creation d'un environment virtuel"; \
	python3 -m venv .venv; \
	. .venv/bin/activate && \
	echo "Installer les librairies" && \
	pip install -r requirements.txt 

run: 
	@echo "Running the flask app...";
	. .venv/bin/activate && \
	python3 app.py

test:
	@echo "Running unittest...";
	. .venv/bin/activate && \
	python3 test.py

test-api:
	@echo "Running the api...";
	. .venv/bin/activate && \
	python3 test.py	
build:
	docker build -t $(IMAGE_NAME) .
run-container: 
	docker run -d -p $(PORT):5001 $(IMAGE_NAME)