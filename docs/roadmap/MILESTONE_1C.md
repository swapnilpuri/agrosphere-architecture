# Milestone 1C — local integration

Implemented in independent Infrastructure 0.2.0, Gateway 0.2.0, Estate 0.2.1 and Spatial 0.2.1 repositories. Architecture release 0.4.0 records ADRs 0010/0011; Contracts 0.3.1 documents compatibility with unchanged 0.3.0 schemas.

The local apps profile integrates real Keycloak, RabbitMQ, isolated service databases/PostGIS, gateway routes/JWT/CORS/limits, health dependencies and Collector/Jaeger tracing. Automated shared-platform acceptance verifies canonical Estate/Spatial integration, trusted role/estate scope, actual API/event contracts, database isolation, duplicate event handling and service/broker outage recovery. Infrastructure README provides run commands and private environment initialization. See infrastructure docs/MILESTONE_1C_REPORT.md for actual results and limitations.

Client implementation, authoritative division lifecycle, production deployment/identity/TLS, retained observability and performance/backup SLAs remain subsequent work. No remote publication or cloud resources were created.

The complete requested two-division/ten-block GeoJSON workflow uses real PKCE development users, asserts direct backend authorization and traces durable outbox/Rabbit publication/consumption. No developer-data or persistent-volume resets are automated.
