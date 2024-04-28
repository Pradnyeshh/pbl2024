import requests

def get_nasa_data(topic):
    api_key = '54VeyOemgPNw9PyQPc7wDepYR8tvAQ2MHdzoxFYO'
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&concept_tags=True&q={topic}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('explanation', 'No data available')
    else:
        return f"Failed to fetch data from NASA API for '{topic}'."
