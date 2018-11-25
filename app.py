import os
from bottle import route, run

@route('/hello/:name')
def index(name='World'):
    return '<b>Hello %s!</b>' % name


if __name__ == '__main__':
    # Get required port, default to 5000.
    port = os.environ.get('PORT', 5000)

    # Run the app.
    run(host='0.0.0.0', port=port)
