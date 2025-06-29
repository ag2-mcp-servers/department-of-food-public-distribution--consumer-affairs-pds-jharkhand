# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T14:51:04+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity

from models import (
    RatcrCertificatePostRequest,
    RatcrCertificatePostResponse,
    RatcrCertificatePostResponse1,
    RatcrCertificatePostResponse2,
    RatcrCertificatePostResponse3,
    RatcrCertificatePostResponse4,
    RatcrCertificatePostResponse5,
    RatcrCertificatePostResponse6,
)

app = MCPProxy(
    description='Public distribution system (PDS) is an Indian food security system. Established by the Government of India under Ministry of Consumer Affairs, Food, and Public Distribution and managed jointly with state governments in India. Jharkhand PDS Ration Card Certificates is available in Digilocker for Citizen.',
    termsOfService='https://apisetu.gov.in/terms.php',
    title='Department of Food, Public Distribution & Consumer Affairs (PDS), Jharkhand',
    version='3.0.0',
    servers=[{'url': 'https://apisetu.gov.in/aaharjh/v3'}],
)


@app.post(
    '/ratcr/certificate',
    description=""" API to verify Ration Card. """,
    tags=['ration_card_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def ratcr(body: RatcrCertificatePostRequest = None):
    """
    Ration Card
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
