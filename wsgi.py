'''
wsgi is to help us live-update the codes on save
'''
from main import app

if __name__ == '__main__':
    app.run()