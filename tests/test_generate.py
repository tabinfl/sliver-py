from pathlib import Path

from ward import test

from sliver import SliverClient
from sliver.pb.clientpb.client_pb2 import ImplantConfig, ImplantProfile, StageProtocol

from .fixtures import data_dir, implant_config, sliver_client, sliverpy_random_name


@test("Client can generate a new implant", tags=["client", "generate", "implant"])
async def _(
    client: SliverClient = sliver_client, config: ImplantConfig = implant_config  # type: ignore
):

    assert await client.generate_implant(config)


@test("Client can regenerate an implant", tags=["client", "generate", "implant"])
async def _(
    client: SliverClient = sliver_client, config: ImplantConfig = implant_config  # type: ignore
):
    assert await client.regenerate_implant(config.Name)


@test("Client can save implant profiles", tags=["client", "generate", "implant"])
async def _(
    client: SliverClient = sliver_client,  # type: ignore
    config: ImplantConfig = implant_config,  # type: ignore
    name: str = sliverpy_random_name,  # type: ignore
):
    implant_profile = ImplantProfile(Name=name, Config=config)
    assert await client.save_implant_profile(implant_profile)


@test("Client can list implant profiles", tags=["client", "generate", "implant"])
async def _(client: SliverClient = sliver_client, name: str = sliverpy_random_name):  # type: ignore
    assert name in [profile.Name for profile in await client.implant_profiles()]


@test("Client can delete implant profiles", tags=["client", "generate", "implant"])
async def _(client: SliverClient = sliver_client, name: str = sliverpy_random_name):  # type: ignore
    await client.delete_implant_profile(name)
    assert name not in [profile.Name for profile in await client.implant_profiles()]


@test("Client can delete implant builds", tags=["client", "generate", "implant"])
async def _(
    client: SliverClient = sliver_client,  # type: ignore
    config: ImplantConfig = implant_config,  # type: ignore
):
    await client.delete_implant_build(config.Name)
    assert config.Name not in [build for build in await client.implant_builds()]


@test("Client can generate an MSF stager", tags=["client", "generate", "implant"])
async def _(client: SliverClient = sliver_client):  # type: ignore
    stager = await client.generate_msf_stager(
        arch="amd64",
        format="raw",
        host="127.0.0.1",
        port=9000,
        os="windows",
        protocol=StageProtocol.TCP,
        badchars=[],
    )
    assert Path(stager.File.Name)


@test("Client can generate Donut shellcode", tags=["client", "generate", "implant"])
async def _(client: SliverClient = sliver_client, data_dir: Path = data_dir):  # type: ignore
    dll_data = Path(data_dir / "test_write.exe").read_bytes()
    assert await client.shellcode(dll_data, "Main")


@test("Client can add website content", tags=["client", "generate", "website"])
async def _(client: SliverClient = sliver_client, data_dir: Path = data_dir):  # type: ignore
    html_content = Path(data_dir / "website.html").read_bytes()
    assert await client.add_website_content(
        "sliverpy-test", "sliverpy", "test/html", html_content
    )


@test("Client can update website content", tags=["client", "generate", "website"])
async def _(client: SliverClient = sliver_client, data_dir: Path = data_dir):  # type: ignore
    html_content = Path(data_dir / "website_update.html").read_bytes()
    assert await client.add_website_content(
        "sliverpy-test", "sliverpy", "test/html", html_content
    )


@test("Client can list websites", tags=["client", "generate", "website"])
async def _(client: SliverClient = sliver_client):  # type: ignore
    assert "sliverpy-test" in [website.Name for website in await client.websites()]


@test("Client can remove website content", tags=["client", "generate", "website"])
async def _(client: SliverClient = sliver_client):  # type: ignore
    assert await client.remove_website_content("sliverpy-test", ["sliverpy"])


@test("Client can remove website", tags=["client", "generate", "website"])
async def _(client: SliverClient = sliver_client):  # type: ignore
    await client.remove_website("sliverpy-test")
    assert "sliverpy-test" not in [website.Name for website in await client.websites()]
