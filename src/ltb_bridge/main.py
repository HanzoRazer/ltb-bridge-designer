"""FastAPI entrypoint for LTB Bridge Designer."""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ltb_bridge.api.bridge_router import router as bridge_router
from ltb_bridge.api.bridge_presets_router import router as bridge_presets_router
from ltb_bridge.api.bridge_export_router import router as bridge_export_router

app = FastAPI(
    title="LTB Bridge Designer",
    description="Acoustic and electric bridge geometry, presets, and DXF export — published from luthiers-toolbox.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(bridge_router, prefix="/api/instrument")
app.include_router(bridge_presets_router, prefix="/api")
app.include_router(bridge_export_router, prefix="/api/cam")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "ltb-bridge-designer"}
