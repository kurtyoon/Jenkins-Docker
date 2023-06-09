FROM tiangolo/uwsgi-nginx-flask:python3.9
# base 이미지 설정

COPY ./app /app
# ./app의 모든 파일들을 docker image 내의 /app 디렉토리로 복사함