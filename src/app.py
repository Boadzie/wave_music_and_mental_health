from h2o_wave import ui, Q, main, app
from cards import app_layout, home


@app("/")
async def serve(q: Q):
    await home(q)
    await app_layout(q)
    await q.page.save()
