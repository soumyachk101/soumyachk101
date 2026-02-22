const jokeAPI = 'https://v2.jokeapi.dev/joke/Any';

async function fetchJoke() {
    try {
        const response = await fetch(jokeAPI);
        const data = await response.json();
        if (data.joke) {
            console.log(`Joke: ${data.joke}`);
        } else if (data.setup && data.delivery) {
            console.log(`Setup: ${data.setup}\nDelivery: ${data.delivery}`);
        }
    } catch (error) {
        console.error('Error fetching joke:', error);
    }
}

fetchJoke();