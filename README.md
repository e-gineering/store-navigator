<h1 align="center">store-navigator</h1>

<p align="center">Helping you group your shopping list</p>

- [Local development](#local-development)
- [Deploying to Azure](#deploying-to-azure)


## Local development

Start the streamlit dev server with:

```
rye run dev
```

Auto-format code with Ruff (included as part of Rye) with:

```
rye fmt
```


## Deploying to Azure

Install terraform and the cdktf cli (or use the devcontainer where they're preinstalled).

A helpful 

Kick off the Azure auth process with this, which should open your browser:

```
az login
```

Then in your terminal you should get a prompt to select which subscription you want to use.


cdktf init --template python

Chose to use Terraform Cloud for the state file storage, and selected `azurerm` from a list of providers to install.
