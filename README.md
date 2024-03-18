# Beat-Bounty

Beat-Bounty is a Python script that allows users to enter the name of their desired artist, searches for the artist's top 10 songs using the Spotify API, and downloads them using Pytube.

## Features

- Retrieve top 10 songs of any artist from Spotify.
- Download songs from YouTube using Pytube.

## Requirements

- Python 3.x
- Spotify Developer Account
- Pytube

## Installation

1. Clone this repository:
```
git clone https://github.com/sunnyallana/beat-bounty.git
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Set up Spotify API:
   - Create a Spotify Developer Account and create a new application.
   - Obtain client ID and client secret.
   - Set environment variables for `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET`.

## Usage

1. Run the script:
```
python beat_bounty.py
```

2. Enter the name of the desired artist when prompted.

3. The script will search for the artist's top 10 songs on Spotify and download them from YouTube.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Spotify API](https://developer.spotify.com/documentation/web-api/)
- [Pytube](https://github.com/pytube/pytube)
