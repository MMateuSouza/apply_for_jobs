#!/bin/bash

docker-compose up -d

docker exec -it password-generator-frontend /bin/bash -c "ln -snf /usr/share/zoneinfo/America/Manaus /etc/localtime && dpkg-reconfigure -f noninteractive tzdata"
