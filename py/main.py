import tornado.ioloop
import tornado.web
import time
from Rotation import Rotation



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class CommandHandler(tornado.web.RequestHandler):
    def get(self):
        status = self.get_argument("flag")
        print(status)
        if status == "false":
            rot = Rotation(19, 0, 0)
            rot.setup()
            rot.specifyRotation(0)
            rot.cleanup()
        else:
            rot = Rotation(19, 170, 180)
            rot.setup()
            rot.specifyRotation(175)
            rot.cleanup()        

def make_app():
    return tornado.web.Application(
        [(r"/", MainHandler),
         (r"/ctrl", CommandHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(5601)
    tornado.ioloop.IOLoop.current().start()
