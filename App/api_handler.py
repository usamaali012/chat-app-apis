import tornado
from tornado import escape
import traceback
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from tornado.web import RequestHandler
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError, DatabaseError

from controllers import registry
from models.app_models import Base


class MainApiHandler(RequestHandler):
    def prepare(self):
        super().prepare()
        self.gdb = None
        self.Data = {}
        self.get_request_data()
        self.get_db_connection()

    def post(self, *args, **kwargs):
        if len(args) != 2:
            raise tornado.web.HTTPError(404)

        slug = args[0]
        method = args[1]
        print('API Called -> {}/{}'.format(slug, method))

        if slug not in registry:
            raise tornado.web.HTTPError(404)

        controller = registry[slug]
        ctrl = controller(self)

        if method not in ctrl.PublicMethods:
            raise tornado.web.HTTPError(404)

        func = getattr(ctrl, method, None)
        if func is None:
            raise tornado.web.HTTPError(404)

        resp = func()

        self.send_response(resp)

    def send_response(self, data):
        if self.gdb is not None:
            self.gdb.commit()

        resp = {
            'Status': 'OK',
            'data': data,
            'message': None
        }

        self.set_status(200)
        self.write(resp)
        self.finish()

    def write_error(self, status_code, **kwargs):
        if self.gdb is not None:
            self.gdb.rollback()

        error_message = 'Unknown Error'
        exc_info = kwargs.get("exc_info", None)
        # (<class 'tornado.web.HTTPError'>, HTTPError(), <traceback object at 0x7f5edf5a0e00>)
        if exc_info is not None:
            error = exc_info[1]

            if isinstance(error, tornado.web.HTTPError):
                error_message = str(error)

            elif isinstance(error, DatabaseError):
                error_message = str(error)

            elif isinstance(error, IntegrityError):
                error_message = str(error)

            elif isinstance(error, KeyError):
                error_message = f"Key {error} is required"

            elif isinstance(error, AttributeError):
                error_message = str(error)

            elif isinstance(error, Exception):
                error_message = str(error)

        resp = {
            'Status': 'Error',
            'data': None,
            'message': error_message
        }


        self.set_status(status_code)
        self.write(resp)
        self.finish()

    def on_finish(self):
        if hasattr(self, 'gdb') and self.gdb is not None:
            self.gdb.close()
            print('Database Connection Closed!!!')

        super().on_finish()
        return

    def get_request_data(self):
        try:
            if hasattr(self.request, 'body') and len(self.request.body) > 0:
                self.Data = tornado.escape.json_decode(self.request.body)

        except Exception:
            traceback.print_exc()
            raise tornado.web.HTTPError(503)

    def get_db_connection(self):
        try:
            engine = create_engine("mysql+mysqlconnector://root:12345@10.8.0.74/App")

            print("Connection Established")
            if not database_exists(engine.url):
                create_database(engine.url)
                print("Database Created")

            print("Database Exists")
            Base.metadata.create_all(engine)
            print("Database Connected")

            Session = sessionmaker(bind=engine)
            self.gdb = Session()
            print('Database Connection Established...')

        except Exception:
            traceback.print_exc()
            raise tornado.web.HTTPError(503)