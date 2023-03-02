dev:
	docker-compose up -d

dev-down:
	docker-compose down

server:
	uvicorn app.app:app --reload