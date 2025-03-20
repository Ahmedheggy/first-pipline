# 🚀 Dockerized Flask App with PostgreSQL, Redis & GitLab CI/CD

This project is a **Flask web application** that interacts with **PostgreSQL** and **Redis**, fully containerized with **Docker Compose**. It also includes a **CI/CD pipeline using GitLab**, automating the **build, test, and deployment** process for seamless updates.

---

## 🔹 Key Features

✅ **Flask Web App** – A simple API-based application.  
✅ **PostgreSQL Database** – Stores user and visitor tracking data.  
✅ **Redis Caching** – Improves performance with quick data access.  
✅ **Docker & Docker Compose** – Simplifies setup and container orchestration.  
✅ **GitLab CI/CD Pipeline** – Automates testing, building, and deployment.  
✅ **Visitor Tracking API** – Logs visitor names and timestamps.  
✅ **Wave Counter API** – A `/wave` endpoint to track interactions.  
✅ **Get Wave Count API** – A `/get_count` endpoint to retrieve data.  
✅ **Health Checks** – PostgreSQL and Redis have built-in health checks.  
✅ **Environment Variables** – Uses `.env` for flexible configuration.  
✅ **Logging & Debugging** – Displays errors and status messages for troubleshooting.  

---

## 📌 Project Structure

```
├── .gitlab-ci.yml          # CI/CD Pipeline configuration  
├── docker-compose.yml      # Defines all services (Flask, PostgreSQL, Redis)  
├── Dockerfile              # Flask application container  
├── app/                    # Flask application code  
│   ├── main.py             # Main Flask app  
│   ├── database.py         # Database connection setup  
│   ├── routes.py           # API routes  
│   ├── models.py           # Database models  
│   ├── templates/          # HTML templates (if applicable)  
│   ├── static/             # Static assets (CSS, JS)  
├── .env                    # Environment variable configuration  
├── tests/                  # Unit and integration tests  
├── README.md               # Documentation (This file)  
```

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository (GitHub)
```bash
git clone https://github.com/Ahmedheggy/first-pipline.git
cd first-pipeline
```

### 1️⃣ Clone the Repository (GitLab)
```bash
git clone https://gitlab.com/ahmadhany122/first-pipeline.git
cd first-pipeline

###################################################################################################
*  you can use : git remote add if you have a local repo
####################################################################################################


### 2️⃣ Create a `.env` File
Create a `.env` file in the root directory:
```env
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=mydatabase
REDIS_HOST=redis
```

### 3️⃣ Build & Start Containers
```bash
docker-compose up --build -d
```

### 4️⃣ Access the Web App
- Open in browser: [http://localhost:8000](http://localhost:8000)

### 5️⃣ Check Database (Inside Container)
```bash
docker exec -it flask_app-db-1 psql -U user -d mydatabase
```

### 6️⃣ Query Data
```sql
SELECT * FROM visits;
```

---

## 📦 CI/CD Pipeline (GitLab)[If you need to use GitHub actions u need to migrate]

This project integrates **GitLab CI/CD** to **automate testing, building, and deploying** new versions whenever updates are pushed to the repository.

### ⚙️ Pipeline Stages

1️⃣ **Build** – Ensures Docker is set up and builds the application image.  
2️⃣ **Test** – Runs automated integration tests.  
3️⃣ **Debug Networks** – Checks network configurations inside Docker.  
4️⃣ **Deploy** – Deploys the updated application automatically.  

### 📜 Pipeline Configuration (`.gitlab-ci.yml`)

```yaml
image: docker:24.0.7  # Using Docker as the base image

variables:
  DOCKER_HOST: unix:///var/run/docker.sock  # Enable Docker socket
  COMPOSE_HTTP_TIMEOUT: 300  # Prevent timeout errors
  IMAGE_NAME: flask_app

stages:
  - build
  - test
  - deploy

before_script:
  - apk add --no-cache docker-compose  # Install docker-compose
  - docker --version  # Verify Docker installation
  - docker-compose --version  # Verify docker-compose installation

build_job:
  stage: build
  services:
    - name: docker:dind  # Enable Docker-in-Docker
      command: ["--tls=false"]
  script:
    - docker-compose build --no-cache  # Build fresh image
  tags:
    - docker

test:
  stage: test
  services:
    - docker:dind
  script:
    - docker-compose up -d
    - sleep 20  # Wait for services to start
    - docker-compose exec web curl http://localhost:5000  # Test API response
  after_script:
    - docker-compose down  # Stop containers

deploy:
  stage: deploy
  only:
    - main  # Deploy only on main branch
  script:
    - docker stop flask_app || true  # Stop running container
    - docker rm flask_app || true  # Remove old container
    - docker-compose up -d  # Start new deployment
```

---

## 🛠️ Running the CI/CD Pipeline Manually

If using GitLab, the pipeline will automatically run on **push**.  
To trigger it manually:

1️⃣ Navigate to **GitLab > CI/CD > Pipelines**.  
2️⃣ Click **Run Pipeline** and select a branch.  

---

## 📌 Additional Docker Commands

### Stop All Containers
```bash
docker-compose down
```

### Rebuild and Restart
```bash
docker-compose up --build -d
```

### View Running Containers
```bash
docker ps
```

---

## 🚀 Deployment Strategy

1. **Push to GitLab → Pipeline Runs**  
   - Any push to `main` triggers **Build**, **Test**, and **Deploy** stages.  
   - Ensures code is tested before deployment.  

2. **Dockerized Deployment**  
   - Containers are automatically rebuilt and restarted.  

3. **Rollback Support**  
   - If a new deployment fails, revert to the previous working image:  
   ```bash
   docker stop flask_app
   docker start flask_app_old
   ```

---

## 📈 Future Enhancements

✅ **Logging & Monitoring** – Add Prometheus/Grafana for observability.  
✅ **CI/CD Security** – Implement container scanning for vulnerabilities.  
✅ **Automated Database Migrations** – Use Alembic for schema updates.  

---

## 💡 Summary

This project integrates **Flask, PostgreSQL, and Redis** with **Docker** for easy deployment.  
It features a **fully automated GitLab CI/CD pipeline**, ensuring that each update is **tested and deployed seamlessly**.  

