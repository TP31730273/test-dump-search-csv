from dataclasses import dataclass

@dataclass
class CSVDataValidator:
    """Class for keeping track of an item in inventory."""
    domain_uuid: str
    start_stamp: str
    start_epoch: int
    hangup_cause:str
    NORMAL_CLEARING=None
    hangup_cause=None
    hangup_cause=None
    duration=None
    billmsec=None
    record_path=None
    record_name=None
    uuid=None
    bridge_uuid=None
    direction=None
    billsec=None 
    caller_id_name=None 
    caller_id_number=None 
    caller_destination=None
    source_number=None 
    destination_number=None 
    leg=None
    raw_data_exists=None
    accountcode=None
    answer_stamp=None
    sip_hangup_disposition=None 
    pdd_ms=None
    rtp_audio_in_mos=None
    tta=None


def data_validator():
    pass