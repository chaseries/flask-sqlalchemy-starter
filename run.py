#!./.env/bin/python

from app import app

if __name__ == '__main__':
  app.run('0.0.0.0', 7000, debug=True)
