.ONESHELL:

dev:
	docker-compose -f docker-compose.yml up --build

test:
	 docker-compose -f docker-compose.yml up -d --build

clean:
	docker-compose down && docker volume rm $(docker volume ls -q)

build-frontend:
	cd ./frontend && npm run build

deploy-frontend:
	cp ./frontend/dist ./frontend-server/ -r
