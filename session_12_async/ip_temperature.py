import asyncio
import json

import aiohttp


async def get_ip_data(session, ip_address):
    print(f'Getting data on IP: {ip_address}')
    response = await session.get(f'http://ip-api.com/json/{ip_address}')
    print(f'Data retrieved for IP: {ip_address}')
    return await response.json()


async def get_temperature_from_coordinates(session, lat, lon):
    print(f'Getting weather data for lat: {lat}, lon: {lon}')
    response = await session.get(
        f'http://www.7timer.info/bin/api.pl?lon={lon}&lat={lat}&product=civil&output=json')
    print(f'Retrieved weather data for lat: {lat}, lon: {lon}')
    text = await response.text()
    data = json.loads(text)
    return data['dataseries'][0]['temp2m']


async def print_info_for_ip(session, ip_address):
    data = await get_ip_data(session, ip_address)
    temperature = await get_temperature_from_coordinates(session, data['lat'], data['lon'])

    print(
        f'\n***** '
        f'IP {ip_address} is in {data["city"]}, {data["country"]} and it is {temperature}C '
        f'*****\n')


async def main():
    async with aiohttp.ClientSession() as session:
        # # Run one after the other - synchronously
        # await asyncio.gather(print_info_for_ip(session, '24.48.0.1'))
        # await asyncio.gather(print_info_for_ip(session, '46.101.5.230'))
        # await asyncio.gather(print_info_for_ip(session, '203.94.32.154'))

        # Run asynchronously
        await asyncio.gather(
            print_info_for_ip(session, '24.48.0.1'),
            print_info_for_ip(session, '46.101.5.230'),
            print_info_for_ip(session, '203.94.32.154')
        )

asyncio.run(main())
