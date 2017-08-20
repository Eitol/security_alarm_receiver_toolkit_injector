from aiohttp import web
from events_handlers import sio, serial_setup

app = web.Application()
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    return web.Response(text="RUNNING", content_type='text/html')

if __name__ == '__main__':
    serial_setup()
    app.router.add_get('/', index)
    web.run_app(app, port=8000)
