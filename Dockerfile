FROM python:3.11-slim

# Install mkdocs-material
RUN pip install mkdocs-material

# Create docs directory
RUN mkdir -p /docs/papers

# Copy all files
COPY . /docs/

# Run MkDocs
WORKDIR /docs
CMD ["mkdocs", "serve", "--dev-addr", "0.0.0.0:8080"]
