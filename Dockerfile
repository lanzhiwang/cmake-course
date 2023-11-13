FROM gcc:12.3-bullseye

RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		indent \
		cmake \
		tree \
		git \
	; \
	rm -rf /var/lib/apt/lists/*
