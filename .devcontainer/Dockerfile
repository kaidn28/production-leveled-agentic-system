# Swap the base image for your stack (e.g. devcontainers/base:ubuntu, devcontainers/javascript-node)
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# Pre-create the mount point owned by vscode so the volume isn't root-owned
RUN mkdir -p /home/vscode/.claude && chown vscode:vscode /home/vscode/.claude