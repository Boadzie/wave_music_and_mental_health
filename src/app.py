from h2o_wave import ui, Q, main, app, data
from cards import app_layout, home
from charts import show_table, streaming_service, fav_age_effect, fav_depression
import pandas as pd
from siuba import *
from siuba.siu import call

# read the data anc cover
music = pd.read_csv("../music_mental_survey_clean.csv")
music = music >> select(~_["Unnamed: 0"])  # remove unwanted column


@app("/")
async def serve(q: Q):
    df = data(
        fields=music.columns.to_list(),
        rows=music.values.tolist(),
        pack=True,
    )
    await home(q)
    await app_layout(q)

    q.page["table"] = ui.form_card(
        box=ui.box("zone1", width="100%", height="100%"),
        title="Music and Mental Condition Dataset",
        items=[await show_table(df=music)],
    )
    q.page["streaming_service"] = ui.frame_card(
        box=ui.box("zone1", width="100%", height="100%"),
        title="Most popular streaming service",
        content=await streaming_service(df=music),
    )
    q.page["separate"] = ui.frame_card(box="separate", title="", content="")
    q.page["fav_depression"] = ui.frame_card(
        box=ui.box("zone2", width="100%", height="100%"),
        title="",
        content=await fav_depression(df=music),
    )
    q.page["fav_age_effect"] = ui.frame_card(
        box=ui.box("zone2", width="100%", height="100%"),
        title="",
        content=await fav_age_effect(df=music),
    )

    await q.page.save()
