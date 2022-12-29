from ward import skip, test

from sliver import SliverClient

from .fixtures import constants, sliver_client


@test("Client can start HTTP listener on port 8080", tags=["client", "listeners"])
async def _(client: SliverClient = sliver_client):  # type: ignore
    assert await client.start_http_listener()


@test("Client can start HTTPS listener on port 8443", tags=["client", "listeners"])
async def _(client: SliverClient = sliver_client):  # type: ignore
    assert await client.start_https_listener()


@test("Client can start DNS listener on port 53", tags=["client", "listeners"])
async def _(client: SliverClient = sliver_client):  # type: ignore
    assert await client.start_dns_listener(domains=["sliverpy.local"])


@test("Client can start MTLS listener on port 8888", tags=["client", "listeners"])
async def _(client: SliverClient = sliver_client):  # type: ignore
    assert await client.start_mtls_listener()


@test("Client can start TCP stager listener on port 9000", tags=["client", "listeners"])
async def _(client: SliverClient = sliver_client):  # type: ignore
    assert await client.start_tcp_stager_listener("0.0.0.0", 9000, b"sliver-pytest")


@test(
    "Client can start HTTP stager listener on port 9001", tags=["client", "listeners"]
)
async def _(client: SliverClient = sliver_client):  # type: ignore
    assert await client.start_http_stager_listener("0.0.0.0", 9001, b"sliver-pytest")


@skip("Cert generation not implemented")
@test(
    "Client can start HTTPS stager listener on port 9002", tags=["client", "listeners"]
)
async def _(client: SliverClient = sliver_client):  # type: ignore
    assert await client.start_http_stager_listener("0.0.0.0", 9002, b"sliver-pytest")


@test("Client can generate a WireGuard IP", tags=["client", "listeners"])
async def _(client: SliverClient = sliver_client):  # type: ignore
    assert await client.generate_wg_ip()


@skip("Something is wrong with killing WG listeners on the server")
@test(
    "Client can start WG listener on ports 5353/8889/1338", tags=["client", "listeners"]
)
async def _(client: SliverClient = sliver_client):  # type: ignore
    ip = await client.generate_wg_ip()
    print(ip.IP)
    assert await client.start_wg_listener(ip.IP, 5353, 8889, 1338)


@test("Client can generate a WireGuard client config", tags=["client", "listeners"])
async def _(client: SliverClient = sliver_client):  # type: ignore
    assert await client.generate_wg_client_config()


@test("Client can kill jobs (again) except WireGuard", tags=["client", "listeners"])
async def _(client: SliverClient = sliver_client):  # type: ignore
    jobs = await client.jobs()
    for job in jobs:
        if job.Name != constants.multiplayer_job_name:
            await client.kill_job(job.ID)
    assert len(await client.jobs()) < 2
