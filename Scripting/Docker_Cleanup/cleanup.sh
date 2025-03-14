#!/bin/sh
# Remove specific containers
sudo docker ps -a --filter "name=nginx" -q | grep -q . && sudo docker rm -f nginx

# Remove specific images
sudo docker images --filter=reference='ngi*' -q | grep -q . && sudo docker rmi $(docker images --filter=reference='ngi*' -q)
