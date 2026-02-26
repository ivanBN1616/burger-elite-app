# burger-elite-app

![badge-license](https://img.shields.io/badge/license-All%20Rights%20Reserved-lightgrey)
![badge-version](https://img.shields.io/badge/version-0.1.0-blue)

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
```

Deploy (simple VPS copy)

After building, copy the `dist/` output to your web root on the VPS. Example command (run from project root on the VPS):

```bash
cd frontend
npm run build
sudo rm -rf /var/www/burger_elite/public/*
sudo cp -r dist/* /var/www/burger_elite/public/
sudo chown -R www-data:www-data /var/www/burger_elite/public
sudo systemctl reload nginx
```

Project structure (important)

- `frontend/` — Vue 3 + Vite + Tailwind (UI, landing, dev server)
- `backend/` — Python services (sniper & antigravity)
- `vps_config/` — Nginx and deployment scripts

Contributing & Owner

Este repositorio es público en GitHub, pero el contenido está bajo la licencia especificada en `LICENSE` (propiedad del autor). Para contribuciones abrir un PR en GitHub.

If you want, I can also add an automated `vps_config/deploy.sh` script that runs the above commands and a GitHub Actions workflow to build and deploy.
