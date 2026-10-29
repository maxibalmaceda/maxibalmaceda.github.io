# Sitio personal de Maximiliano Balmaceda

Publicado en **https://maxibalmaceda.github.io**, hecho con [Quarto](https://quarto.org).

## Cómo se publica

Cada vez que cambia un archivo en este repositorio, GitHub genera el sitio y lo publica solo (archivo `.github/workflows/publicar.yml`). No hace falta instalar nada en la computadora.

## Qué hay en cada carpeta

| Archivo o carpeta | Qué es |
|---|---|
| `_quarto.yml` | Configuración general: menú, enlaces, colores |
| `styles.scss` | Estilos: tipografías, colores, tarjetas, línea de tiempo |
| `index.qmd` | Página de inicio |
| `blog.qmd`, `proyectos.qmd` | Listados automáticos de artículos y proyectos |
| `sobre-mi.qmd` | Presentación personal |
| `posts/` | Un artículo por carpeta (`index.qmd` + `portada.png`) |
| `proyectos/` | Un proyecto por carpeta, misma lógica |
| `img/` | Foto y favicon |

## Borradores

Los archivos con `draft: true` en el encabezado no aparecen en el sitio publicado. Para publicarlos, cambiar a `draft: false`.

## Pendientes

- [ ] Foto nueva en `img/foto.png` (cuadrada, mínimo 400 × 400 px).
- [ ] Reescribir y publicar el primer post (`posts/2026-11-01-empiezo/`).
- [ ] Agregar el CV en PDF y su botón.
