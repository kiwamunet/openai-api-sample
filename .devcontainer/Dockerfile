# 既存のPythonイメージをベースにする
FROM python:3.10-buster

# ワーキングディレクトリを設定
ENV APP_ROOT /app
WORKDIR ${APP_ROOT}

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
