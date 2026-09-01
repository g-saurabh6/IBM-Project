from datetime import datetime


def show_incident(incident_type):
    incidents = {
        "1": {
            "name": "Phishing Attack",
            "severity": "High",
            "risk": "Credential theft and unauthorized account access",
            "actions": [
                "Disable the affected account",
                "Reset the user's password",
                "Enable or verify MFA",
                "Review recent login activity",
                "Report and block the suspicious email"
            ]
        },
        "2": {
            "name": "Malware Infection",
            "severity": "High",
            "risk": "System damage and possible data theft",
            "actions": [
                "Disconnect the affected device from the network",
                "Run a security scan",
                "Remove malicious software",
                "Apply security updates",
                "Restore affected data from a clean backup"
            ]
        },
        "3": {
            "name": "Ransomware Attack",
            "severity": "Critical",
            "risk": "Data encryption and business disruption",
            "actions": [
                "Isolate affected systems immediately",
                "Disable compromised accounts",
                "Preserve relevant evidence",
                "Identify clean backups",
                "Restore systems after security verification"
            ]
        },
        "4": {
            "name": "Unauthorized Access",
            "severity": "High",
            "risk": "Unauthorized access to business information",
            "actions": [
                "Disable the compromised account",
                "Reset credentials",
                "Review access logs",
                "Check for unauthorized changes",
                "Enable MFA and monitor the account"
            ]
        }
    }

    return incidents.get(incident_type)


def generate_report(incident):
    print("\n" + "=" * 55)
    print("        INCIDENT RESPONSE SIMULATION REPORT")
    print("=" * 55)

    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Incident: {incident['name']}")
    print(f"Severity: {incident['severity']}")
    print(f"Risk: {incident['risk']}")

    print("\nIncident Response Steps:")

    steps = [
        "Identification",
        "Containment",
        "Eradication",
        "Recovery",
        "Lessons Learned"
    ]

    for number, step in enumerate(steps, 1):
        print(f"\n{number}. {step}")

        if step == "Identification":
            print("   Incident identified and assessed.")

        elif step == "Containment":
            print("   Affected systems/accounts are isolated.")

        elif step == "Eradication":
            print("   Threat is removed and security weaknesses are addressed.")

        elif step == "Recovery":
            print("   Systems are restored and monitored.")

        elif step == "Lessons Learned":
            print("   Incident is reviewed and preventive measures are improved.")

    print("\nRecommended Actions:")

    for action in incident["actions"]:
        print(f"   - {action}")

    print("\nFinal Status: INCIDENT CONTAINED")
    print("=" * 55)


def main():
    print("=" * 55)
    print("       SMALL BUSINESS INCIDENT RESPONSE SYSTEM")
    print("=" * 55)

    print("\nSelect the security incident:")
    print("1. Phishing Attack")
    print("2. Malware Infection")
    print("3. Ransomware Attack")
    print("4. Unauthorized Access")

    choice = input("\nEnter your choice (1-4): ")

    incident = show_incident(choice)

    if incident:
        generate_report(incident)
    else:
        print("\nInvalid choice. Please select a number from 1 to 4.")


if __name__ == "__main__":
    main()
