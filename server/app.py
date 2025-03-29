import subprocess
from pydantic import BaseModel
from yapeco import BaseEnvironment
from fastapi import FastAPI, status, Header, HTTPException


class Env(BaseEnvironment):
    write_key: str


class Mapping(BaseModel):
    public_ip: str
    ip_map: dict[str, str]


app = FastAPI()


@app.post("/set-mapping")
async def add_mapping(mapping: Mapping, x_write_key: str = Header()):
    if x_write_key != Env.write_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid write key"
        )

    for internal_port, external_port in mapping.ip_map.items():
        # NOTE: this MUST be whitelisted, see readme
        subprocess.run(
            [
                "sudo",
                "-n",
                "bash",
                "add_mapping.sh",
                mapping.public_ip,
                internal_port,
                external_port,
            ],
            check=True,
        )
    return status.HTTP_200_OK
