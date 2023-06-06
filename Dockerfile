FROM python:3.10-alpine AS base
COPY requirements.txt ./
RUN python -m venv /opt/venv \
    && . /opt/venv/bin/activate \
    && pip install --upgrade pip \
    && pip install --no-cache -r requirements.txt 

# In-Docker development image
FROM python:3.10-alpine AS development
COPY --from=base /opt/venv /opt/venv
WORKDIR /app
CMD tail -f /dev/null

# Docker test image
FROM python:3.10-alpine AS test
COPY --from=install /opt/venv /opt/venv
WORKDIR /app
COPY . ./
RUN . /opt/venv/bin/activate \
    && pip install --upgrade pip \
    && pip install pytest mypy pylint
RUN RUN mypy --install-types
CMD . /opt/venv/bin/activate \
    && pytest && python -m doctest *.py \
    && mypy ./ && pylint ./*.py

# Docker deployment image
FROM python:3.10-alpine AS deployment
COPY --from=base /opt/venv /opt/venv
WORKDIR /app
COPY calculator.py ./
CMD . /opt/venv/bin/activate \
    && python calculator.py