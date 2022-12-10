from h2o_wave import Q, ui

# app layout
async def app_layout(q: Q):
    q.page["meta"] = ui.meta_card(
        box="",
        layouts=[
            ui.layout(
                breakpoint="xs",
                zones=[
                    ui.zone("header"),
                    ui.zone(
                        name="zone1", direction=ui.ZoneDirection.COLUMN, size="100%", align="center", justify="center"
                    ),
                    ui.zone("footer"),
                ],
            ),
            ui.layout(
                breakpoint="m",
                zones=[
                    ui.zone("header"),
                    ui.zone(name="zone1", direction=ui.ZoneDirection.ROW, size="50%"),
                    ui.zone(name="zone2", direction=ui.ZoneDirection.ROW, size="50%"),
                    ui.zone("footer"),
                ],
            ),
        ],
    )


async def home(q: Q):
    q.page["header"] = ui.header_card(
        box=ui.box("header", width="100%", height="86px"),
        icon="home",
        icon_color="white",
        title="Music and its effect on Mental Health",
        subtitle="Can music impact mental health? Let's find out",
    )

    q.page["footer"] = ui.footer_card(
        box="footer",
        caption="""[By Daniel Boadzie](https://www.linkedin.com/in/boadzie/) -
        This dataset was obtained from [kaggle](https://www.kaggle.com/code/totoro29/music-and-mental-condition/notebook)
        """,
    )
