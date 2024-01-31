build:
	docker build -t flask-app .
start:
	docker run -p 5000:5000 flask-app
