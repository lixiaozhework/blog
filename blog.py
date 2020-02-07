from sanic import Sanic
from sanic.response import text

app = Sanic(__name__)

print(__name__)


@app.route('/')
def index(request):
    return text('hello')


if __name__ == '__main__':
    app.run(port=8000)