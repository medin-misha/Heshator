FROM ghcr.io/astral-sh/uv:python3.13-bookworm

COPY . app/

EXPOSE 5001

WORKDIR app/
CMD ["uv", "run", "gunicorn", "main:app", "--workers", "33", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:5001"]