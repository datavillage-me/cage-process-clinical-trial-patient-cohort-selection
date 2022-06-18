# Template for a process to be deployed in the data cage

This is a sample project with a representative set of resources to deploy a data processing algorithm in a Datavillage cage.

__TL;DR__ : clone this repo and edit the `process.py` file

## Content of this repo
Apart from this file, this repo contains :

| | |
|----------|-------------|
| `datavillage.yaml` | __[mandatory]__ the config that describes how the project should be built and executed in the cage (see below) |
| `requirements.txt` | the python dependencies to install, as this is a python project |
| `listener.py` | the entry point executable to start the process, as declared in `datavillage.yaml`. In this example, it waits for one message on the local redis queue, processes it with `process.py`, then exits |
| `process.py` | the code that actually processes incoming events |
| `dv_tools.py` | a set of helper methods to interact with the Datavillage platform |
| `test.py` | some local tests |

## Config file
The root of the repo must contain a `datavillage.yaml` file with following properties :

| variable | description |
|----------|-------------|
| `env` |  the type of environment, i.e. pip, npm, yarn, bash, ...    |
| `script` | the build script to use for the build (needed for npm or yarn, not for pip)      |
| `entry` | the entry point to the process, i.e. the executable file (a `.py` file, a `.js` file that may result from the npm build, ... ) |

Example for a node environment :
```
env: npm
script: build
entry: dist/index.js
```  

## Deployment process
What happens when such a repo is deployed in the cage ?

### pip
If a `requirements.txt` is present, the deploying process first executes
```
pip install -r requirements.txt
```

If a `setup.py` or `pyproject.toml` file is found, it executes
```
pip install -e .
```

## Execution process

When starting the process as defined in the `entry` config variable, the following environment variables are made available to the executable :
 
| variable | description |
|----------|-------------|
| DV_TOKEN |        |
| DV_APP_ID |       |
| DV_CLIENT_ID |       |
| DV_URL |       |
| REDIS_SERVICE_HOST |       |
| REDIS_SERVICE_PORT |       |

The process execution is event-driven : triggering events are sent on a local Redis queue; the executable should 
subscribe to that queue and handle events appropriately.

The events are of the form 
```
{
    userIds: <optional list of user IDs>,
    jobId: <ID of the job that this event is bound to>,
    trigger: <type of event>,
}
```