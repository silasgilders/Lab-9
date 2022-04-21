import requests

def get_pokemon_info(poke_id):
    """
    
    Irrelevant to this script 
    
    
    """
    print("Getting Pokemon Information...", end= " ")
    poke_id = poke_id.strip().lower()
    if poke_id in (None, ''):
      return
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(poke_id))

    if response.status_code == 200:
      print('Success')
      return response.json()
    else:
      print('Failed, Response code:', response.status_code)
      return

def get_poke_list(limit=1500, offset=0):

  """Gets our information on Pokemon, as it always does in these Pokemon Script 
  
    :param offset: Determines where in the Pokedex we start from
    :param limit: Determines how many pokemon will be printed
    """

    
  print("Getting Pokemon Information...", end= " ")


  URL = 'https://pokeapi.co/api/v2/pokemon/'
  
  params = {
    'offset': offset,
    'limit': limit
  }
  response = requests.get(URL, params=params)


  if response.status_code == 200:
      print('Success')
      poke_dict = response.json()

      return [p['name'] for p in poke_dict['results']]
  else:
      print('Failed, Response code:', response.status_code)
      return

def get_poke_image(name):
  """Gets you the image, notably the official artwork of each Pokemon on the API
    :param name: The name of a pokemon, which is then applied to the get_pokemon_info function"""
  poke_dict = get_pokemon_info(name)
  if poke_dict:
    poke_url = poke_dict['sprites']['other']['official-artwork']['front_default']
    return poke_url