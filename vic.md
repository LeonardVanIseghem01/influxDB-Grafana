# VIC

## netwerk

1. verbinden met kabel

2. ip in range 10.13.254.0 /16

3. default gateway 10.10.0.1

4. dns 8.8.8.8 of 1.1.1.1

5. interface resetten

## vcenter

1. ip in browser zetten

2. [vcenter](10.13.0.50)

3. account en wachtwoord in teams

## nieuwe vm maken

1. onder de 10.13.0.4

2. create new

3. sandbox

4. 10.13.0.4

5. gebruik thin provisioning

6. powervault

7. alma linux

8. datastore iso file

### alma

root leonard321

vi : esc + : + w + q

1. nmcli con mod ens33 ipv4.addresses 192.168.2.20/24

2. nmcli con mod ens33 ipv4.gateway 192.168.2.1

3. nmcli con mod ens33 ipv4.dns “8.8.8.8”

4. nmcli con mod ens33 ipv4.method manual

5. nmcli connection reload

https://github.com/LeonardVanIseghem01/influxDB-Grafana

docker compose up -d

docker compose stop


