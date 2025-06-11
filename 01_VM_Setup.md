# VM Setup

**Platform:** Azure IaaS  
**OS Image:** Ubuntu 22.04 LTS  
**Size:** Standard_B1s

## Steps:

```bash
az login

az group create --name OptusProject --location australiaeast

az vm create \
--resource-group OptusProject \
--name OptusTools \
--image UbuntuLTS \
--size Standard_B1s \
--admin-username azureuser \
--generate-ssh-keys \
--public-ip-sku Standard

az vm open-port --port 80 --resource-group OptusProject --name OptusTools
az vm open-port --port 443 --resource-group OptusProject --name OptusTools
az vm open-port --port 22 --resource-group OptusProject --name OptusTools

