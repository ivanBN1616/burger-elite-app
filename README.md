# burger-elite-app

Landing & dashboard for Burger Elite — Solana sniping + Antigravity protection.

Quick start (development)

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0
# open: http://46.225.109.134:5173/ or https://burger-elite.com/ (if Nginx proxy enabled)
```

Build for production

```bash
cd frontend
npm run build
# copy dist/ to your web server (e.g. /var/www/burger_elite/public) and serve with Nginx
```

Project structure (important)

- `frontend/` — Vue 3 + Vite + Tailwind (UI, landing, dev server)
- `backend/` — Python services (sniper & antigravity)
- `vps_config/` — Nginx and deployment scripts

Contributing & Owner

Este repositorio es público en GitHub, pero el contenido está bajo la licencia especificada en `LICENSE` (propiedad del autor). Para contribuciones abrir un PR en GitHub.
