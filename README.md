## Spotify APIs Python Code

This Python code interacts with Spotify APIs, offering functionalities to test and query various public endpoints. Authentication is handled through a conf.json file containing Spotify API credentials.

## Getting Started

1. Create a Spotify Developer Application and get your `CLIENT_ID` and `CLIENT_SECRET`. You can create one [here](https://developer.spotify.com/dashboard/applications).

2. Install Dependencies:
 ```
 pip install -r requirements.txt
 ```

3. Clone this repository to your local machine.

4. Open the `conf.json` file and replace the `CLIENT_ID` and `CLIENT_SECRET` with your own credentials.

5. Start the application:
    ```
    python main_api.py
    ```

## Note

- Keep your Spotify API credentials confidential. Do not share them publicly or expose them in your code repository.
- Refer to the Spotify API documentation for information on available endpoints and query parameters: Spotify API Reference