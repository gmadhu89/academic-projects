##############################################################
# This code extracts player's data in the steam-200k dataset #
##############################################################

import pandas as pd
import requests


def get_player_country(steam_id):
    # get player information from API
    param = {'key': '949DDA17D1A94CB9D387F2BE0727EB5F',
             'steamids': str(steam_id)}
    r = requests.get(player_url, params=param)
    player = r.json()
    try:
        player_country = player['response']['players'][0]['loccountrycode']
    except KeyError:
        return None
    except IndexError:
        return None
    return player_country


def parse_userid_into_steamid(user_id):
    # Universe is "Public" by default
    univ = '00000001'
    # Steam Account Type is "Individual" by default
    act_type = '0001'
    # Instance of Acccount is usually 1
    act_inst = '00000000000000000001'
    # Convert the account number to 31 bits representation
    act_num = '{:031b}'.format(user_id)
    # Y is "1" by default
    Y = '1'
    # Concatenate to get the final 64-bit representation of the Steam Account
    steam_id_b = univ + act_type + act_inst + act_num + Y
    # Convert Account bit representation into Steam ID
    steam_id = int(steam_id_b, 2)
    return steam_id


if __name__ == '__main__':
    # set required parameters
    player_url = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2'

    # read the steam_200k file
    steam_200k_path = './DB/steam-200k.csv'
    header_list = ["user_id", "game", "action", "time", "type"]
    basic_df = pd.read_csv(steam_200k_path, names=header_list)

    # get all the players in the file
    players = list(set(basic_df['user_id'].tolist()))
    players.sort()

    # get all player information
    players_info = {'user_id': [],
                    'steam_id': [],
                    'country_code': []}
    for idx, player_id in enumerate(players):
        if idx < 1000:
            print(str(idx / len(players) * 100) + "% has done!")
            steam_id = parse_userid_into_steamid(player_id)
            player_country = get_player_country(steam_id)
            players_info['user_id'].append(str(player_id))
            players_info['steam_id'].append(str(steam_id))
            players_info['country_code'].append(player_country)

    df = pd.DataFrame(players_info)

    # write to output file
    output_path = './DB/player_country_1.csv'
    df.to_csv(output_path, index=False)