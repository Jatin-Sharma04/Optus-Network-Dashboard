
---

### `docs/03_SSL_Setup.md`

```markdown
# SSL (Let's Encrypt)

1️⃣ Install Certbot:

```bash
sudo apt update
sudo apt install certbot python3-certbot-nginx -y

sudo certbot --nginx -d status.teleco-optus-field-tools.com

Verify HTTPS works:
https://status.teleco-optus-field-tools.com
