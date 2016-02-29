import goldsberry
import pandas as pd
import urllib


gameids = goldsberry.GameIDs()

print("game ids: {}".format(gameids))
print(gameids.game_list())

def get_player_img(player_id):
    """Returns the image of the player from stats.nba.com

    Parameters
    ----------
    player_id: int
        The player ID used to find the image.
    """
    url = "http://stats.nba.com/media/players/230x185/"+str(player_id)+".png"
    img_file = str(player_id) + ".png"
    # img = plt.imread(urllib.urlretrieve(url, img_file)[0])
    # return plt.imshow(img)
    print ("img file: {}".format(url))
