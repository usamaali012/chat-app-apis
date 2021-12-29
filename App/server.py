import tornado
from tornado.web import Application
from api_handler import MainApiHandler


class AppServer(Application):
    def __init__(self):
        handlers = self.GetHandlers()
        settings = {
            "autoreload": True
        }
        Application.__init__(self, handlers, **settings)

        return

    def GetHandlers(self):
        handlers = [
            ("/api/(.*)/(.*)", MainApiHandler)
        ]

        return handlers

    def StartServer(self):
        self.listen(4001)
        print("Web Api Server is ready @ 4001")
        tornado.ioloop.IOLoop.current().start()