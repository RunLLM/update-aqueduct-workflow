# Update Aqueduct Workflow GitHub Action

This action installs the `aqueduct-sdk` package and runs an Aqueduct workflow script.
The workflow script can access the Aqueduct server address and the api key via environment variables
`AQUEDUCT_SERVER_ADDRESS` and `AQUEDUCT_API_KEY`.

## Inputs

## `server_address`

**Required**: The IP address of the Aqueduct server.

## `port`

**Optional**: Port on which the server is listening; if none is provided, we assume port 8080.

## `api_key`

**Required**: The API key associated with your Aqueduct server. To find this, you can run `aqueduct apikey` on the machine where Aqueduct is running.

This should be passed in as a [GitHub Actions secret](https://docs.github.com/en/actions/security-guides/encrypted-secrets).

## `path`

**Required**: The path to the workflow script in the repository you're running the action. The script should contain the full definition of the workflow as well as a call to `publish_flow`.

## Example usage
```
uses: aqueducthq/update-aqueduct-workflow@v1
with:
  server_address: 127.0.0.1
  port: 8080 # Optional
  api_key: ${{ secrets.AQUEDUCT_API_KEY }}
  path: workflow/churn_prediction.py
```
