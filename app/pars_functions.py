from bs4 import BeautifulSoup as bs
import requests
import re


def vikings_tv_pars():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.149 Safari/537.36'}

    cast_list = []

    main_link = 'https://www.history.com'

    vikings_html = requests.get(f'{main_link}/shows/vikings/cast', headers=header).text
    vikings_soup = bs(vikings_html, 'html.parser')

    vikings_cast_block = vikings_soup.find('div', {'class': 'tile-list tile-boxed'})
    vikings_cast = vikings_cast_block.find_all('li')

    for vik in vikings_cast:

        char_data = {}
        actor_data = {}

        img_link = vik.find('img')['src']
        img = requests.get(img_link).content

        desc_link = vik.find('a')['href']
        vik_html = requests.get(f'{main_link}{desc_link}', headers=header).text
        vik_soup = bs(vik_html, 'html.parser')

        info_block = vik_soup.find('article', {'class': 'main-article'})

        char_name = info_block.find('strong', {'itemprop': 'name'}).getText()
        char_desc = info_block.find('p').getText()

        actor_name = info_block.find_all('p')[2].getText()
        i = 3
        actor_story = None

        while True:
            try:
                new_part = info_block.find_all('p')[i].getText()
                actor_story += new_part
                i += 1

            except:
                break

        # char_data['img'] = img
        char_data['char_name'] = char_name
        char_data['char_desc'] = char_desc
        char_data['type'] = 'is_character'
        char_data['comment'] = f'Was played by {actor_name}'
        char_data['source'] = 'vikings_tv'

        # actor_data['img'] = img
        actor_data['char_name'] = actor_name
        actor_data['char_desc'] = actor_story
        actor_data['type'] = 'is_actor'
        actor_data['comment'] = f'Played {char_name}'
        actor_data['source'] = 'vikings_tv'

        cast_list.append(char_data)
        cast_list.append(actor_data)

    return cast_list


def norsemen_tv_pars_wiki():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.149 Safari/537.36'}

    cast_list = []
    main_link = 'https://en.wikipedia.org'

    norsemen_html = requests.get(f'{main_link}/wiki/Norsemen_(TV_series)', headers=header).text
    norsemen_soup = bs(norsemen_html, 'html.parser')

    norsemen_cast_block = norsemen_soup.find_all('ul')[4]
    norsemen_cast = norsemen_cast_block.find_all('li')

    for nor in norsemen_cast:

        char_data = {}
        actor_data = {}
        desc_str = nor.getText().split('.')

        actor_name = desc_str[0].split(' as')[0]
        char_name = re.sub(r"^\s+", "", desc_str[0].split(' as')[1].split(',')[0])

        char_desc = ''

        for i in range(1, len(nor.getText().split('.'))):
            if nor.getText().split('.')[i] != None:
                char_desc = char_desc + nor.getText().split('.')[i]

        char_desc = re.sub(r"^\s+", "", char_desc)
        desc_link = nor.find('a')['href']

        nor_html = requests.get(f'{main_link}{desc_link}', headers=header).text
        nor_soup = bs(nor_html, 'html.parser')

        try:
            img_link = nor_soup.find('a', {'class': 'image'})['href']
            img = requests.get(img_link).content

        except:
            img = ''

        actor_story = ''

        for i in range(len(nor_soup.find_all('p'))):
            try:
                new_part = nor_soup.find_all('p')[i].getText()
                actor_story += new_part
                i += 1

            except:
                pass

        # char_data['img'] = img
        char_data['char_name'] = char_name
        char_data['char_desc'] = char_desc
        char_data['type'] = 'is_character'
        char_data['comment'] = f'Was played by {actor_name}'
        char_data['source'] = 'norsemen_tv'

        # actor_data['img'] = img
        actor_data['char_name'] = actor_name
        actor_data['char_desc'] = actor_story
        actor_data['type'] = 'is_actor'
        actor_data['comment'] = f'Played {char_name}'
        actor_data['source'] = 'norsemen_tv'

        cast_list.append(char_data)
        cast_list.append(actor_data)
    return cast_list


def norsemen_nfl_wiki():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.149 Safari/537.36'}

    team_list = []
    main_link = 'https://www.vikings.com'

    nfl_html = requests.get(f'{main_link}/team/players-roster/', headers=header).text
    nfl_soup = bs(nfl_html, 'html.parser')

    nfl_team_block = nfl_soup.find('table', {'summary': 'Roster'})
    nfl_team = nfl_team_block.find_all('a')

    check = []

    for player in nfl_team:

        team_data = {}

        link = player['href']

        player_html = requests.get(f'{main_link}{link}', headers=header).text
        player_soup = bs(player_html, 'html.parser')

        try:
            img_link = player.find('img', {'class': 'img-responsive'})['src'].split('/')[-1]
            img = requests.get(
                f'https://static.clubs.nfl.com/image/private/t_thumb_squared/f_auto/vikings/{img_link}').content

        except:
            img = ''

        player_name = player_soup.find('h1').getText()
        player_story = player_soup.find('div', {'class': 'nfl-c-body-part nfl-c-body-part--text'}).getText()

        if player_name in check:
            continue

        # team_data['img'] = img
        team_data['char_name'] = player_name
        team_data['char_desc'] = player_story
        team_data['type'] = 'is_player'
        team_data['comment'] = ''
        team_data['source'] = 'norsemen_nfl'

        team_list.append(team_data)
        check.append(player_name)

    return team_list
