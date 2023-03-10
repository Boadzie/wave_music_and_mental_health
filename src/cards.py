from h2o_wave import Q, ui

# app layout
async def app_layout(q: Q):
    q.page["meta"] = ui.meta_card(
        box="",
        themes=[
            ui.theme(
                name="cool7",
                primary="#ffffff",
                text="#ffffff",
                card="#111111",
                page="#ffffff",
            )
        ],
        theme="cool7",
        layouts=[
            ui.layout(
                breakpoint="xs",
                zones=[
                    ui.zone("header", align="start", justify="around"),
                    ui.zone(
                        name="zone1", direction=ui.ZoneDirection.COLUMN, size="100%", align="center", justify="center"
                    ),
                    ui.zone(
                        name="zone2", direction=ui.ZoneDirection.COLUMN, size="100%", align="center", justify="center"
                    ),
                    ui.zone("footer"),
                ],
            ),
            ui.layout(
                breakpoint="m",
                zones=[
                    ui.zone("header"),
                    ui.zone(
                        "body",
                        direction=ui.ZoneDirection.COLUMN,
                        align="stretch",
                        justify="between",
                        size="60rem",
                        zones=[
                            ui.zone(
                                "zone1", direction=ui.ZoneDirection.ROW, align="center", justify="around", size="50%"
                            ),
                            ui.zone("separate", direction="column", size="10px"),
                            ui.zone(
                                "zone2", direction=ui.ZoneDirection.ROW, align="center", justify="around", size="50%"
                            ),
                        ],
                    ),
                    ui.zone("depression"),
                    ui.zone("footer"),
                ],
            ),
        ],
    )


async def home(q: Q):
    q.page["header"] = ui.header_card(
        box=ui.box("header", width="100%", height="80px"),
        icon="HealthRefresh",
        color="primary",
        title="Music's effect on Mental Health",
        subtitle="Can music impact mental health? Let's find out",
    )

    q.page["footer"] = ui.footer_card(
        box="footer",
        caption="""[By Daniel Boadzie](https://www.linkedin.com/in/boadzie/) -
        This dataset was obtained from [kaggle](https://www.kaggle.com/code/totoro29/music-and-mental-condition/notebook)
        """,
    )
