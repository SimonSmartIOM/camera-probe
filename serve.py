"""Serve the camera probe on localhost. Usage: python3 serve.py [port]"""
import http.server
import sys

DEFAULT_PORT = 8799


class ProbeHandler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                      '.webmanifest': 'application/manifest+json'}

    def end_headers(self):
        # Edits to the probe should reach the device without clearing site data, which would also reset the permission.
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PORT
    http.server.ThreadingHTTPServer(('127.0.0.1', port), ProbeHandler).serve_forever()
