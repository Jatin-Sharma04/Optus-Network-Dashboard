# Optus Field Technician Network Status Dashboard

Student Name: Jatin Sharma  
Student ID: 35257547  
Domain: [https://status.teleco-optus-field-tools.com](https://status.teleco-optus-field-tools.com)  
Server IP: 20.5.48.154
**Video Link:** (Insert Loom or YouTube unlisted link)

---

## Project Overview

This project is built as part of ICT171 Assignment 2 to demonstrate IaaS deployment and full-stack server configuration using Azure Virtual Machines. The server simulates an internal Optus field technician dashboard displaying live network service status, a Perth store map location, and a Q&A section for internal support teams.

The stack includes:

- Azure IaaS VM (Ubuntu 22.04)
- Full manual setup of NGINX, SSL, Python, Flask
- Custom reverse proxy configuration
- Self-hosted API providing simulated service status data
- HTML/JS/CSS front-end dashboard
- Embedded live Perth Optus Booragoon store map

---

## Rebuild Guide

> This guide allows full rebuild of the system within ~60-90 minutes.

1️⃣ [VM Setup](docs/01_VM_Setup.md)  
2️⃣ [DNS Configuration](docs/02_DNS_Config.md)  
3️⃣ [SSL Setup](docs/03_SSL_Setup.md)  
4️⃣ [NGINX Reverse Proxy](docs/04_Nginx_Config.md)  
5️⃣ [Flask API Deployment](docs/05_Flask_API.md)  
6️⃣ [Frontend UI Configuration](docs/06_Frontend_UI.md)

---

## Bonus Features

- Fully secured HTTPS (Let's Encrypt SSL)
- API service running persistently with Systemd
- Live simulated data with randomized statuses
- Interactive embedded Google Map of Optus Booragoon
