from http.server import HTTPServer, BaseHTTPRequestHandler
import mimetypes
import os
import time


class CS2610Assn2(BaseHTTPRequestHandler):
    def dataHelper(self, requestHandler, type_location, fileName, code):
        header = f"Server: Carter's Server\nDate: {time.strftime('%c')}\nConnection: close\nCache-Control: max-age=10\n"
        if code == "200 OK": # regular request
            if os.path.isfile(self.path[1:]):
                f = open(fileName, "rb")
                data = f.read()
                f.close()
            else: # debug page
                data = fileName
            header += f"Content-type: {type_location}\n"
            header += f"Content-length: {len(data)}\n"
        elif code != "301 Moved Permanently": # error
            data = fileName
            header += f"Content-type: {type_location}\n"
            header += f"Content-length: {len(data)}\n"
        else: # redirect
            header += f"Location: {type_location}\n"
        header += "\n"
        requestHandler.wfile.write(bytes(f"HTTP/1.1 {code}\n" + header, encoding="utf-8"))
        if code != "301 Moved Permanently":
            requestHandler.wfile.write(data)

    def do_GET(self):
        # pages/images/icons
        if os.path.isfile(self.path[1:]):
            self.dataHelper(self, mimetypes.guess_type(self.path[1:]), self.path[1:], "200 OK")
        # 301 Redirects
        elif self.path in ["/", "/index", "/about", "/techtips+css", "/tips", "/techtips-css", "/help"] or self.path[0:4] == "/bio":
            if self.path in ["/", "/index"]:
                location = "index.html"
            elif self.path == "/about" or self.path[0:4] == "/bio":
                location = "about.html"
            elif self.path in ["/techtips+css", "/tips"]:
                location = "techtips+css.html"
            elif self.path in ["/techtips-css", "/help"]:
                location = "techtips-css.html"
            self.dataHelper(self, location,  "", "301 Moved Permanently")
        # errors
        elif self.path == "/debugging": # debug page
            # create page
            page = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/><title>Debug</title></head><body>
                <h1>Debugging</h1><p style="white-space: pre-line;">"""
            page += "Server Version: " + self.server_version + "\n" + "Date & Time: " + time.strftime('%c') + "\n"
            page += "Client IP & port: " + str(self.client_address[0]) + ":" + str(self.client_address[1]) + "\n"
            page += "Requested Path: " + self.path + "\n"
            page += "HTTP Requested Type: " + self.requestline + "\n"
            page += "HTTP Version of Requested: " + self.request_version + "\n"
            page += "Ordered list of HTTP request headers: "
            for i in self.headers:
                page += str(i) + "; "
            page += """</p>\n</body>\n</html>"""
            data = bytes(page, encoding="utf-8")
            self.dataHelper(self, "text/html", data, "200 OK")
        elif self.path == "/teapot": # ERROR 418
            page = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>418 teapot</title></head><body>
                <h1>Error 418, I'm a teapot</h1><p>This page is short and stout.</p><a href="/">Go to main page</a></body></html>"""
            data = bytes(page, encoding="utf-8")
            self.dataHelper(self, "text/html", data, "418 I'm a teapot")
        elif self.path == "/forbidden": # ERROR 403
            page = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>403 Forbidden</title></head><body>
                <h1>Error 403, Forbidden</h1><p>This is a stern warning that will make even the most determined hacker think twice about their chances.</p>
                <p>A complaint has been filed to the FBI.</p><a href="/">Go to main page</a></body></html>"""
            data = bytes(page, encoding="utf-8")
            self.dataHelper(self, "text/html", data, "403 Forbidden")
        else: # ERROR 404
            page = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>404 Error</title></head>
                <body><h1>Error 404, Page not found</h1><p>The requested page was not found</p><a href="/">Go to main page</a></body></html>"""
            data = bytes(page, encoding="utf-8")
            self.dataHelper(self, "text/html", data, "404 Page Not Found")


if __name__ == '__main__':
    server_address = ('localhost', 8000)
    print(f"Serving from http://{server_address[0]}:{server_address[1]}")
    print("Press Ctrl-C to quit\n")
    try:
        HTTPServer(server_address, CS2610Assn2).serve_forever()
    except KeyboardInterrupt:
        print(" Exiting")
        exit(0)