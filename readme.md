# 🚀 RadarChart API 📊✨

¡Bienvenido a **RadarChart API**! Un micro-servicio que convierte tus números en un vistoso diagrama de radar con solo un `POST` 📨➡️🎯.

---

## 🗺️ Tabla de contenido
1. 🌟 [Características principales](#-características-principales)
2. ⚡ [Instalación rápida](#-instalación-rápida)
3. 🔗 [Endpoint](#-endpoint)
4. 🛠️ [Ejemplo de uso](#-ejemplo-de-uso)
5. 🧩 [Esquema del JSON](#-esquema-del-json)
6. 🎨 [Respuesta](#-respuesta)
7. 🤝 [Contribuir](#-contribuir)
8. 📝 [Licencia](#-licencia)

---

## ✨ Características principales
- 🔥 **Simple**: un solo endpoint, sin complicaciones.  
- 🎨 **Gráficas hermosas**: radar charts nítidos listos para incrustar.  
- ⚙️ **Personalizable**: colores, títulos y más vía JSON.  
- 🚀 **Ligero & stateless**: perfecto para serverless o contenedores.

---

## ⚡ Instalación rápida

```bash
# 1️⃣ Clona el repo
git clone https://github.com/tu-org/radarchart-api.git
cd radarchart-api

# 2️⃣ Construye la imagen (opcional)
docker build -t radarchart-api .

# 3️⃣ ¡Despega!
docker run -p 8000:8000 radarchart-api
# → Servicio disponible en http://localhost:8000 🎉
