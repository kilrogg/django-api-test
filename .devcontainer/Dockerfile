ARG VARIANT="3.12-slim"
FROM python:${VARIANT}

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends git wget curl procps

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1; fi

# Poetry
ARG POETRY_VERSION="none"
RUN if [ "${POETRY_VERSION}" != "none" ]; then umask 0002 && pip3 install poetry==${POETRY_VERSION}; fi

# Nox
ARG NOX_VERSION="none"
RUN if [ "${NOX_VERSION}" != "none" ]; then sumask 0002 && pip3 install nox-poetry nox==${NOX_VERSION}; fi

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1
