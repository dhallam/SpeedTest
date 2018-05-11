import json
import os
import time
from time import sleep, time

import requests
import speedtest


def main():
    database_host = os.getenv('DATABASE_HOST', 'influxdb')
    database = os.getenv('DATABASE', 'speedtest')
    sleep_seconds = int(os.getenv('POLL_EVERY_SECONDS', '5'))
    _servers = os.getenv('SERVERS', '')
    servers = _servers.split(',') if _servers else []

    speed_template = 'speed_bps,direction={direction},server_id={server_id} value={bps} {timestamp}'
    ping_template = 'ping_ms,server_id={server_id} value={ping} {timestamp}'

    url = 'http://{database_host}:8086/write?db={database}'.format(database_host=database_host, database=database)

    while True:
        try:
            s = speedtest.Speedtest()
            s.get_servers(servers)
            s.get_best_server()
            s.download()
            s.upload(pre_allocate=False)

            results_dict = s.results.dict()

            print(json.dumps(results_dict, indent=2))

            # Take current time rather than parsing the timestamp out of the dict
            timestamp = int(round(time() * 1000000000))

            upload_data = speed_template.format(direction='upload',
                                                server_id=results_dict['server']['id'],
                                                bps=results_dict['upload'],
                                                timestamp=timestamp)

            download_data = speed_template.format(direction='download',
                                                  server_id=results_dict['server']['id'],
                                                  bps=results_dict['download'],
                                                  timestamp=timestamp)

            ping_data = ping_template.format(server_id=results_dict['server']['id'],
                                             ping=results_dict['ping'],
                                             timestamp=timestamp)

            requests.post(url=url, data=upload_data)
            requests.post(url=url, data=download_data)
            requests.post(url=url, data=ping_data)
        except Exception as e:
            print(e)

        sleep(sleep_seconds)


if __name__ == '__main__':
    main()
