# SpeedTest

Want to monitor your network's upload speed, download speed and ping time throughout the day?

NB: please refer to https://pypi.org/project/speedtest-cli/#inconsistency for an explanation of inconsistencies.

## Instructions

### Pre-requisites

- Docker https://docs.docker.com/install/
- Docker Compose https://docs.docker.com/compose/install/

### Running

Clone the repo
```
git clone https://github.com/dhallam/SpeedTest.git
```

Start the containers
```
docker-compose up
```

Point your browser at http://localhost:3000/dashboard/db/speed-test

### Customisation

Customise the environment for the `speedtest` container:

- `POLL_EVERY_SECONDS`: defaults to 300s 
- `SERVERS`: optional comma separated string of server ids (ints) to select from


## Technologies

- Docker (platform for developing, shipping and running applications) https://docs.docker.com/
- Docker Compose (management and linking of docker containers) https://docs.docker.com/compose/
- speedtest-cli (library to run speedtest) https://pypi.org/project/speedtest-cli/
- InfluxDB (time series database) https://docs.influxdata.com/influxdb 
