import whois


def domain_scan(target):

    try:

        info = whois.whois(target)

        return {

            "target": target,

            "scan_type": "Domain Intelligence",

            "registrar": info.registrar,

            "creation_date": info.creation_date,

            "expiration_date": info.expiration_date,

            "name_servers": info.name_servers,

            "status": "Completed Successfully"

        }

    except Exception as e:

        return {

            "target": target,

            "scan_type": "Domain Intelligence",

            "status": f"Error : {e}"

        }