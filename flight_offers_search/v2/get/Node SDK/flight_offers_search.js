var Amadeus = require("amadeus");
var amadeus = new Amadeus({
  clientId: 'pI7YjB7jHWDWHxPe0uTzx1Af4bMbsPza',
  clientSecret: 'vp44UpuSeotv1ORT'
});

// Find the cheapest flights from SYD to BKK
amadeus.shopping.flightOffersSearch.get({
  originLocationCode: 'SYD',
  destinationLocationCode: 'BKK',
  departureDate: '2022-08-01',
  adults: '2'
}).then(function (response) {
  console.log(response);
}).catch(function (response) {
  console.error(response);
});