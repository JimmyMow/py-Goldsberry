def get_player_img(player_id):
    """Returns the image of the player from stats.nba.com

    Parameters
    ----------
    player_id: int
        The player ID used to find the image.
    """
    url = "http://stats.nba.com/media/players/230x185/"+str(player_id)+".png"
    img_file = str(player_id) + ".png"
    img = plt.imread(urllib.request.urlretrieve(url, img_file)[0])
    plt.imshow(img)
    return plt.imshow(img)
