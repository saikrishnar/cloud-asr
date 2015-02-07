SHELL=/bin/bash
IP=`ip addr show docker0 | grep -Po 'inet \K[\d.]+'`
MESOS_SLAVE_IP=`docker inspect --format '{{ .NetworkSettings.IPAddress }}' mesos-slave`
FRONTEND_HOST_PORT=8000
MONITOR_HOST_PORT=8001
ANNOTATION_INTERFACE_HOST_PORT=8002
MONITOR_STATUS_PORT=5681
MONITOR_STATUS_ADDR=tcp://${IP}:${MONITOR_STATUS_PORT}
WORKER_PORT=5678
WORKER_ADDR=tcp://${IP}:${WORKER_PORT}
MASTER_TO_WORKER_PORT=5679
MASTER_TO_WORKER_ADDR=tcp://${IP}:${MASTER_TO_WORKER_PORT}
MASTER_TO_FRONTEND_PORT=5680
MASTER_TO_FRONTEND_ADDR=tcp://${IP}:${MASTER_TO_FRONTEND_PORT}
RECORDINGS_SAVER_HOST_PORT=5682
RECORDINGS_SAVER_GUEST_PORT=5682
RECORDINGS_SAVER_ADDR=tcp://${IP}:${RECORDINGS_SAVER_HOST_PORT}
MYSQL_ROOT_PASSWORD=123456
MYSQL_USER=cloudasr
MYSQL_PASSWORD=cloudasr
MYSQL_DATABASE=cloudasr
MYSQL_IP=`docker inspect --format '{{ .NetworkSettings.IPAddress }}' mysql`
MYSQL_CONNECTION_STRING="mysql://${MYSQL_USER}:${MYSQL_PASSWORD}@${MYSQL_IP}/${MYSQL_DATABASE}?charset=utf8"

SHARED_VOLUME=${CURDIR}/cloudasr/shared/cloudasr:/usr/local/lib/python2.7/dist-packages/cloudasr
MASTER_VOLUMES=-v ${CURDIR}/cloudasr/master:/opt/app -v ${SHARED_VOLUME}
MASTER_OPTS=--name master \
	-p ${MASTER_TO_WORKER_PORT}:${MASTER_TO_WORKER_PORT} \
	-p ${MASTER_TO_FRONTEND_PORT}:${MASTER_TO_FRONTEND_PORT} \
	-e WORKER_ADDR=tcp://0.0.0.0:${MASTER_TO_WORKER_PORT} \
	-e FRONTEND_ADDR=tcp://0.0.0.0:${MASTER_TO_FRONTEND_PORT} \
	-e MONITOR_ADDR=${MONITOR_STATUS_ADDR} \
	${MASTER_VOLUMES}

WORKER_VOLUMES=-v ${CURDIR}/cloudasr/worker:/opt/app -v ${SHARED_VOLUME}
WORKER_OPTS=--name worker \
	-p ${WORKER_PORT}:${WORKER_PORT} \
	-e HOST=${IP} \
	-e PORT0=${WORKER_PORT} \
	-e MASTER_ADDR=${MASTER_TO_WORKER_ADDR} \
	-e RECORDINGS_SAVER_ADDR=${RECORDINGS_SAVER_ADDR} \
	-e MODEL=en-towninfo \
	-v ${CURDIR}/data:/tmp/data \
	${WORKER_VOLUMES}

WEB_VOLUMES=-v ${CURDIR}/cloudasr/web:/opt/app -v ${SHARED_VOLUME}
WEB_OPTS=--name web \
	-p 8004:80 \
	${WEB_VOLUMES}

FRONTEND_VOLUMES=-v ${CURDIR}/cloudasr/frontend:/opt/app -v ${SHARED_VOLUME}
FRONTEND_OPTS=--name frontend \
	-p ${FRONTEND_HOST_PORT}:80 \
	-e MASTER_ADDR=${MASTER_TO_FRONTEND_ADDR} \
	${FRONTEND_VOLUMES}

MONITOR_VOLUMES=-v ${CURDIR}/cloudasr/monitor:/opt/app -v ${SHARED_VOLUME}
MONITOR_OPTS=--name monitor \
	-p ${MONITOR_HOST_PORT}:80 \
	-p ${MONITOR_STATUS_PORT}:${MONITOR_STATUS_PORT} \
	-e MONITOR_ADDR=tcp://0.0.0.0:${MONITOR_STATUS_PORT} \
	${MONITOR_VOLUMES}

MYSQL_OPTS=--name mysql \
	-e MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} \
	-e MYSQL_USER=${MYSQL_USER} \
	-e MYSQL_PASSWORD=${MYSQL_PASSWORD} \
	-e MYSQL_DATABASE=${MYSQL_DATABASE} \
	-v ${CURDIR}/mysql_data:/var/lib/mysql \
	-v ${CURDIR}/resources/mysql_utf8.cnf:/etc/mysql/conf.d/mysql_utf8.cnf

ANNOTATION_INTERFACE_VOLUMES=-v ${CURDIR}/cloudasr/annotation_interface:/opt/app \
	-v ${CURDIR}/cloudasr/annotation_interface/static/data:/opt/app/static/data \
	-v ${SHARED_VOLUME}
ANNOTATION_INTERFACE_OPTS=--name annotation_interface \
	--link mysql:mysql \
	-p ${RECORDINGS_SAVER_HOST_PORT}:${RECORDINGS_SAVER_GUEST_PORT} \
	-p ${ANNOTATION_INTERFACE_HOST_PORT}:80 \
	-e CONNECTION_STRING=${MYSQL_CONNECTION_STRING} \
	-e GOOGLE_LOGIN_CLIENT_ID=${CLOUDASR_GOOGLE_LOGIN_CLIENT_ID} \
	-e GOOGLE_LOGIN_CLIENT_SECRET=${CLOUDASR_GOOGLE_LOGIN_CLIENT_SECRET} \
	${ANNOTATION_INTERFACE_VOLUMES}

build:
	docker build -t ufaldsg/cloud-asr-base cloudasr/shared
	docker build -t ufaldsg/cloud-asr-web cloudasr/web
	docker build -t ufaldsg/cloud-asr-frontend cloudasr/frontend/
	docker build -t ufaldsg/cloud-asr-worker cloudasr/worker/
	docker build -t ufaldsg/cloud-asr-master cloudasr/master/
	docker build -t ufaldsg/cloud-asr-monitor cloudasr/monitor/
	docker build -t ufaldsg/cloud-asr-annotation-interface cloudasr/annotation_interface/

build_local:
	cp -r cloudasr/shared/cloudasr cloudasr/frontend/cloudasr
	cp -r cloudasr/shared/cloudasr cloudasr/worker/cloudasr
	cp -r cloudasr/shared/cloudasr cloudasr/master/cloudasr
	cp -r cloudasr/shared/cloudasr cloudasr/monitor/cloudasr
	cp -r cloudasr/shared/cloudasr cloudasr/annotation_interface/cloudasr
	docker build -t ufaldsg/cloud-asr-frontend cloudasr/frontend/
	docker build -t ufaldsg/cloud-asr-worker cloudasr/worker/
	docker build -t ufaldsg/cloud-asr-master cloudasr/master/
	docker build -t ufaldsg/cloud-asr-monitor cloudasr/monitor/
	docker build -t ufaldsg/cloud-asr-annotation-interface cloudasr/annotation_interface/
	rm -rf cloudasr/frontend/cloudasr
	rm -rf cloudasr/worker/cloudasr
	rm -rf cloudasr/master/cloudasr
	rm -rf cloudasr/monitor/cloudasr
	rm -rf cloudasr/annotation_interface/cloudasr

pull:
	docker pull mysql
	docker pull ufaldsg/cloud-asr-frontend
	docker pull ufaldsg/cloud-asr-worker
	docker pull ufaldsg/cloud-asr-master
	docker pull ufaldsg/cloud-asr-monitor
	docker pull ufaldsg/cloud-asr-annotation-interface

mysql_data:
	echo "PREPARING MySQL DATABASE"
	docker run ${MYSQL_OPTS} -d mysql
	docker stop mysql && docker rm mysql

run_locally: mysql_data
	docker run ${MYSQL_OPTS} -d mysql
	docker run ${WEB_OPTS} -d ufaldsg/cloud-asr-web
	docker run ${FRONTEND_OPTS} -d ufaldsg/cloud-asr-frontend
	docker run ${WORKER_OPTS} -d ufaldsg/cloud-asr-worker
	docker run ${MASTER_OPTS} -d ufaldsg/cloud-asr-master
	docker run ${MONITOR_OPTS} -d ufaldsg/cloud-asr-monitor
	docker run ${ANNOTATION_INTERFACE_OPTS} -d ufaldsg/cloud-asr-annotation-interface

run_mesos:
	python ${CURDIR}/deployment/run_on_mesos.py ${CURDIR}/deployment/mesos.json

run_worker:
	docker run ${WORKER_OPTS} -i -t --rm ufaldsg/cloud-asr-worker

run_web:
	docker run ${WEB_OPTS} -i -t --rm ufaldsg/cloud-asr-frontend python run.py

run_frontend:
	docker run ${FRONTEND_OPTS} -i -t --rm ufaldsg/cloud-asr-frontend

run_master:
	docker run ${MASTER_OPTS} -i -t --rm ufaldsg/cloud-asr-master

run_monitor:
	docker run ${MONITOR_OPTS} -i -t --rm ufaldsg/cloud-asr-monitor

run_annotation_interface:
	docker run ${ANNOTATION_INTERFACE_OPTS} -i -t --rm ufaldsg/cloud-asr-annotation-interface

stop:
	docker kill frontend worker master monitor annotation_interface mysql
	docker rm frontend worker master monitor annotation_interface mysql

unit-test:
	nosetests cloudasr/shared
	PYTHONPATH=${CURDIR}/cloudasr/shared nosetests -e test_factory cloudasr/frontend
	PYTHONPATH=${CURDIR}/cloudasr/shared nosetests -e test_factory cloudasr/master
	PYTHONPATH=${CURDIR}/cloudasr/shared nosetests -e test_factory cloudasr/worker
	PYTHONPATH=${CURDIR}/cloudasr/shared nosetests -e test_factory cloudasr/monitor
	PYTHONPATH=${CURDIR}/cloudasr/shared nosetests -e test_factory cloudasr/annotation_interface

integration-test:
	docker run ${FRONTEND_VOLUMES} --rm ufaldsg/cloud-asr-frontend nosetests /opt/app/test_factory.py
	docker run ${MASTER_VOLUMES} --rm ufaldsg/cloud-asr-master nosetests /opt/app/test_factory.py
	docker run ${MONITOR_VOLUMES} --rm ufaldsg/cloud-asr-monitor nosetests /opt/app/test_factory.py
	docker run ${ANNOTATION_INTERFACE_VOLUMES} --rm ufaldsg/cloud-asr-annotation-interface nosetests /opt/app/test_factory.py
	docker run ${WORKER_VOLUMES} --rm ufaldsg/cloud-asr-worker nosetests /opt/app/test_factory.py

test:
	nosetests tests/

compile-messages:
	protoc --python_out=. ./cloudasr/shared/cloudasr/messages/messages.proto
