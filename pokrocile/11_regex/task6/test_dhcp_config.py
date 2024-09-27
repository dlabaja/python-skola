import re
from dhcp_config import check_dhcp_config, transfer_dhcp_config


def test_check_dhcp_config():
    assert check_dhcp_config("cosi.kdesi.cz ha=0040389A5B60:ip=1.2.3.4:") is True
    assert check_dhcp_config("cosi.kdesi.cz ha=ff4b389a5b60:ip=1.2.3.4:") is True
    assert (
        check_dhcp_config(
            "   cosi.kdesi.cz      ha=ff4b389a5b60:ip=1.2.3.4:           "
        )
        is True
    )
    assert check_dhcp_config("cosikdesicz   ha=0040389A5B60:ip=1.2.3.4:") is False
    assert check_dhcp_config("cosi.kdesi.cz ha=0040389A5B60:ip=1.2.3.4") is False
    assert check_dhcp_config("cosi.kdesi.cz ha=0040389A5B6:ip=1.2.3.4:") is False

    assert check_dhcp_config("cosi.kdesi.cz ha=ff4b389a5b60:ip=172.20.34.200") is False
    assert check_dhcp_config("cosi.kdesi.cz ha=ff4b389a5b60:ip=172.20.34") is False


def new_format_check(text: str) -> bool:
    regular = re.compile(
        r"""
\s*[\w\.]+\s+\{                                           # header
\s*link\ +address\ +([\dABCDEF]{2}:){5}[\dABCDEF]{2};     # link address
\s*fix\ +address\ +                                       # fix address
(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}  # start IPv4
(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]);  # IP    # end IPv4
\s*\}                                                     # footer
    """,
        flags=re.MULTILINE | re.VERBOSE | re.IGNORECASE,
    )
    return bool(regular.search(text))


def test_transfer_dhcp_config():
    input = "cosi.kdesi.cz ha=0040389a5b60:ip=192.51.38.244:"
    output = """host cosi.kdesi.cz {
  link address 00:40:38:9a:5b:60;
  fix  address 192.51.38.244;
}"""
    # assert transfer_dhcp_config(input) == output
    assert new_format_check(transfer_dhcp_config(input)) is True


if __name__ == "__main__":
    test_transfer_dhcp_config()
