# backend/Dockerfile
FROM node:20-alpine

WORKDIR /app

# Copy app source
COPY . .

# Install runtime dependencies from package.json
RUN npm install --production --no-audit --no-fund

EXPOSE 3000

CMD ["node", "server.js"]