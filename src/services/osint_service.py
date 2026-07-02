from src.services.domain_service import domain_scan
from src.services.ip_service import ip_scan


def run_scan(target, scan_type):

    if scan_type == "Domain Intelligence":
        return domain_scan(target)

    if scan_type == "IP Intelligence":
        return ip_scan(target)

    return {
        "target": target,
        "scan_type": scan_type,
        "status": "Scanner Not Implemented Yet"
    }