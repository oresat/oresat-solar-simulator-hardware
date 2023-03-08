import os
import sys
import tornado.ioloop
from tornado.options import define, options, parse_command_line
import tornado.web

import socketio

define("port", default=8080, help="run on the given port", type=int)
define("debug", default=True, help="run in debug mode")

msg1 ="ON"
msg2 ="OFF"

sio = socketio.AsyncServer(async_mode='tornado')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("latency.html")


@sio.event
async def ping_from_client(sid):
    await sio.emit('pong_from_server', room=sid)
    #print ('pong from server')
    #print (sid)

@sio.event
def command(sid, data):
    print('message',data);

@sio.event
def disconnect(sid):
        print('disconnect ', sid)


def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/socket.io/", socketio.get_tornado_handler(sio)),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=options.debug,
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    print(f"Arg counts: {len(sys.argv)}")
    mes = sys.argv
    print(f"Arg is: {mes}")
    main()
