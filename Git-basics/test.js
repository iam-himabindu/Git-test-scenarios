from http.server import SimpleHTTPRequestHandler, HTTPServer

html_page = """
<!DOCTYPE html>
<html>
<head>
<style>
body { font-family: Arial; background: #f0f0f0; }
button { padding: 10px; }
</style>
</head>
<body>
<h2>Hello from HTML + CSS + JS</h2>
<button onclick="sayHi()">Click me</button>
<script>
function sayHi() { alert("Hello from JavaScript!"); }
</script>
</body>
</html>
"""

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(html_page.encode())

HTTPServer(("localhost", 5000), Handler).serve_forever()

