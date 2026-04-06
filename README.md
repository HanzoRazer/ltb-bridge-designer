# ltb-bridge-designer

Acoustic and electric bridge geometry: scale-to-bridge placement, pin positions, break angle, string tension, archtop floating bridge (Benedetto), electric bridge presets, Floyd Rose routing, saddle compensation, CAM presets, and DXF export.

**Source of truth:** [luthiers-toolbox](https://github.com/HanzoRazer/luthiers-toolbox) — populated via **Staged Copy Publish** (see `SPRINTS.md` there).

## Layout

```
src/ltb_bridge/
  calculators/           # bridge_calc, bridge_break_angle, acoustic_bridge_calc, string_tension
  instrument_geometry/
    models.py            # InstrumentModelId, specs (shared with bridge/neck)
    neck/neck_profiles.py
    bridge/              # geometry, placement, compensation, archtop_floating_bridge, electric_bridges, floyd_rose_tremolo
  api/
    bridge_router.py
    bridge_presets_router.py
    bridge_export_router.py
  main.py
scripts/populate_imports.py   # optional re-sync helper
```

## API

```bash
pip install -e .
uvicorn ltb_bridge.main:app --reload --host 0.0.0.0 --port 8000
```

- `GET /health`
- `GET /docs`
- `POST /api/instrument/bridge`, `/api/instrument/bridge/pin-positions`, `GET /api/instrument/bridge/options`
- Presets: `/api/cam/bridge/...` (see OpenAPI)
- DXF: `POST /api/cam/bridge/export_dxf`

## Dependencies

Python 3.11+. `ezdxf` is required for archtop DXF generation in `archtop_floating_bridge`.

## License

See `LICENSE`.
