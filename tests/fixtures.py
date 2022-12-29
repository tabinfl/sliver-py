from pathlib import Path

from ward import fixture

from sliver import SliverClient, SliverClientConfig
from sliver.pb.clientpb.client_pb2 import ImplantC2, ImplantConfig, OutputFormat


class TestConstants:
    def __init__(self):
        self.multiplayer_job_name = "grpc"
        self.multiplayer_job_port = 31337
        self.listen_addr = "0.0.0.0"
        self.http_listen_port = 8080
        self.https_listen_port = 8443
        self.dns_listen_port = 5300
        self.dns_domain = "sliverpy.local"
        self.mtls_listen_port = 8888
        self.stager_listen_port = (
            9000  # will be incremented by 1 for each stager listener test
        )
        self.wg_listen_ports = [5553, 8889, 1338]


@fixture(scope="global")
def constants() -> TestConstants:
    return TestConstants()


@fixture(scope="global")
async def sliver_client() -> SliverClient:
    CONFIG_PATH = Path("~/.sliver-client/configs/sliverpy.cfg").expanduser()
    config = SliverClientConfig.parse_config_file(CONFIG_PATH)
    client = SliverClient(config)
    await client.connect()
    return client


@fixture(scope="global")
async def implant_config() -> ImplantConfig:
    return ImplantConfig(
        IsBeacon=False,
        Name="sliver-pytest-" + os.urandom(8).hex(),
        GOARCH="amd64",
        GOOS="linux",
        Format=OutputFormat.EXECUTABLE,
        ObfuscateSymbols=False,
        C2=[ImplantC2(Priority=0, URL="http://localhost:80")],
    )


@fixture(scope="global")
def sliverpy_random_name() -> str:
    return "sliver-pytest-" + os.urandom(8).hex()


@fixture(scope="global")
def data_dir() -> Path:
    return Path(__file__).parent / "data"
