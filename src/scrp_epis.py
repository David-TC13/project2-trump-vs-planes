def episode_season(love_island_episode):
    """Splits the seasons and the episodes by usign fplit (E)"""
    season_episode = [i.getText().split('E') for i in love_island_episode]
    return season_episode

def episodes(season_episode):
    """Create a list with the episodes"""
    lst_episodes=[i[1] for i in season_episode]
    return lst_episodes

def seasons(season_episode):
    """Create a list of the seasons"""
    lst_seasons=[i[0].replace('S','') for i in season_episode]
    return lst_seasons