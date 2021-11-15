# Install the Python library from https://pypi.org/project/amadeus
from amadeus import Client, ResponseError

amadeus = Client(
    client_id='YOUR_AMADEUS_API_KEY',
    client_secret='YOUR_AMADEUS_API_SECRET'
)

try:
    '''
    Will there be a delay from BRU to FRA? If so how much delay?
    '''
    response = amadeus.travel.predictions.flight_delay.get(originLocationCode='NCE', destinationLocationCode='IST',
                                                           departureDate='2022-08-01', departureTime='18:20:00',
                                                           arrivalDate='2022-08-01', arrivalTime='22:15:00',
                                                           aircraftCode='321', carrierCode='TK',
                                                           flightNumber='1816', duration='PT31H10M')
    print(response.data)
except ResponseError as error:
    raise error
