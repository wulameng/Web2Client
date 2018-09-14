from web2client.app import app


def start():
    print('start...')
    app.run(host='0.0.0.0', port=8080, debug=False)
