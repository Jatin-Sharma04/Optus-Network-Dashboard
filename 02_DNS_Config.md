ssh -i ~/.ssh/id_rsa azureuser@<your_vm_ip>


---

### `docs/02_DNS_Config.md`

```markdown
# DNS Configuration

1️⃣ Domain purchased via Namecheap: `teleco-optus-field-tools.com`

2️⃣ Created A Record:

- Host: `status`
- Type: A
- Value: `<Azure_VM_Public_IP>`
- TTL: Automatic

3️⃣ DNS Verified via:

```bash
dig +short status.teleco-optus-field-tools.com
