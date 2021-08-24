#!/usr/bin/env python

import json
import urllib
import urllib.parse
import urllib.request
import os


def main():
    city = "Reynosa"
    api_key = "241f1cb2fc6c2a36e0fb1718389f1fbe"

    try:
        data = urllib.parse.urlencode({'q': city, 'appid': api_key, 'units': 'metric'})
        weather = json.loads(urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?' + data)
            .read())
        desc = weather['weather'][0]['description'].upper()
        temp = int(float(weather['main']['temp']))
        return ' {}°C {}'.format(temp, 'at Reynosa, Tamaulipas')
        #return '{}°F'.format(temp)
    except:
        return ''


if __name__ == "__main__":
	print(main())