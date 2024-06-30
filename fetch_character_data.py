import requests

def update_character_sheet(character_id):
    url = f"https://character-service.dndbeyond.com/character/v5/character/{character_id}"
    try:
        # Make the GET request
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        character_data = response.json()

        if character_data['success']:  # Check if the API call was successful
            # Parse the data
            character = character_data['data']
            character_sheet = {
                'id': character['id'],
                'user_id': character['userId'],
                'username': character['username'],
                'is_assigned_to_player': character['isAssignedToPlayer'],
                'readonly_url': character['readonlyUrl'],
                'avatar_url': character['decorations']['avatarUrl'],
                'frame_avatar_url': character['decorations']['frameAvatarUrl'],
                'small_backdrop_avatar_url': character['decorations']['smallBackdropAvatarUrl'],
                'large_backdrop_avatar_url': character['decorations']['largeBackdropAvatarUrl'],
                'name': character['name'],
                'social_name': character['socialName'],
                'gender': character['gender'],
                'faith': character['faith'],
                'age': character['age'],
                'hair': character['hair'],
                'eyes': character['eyes'],
                'skin': character['skin'],
                'height': character['height'],
                'weight': character['weight'],
                'inspiration': character['inspiration'],
                'base_hit_points': character['baseHitPoints'],
                'stats': {stat['id']: stat['value'] for stat in character['stats']},
                'background_name': character['background']['definition']['name'],
                'background_description': character['background']['definition']['description'],
                'race_full_name': character['race']['fullName'],
                'race_description': character['race']['description'],
                'inventory': [{
                    'item_id': item['id'],
                    'item_name': item['definition']['name'],
                    'item_type': item['definition']['type'],
                    'equipped': item['equipped']
                } for item in character['inventory']],
                'notes_allies': character['notes']['allies'],
                'notes_personal_possessions': character['notes']['personalPossessions'],
                'personality_traits': character['traits']['personalityTraits'],
                'ideals': character['traits']['ideals'],
                'bonds': character['traits']['bonds'],
                'flaws': character['traits']['flaws'],
                'use_homebrew_content': character['preferences']['useHomebrewContent']
            }

            return character_sheet
        else:
            raise Exception(f"Failed to update character sheet: {character_data['message']}")
    except requests.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")

def print_character_sheet(character_sheet):
    for key, value in character_sheet.items():
        if isinstance(value, dict):
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value}")
        elif isinstance(value, list):
            print(f"{key}:")
            for item in value:
                if isinstance(item, dict):
                    print("  -")
                    for item_key, item_value in item.items():
                        print(f"    {item_key}: {item_value}")
                else:
                    print(f"  - {item}")
        else:
            print(f"{key}: {value}")

if __name__ == "__main__":
    character_id = input("Please enter the character ID: ")
    try:
        character_sheet = update_character_sheet(character_id)
        print("Character sheet updated successfully:")
        print_character_sheet(character_sheet)
    except Exception as e:
        print(str(e))
