from ward import skip, test

from sliver import SliverClient

from .fixtures import TestConstants, constants, sliver_client


@test(
    "Client can start HTTP listener on specified port",
    tags=["client", "listeners"],
)
async def _(client: SliverClient = sliver_client, const: TestConstants = constants):  # type: ignore
    assert await client.start_http_listener(port=const.http_listen_port)


@test(
    "Client can start HTTPS listener on specified port",
    tags=["client", "listeners"],
)
async def _(client: SliverClient = sliver_client, const: TestConstants = constants):  # type: ignore
    assert await client.start_https_listener(port=const.https_listen_port)


@test("Client can start DNS listener on specified port", tags=["client", "listeners"])
async def _(client: SliverClient = sliver_client, const: TestConstants = constants):  # type: ignore
    assert await client.start_dns_listener(
        port=const.dns_listen_port, domains=[const.dns_domain]
    )


@test(
    "Client can start MTLS listener on specified port",
    tags=["client", "listeners"],
)
async def _(client: SliverClient = sliver_client, const: TestConstants = constants):  # type: ignore
    assert await client.start_mtls_listener(port=const.mtls_listen_port)


@test(
    "Client can start TCP stager listener on specified port",
    tags=["client", "listeners"],
)
async def _(client: SliverClient = sliver_client, const: TestConstants = constants):  # type: ignore
    assert await client.start_tcp_stager_listener(
        const.listen_addr, const.stager_listen_port, b"sliver-pytest"
    )


@test(
    "Client can start HTTP stager listener on specified ports",
    tags=["client", "listeners"],
)
async def _(client: SliverClient = sliver_client, const: TestConstants = constants):  # type: ignore
    assert await client.start_http_stager_listener(
        const.listen_addr, const.stager_listen_port + 1, b"sliver-pytest"
    )


@skip("Cert generation not implemented")
@test(
    "Client can start HTTPS stager listener on specified ports",
    tags=["client", "listeners"],
)
async def _(client: SliverClient = sliver_client, const: TestConstants = constants):  # type: ignore
    assert await client.start_http_stager_listener(
        const.listen_addr, const.stager_listen_port + 2, b"sliver-pytest"
    )


@test("Client can generate a WireGuard IP", tags=["client", "listeners"])
async def _(client: SliverClient = sliver_client):  # type: ignore
    assert await client.generate_wg_ip()


@skip("Something is wrong with killing WG listeners on the server")
@test("Client can start WG listener on specified ports", tags=["client", "listeners"])
async def _(client: SliverClient = sliver_client, const: TestConstants = constants):  # type: ignore
    ip = await client.generate_wg_ip()
    print(ip.IP)
    assert await client.start_wg_listener(
        ip.IP,
        const.wg_listen_ports[0],
        const.wg_listen_ports[1],
        const.wg_listen_ports[2],
    )


@test("Client can generate a WireGuard client config", tags=["client", "listeners"])
async def _(client: SliverClient = sliver_client):  # type: ignore
    assert await client.generate_wg_client_config()


@test("Client can kill jobs except WireGuard", tags=["client", "listeners"])
async def _(client: SliverClient = sliver_client, const: TestConstants = constants):  # type: ignore
    jobs = await client.jobs()
    for job in jobs:
        if job.Name != const.multiplayer_job_name:
            await client.kill_job(job.ID)
    assert len(await client.jobs()) < 2
