from stack.config import create_app
from os import getenv

app_config = getenv('APP_CONFIG')
app = create_app(app_config)

if __name__ == '__main__':
    app.run()