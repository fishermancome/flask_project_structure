from app import create_app


application = app = create_app("production")


# gunicorn 启动方式
# gunicorn -w 4 wsgi:app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
