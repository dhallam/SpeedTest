FROM grafana/grafana

# Passwordless readonly
ENV GF_AUTH_ANONYMOUS_ENABLED true

ENV GF_DASHBOARDS_JSON_ENABLED true
ENV GF_LOG_MODE console

# Set the paths that we add in in a moment
ENV GF_DASHBOARDS_JSON_PATH /dashboards
ENV GF_PATHS_PROVISIONING /provisioning

ADD provisioning /provisioning
ADD dashboards /dashboards

