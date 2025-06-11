# Issues Encountered & Solutions

## Overview

This document summarizes the key problems I encountered while building and deploying my Azure-hosted Optus Network Monitoring Dashboard, as well as the solutions implemented to resolve them. The troubleshooting steps demonstrate my application of cloud computing, networking, Linux system administration, and problem-solving skills developed throughout ICT171.

---

1 Azure Bastion Access Issues

**Problem:**  
Azure Bastion repeatedly failed to deploy, giving resource group errors, subnet conflicts, and bastion host allocation failures (ResourceNotFound / 404). Bastion often crashed after idle timeout, requiring multiple redeployments.

**Root Cause:**  
Bastion was tied to virtual network (VNet) dependencies that became misaligned after several VM recreations and resource deletions.

**Solution:**  
- Fully deleted and recreated all dependent Azure resources: Bastion, VNets, NICs, IPs, and subnets.
- Ensured correct subnet creation: `AzureBastionSubnet` with `/27` address space.
- Redeployed Bastion only after VM and VNet were properly rebuilt.
- After multiple failed attempts, I ultimately used native SSH on my Mac for stable long-term access.

---

2 SSH Connection Timeout on Mac

**Problem:**  
SSH could not establish a connection from my Mac to the Azure VM (`operation timed out`).

**Root Cause:**  
Port 22 (SSH) was not allowed in the Network Security Group (NSG) after new VM creation.

**Solution:**  
- Added inbound rule for port 22 on Azure NSG.
- Verified with `nc -zv <IP> 22` that port 22 was now reachable.
- SSH access worked successfully after NSG fix.

---

3 DNS (Namecheap) Issues

**Problem:**  
After rebuilding VM and receiving new public IP addresses, Namecheap refused to accept the updated IP.

**Root Cause:**  
Namecheap sometimes caches previous DNS entries or rejects rapid IP changes if record conflicts exist.

**Solution:**  
- Cleared stale DNS entries.
- Deleted old A records completely.
- Re-added clean A record pointing to the new Azure Public IP.

---

4 Certbot SSL Setup Issues

**Problem:**  
Certbot installation repeatedly failed while attempting to execute inside Azure Cloud Shell (no sudo access).

**Root Cause:**  
Azure Cloud Shell is a restricted container without root permissions.

**Solution:**  
- SSH’d directly into my VM.
- Installed Certbot via `sudo apt install certbot python3-certbot-nginx -y`.
- Successfully generated SSL certificates for `status.teleco-optus-field-tools.com`.

---

5 403 Forbidden Error on NGINX

**Problem:**  
After cloning my web dashboard repo into `/var/www/html`, the website displayed HTTP 403 Forbidden errors.

**Root Cause:**  
- Incorrect file permissions on `/var/www/html/dist/` directory.
- NGINX lacked read access to web root.

**Solution:**  
- Set correct ownership:  
  ```bash
  sudo chown -R www-data:www-data /var/www/html
6 Flask API Errors
Problem:
Flask API failed to launch due to missing Python modules (ModuleNotFoundError: No module named 'flask').

Root Cause:
Debian 12 uses externally-managed Python environments which prevent system-wide pip install.

Created virtual environment:

python3 -m venv venv
source venv/bin/activate
Installed Flask inside virtualenv:

pip install flask


7 Systemd Service Failures
Problem:
The Flask API systemd service (optus-api.service) repeatedly failed on startup with exit-code=1.

Root Cause:
Incorrect path to Python interpreter in ExecStart due to virtualenv usage.

Solution:

Verified path with:
realpath /opt/scripts/venv/bin/python3

Updated systemd unit file:
ExecStart=/opt/scripts/venv/bin/python3 /opt/scripts/api_server.py

Reloaded systemd daemon and restarted service:
sudo systemctl daemon-reload
sudo systemctl restart optus-api


8 NGINX Reverse Proxy Misconfigurations
Problem:

Despite Flask working locally, API calls via NGINX proxy returned 404 errors.

Root Causes:

Multiple conflicting server_name blocks (from Certbot automatic rewrites).
Incorrect proxy path translation between /api/ and backend Flask routes.

Solutions:

Cleaned up redundant server blocks in /etc/nginx/sites-available/default.

Correct reverse proxy configuration:

location /api/ {
    proxy_pass http://127.0.0.1:5000/api/;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}

Restarted NGINX after syntax validation


9 Frontend Dashboard Issues

Problems Encountered:
index.html initially missing from /var/www/html/dist/.
Static dashboard didn’t reflect real network-like data.
Map embedding failed intermittently.

Solutions:
Rebuilt entire dashboard using custom index.html:
Live service status (mocked network data from Flask).
Optus Booragoon store location embedded via Google Maps iframe.
Internal IT Q&A table for technicians.
Verified NGINX served updated frontend correctly.

Final Outcome
Fully functional Azure-hosted dashboard.
Secure HTTPS domain: https://status.teleco-optus-field-tools.com.
Live API data served via Flask backend.
Reverse proxy via NGINX working properly.
Fully documented build process with resilient troubleshooting logs.
