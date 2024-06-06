# Movie Recommender System

This is a simple movie recommender system built using Bag of Words and Cosine Similarity, and implemented with Streamlit for the frontend interface. The system recommends movies based on a selected movie and provides posters for the recommended movies using the TMDB API.

## Features

- Recommends movies based on cosine similarity.
- Fetches movie posters from the TMDB API.
- Interactive UI built with Streamlit.

## Installation

To run this application, you'll need to have Python installed. Follow the steps below to set up the environment and run the app:

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/movie-recommender-system.git
    cd movie-recommender-system
    ```

2. **Install the required packages**:

    It's recommended to create a virtual environment:

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

    Install the packages:

    ```sh
    pip install -r requirements.txt
    ```

3. **Add TMDB API Key**:

    Replace `'your_api_key_here'` in the `fetch_poster` function with your actual TMDB API key.

## Usage

To run the Streamlit app, use the following command:

```sh
streamlit run app.py
