import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options

define("port", default=8000, help="run on the set port", type=int)


class Mainhandler(tornado.web.RequestHandler):

    def get(self):
        cookie = self.get_secure_cookie("count")
        count = int(cookie) + 1 if cookie else 1

        countString = "1 time" if count == 1 else "%d times" % count

        self.set_secure_cookie("count", str(count))
        self.write(
            '<html><head><title>Cookie Counter</title></head>'
            '<body><h1>You&rsquo;ve viewed this page ' + countString + ' times.</h1>'
            '</body></html>'
        )

if __name__ == '__main__':
    tornado.options.parse_command_line()

    settings = {
        "cookie_secret": "8WiPo9WBig7S0P2DTq8D2wfvJMFzzoOzzd76IAVFOUo="
    }

    application = tornado.web.Application([
        (r'/', Mainhandler)
    ], **settings)

    httpserver = tornado.httpserver.HTTPServer(application)
    httpserver.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
