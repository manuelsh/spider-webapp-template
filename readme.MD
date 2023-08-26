# Spider-Webapp: Swing Into Action with This Webapp Template

!["With great power comes great responsibility"](media/spiderman.JPG)

## The Origin Story

Just like Peter Parker didn't become Spider-Man overnight, building a webapp from scratch isn't a walk in Central Park. You've got villains—err, base technologies—to wrangle: a server, APIs, SSL certificates, databases, and even authentication. It's like trying to balance school, work, and being a superhero all at once! But fret not, true believer! Spider-Webapp is here to give you a head start, offering a template based on the following state-of-the-art technologies:

## The Tech Lineup

- **Nginx Server**: Directing web traffic faster than you can say "I need the help of Spider-Man!" Acts as a reverse proxy to route web traffic to the right application services.
  
- **Certbot**: The "Spider-Sense" of our setup, alerting you to SSL certificate needs and configuring Nginx to use them securely.
  
- **Gunicorn with FastAPI**: Think of Gunicorn as the webbing that holds your FastAPI application together. FastAPI is the high-performance, easy-to-use framework that's as agile as our web-crawler hero.
  
- **SQLite Database**: Lighter than Peter Parker's backpack, this self-contained, serverless, and zero-configuration database engine is perfect for data storage on starting projects. Can be swapped out for heavy-hitters like PostgreSQL or MySQL when it's time to join the Avengers.
  
- **Optional Firebase Authentication**: Need to know who's behind the mask? Use Firebase for user authentication, if you so choose.

## Why Choose Spider-Webapp?

This template is designed to be as customizable as a Spidey suit and scalable enough to handle anything from a local skirmish to an intergalactic threat. Ideal for deployment on a server (e.g., AWS's EC2).

## Configuration


### Domain Association: Your Web Identity

1. **Purchase a Domain**: Acquire a domain from a reputable domain registrar.
2. **DNS Setup**: Point your domain to your server's IP address via the domain registrar's dashboard.
3. **Nginx Configuration**: Update the `server_name` directive in `nginx-prod.conf` to your domain.
4. **SSL Certificate**: Run `certbot --nginx` and follow the on-screen instructions to secure your domain with SSL.


In `nginx.conf` within the `/nginx` folder, replace `[yourdomain.zzz]` with your domain. If using a subdomain like `api.yourdomain.zzz`, replace `[name of your subdomain]` with `API`.

## Nginx Server

Edit `nginx-prod.conf` in the `nginx` directory to configure the server, including server name and upstream API server settings.

### Certbot

Certbot is ready to go with Nginx. To get a new certificate, simply run `certbot --nginx`. Note: A domain is required.

### FastAPI

Navigate to `fastapi-app` and modify `main.py` to add or alter API endpoints. Middleware support is also available.


### Environment Variables

These are stored in a `.env` file in the project root. Docker Compose uses this file during container build and run. Here's a sample:

```env
# Database
DATABASE_PATH=/path/to/database
DATABASE_FILE_NAME="database.db"

# API
API_TIMEOUT=360
```

Remember to update the `.env` file with your specific configuration before building and running the Docker containers.

Note: Do not commit the `.env` file to version control. It contains sensitive information and should be kept private.


### SQLite Database

The SQLite database is file-based, and it will be stored in the server. Use a SQLite client for schema modifications, for example the python library `sqlite3` .To initialize it, edit the file `init_db.py` to include the fields that you need, and start it with:

```
python init_db.py
```

Most probably you would need root access to modify the file (you can use `sudo` before).

### Firebase Authentication (Optional)

1. Create a Firebase project.
2. Enable desired sign-in methods under 'Authentication'.
3. Moify the file `website/sign-in.html` accordingly.

### Server port configuration

Typically, open the following ports:

1. **Port 80**: For HTTP and Certbot's ACME challenge.
2. **Port 443**: For HTTPS.

## Running the Application: Launch Time

1. **Build and Run**: Navigate to the project root and execute:
   \`\`\`bash
   docker-compose --env-file .env -f docker-compose.yml up -d --build
   \`\`\`
2. **Stopping the App**: To halt the application, run:
   \`\`\`bash
   docker-compose -f docker-compose.yml down
   \`\`\`

Remember to rebuild Docker images after any configuration changes.
