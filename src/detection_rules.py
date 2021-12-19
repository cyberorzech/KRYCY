from loguru import logger

from src.files_management.pcap_file import PCAP_File

@logger.catch
def detect_external_dns_request(**kwargs):
    condition = False
    for pcap in kwargs["pcap"]:
        try:
            pcap_file = PCAP_File(pcap)
            pcap_content = pcap_file.read()
            
        except Exception as e:
            logger.error(str(e))
    for evtx in kwargs["evtx"]:
        pass
    for xml in kwargs["xml"]:
        pass
    for json in kwargs["json"]:
        pass
    for txt in kwargs["txt"]:
        pass

    if not condition:
        return None, None, None
    
    action_alert = ""
    action_block = True
    description = ""
    return action_alert, action_block, description


def main():
    raise NotImplementedError("Use as package")

if __name__ == "__main__":
    main()
