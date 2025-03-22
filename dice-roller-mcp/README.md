# Dice Roller MCP Server

A simple dice rolling server implemented using the Model Context Protocol (MCP). This implementation is based on the MCP server Quickstart from [modelcontextprotocol.io/quickstart/server](https://modelcontextprotocol.io/quickstart/server).

## Overview

This server provides a tool for rolling dice with any number of sides. It uses the FastMCP server implementation to expose a `roll_dice` function that generates random numbers.

## Features

- Roll dice with any number of sides (must be positive integer)
- Simple stdio transport implementation
- Built using the Model Context Protocol specification

## Usage

The server exposes a single tool:

- `roll_dice(sides: int)`: Returns a random number between 1 and the specified number of sides