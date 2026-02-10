
# services/config_service.py
from __future__ import annotations
import os
from pathlib import Path
from typing import Dict, Optional
from dataclasses import dataclass
from dotenv import load_dotenv, dotenv_values

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class Settings:
    APP_ENV: str
    DB_URL: str
    APP_PASSWORD_PEPPER: str = ""

class ConfigService:
    def __init__(self, base_dir: Optional[Path] = None, env_filename: str = ".env"):
        self.base_dir = Path(base_dir) if base_dir else Path(__file__).resolve().parents[1]
        self.env_path = self.base_dir / env_filename
        self.env_local_path = self.base_dir / f"{env_filename}.local"
        self._settings: Optional[Settings] = None

    def load(self, override: bool = False) -> Settings:
        # Carga archivos .env → os.environ
        if self.env_path.exists():
            load_dotenv(self.env_path, override=override, encoding="utf-8")
        if self.env_local_path.exists():
            load_dotenv(self.env_local_path, override=True, encoding="utf-8")

        # Construye Settings desde os.environ
        s = Settings(
            APP_ENV=os.getenv("APP_ENV", "development"),
            DB_URL=os.getenv("DB_URL", ""),
            APP_PASSWORD_PEPPER=os.getenv("APP_PASSWORD_PEPPER", "")
        )
        # Validación mínima
        missing = [k for k, v in vars(s).items() if k in ("DB_URL",) and not v]
        if missing:
            raise ConfigError(f"Faltan variables requeridas: {', '.join(missing)}")

        self._settings = s
        return s

    def settings(self) -> Settings:
        if not self._settings:
            # Garantiza que siempre cargaste antes de pedir settings
            return self.load(override=False)
        return self._settings

    # Opcional: leer los valores “crudos” para mostrarlos/editar en UI
    def current_values(self) -> Dict[str, str]:
        combined: Dict[str, str] = {}
        for p in (self.env_path, self.env_local_path):
            if p.exists():
                combined.update({k: v or "" for k, v in dotenv_values(p).items()})
        for k in list(combined.keys()):
            combined[k] = os.getenv(k, combined[k])
        return combined

    # Opcional: guardar un .env básico (sin .env.local)
    def save_env(self, data: Dict[str, str]) -> None:
        lines = ["# .env generado por la app\n"]
        for k in sorted(data.keys()):
            v = (data[k] or "").strip()
            if any(ch.isspace() for ch in v) or "#" in v or "=" in v:
                v = f'"{v}"'
            lines.append(f"{k}={v}")
        self.env_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        # Recarga para reflejar en os.environ
        self.load(override=True)
