#!.env/bin/python

from migrate.versioning import api
from config_dev import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO
from main import db
import os.path
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
  api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
  api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
  api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
