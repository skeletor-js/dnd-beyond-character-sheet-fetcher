# D&D Beyond Character Sheet Fetcher

A Python script that fetches and prints the detailed character sheet from D&D Beyond using the character ID. Ideal for manually updating custom GPTs with real-time data from D&D Beyond.

## Features

- Fetches character data from D&D Beyond using a character ID
- Parses and prints detailed character sheet information
- User-friendly terminal prompt for entering the character ID

## Requirements

- Python 3.x
- `requests` library

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/dnd-beyond-character-sheet-fetcher.git
    cd dnd-beyond-character-sheet-fetcher
    ```

2. **Install the required library:**

    ```sh
    pip install requests
    ```

## Usage

1. **Run the script:**

    ```sh
    python3 fetch_character_data.py
    ```

2. **Enter the character ID when prompted:**

    ```plaintext
    Please enter the character ID: 127373542
    ```

3. **The script will print the fully parsed character sheet to the terminal:**

    ```plaintext
    Character sheet updated successfully:
    name: Ezra Trickweaver
    race_full_name: Lightfoot Halfling
    ...
    ```

## Example Output

```plaintext
Please enter the character ID: 127373542
Character sheet updated successfully:
id: 127373542
user_id: 123456
username: EzraTrick
is_assigned_to_player: True
readonly_url: https://www.dndbeyond.com/profile/EzraTrick/characters/127373542
avatar_url: https://www.dndbeyond.com/avatars/123456.png
frame_avatar_url: https://www.dndbeyond.com/frames/123456.png
small_backdrop_avatar_url: https://www.dndbeyond.com/backdrops/small/123456.png
large_backdrop_avatar_url: https://www.dndbeyond.com/backdrops/large/123456.png
name: Ezra Trickweaver
social_name: Ezra
gender: Male
faith: None
age: 32
hair: Brown
eyes: Green
skin: Fair
height: 3'2"
weight: 40 lbs
inspiration: 0
base_hit_points: 8
stats:
  1: 10
  2: 14
  3: 10
  4: 12
  5: 10
  6: 10
background_name: Criminal/Spy
background_description: You have a history of operating outside the law...
race_full_name: Lightfoot Halfling
race_description: Halflings are a small race known for their agility and luck...
...
