function updateMap() {
    fetch("/india.json").then(response => response.json()).then(rsp => {
        console.log(rsp.data)
        rsp.data.forEach(element => {
            latitude = element.latitude;
            longitude = element.longitude;

            lastUpdate = element.lastUpdated;

            name = element.name;

            deaths = element.dead;
            recovered = element.recovered;
            cases = element.infected;

            if (cases > 175) {
                color = "rgb(252, 0,0)"
            }

            else if(cases >= 50 && cases <= 175) {
                color = `rgb(247, 239, 0)`;
            }

            else {
                color = `rgb(45, 247, 0)`;
            }

            // create the popup
            var dataDisplay=[name,
                '\nCases:', cases,
                '\nRecovered:', recovered,
                '\nDeaths:', deaths,
                'Last Updated:',lastUpdate]

            var popup = new mapboxgl.Popup({ offset: 25 }).setText(
                [dataDisplay]
            );

            // create DOM element for the marker
            var el = document.createElement('div');
            el.id = 'marker';

            // create the marker
            new mapboxgl.Marker({
                color: color
            })
                .setLngLat([longitude, latitude])
                .setPopup(popup) // sets a popup on this marker
                .addTo(map);

        });
    })

}

updateMap();