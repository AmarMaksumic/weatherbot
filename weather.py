import python_weather

from datetime import date, timedelta
from msilib.schema import Error

async def is_loc_valid(loc):
  try:
    w_client = python_weather.Client(format=python_weather.IMPERIAL)
    await w_client.find(loc)
    await w_client.close()
    return True
  except Error:
    return False

async def get_forecast(loc, day):
  if not is_loc_valid:
    return 'none', -1, -1
  
  # declare the client. format defaults to metric system (celcius, km/h, etc.)
  client = python_weather.Client(format=python_weather.IMPERIAL)

  # fetch a weather forecast from a city
  weather = await client.find(loc)

  # returns the current day's forecast temperature (int)
  if (day == 'now'): 
    await client.close()
    return weather.current.sky_text, weather.current.temperature, weather.provider

  # get the weather forecast for a few days
  day_select = str(date.today() + timedelta(days = int(day)))
  for forecast in weather.forecasts:
    if str(forecast.date)[:10] == day_select:
      await client.close()
      print(forecast)
      return forecast.sky_text, forecast.temperature, weather.provider

  # close the wrapper once done
  await client.close()
  return 'none', -1, -1
