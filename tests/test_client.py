from ward import test

from sliver import SliverClient

from .fixtures import TestConstants, constants, sliver_client


@test("Client can get version", tags=["client", "server_info", "connect"])
async def _(client: SliverClient = sliver_client):  # type: ignore
    assert await client.version()


@test("Client can list operators", tags=["client", "server_info"])
async def _(client: SliverClient = sliver_client):  # type: ignore
    assert await client.operators()


@test("Client can list jobs", tags=["client", "server_info"])
async def _(client: SliverClient = sliver_client):  # type: ignore
    assert await client.jobs()


@test("Client can get job by ID", tags=["client", "server_info"])
async def _(client: SliverClient = sliver_client):  # type: ignore
    jobs = await client.jobs()
    assert await client.job_by_id(jobs[0].ID)


@test("Client can get job by port", tags=["client", "server_info"])
async def _(client: SliverClient = sliver_client, const: TestConstants = constants):  # type: ignore
    assert await client.job_by_port(const.multiplayer_job_port)
