const url = "https://api.thingspeak.com/channels/3082700/feeds.json?api_key=6EJK1TEE7QKQFOTA";

fetch(url)
  .then(response => response.json())
  .then(data => {
    const feeds = data.feeds;
    const temperature = feeds.map(feed => ({
      time: feed.created_at,
      temp: parseFloat(feed.field1)
    }));
    document.getElementById("output").textContent = JSON.stringify(temperature);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
    document.getElementById("output").textContent = 'Error loading data';
  });