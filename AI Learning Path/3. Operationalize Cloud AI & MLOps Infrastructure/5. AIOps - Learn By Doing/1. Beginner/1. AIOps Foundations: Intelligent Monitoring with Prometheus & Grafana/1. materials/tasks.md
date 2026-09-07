## Step 1: Understanding AIOps Fundamentals

🎯 The AIOps Conceptual Pyramid
AIOps applies artificial intelligence to IT operations, enhancing efficiency and reliability through a three-layer architecture:

Layer 3: Intelligent Actions (Auto-remediation, Self-healing)
Layer 2: AI-Driven Insights (Anomaly detection, Prediction)
Layer 1: High-Quality Data (Metrics, Logs, Traces) ← Today's Focus
💡 Key Principle: AI-driven insights are built upon a foundation of high-quality data. Without good data, AI cannot deliver reliable results!

📊 Why Metrics Are the Primary Data Source
Structured Format: Perfect for machine learning algorithms
Time-Series Data: Reveals trends, patterns, and anomalies
High Frequency: Real-time monitoring and immediate detection
Scalable Storage: Efficient time-series databases handle millions of data points
Multi-Dimensional: Labels enable detailed, granular analysis
📖 Next: We'll deploy the tools that collect and visualize these metrics

---

## Step 2: Review the Monitoring Architecture

📝 Understand Prometheus and Grafana
Your lab environment includes a pre-configured docker-compose.yml that defines the complete monitoring stack:

🔍 Prometheus (Port 9090)
Role: Time-series database and metrics collector
Architecture: Pull-based scraping model
Storage: Efficient TSDB for millions of data points
Query Language: PromQL for powerful metric analysis
📈 Grafana (Port 3000)
Role: Visualization and dashboard platform
Integration: Connects to Prometheus as data source
Capabilities: Beautiful, interactive dashboards
Alerting: Foundation for intelligent notifications
🚀 Review the Configuration
Let's examine the docker-compose.yml that orchestrates these services:

cat /root/docker-compose.yml
📋
💡 Notice the service definitions, port mappings, and volume mounts

---

## Step 3: Launch Your AIOps Stack

⚡ Deploy with a Single Command
This is the magic moment - watch your complete monitoring infrastructure come to life with one command:

What Happens When You Run This:
✅ Docker pulls Prometheus and Grafana images (if needed)
✅ Creates isolated network for services to communicate
✅ Starts Prometheus container on port 9090
✅ Starts Grafana container on port 3000
✅ Mounts configuration volumes
✅ All services become healthy and ready
⏱️ Expected time: 30-60 seconds for full startup

🎯 Launch Command
docker compose up -d
📋
💡 The -d flag runs containers in detached mode (background)

📊 Verify Deployment
After launching, check that all services are running:

docker compose ps
📋
✨ Look for "Up" status on both prometheus and grafana services

---

## Step 4: Access Prometheus Web UI

🎯 Verify Prometheus is Running
Prometheus is the heart of your metrics pipeline. Let's verify it's collecting and storing data:

📍 Access Information
Port: 9090
Authentication: None required (lab environment)
Initial Page: Prometheus Graph interface
Navigation: Top menu bar with Status, Alerts, Graph options
🔍 What to Look For
✅ Query input box at the top of the page
✅ "Execute" button to run queries
✅ Graph/Table toggle for results
✅ Status menu showing targets and configuration
🚀 Check Prometheus Status
Verify the service is healthy and accessible:

curl -s http://localhost:9090/-/healthy
📋
💡 Expected response: "Prometheus is Healthy."

🌐 Open in Browser
To access the Prometheus web interface:

Click the 3-dot menu icon (⋮) at the top-right of the terminal
Select "View Port"
Enter port number: 9090
Click "Open Port"
✨ You should see the Prometheus query interface ready for exploration

---

## Step 5: Access Grafana Dashboard

🎯 Verify Grafana Login Screen
Grafana transforms raw metrics into beautiful, actionable visualizations. Let's verify the dashboard platform is ready:

📍 Access Information
Port: 3000
Default Username: admin
Default Password: GrafanaRocks123!
First Login: You'll be prompted to change password
🔍 What to Look For
✅ Grafana logo and login form
✅ Username and password input fields
✅ "Log in" button
✅ Clean, modern web interface
🚀 Check Grafana Status
Verify the service is healthy and accessible:

curl -s http://localhost:3000/api/health
📋
💡 Expected response: JSON with "database": "ok"

🌐 Open in Browser
To access the Grafana web interface:

Click the 3-dot menu icon (⋮) at the top-right of the terminal
Select "View Port"
Enter port number: 3000
Click "Open Port"
✨ You should see the Grafana login screen ready for authentication
