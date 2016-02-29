import goldsberry
import pandas as pd
import numpy as np
from scipy.stats import binned_statistic_2d
import seaborn as sns
from bokeh.plotting import figure
from math import pi


pd.set_option("display.max_columns", 50)
goldsberry.__version__

players_2015 = goldsberry.PlayerList()
players_2015 = pd.DataFrame(players_2015.players())

harden_id = players_2015['PERSON_ID'].ix[players_2015['DISPLAY_LAST_COMMA_FIRST'].str.contains("Harden")]

harden_shots = goldsberry.player.shot_chart(harden_id)
harden_shots = pd.DataFrame(harden_shots.chart())
harden_shots.head()

sns.set_style("white")
sns.set_color_codes()
plt.figure(figsize=(12,11))
plt.scatter(harden_shots.LOC_X, harden_shots.LOC_Y)
plt.show()


right = harden_shots[harden_shots.SHOT_ZONE_AREA == "Right Side(R)"]
plt.figure(figsize=(12,11))
plt.scatter(right.LOC_X, right.LOC_Y)
plt.xlim(-300,300)
plt.ylim(-100,500)
plt.show()

from matplotlib.patches import Circle, Rectangle, Arc

exec(open("./drawcourt.py").read())

plt.figure(figsize=(12,11))
draw_court(outer_lines=True, color="red")
plt.xlim(-300,300)
plt.ylim(-100,500)
plt.show()

plt.figure(figsize=(12,11))
plt.scatter(harden_shots.LOC_X, harden_shots.LOC_Y)
draw_court(outer_lines=True)
# Descending values along the axis from left to right
plt.xlim(300,-300)
plt.show()

plt.figure(figsize=(12,11))
plt.scatter(harden_shots.LOC_X, harden_shots.LOC_Y)
draw_court()
# Adjust plot limits to just fit in half court
plt.xlim(-300,300)
# Descending values along th y axis from bottom to top
# in order to place the hoop by the top of plot
plt.ylim(422.5, -47.5)
# get rid of axis tick labels
# plt.tick_params(labelbottom=False, labelleft=False)
plt.show()

x = harden_id.tolist()[0]

exec(open("./drawcourt.py").read())
