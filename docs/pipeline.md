# Pipeline CI/CD

## Introducción

Este proyecto implementa un pipeline de Integración Continua y Entrega Continua (CI/CD) utilizando GitHub Actions.

El objetivo del pipeline es automatizar:

- Validación del código
- Ejecución de pruebas unitarias
- Análisis de seguridad
- Construcción de la imagen Docker
- Publicación de artefactos

---

# Flujo del Pipeline

El pipeline se ejecuta automáticamente cuando:

- Se realiza un push a la rama main
- Se crea un pull request hacia main

Archivo:

.github/workflows/ci-cd.yml

---

# Etapas del Pipeline

## 1. Checkout del código

Se descarga el repositorio desde GitHub.

```yaml
- uses: actions/checkout@v4