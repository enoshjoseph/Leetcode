import re
class Solution:
    def validIPAddress(self, IP: str) -> str:
        v4 = re.compile(r"((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}"r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])")
        v6 = re.compile(r"([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}")

        if v4.fullmatch(IP):
            return "IPv4"
        elif v6.fullmatch(IP):
            return "IPv6"
        else:
            return "Neither"