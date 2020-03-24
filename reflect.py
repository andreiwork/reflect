#!/usr/bin/env python -u
# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
# Written by Nathan Hamiel (2010)

from http.server import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser
import json
    
class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        request_path = self.path

        print("\n----- Request Start ----->\n")
        print("Request path:", request_path)
        for (k,v) in request_headers.items():
            print(f"\t{k}: {v}")
        print("<----- Request End -----\n")

        self.send_response(200)
        self.end_headers()

    def do_POST(self):

        request_path = self.path

        print("\n----- Request Start ----->\n")
        print("Request path:", request_path)

        request_headers = self.headers
        content_length = request_headers.get('Content-Length')
        length = int(content_length) if content_length else 0

        print("Content Length:", length)
        print("Request headers:")
        for (k,v) in request_headers.items():
            print(f"\t{k}: {v}")

        print("\n----- Request Body ----->\n")
        try:
            body = b""
            for i in range(length):
                body += self.rfile.read(1)

            print(
                json.dumps(
                        json.loads(
                            # self.rfile.read(length)
                            body
                        ),
                        indent=4
                )
            )
        except Exception as e:
            print(self.rfile.read(10))
            print(e)
        print("\n----- Request Body End ----->\n")
        print("<----- Request End -----\n")

        self.send_response(200)
        self.end_headers()

    do_PUT = do_POST
    do_PATCH = do_POST
    do_DELETE = do_GET

def main():
    port = 8080
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Creates an http-server that will echo out any GET or POST parameters\n"
                    "Run:\n\n"
                    "   reflect")
    (options, args) = parser.parse_args()

    main()
