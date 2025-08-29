# File Sharing Bot

## Overview

A Telegram file sharing bot that allows users to store files and documents in a designated channel and access them through special shareable links. The bot creates encoded links for individual files or batch files, supports force subscription to channels, and provides an admin interface for managing content. Built with Python using the Pyrogram library for Telegram API interaction and MongoDB for user data storage.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Bot Framework
- **Pyrogram Client**: Core Telegram bot framework handling all API interactions
- **Async Architecture**: Built with asyncio for handling concurrent operations
- **Plugin System**: Modular design with separate plugin files for different functionalities

### File Storage System
- **Database Channel**: Uses a designated Telegram channel as the primary file storage backend
- **Link Generation**: Creates base64-encoded shareable links for individual files and batch file ranges
- **Message ID Mapping**: Converts Telegram message IDs to encoded strings for secure access

### User Management
- **MongoDB Integration**: Stores user data including user IDs and subscription status
- **Force Subscription**: Optional feature requiring users to join specific channels before accessing files
- **Admin Controls**: Separate permission levels for bot administrators

### Web Components
- **Aiohttp Web Server**: Lightweight web server for health checks and potential web interface
- **Route Handling**: Basic HTTP endpoints for monitoring bot status

### Authentication & Authorization
- **Admin System**: Environment variable-based admin user configuration
- **Subscription Verification**: Real-time checking of user membership in required channels
- **Access Control**: Different permission levels for regular users vs administrators

### Link Management
- **Encoding System**: Base64 URL-safe encoding for generating shareable links
- **Batch Processing**: Support for creating links that provide access to multiple files in sequence
- **Link Validation**: Server-side validation of encoded links before serving content

## External Dependencies

### Telegram Integration
- **Telegram Bot API**: Core bot functionality through Pyrogram library
- **Bot Token**: Required authentication token from @Botfather
- **API Credentials**: App ID and API Hash from my.telegram.org

### Database Services
- **MongoDB**: Primary database for user management and bot statistics
- **Database URL**: MongoDB connection string for data persistence
- **Collections**: User data storage with document-based structure

### Python Libraries
- **Pyrogram**: Telegram MTProto API client library
- **PyMongo**: MongoDB driver for Python
- **Aiohttp**: Asynchronous HTTP client/server framework
- **Base64**: Built-in encoding/decoding for link generation

### Optional Integrations
- **Force Subscription Channels**: Telegram channels for mandatory user subscription
- **Database Channel**: Dedicated Telegram channel for file storage
- **Web Server**: Optional HTTP server for monitoring and health checks

### Environment Configuration
- **Heroku Deployment**: Configured for easy deployment on Heroku platform
- **Environment Variables**: All sensitive configuration through environment variables
- **Port Configuration**: Configurable web server port for hosting requirements
