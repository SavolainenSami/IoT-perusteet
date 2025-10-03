google.charts.load('current', { 'packages': ['corechart'] });
google.charts.setOnLoadCallback(fetchData);

function fetchData() {
  const url = " https://api.thingspeak.com/channels/3099516/feeds.json?api_key=86RM6EXXCAPUD7KG";

  fetch(url)
    .then(response => response.json())
    .then(data => {
      const feeds = data.feeds;

      const chartData = [['Aika', 'Lämpötila (°C)', 'Ilmankosteus (%)']];
      feeds.forEach(feed => {
        if (feed.field1 && feed.field2) {
          chartData.push([
            new Date(feed.created_at),
            parseFloat(feed.field1),
            parseFloat(feed.field2)
          ]);
        }
      });

      drawChart(chartData);
    })
    .catch(error => {
      console.error('Error fetching data:', error);
      document.getElementById("curve_chart").textContent = 'Virhe datan haussa';
    });
}

function drawChart(chartData) {
  var data = google.visualization.arrayToDataTable(chartData);

  var options = {
    title: 'Lämpötila ja Ilmankosteus',
    curveType: 'function',
    legend: { position: 'bottom' },
    hAxis: {
      title: 'Aika',
      format: 'HH:mm:ss'
    },
    vAxis: {
      title: 'Arvo'
    }
  };

  var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
  chart.draw(data, options);
}
