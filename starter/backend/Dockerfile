FROM public.ecr.aws/docker/library/python:3.10-slim
ENV FLASK_RUN_HOST=0.0.0.0

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc build-essential libpcre2-dev && \
    pip install --no-cache-dir pipenv && \
    rm -rf /var/lib/apt/lists/*

COPY Pipfile* ./
RUN pipenv install --system --deploy

COPY . ./backend/

EXPOSE 5000

CMD ["uwsgi", "--http", ":5000", "--master", "--enable-threads", "--manage-script-name", "--mount", "/=backend:app"]