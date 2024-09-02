import os
import subprocess
import speedtest
import socket
import time
from datetime import datetime


def test_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        ping = st.results.ping
        return download_speed, upload_speed, ping
    except speedtest.SpeedtestException:
        return 0, 0, 0
    except Exception as e:
        return 0, 0, 0


def test_dns_resolution(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None


def test_ping(domain):
    command = ["ping", "-c", "4", domain]
    response = subprocess.run(command, stdout=subprocess.PIPE)
    return response.stdout.decode()


def test_traceroute(domain):
    if os.name == "nt":  # Windows
        command = ["tracert", domain]
    else:  # Unix-based systems (Linux/Mac)
        command = ["traceroute", domain]
    response = subprocess.run(command, stdout=subprocess.PIPE)
    return response.stdout.decode()


def load_domains(filename="domains.txt"):
    with open(filename, 'r') as file:
        domains = file.read().splitlines()
    return domains


def save_results(filename, domain, speed, dns, ping, traceroute):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, 'a') as file:  # Append mode
        file.write(f"=== Test Results for {domain} ===\n")
        file.write(f"Timestamp: {current_time}\n")
        file.write("=== Speed Test ===\n")
        file.write(f"Download Speed: {speed[0]:.2f} Mbps\n")
        file.write(f"Upload Speed: {speed[1]:.2f} Mbps\n")
        file.write(f"Ping: {speed[2]:.2f} ms\n")
        file.write("\n=== DNS Resolution ===\n")
        file.write(f"IP Address for {domain}: {dns}\n")
        file.write("\n=== Ping Test ===\n")
        file.write(ping)
        file.write("\n=== Traceroute Test ===\n")
        file.write(traceroute)
        file.write("\n\n")


if __name__ == "__main__":
    domains = load_domains("domains.txt")
    filename = "internet_test_results.txt"

    while True:
        for domain in domains:
            print(f"Running tests for {domain}...")

            print("Running speed test...")
            speed = test_speed()

            print(f"Testing DNS resolution for {domain}...")
            dns = test_dns_resolution(domain)

            print(f"Running ping test for {domain}...")
            ping = test_ping(domain)

            print(f"Running traceroute test for {domain}...")
            traceroute = test_traceroute(domain)

            print(f"Saving results for {domain}...")
            save_results(filename, domain, speed, dns, ping, traceroute)

            print(f"Finished tests for {domain}. Waiting before next domain...\n")

        time.sleep(240)  # Wait 60 seconds before the next round of tests
