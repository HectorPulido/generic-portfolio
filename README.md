# Generic Portfolio

A Dockerized Django “portfolio” application with a headless CMS interface, dynamic page and section management, and a REST/HTML hybrid front-end.

## Features

- **Dynamic Pages**: Create and organize pages composed of Markdown sections and images.
- **Configurable Themes**: Store colors, fonts, logos, and more in the database via a simple key/value model.
- **REST + Templating**: Expose pages through Django REST Framework with HTML rendering.
- **Nested Admin**: Manage pages, sections, and images in a hierarchical interface.
- **Arbitrary File Serving**: Upload any file and serve it by slug.

## Prerequisites

- Docker & Docker Compose
- (Optional) A `.env` file at the project root to override default settings:
  ```env
  SECRET_KEY=your-secret-key
  DEBUG=0
  ALLOWED_HOSTS=your.domain.com
  DB_NAME=mydb
  DB_USER=myuser
  DB_PASSWORD=mypassword
  DB_HOST=portfoliodb
  DB_PORT=5432
  DJANGO_SUPERUSER_USERNAME=admin
  DJANGO_SUPERUSER_EMAIL=admin@example.com
  DJANGO_SUPERUSER_PASSWORD=strongpassword
````

## Getting Started

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/generic-portfolio.git
   cd generic-portfolio
   ```

2. **Build & run**

   ```bash
   docker-compose up --build
   ```

3. **Access the app**

   * Front-end:  `http://localhost:9900/`
   * Admin UI:   `http://localhost:9900/admin/`
     (use the superuser credentials from your `.env` or defaults)

4. **Stop & remove**

   ```bash
   docker-compose down
   ```

## Configuration

* Default configurations (colors, titles, favicon, etc.) are created automatically on startup.
* To customize, log in to the Django admin and edit the **Config** entries.
* Pages, sections, and images can be managed under the **Portfolio** app in admin.

## Deployment

* Adjust `DEBUG`, `ALLOWED_HOSTS`, and `SECRET_KEY` in your production `.env`.
* Use `docker-compose -f docker-compose.prod.yml up --build -d` (if you create a production compose file).
* Point your web server (Nginx, Traefik, etc.) to the Gunicorn port `8000` inside the container.

## Contributing

1. Fork the repo
2. Create a feature branch
3. Submit a pull request

---


<div align="center">
<h3 align="center">Let's connect 😋</h3>
</div>
<p align="center">
<a href="https://www.linkedin.com/in/hector-pulido-17547369/" target="blank">
<img align="center" width="30px" alt="Hector's LinkedIn" src="https://github.com/HectorPulido/HectorPulido/blob/master/img/linkedin-icon.svg?raw=true"/></a> &nbsp; &nbsp;
<a href="https://twitter.com/Hector_Pulido_" target="blank">
<img align="center" width="30px" alt="Hector's Twitter" src="https://github.com/HectorPulido/HectorPulido/blob/master/img/twitter-official.svg?raw=true"/></a> &nbsp; &nbsp;
<a href="https://www.twitch.tv/hector_pulido_" target="blank">
<img align="center" width="30px" alt="Hector's Twitch" src="https://github.com/HectorPulido/HectorPulido/blob/master/img/twitch-icon.svg?raw=true"/></a> &nbsp; &nbsp;
<a href="https://www.youtube.com/channel/UCS_iMeH0P0nsIDPvBaJckOw" target="blank">
<img align="center" width="30px" alt="Hector's Youtube" src="https://github.com/HectorPulido/HectorPulido/blob/master/img/youtube-icon.svg?raw=true"/></a> &nbsp; &nbsp;
<a href="https://pequesoft.net/" target="blank">
<img align="center" width="30px" alt="Pequesoft website" src="https://github.com/HectorPulido/HectorPulido/blob/master/img/pequesoft-favicon.png?raw=true"/></a> &nbsp; &nbsp;

</p>