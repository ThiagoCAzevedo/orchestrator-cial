
# Orchestrator Microservice

The Orchestrator Microservice is a core infrastructure component designed to coordinate, manage, and integrate multiple internal services within the CIAL ecosystem. It acts as a central automation layer, enabling reliable communication, event processing, and system orchestration across the broader architecture.

#### Key Responsibilities
- MQTT Event Orchestration
- Session and Process Coordination
- System Health Monitoring
- Service Automation Backbone

## 🟢 API Reference 

### Start MQTT Listener

```http
  POST /mqtt/start
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| _None_ | — | Starts the MQTT orchestrator if not already running |

**Description:** Initializes, connects and starts the MQTT listener.


### Stop MQTT Listener

```http
  POST /mqtt/stop
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| _None_     | — | Stops the MQTT orchestrator if it is running |

**Description:** Gracefully stops the MQTT listener.


### Get MQTT Status

```http
    GET /mqtt/status
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| _None_     | — | Returns whether MQTT is running or stopped |

**Description:** Retrieves the current operational state of the MQTT listener.


### Health Check

```http
    GET /health
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| _None_     | — | Simple health check for the service |

**Description:** Description: Verifies if the service is healthy and returns basic metadata.


## 🟢 Run Locally

Clone the project

```bash
  git clone https://github.com/ThiagoCAzevedo/orquestrator-cial.git
```

Go to the project directory

```bash
  cd orchestrator-cial
```

Install dependencies

```bash
  pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org 
```

Start the server

```bash
  python main.py
```

or

```bash
  python -m uvicorn main:app --reload --port <PORT TO RUN>
```

***Observation:** Use Python 3.10.0*


## 🟢 Running Tests

To run tests, run the following command

```bash
  npm run test
```


## 🟢 Authors

- [@ThiagoCAzevedo](https://www.github.com/thiagocazevedo)
- [@ThiagoCanatoAzevedo](https://www.github.com/thiagocanatoazevedo)


## 🟢 Support

For support, email nata.silva@gruposese.com or contact Sesé IT support.

