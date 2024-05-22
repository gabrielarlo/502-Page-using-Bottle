from bottle import route, run, static_file

@route('/')
def index():
    return static_file('index.html', root='public')

@route('/bg.png')
def favicon():
    return static_file('bg.png', root='public')

@route('/styles.css')
def favicon():
    return static_file('styles.css', root='public')

run(host='0.0.0.0', port=8502, debug=True)