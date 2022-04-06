# Docker_Flask

to build image (will replace everytime for same image)<br>
sudo docker build -t docker-flask-test .

to recreate image force<br>
docker-compose up --force-recreate

to show all docker images:<br>
sudo docker image ls

to remove docker images:<br>
sudo docker rmi -f docker-flask-test

start docker application<br>
#first external 9000  and second internal system port<br>
sudo docker run -p 9000:9000 -d docker-flask-test

to stop docker:<br>
docker stop <container_id>


to show all running containers:<br>
sudo docker ps

to view logs realtime:<br>
sudo docker logs -f <CONTAINER>

to get into container shell:<br>
sudo docker exec -it <container_id> bash

Copy file to container:<br>
docker cp foo.txt container_id:/foo.txt

Copy file from container:<br>
docker cp container_id:/foo.txt foo.txt




-------------------------------------------------------------------------------------------------

to remove all resources:<br>
#it will delete all docker images and containers<br>
sudo docker system prune



To check all docker container running:<br>
sudo docker ps -a

To kill docker container:<br>
sudo docker rm -f container_id



Save docker image:<br>
docker save -o <path for generated tar file> <image name>


load docker image:<br>
docker load -i <path to image tar file>
