# simple-python-containers

-- EXPOSE 5000

sudo docker build -t app:latest .

sudo docker image ls

sudo docker run -it -p 5000:5000 app:latest

sudo docker ps -a

docker-app/
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── db/
│   └── init.sql
└── docker-compose.yml
